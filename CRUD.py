import streamlit as st
from supabase import create_client

# =====================================
# CONFIGURACIÓN SUPABASE
# =====================================
SUPABASE_URL = "TU_URL_SUPABASE"
SUPABASE_KEY = "TU_API_KEY"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="CRUD Alumnos", layout="wide")

st.title("📚 Mantenimiento de Alumnos")

# =====================================
# CREAR REGISTRO
# =====================================
st.subheader("➕ Registrar Alumno")

with st.form("form_alumno"):
    dni = st.text_input("DNI")
    apellidos = st.text_input("Apellidos")
    nombres = st.text_input("Nombres")
    edad = st.number_input("Edad", min_value=0, max_value=120)
    sexo = st.selectbox("Sexo", ["M", "F"])

    guardar = st.form_submit_button("Guardar")

    if guardar:
        supabase.table("Alumnos2").insert({
            "dni": dni,
            "apellidos": apellidos,
            "nombres": nombres,
            "edad": edad,
            "sexo": sexo
        }).execute()

        st.success("Alumno registrado correctamente")

# =====================================
# LISTAR REGISTROS
# =====================================
st.subheader("📋 Lista de Alumnos")

datos = supabase.table("Alumnos2").select("*").execute()

if datos.data:
    st.dataframe(datos.data, use_container_width=True)

# =====================================
# ACTUALIZAR REGISTRO
# =====================================
st.subheader("✏️ Actualizar Alumno")

dni_buscar = st.text_input("Ingrese DNI para actualizar")

if st.button("Buscar"):
    alumno = supabase.table("Alumnos2").select("*").eq("dni", dni_buscar).execute()

    if alumno.data:
        st.session_state.alumno = alumno.data[0]
    else:
        st.error("No existe el alumno")

if "alumno" in st.session_state:

    alumno = st.session_state.alumno

    nuevo_apellido = st.text_input(
        "Apellidos",
        value=alumno["apellidos"]
    )

    nuevo_nombre = st.text_input(
        "Nombres",
        value=alumno["nombres"]
    )

    nueva_edad = st.number_input(
        "Edad",
        value=int(alumno["edad"])
    )

    nuevo_sexo = st.selectbox(
        "Sexo",
        ["M", "F"],
        index=0 if alumno["sexo"] == "M" else 1
    )

    if st.button("Actualizar Registro"):

        supabase.table("Alumnos2").update({
            "apellidos": nuevo_apellido,
            "nombres": nuevo_nombre,
            "edad": nueva_edad,
            "sexo": nuevo_sexo
        }).eq("dni", alumno["dni"]).execute()

        st.success("Registro actualizado")

# =====================================
# ELIMINAR REGISTRO
# =====================================
st.subheader("🗑️ Eliminar Alumno")

dni_eliminar = st.text_input("DNI a eliminar")

if st.button("Eliminar"):

    supabase.table("Alumnos2").delete().eq(
        "dni",
        dni_eliminar
    ).execute()

    st.success("Registro eliminado")
