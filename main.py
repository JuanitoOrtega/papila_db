from image_manager import ImageManager
from contour_manager import ContourManager
from clinical_data_manager import ClinicalDataManager


def main():
    dataset_path = "./DB_PAPILA"
    image_manager = ImageManager(dataset_path)
    contour_manager = ContourManager(dataset_path)
    clinical_data_manager = ClinicalDataManager(dataset_path)

    while True:
        print("\nGestión de Datos del Dataset PAPILA")
        print("1. Listar imágenes")
        print("2. Agregar imagen con metadatos")
        print("3. Modificar imagen y sus metadatos")
        print("4. Eliminar imagen y sus metadatos")
        print("5. Ver metadatos de una imagen")
        print("6. Listar contornos")
        print("7. Leer contorno")
        print("8. Listar pacientes")
        print("9. Ver datos de un paciente")
        print("10. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            images = image_manager.list_images()
            print("Imágenes disponibles:", images)
        elif choice == "2":
            source_path = input("Ruta de la imagen a agregar: ")
            dest_name = input("Nombre para guardar la imagen: ")
            excel_file = input("Nombre del archivo Excel para guardar los metadatos (ej. patient_data_od.xlsx): ")
            metadata_input = input("Ingrese los metadatos en formato clave:valor separados por comas (ej. resolution:1920x1080,modality:Fundus): ")
            metadata = dict(item.split(":") for item in metadata_input.split(","))
            try:
                image_manager.add_image(source_path, dest_name, metadata, excel_file)
            except (FileNotFoundError, ValueError) as e:
                print(e)
        elif choice == "3":
            source_path = input("Ruta de la nueva imagen a reemplazar: ")
            dest_name = input("Nombre de la imagen a reemplazar: ")
            excel_file = input("Nombre del archivo Excel donde se actualizarán los metadatos (ej. patient_data_od.xlsx): ")
            metadata_input = input("Ingrese los metadatos a actualizar en formato clave:valor separados por comas (ej. resolution:2560x1440,modality:OCT): ")
            metadata_updates = dict(item.split(":") for item in metadata_input.split(","))
            try:
                image_manager.update_image_and_metadata(source_path, dest_name, metadata_updates, excel_file)
            except (FileNotFoundError, ValueError) as e:
                print(e)
        elif choice == "4":
            image_name = input("Nombre de la imagen a eliminar: ")
            image_manager.delete_image(image_name)
        elif choice == "5":
            image_name = input("Nombre de la imagen: ")
            metadata = image_manager.get_metadata(image_name)
            print(f"Metadatos de {image_name}:", metadata)
        elif choice == "6":
            contours = contour_manager.list_contours()
            print("Contornos disponibles:", contours)
        elif choice == "7":
            contour_file = input("Nombre del archivo de contorno: ")
            try:
                points = contour_manager.read_contour(contour_file)
                print("Puntos del contorno:", points)
            except FileNotFoundError as e:
                print(e)
        elif choice == "8":
            file_name = input("Nombre del archivo de datos clínicos (ej. patient_data_od.xlsx): ")
            try:
                patients = clinical_data_manager.list_patients(file_name)
                print("Pacientes disponibles:", patients)
            except FileNotFoundError as e:
                print(e)
        elif choice == "9":
            file_name = input("Nombre del archivo de datos clínicos (ej. patient_data_od.xlsx): ")
            patient_id = input("ID del paciente (ej. #002): ")
            try:
                patient_data = clinical_data_manager.get_patient_data(file_name, patient_id)
                print("Datos del paciente:", patient_data)
            except (FileNotFoundError, ValueError) as e:
                print(e)
        elif choice == "10":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()