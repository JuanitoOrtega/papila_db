from image_manager import ImageManager
from metadata_manager import MetadataManager


def main():
    dataset_path = "./DB_PAPILA"
    metadata_file = "./data/metadata.json"

    image_manager = ImageManager(dataset_path)
    metadata_manager = MetadataManager(metadata_file)

    while True:
        print("\nGestión de Imágenes y Metadata")
        print("1. Listar imágenes")
        print("2. Agregar imagen")
        print("3. Eliminar imagen")
        print("4. Agregar/Actualizar metadata")
        print("5. Eliminar metadata")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            images = image_manager.list_images()
            print("Imágenes disponibles:", images)
        elif choice == "2":
            source_path = input("Ruta de la imagen a agregar: ")
            dest_name = input("Nombre para guardar la imagen: ")
            image_manager.add_image(source_path, dest_name)
        elif choice == "3":
            image_name = input("Nombre de la imagen a eliminar: ")
            image_manager.delete_image(image_name)
        elif choice == "4":
            image_name = input("Nombre de la imagen: ")
            metadata = input("Ingrese la metadata (en formato clave:valor, separada por comas): ")
            metadata_dict = dict(item.split(":") for item in metadata.split(","))
            metadata_manager.add_metadata(image_name, metadata_dict)
        elif choice == "5":
            image_name = input("Nombre de la imagen: ")
            metadata_manager.delete_metadata(image_name)
        elif choice == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()