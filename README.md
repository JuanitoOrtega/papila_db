```shell
papila_db/
│
├── main.py                # Archivo principal para ejecutar el programa
├── image_manager.py       # Módulo para gestionar imágenes y metadatos
├── metadata_manager.py    # Módulo para gestionar la metadata
├── utils.py               # Funciones auxiliares
├── DB_PAPILA/             # Dataset original
│   ├── ClinicalData/
│   │   ├── patient_data_od.xlsx
│   │   └── patient_data_os.xlsx
│   ├── ExpertsSegmentations/
│   │   ├── Contours/
|   |   |   ├── RET002OD_cup_exp1.txt
|   |   |   ├── RET002OD_cup_exp2.txt
|   |   |   ├── RET002OD_disc_exp1.txt
|   |   |   ├── RET002OD_disc_exp2.txt
|   |   |   ├── RET002OS_cup_exp1.txt
|   |   |   ├── RET002OS_cup_exp2.txt
|   |   |   ├── RET002OS_disc_exp1.txt
|   |   |   ├── RET002OS_disc_exp2.txt
|   |   |   ├── RET0040D_cup_exp1.txt
|   |   |   ├── RET0040D_cup_exp2.txt
|   |   |   ├── RET0040D_disc_exp1.txt
|   |   |   ├── RET0040D_disc_exp2.txt
|   |   |   ├── RET0040S_cup_exp1.txt
|   |   |   ├── RET0040S_cup_exp2.txt
|   |   |   ├── RET0040S_disc_exp1.txt
|   |   |   ├── RET0040S_disc_exp2.txt
|   |   |   ├── ...
│   │   ├── ImagesWithContours/
|   |   |   ├── Opht_cont_RET002OD.jpg
|   |   |   ├── Opht_cont_RET002OS.jpg
|   |   |   ├── Opht_cont_RET004OD.jpg
|   |   |   ├── Opht_cont_RET004OS.jpg
|   |   |   ├── ...
│   ├── FundusImages/
|   |   ├── RET002OD.jpg
|   |   ├── RET002OS.jpg
|   |   ├── RET004OD.jpg
|   |   ├── RET004OS.jpg
|   |   ├── ...
```