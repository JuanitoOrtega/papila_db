import os


class ContourManager:
    def __init__(self, dataset_path):
        self.contours_folder = os.path.join(dataset_path, "ExpertsSegmentations/Contours")

    def list_contours(self):
        """Lista todos los archivos de contornos disponibles."""
        return [f for f in os.listdir(self.contours_folder) if f.endswith(".txt")]

    def read_contour(self, contour_file):
        """Lee un archivo de contorno y devuelve los puntos como una lista de tuplas."""
        contour_path = os.path.join(self.contours_folder, contour_file)
        if not os.path.exists(contour_path):
            raise FileNotFoundError(f"El archivo {contour_file} no existe.")
        
        with open(contour_path, 'r') as file:
            points = [tuple(map(float, line.split())) for line in file]
        return points