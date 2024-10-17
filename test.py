import os
import pandas as pd
import pyreadstat
import pyreadr

def process_files(folder_path):
    # Создаем папку ALL_DATA, если она не существует
    all_data_folder = os.path.join(folder_path, 'ALL_DATA')
    os.makedirs(all_data_folder, exist_ok=True)

    # Ищем файлы с нужными расширениями
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_extension = os.path.splitext(file)

            # Обработка .dta файлов
            if file_extension == ".dta":
                df, meta = pyreadstat.read_dta(file_path)
                output_path = os.path.join(all_data_folder, f"{file_name}.xlsx")
                df.to_excel(output_path, index=False)
                print(f"Сохранен файл: {output_path}")

            # Обработка .rdata файлов
            elif file_extension == ".rdata":
                result = pyreadr.read_r(file_path)
                df = list(result.values())[0]  # получаем датафрейм
                output_path = os.path.join(all_data_folder, f"{file_name}.xlsx")
                df.to_excel(output_path, index=False)
                print(f"Сохранен файл: {output_path}")

            # Обработка .sav файлов
            elif file_extension == ".sav":
                df, meta = pyreadstat.read_sav(file_path)
                output_path = os.path.join(all_data_folder, f"{file_name}.xlsx")
                df.to_excel(output_path, index=False)
                print(f"Сохранен файл: {output_path}")

root_folder = r'/Users/grobye/Downloads/Lab723'
process_files(root_folder)