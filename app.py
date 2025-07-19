import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('C:/Users/Korisnik/Documents/Mis documentos/TripleTen/Sprit_7_Proyecto/Sprit_7_Proyecto/notebooks/vehicles_us.csv')

hist_button = st.button('Construir histograma')
     
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


disp_button = st.button('Construir gráfico de dispersión') # crear un botón
     
if disp_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    graph = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(graph, use_container_width=True)