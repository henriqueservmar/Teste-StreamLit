import streamlit as st

# Definindo o título da aba, ícone e layout
titulo_aba = "Meu Aplicativo"
icone_aba = "👀"  # Substitua pelo emoji ou caminho do ícone desejado
layout_aba = "centered"  # Outras opções: "centered"

# Usando st.set_page_config para configurar título, ícone e layout da aba
st.set_page_config(page_title=titulo_aba, page_icon=icone_aba, layout=layout_aba)

# Título do aplicativo
st.title('Aplicativo Streamlit Interativo')

# Sidebar para configuraçõesleia
st.sidebar.header('Configurações')

# Número de pontos
num_pontos = st.sidebar.slider('Número de Pontos:', min_value=1, max_value=200, value=90)


