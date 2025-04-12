# Recorer carpetas
import os


# Definimos la carpeta de origen y destino
source_folder = "./DB_PAPILA"
# Listar subcarpetas
subfolders = [f.path for f in os.scandir(source_folder) if f.is_dir()]  # ['./DB_PAPILA/FundusImages', './DB_PAPILA/ExpertsSegmentations', './DB_PAPILA/HelpCode', './DB_PAPILA/ClinicalData']

# lista imagenes dentro de la carpeta FundusImages
# FundusImages
images_folder = os.path.join(source_folder, "FundusImages")
images = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]  # ['0001.jpg', '0002.jpg', '0003.jpg', '0004.jpg', '0005.jpg', '0006.jpg', '0007.jpg', '0008.jpg', '0009.jpg', '0010.jpg']
print(f"Imagenes: {images}")
