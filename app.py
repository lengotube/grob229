import streamlit as st
import pandas as pd
import os

# Путь к папке с данными
DATA_FOLDER = 'ALL_DATA'

# Функция для загрузки данных
def load_data(year, country):
    file_name = f"{country}_{year}.xlsx"  # Предполагается, что файлы имеют такой формат
    file_path = os.path.join(DATA_FOLDER, file_name)
    if os.path.exists(file_path):
        return pd.read_excel(file_path)
    else:
        st.error(f"Файл {file_name} не найден.")
        return None

# Получаем доступные годы и страны
years = [file.split('_')[1].split('.')[0] for file in os.listdir(DATA_FOLDER) if file.endswith('.xlsx')]
countries = list(set(file.split('_')[0] for file in os.listdir(DATA_FOLDER) if file.endswith('.xlsx')))

# Выбор года и страны
selected_year = st.selectbox('Выберите год:', sorted(years))
selected_country = st.selectbox('Выберите страну:', sorted(countries))

# Загрузка данных и отображение
data = load_data(selected_year, selected_country)
if data is not None:
    st.write(data)

# Заголовок
st.title('Дэшборд данных из ALL_DATA')
