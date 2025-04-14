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
        print("2. Listar contornos")
        print("3. Leer contorno")
        print("4. Listar pacientes")
        print("5. Ver datos de un paciente")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            images = image_manager.list_images()
            print("Imágenes disponibles:", images)
        elif choice == "2":
            contours = contour_manager.list_contours()
            print("Contornos disponibles:", contours)
        elif choice == "3":
            contour_file = input("Nombre del archivo de contorno: ")
            try:
                points = contour_manager.read_contour(contour_file)
                print("Puntos del contorno:", points)
            except FileNotFoundError as e:
                print(e)
        elif choice == "4":
            file_name = input("Nombre del archivo de datos clínicos (ej. patient_data_od.xlsx): ")
            try:
                patients = clinical_data_manager.list_patients(file_name)
                print("Pacientes disponibles:", patients)
            except FileNotFoundError as e:
                print(e)
        elif choice == "5":
            file_name = input("Nombre del archivo de datos clínicos (ej. patient_data_od.xlsx): ")
            patient_id = input("ID del paciente (ej. #002): ")
            try:
                patient_data = clinical_data_manager.get_patient_data(file_name, patient_id)
                print("Datos del paciente:", patient_data)
            except (FileNotFoundError, ValueError) as e:
                print(e)
        elif choice == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()