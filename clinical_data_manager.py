import pandas as pd
import os


class ClinicalDataManager:
    def __init__(self, dataset_path):
        self.clinical_data_folder = os.path.join(dataset_path, "ClinicalData")

    def load_clinical_data(self, file_name):
        """Carga un archivo de datos clínicos en un DataFrame de pandas."""
        file_path = os.path.join(self.clinical_data_folder, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo {file_name} no existe.")
        
        return pd.read_excel(file_path, index_col="ID")

    def get_patient_data(self, file_name, patient_id):
        """Obtiene los datos de un paciente específico."""
        data = self.load_clinical_data(file_name)
        if patient_id not in data.index:
            raise ValueError(f"El paciente {patient_id} no está en el archivo {file_name}.")
        
        return data.loc[patient_id]

    def list_patients(self, file_name):
        """Lista todos los IDs de pacientes en el archivo."""
        data = self.load_clinical_data(file_name)
        return data.index.tolist()