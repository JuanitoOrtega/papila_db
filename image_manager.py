import os
import shutil


# This script manages images in a dataset for a medical imaging project.
class ImageManager:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.images_folder = os.path.join(dataset_path, "FundusImages")

    def list_images(self):
        """Lista todas las imágenes en la carpeta FundusImages."""
        return [f for f in os.listdir(self.images_folder) if os.path.isfile(os.path.join(self.images_folder, f))]

    def add_image(self, source_path, dest_name):
        """Agrega una nueva imagen al dataset."""
        dest_path = os.path.join(self.images_folder, dest_name)
        shutil.copy(source_path, dest_path)
        print(f"Imagen {dest_name} agregada exitosamente.")

    def delete_image(self, image_name):
        """Elimina una imagen del dataset."""
        image_path = os.path.join(self.images_folder, image_name)
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Imagen {image_name} eliminada exitosamente.")
        else:
            print(f"La imagen {image_name} no existe.")