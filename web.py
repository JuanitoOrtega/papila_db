import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask, send_from_directory
from image_manager import ImageManager

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/FundusImages/<path:filename>')
def fundus_images(filename):
    return send_from_directory('./DB_PAPILA/FundusImages', filename)

# Ruta del dataset
dataset_path = "./DB_PAPILA"
image_manager = ImageManager(dataset_path)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/list_images")
def list_images():
    images = image_manager.list_images()
    return render_template("list_images.html", images=images)

@app.route("/add_image", methods=["GET", "POST"])
def add_image():
    if request.method == "POST":
        # Manejar el archivo subido
        uploaded_file = request.files["source_path"]
        if uploaded_file.filename == "":
            flash("No se seleccionó ningún archivo.", "danger")
            return redirect(request.url)

        # Guardar el archivo en una ubicación temporal
        source_path = f"./DB_PAPILA/FundusImages/{uploaded_file.filename}"
        uploaded_file.save(source_path)

        # Obtener otros datos del formulario
        dest_name = request.form["dest_name"]
        excel_file = request.form["excel_file"]
        metadata_input = request.form["metadata"]
        metadata = dict(item.split(":") for item in metadata_input.split(","))

        try:
            # Llamar al método para agregar la imagen y los metadatos
            image_manager.add_image(source_path, dest_name, metadata, excel_file)
            flash(f"Imagen {dest_name} agregada exitosamente.", "success")

            # Eliminar la imagen original después de procesarla
            if os.path.exists(source_path):
                os.remove(source_path)

            return redirect(url_for("home"))
        except (FileNotFoundError, ValueError) as e:
            flash(str(e), "danger")
    return render_template("add_image.html")

@app.route("/update_image", methods=["GET", "POST"])
def update_image():
    if request.method == "POST":
        source_path = request.form["source_path"]
        dest_name = request.form["dest_name"]
        excel_file = request.form["excel_file"]
        metadata_input = request.form["metadata"]
        metadata_updates = dict(item.split(":") for item in metadata_input.split(","))
        try:
            image_manager.update_image_and_metadata(source_path, dest_name, metadata_updates, excel_file)
            flash(f"Imagen {dest_name} actualizada exitosamente.", "success")
            return redirect(url_for("home"))
        except (FileNotFoundError, ValueError) as e:
            flash(str(e), "danger")
    return render_template("update_image.html")

@app.route("/delete_image", methods=["GET", "POST"])
def delete_image():
    if request.method == "POST":
        image_name = request.form["image_name"]
        try:
            image_manager.delete_image(image_name)
            flash(f"Imagen {image_name} eliminada exitosamente.", "success")
            return redirect(url_for("home"))
        except FileNotFoundError as e:
            flash(str(e), "danger")
    return render_template("delete_image.html")

if __name__ == "__main__":
    app.run(debug=True)