import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Генерация данных
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создание графика
plt.plot(x, y)
plt.title('График синуса')
plt.xlabel('X')
plt.ylabel('sin(X)')

# Отображение графика в Streamlit
st.pyplot(plt)

# Заголовок
st.title('Мой график с использованием Streamlit!')
