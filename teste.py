# Importando a biblioteca Streamlit e a biblioteca numpy
import streamlit as st
import numpy as np

# Definindo o título da aba, ícone e layout
titulo_aba = "Meu Aplicativo"
icone_aba = "👀"  # Substitua pelo emoji ou caminho do ícone desejado
layout_aba = "centered"  # Outras opções: "centered"

# Usando st.set_page_config para configurar título, ícone e layout da aba
st.set_page_config(page_title=titulo_aba, page_icon=icone_aba, layout=layout_aba)

# Criando uma função para gerar dados aleatórios
def generate_data(num_pontos):
    data = {
        'x': list(range(num_pontos)),
        'y': np.random.randn(num_pontos)
    }
    return data

# Criando o aplicativo Streamlit
def main():
    # Título do aplicativo
    st.title('Aplicativo Streamlit Interativo')

    # Sidebar para configurações
    st.sidebar.header('Configurações')

    # Número de pontos
    num_pontos = st.sidebar.slider('Número de Pontos:', min_value=1, max_value=200, value=90)

    # Gerando dados aleatórios
    data = generate_data(num_pontos)

    # Exibindo o DataFrame
    st.subheader('Dados Gerados Aleatoriamente')
    st.write(data)

    # Exibindo um gráfico interativo
    st.subheader('Gráfico Interativo')
    st.line_chart(data)

if __name__ == "__main__":
    main()
