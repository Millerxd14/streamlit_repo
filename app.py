import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

#Configuracion inicia
st.set_page_config(
    page_title="Proyecto Sprint 7 | Miller Hurtado",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Análisis de vehículos usados")
st.header("Proyecto Sprint 7 — Miller Hurtado")
st.caption("Explora datos y visualizaciones de vehículos en Estados Unidos.")


df_carros = pd.read_csv('vehicles_us.csv')

boton_histograma = st.button('Construir histograma')

if boton_histograma:
    st.write('Histograma del odómetro de los vehículos en US')
    fig = go.Figure(data=[go.Histogram(x=df_carros['odometer'])])
    fig.update_layout(
        title_text='Distribución del odómetro',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Cantidad de vehículos',
    )
    st.plotly_chart(fig, use_container_width=True)
    odometros = df_carros['odometer'].dropna()
    cantidad_baja = odometros.between(0, 1999).sum()
    porcentaje_bajo = cantidad_baja / len(odometros) * 100
    st.caption(
        'La distribución está sesgada positivamente: la mayoría de los valores '
        'se concentra en odómetros bajos y hay una cola hacia valores altos. '
        f'Entre 0 y 1.999 millas hay {cantidad_baja:,} vehículos '
        f'({porcentaje_bajo:.1f}% de los registros con odómetro), por lo que '
        'ese intervalo no representa una cantidad considerable del total.'
    )


boton_dispersion = st.button('Construir dispersion')

if boton_dispersion:
    st.write('Dispersión entre el odómetro y el precio de los vehículos')
    fig = go.Figure(data=[go.Scatter(x=df_carros['odometer'], y=df_carros['price'], mode='markers')])
    fig.update_layout(
        title_text='Odómetro vs. precio',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Precio (USD)',
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption(
        'Cada punto representa un vehículo: su posición horizontal indica el '
        'odómetro y la vertical, el precio. La dispersión permite observar '
        'cómo varían los precios entre vehículos con distintos odómetros y '
        'cuánto difieren los precios para un odómetro similar.'
    )
