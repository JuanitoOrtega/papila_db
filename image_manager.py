import os
import shutil


class ImageManager:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.images_folder = os.path.join(dataset_path, "FundusImages")

    def list_images(self):
        """Lista todas las imágenes en la carpeta FundusImages."""
        return [f for f in os.listdir(self.images_folder) if os.path.isfile(os.path.join(self.images_folder, f))]

    def add_image(self, source_path, dest_name, metadata=None, excel_file=None):
        """
        Agrega una nueva imagen al dataset y registra sus metadatos en un archivo Excel.
        :param source_path: Ruta de la imagen a agregar.
        :param dest_name: Nombre con el que se guardará la imagen.
        :param metadata: Diccionario con los metadatos de la imagen.
        :param excel_file: Nombre del archivo Excel donde se guardarán los metadatos.
        """
        dest_path = os.path.join(self.images_folder, dest_name)
        shutil.copy(source_path, dest_path)
        print(f"Imagen {dest_name} agregada exitosamente.")

        # Registrar metadatos si se proporcionan y se especifica un archivo Excel
        if metadata and excel_file:
            self.add_metadata_to_excel(dest_name, metadata, excel_file)
    
    def add_metadata_to_excel(self, image_name, metadata, excel_file):
        """
        Agrega los metadatos de una imagen como una nueva fila en el archivo Excel.
        :param image_name: Nombre de la imagen.
        :param metadata: Diccionario con los metadatos.
        :param excel_file: Nombre del archivo Excel donde se guardarán los metadatos.
        """
        import pandas as pd

        # Ruta completa del archivo Excel
        excel_path = os.path.join(self.dataset_path, "ClinicalData", excel_file)

        # Verificar si el archivo Excel existe
        if not os.path.exists(excel_path):
            raise FileNotFoundError(f"El archivo {excel_file} no existe en la carpeta ClinicalData.")

        # Leer el archivo Excel
        try:
            data = pd.read_excel(excel_path)
        except Exception as e:
            raise ValueError(f"Error al leer el archivo Excel: {e}")

        # Extraer el ID del nombre de la imagen
        try:
            patient_id = f"#{image_name[3:6]}"  # Extraer los caracteres 3 a 6 y concatenar #
        except IndexError:
            raise ValueError(f"No se pudo extraer un ID válido del nombre de la imagen: {image_name}")

        # Agregar el ID al diccionario de metadatos
        metadata["ID"] = patient_id

        # Convertir los metadatos a un DataFrame y agregarlo al archivo Excel
        new_row = pd.DataFrame([metadata])
        updated_data = pd.concat([data, new_row], ignore_index=True)

        # Guardar los datos actualizados en el archivo Excel
        try:
            updated_data.to_excel(excel_path, index=False)
            print(f"Metadatos para {image_name} agregados al archivo {excel_file}.")
        except Exception as e:
            raise ValueError(f"Error al guardar los metadatos en el archivo Excel: {e}")

    def delete_image(self, image_name, clinical_data_manager):
        """
        Elimina una imagen del dataset y sus metadatos asociados.
        :param image_name: Nombre de la imagen.
        :param clinical_data_manager: Instancia de ClinicalDataManager para manejar los datos clínicos.
        """
        import pandas as pd

        # Ruta completa de la imagen
        image_path = os.path.join(self.images_folder, image_name)

        # Verificar si la imagen existe
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"La imagen '{image_name}' no existe.")

        # Eliminar la imagen
        os.remove(image_path)
        print(f"Imagen {image_name} eliminada exitosamente.")

        # Determinar el archivo Excel según las últimas letras del nombre de la imagen
        if image_name.endswith("OD.jpg") or image_name.endswith("OD.png"):
            excel_file = "patient_data_od.xlsx"
        elif image_name.endswith("OS.jpg") or image_name.endswith("OS.png"):
            excel_file = "patient_data_os.xlsx"
        else:
            print(f"No se pudo determinar el archivo de metadatos para la imagen {image_name}.")
            return

        # Cargar los datos clínicos usando ClinicalDataManager
        try:
            data = clinical_data_manager.load_clinical_data(excel_file)
        except FileNotFoundError as e:
            print(e)
            return

        # Extraer el ID del paciente del nombre de la imagen
        try:
            patient_id = f"#{image_name[3:6]}"  # Extraer los caracteres 3 a 6 y concatenar #
        except IndexError:
            print(f"No se pudo extraer un ID válido del nombre de la imagen: {image_name}.")
            return

        # Verificar si el ID existe en el archivo Excel
        if patient_id not in data.index:
            print(f"No se encontraron metadatos para el ID {patient_id} en el archivo {excel_file}.")
            return

        # Eliminar la fila correspondiente al ID
        data = data.drop(index=patient_id)

        # Guardar los datos actualizados en el archivo Excel
        try:
            data.to_excel(os.path.join(clinical_data_manager.clinical_data_folder, excel_file), index=True)
            print(f"Metadatos para el ID {patient_id} eliminados del archivo {excel_file}.")
        except Exception as e:
            print(f"Error al guardar los datos actualizados en el archivo Excel: {e}")
            
    def get_metadata(self, image_name):
        """
        Obtiene los metadatos de una imagen desde el archivo Excel.
        :param image_name: Nombre de la imagen.
        :return: Diccionario con los metadatos de la imagen.
        """
        import pandas as pd

        # Extraer el ID del nombre de la imagen
        try:
            patient_id = f"#{image_name[3:6]}"  # Extraer los caracteres 3 a 6 y concatenar #
        except IndexError:
            return f"No se pudo extraer un ID válido del nombre de la imagen: {image_name}"

        # Ruta del archivo Excel
        excel_file = os.path.join(self.dataset_path, "ClinicalData", "patient_data_od.xlsx")

        # Verificar si el archivo existe
        if not os.path.exists(excel_file):
            return f"El archivo {excel_file} no existe."

        # Leer el archivo Excel
        try:
            data = pd.read_excel(excel_file, index_col="ID")
        except Exception as e:
            return f"Error al leer el archivo Excel: {e}"

        # Buscar el ID en los datos
        if patient_id not in data.index:
            return f"No se encontraron metadatos para el ID {patient_id}."

        # Retornar los metadatos como un diccionario
        metadata = data.loc[patient_id].to_dict()
        return metadata

    
    def update_image_and_metadata(self, source_path, dest_name, metadata_updates=None, excel_file=None):
        """
        Modifica o reemplaza una imagen y actualiza su metadata en el archivo Excel.
        :param source_path: Ruta de la nueva imagen a reemplazar.
        :param dest_name: Nombre de la imagen a reemplazar.
        :param metadata_updates: Diccionario con las columnas a actualizar y sus nuevos valores.
        :param excel_file: Nombre del archivo Excel donde se actualizarán los metadatos.
        """
        import pandas as pd

        # Reemplazar la imagen en el directorio FundusImages
        dest_path = os.path.join(self.images_folder, dest_name)
        if os.path.exists(dest_path):
            os.remove(dest_path)  # Eliminar la imagen existente
            print(f"Imagen {dest_name} eliminada exitosamente.")
        shutil.copy(source_path, dest_path)
        print(f"Imagen {dest_name} reemplazada exitosamente.")

        # Actualizar los metadatos en el archivo Excel
        if metadata_updates and excel_file:
            # Ruta completa del archivo Excel
            excel_path = os.path.join(self.dataset_path, "ClinicalData", excel_file)

            # Verificar si el archivo Excel existe
            if not os.path.exists(excel_path):
                raise FileNotFoundError(f"El archivo {excel_file} no existe en la carpeta ClinicalData.")

            # Leer el archivo Excel
            try:
                data = pd.read_excel(excel_path, index_col="ID")
            except Exception as e:
                raise ValueError(f"Error al leer el archivo Excel: {e}")

            # Extraer el ID del nombre de la imagen
            try:
                patient_id = f"#{dest_name[3:6]}"  # Extraer los caracteres 3 a 6 y concatenar #
            except IndexError:
                raise ValueError(f"No se pudo extraer un ID válido del nombre de la imagen: {dest_name}")

            # Verificar si el ID existe en el archivo Excel
            if patient_id not in data.index:
                raise ValueError(f"No se encontraron metadatos para el ID {patient_id} en el archivo {excel_file}.")

            # Actualizar únicamente las columnas especificadas
            for key, value in metadata_updates.items():
                if key in data.columns:
                    data.at[patient_id, key] = value
                else:
                    print(f"Advertencia: La columna '{key}' no existe en el archivo Excel y será ignorada.")

            # Guardar los datos actualizados en el archivo Excel
            try:
                data.to_excel(excel_path, index=True)
                print(f"Metadatos para {dest_name} actualizados en el archivo {excel_file}.")
            except Exception as e:
                raise ValueError(f"Error al guardar los metadatos en el archivo Excel: {e}")