import streamlit as st import pandas as pd import matplotlib.pyplot as plt

Simulación de datos actualizados semanalmente

data = { "Indicador": [ "Cash institucional", "Fear & Greed Index", "AAII Sentiment (Bullish)", "AAII Sentiment (Bearish)", "CFTC Positioning", "Flujos hacia ETFs" ], "Valor actual": [ "4.8% (subiendo)", "35 (Miedo)", "22%", "48%", "Net short leve", "Salidas netas" ], "Señal contraria": [ "Alcista", "Alcista", "Alcista", "Alcista", "Alcista", "Alcista" ] }

df = pd.DataFrame(data)

st.title("Dashboard de Sentimiento del Mercado")

st.subheader("Tabla de Indicadores de Sentimiento") st.dataframe(df)

st.subheader("Señales Contrarias por Indicador") fig, ax = plt.subplots(figsize=(10, 6)) colors = ['green' if val == "Alcista" else 'red' for val in df["Señal contraria"]] bars = ax.barh(df["Indicador"], [1]*len(df), color=colors) ax.set_xlim(0, 1.2) ax.set_xticks([]) ax.set_title("Señales Contrarias por Indicador de Sentimiento", fontsize=14) ax.bar_label(bars, labels=df["Valor actual"], padding=5) st.pyplot(fig)

st.markdown("Actualización semanal sugerida. Fuente: datos propios y públicos")

