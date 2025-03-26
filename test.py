import streamlit as st 
st.markdown(
    "<h1 style='font-size:30px; font-family:Arial; color:dark;'text-align: center;'>Bienvenue dans la galerie privée de Camille Caussel</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<h1 style='font-size:20px; font-family:Arial; color:grey;'text-align: center;'>Photos de charme accessibles gratuitement</h1>", 
    unsafe_allow_html=True
)
search_query = st.text_input("🔍 Rechercher :", "")
if search_query:
    st.write(f"Résultats pour : **{search_query}**")
st.image("https://media.istockphoto.com/photos/defocused-backyard-background-picture-id1125087982?k=20&m=1125087982&s=612x612&w=0&h=DOP2B-pjMzXxQjkSecVdZP-JuFpKXkMCMfx9MAlFDho=", caption="créée un compte premium pour voir cette image")
