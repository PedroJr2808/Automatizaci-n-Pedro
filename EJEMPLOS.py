import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Graficador Polinómico Interactivo",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("📊 Visualizador de Funciones Polinómicas")
st.markdown("""
Esta aplicación permite interactuar en tiempo real con un polinomio de cuarto grado:
$$f(x) = ax^4 + bx^3 + cx^2 + dx + e$$
Usa los controles de la barra lateral para modificar los coeficientes.
""")

# --- Barra Lateral (Sliders Interactivos) ---
st.sidebar.header("🎛️ Coeficientes del Polinomio")

# Botón para reiniciar valores (Streamlit recrea la app, así que usamos session_state o valores por defecto)
if st.sidebar.button("🔄 Reiniciar Valores"):
    st.rerun()

a = st.sidebar.slider("Coeficiente a ($x^4$)", min_value=-2.0, max_value=2.0, value=0.0, step=0.1)
b = st.sidebar.slider("Coeficiente b ($x^3$)", min_value=-5.0, max_value=5.0, value=0.1, step=0.1)
c = st.sidebar.slider("Coeficiente c ($x^2$)", min_value=-10.0, max_value=10.0, value=-0.5, step=0.1)
d = st.sidebar.slider("Coeficiente d ($x$)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
e = st.sidebar.slider("Constante e", min_value=-20.0, max_value=20.0, value=0.0, step=0.5)

# --- Cálculo de la Función ---
x = np.linspace(-10, 10, 500)
y = a*x**4 + b*x**3 + c*x**2 + d*x + e

# --- Configuración Gráfica (Matplotlib adaptado a Streamlit) ---
fig, ax = plt.subplots(figsize=(10, 5))

# Estética oscura/profesional para el gráfico
fig.patch.set_facecolor('#0e1117')  # Fondo oscuro a juego con el tema de Streamlit
ax.set_facecolor('#131722')
plt.rcParams['text.color'] = '#ffffff'
plt.rcParams['axes.labelcolor'] = '#ffffff'

# Dibujar la curva y líneas de guía
ax.plot(x, y, lw=2.5, color='#00adb5', label='$f(x)$')
ax.axhline(0, color='#ffffff', linewidth=0.8, alpha=0.3)
ax.axvline(0, color='#ffffff', linewidth=0.8, alpha=0.3)

# Detalles de los ejes
ax.set_xlim([-10, 10])
ax.set_ylim([-50, 50])
ax.grid(True, color='#4f5b66', linestyle='--', alpha=0.4)
ax.tick_params(colors='#eeeeee', labelsize=9)
ax.set_xlabel('Eje X', color='#eeeeee')
ax.set_ylabel('Eje Y', color='#eeeeee')

# --- Mostrar en Streamlit ---
st.pyplot(fig)

# Muestra la ecuación matemática dinámica debajo del gráfico
st.subheader("📝 Ecuación Actual:")
st.latex(f"f(x) = ({a:1.1f})x^4 + ({b:1.1f})x^3 + ({c:1.1f})x^2 + ({d:1.1f})x + ({e:1.1f})")
