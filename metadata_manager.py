import json
import os


class MetadataManager:
    def __init__(self, metadata_file):
        self.metadata_file = metadata_file
        if not os.path.exists(metadata_file):
            with open(metadata_file, 'w') as f:
                json.dump({}, f)

    def load_metadata(self):
        """Carga la metadata desde el archivo JSON."""
        with open(self.metadata_file, 'r') as f:
            return json.load(f)

    def save_metadata(self, metadata):
        """Guarda la metadata en el archivo JSON."""
        with open(self.metadata_file, 'w') as f:
            json.dump(metadata, f, indent=4)

    def add_metadata(self, image_name, metadata):
        """Agrega o actualiza la metadata de una imagen."""
        data = self.load_metadata()
        data[image_name] = metadata
        self.save_metadata(data)
        print(f"Metadata para {image_name} actualizada.")

    def delete_metadata(self, image_name):
        """Elimina la metadata de una imagen."""
        data = self.load_metadata()
        if image_name in data:
            del data[image_name]
            self.save_metadata(data)
            print(f"Metadata para {image_name} eliminada.")
        else:
            print(f"No se encontró metadata para {image_name}.")