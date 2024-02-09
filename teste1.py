import streamlit as st
import pandas as pd
import os
import Ceimic
import Organizar
import Analise2
import Analise3

def abrir_radiobutton_modal(contador, escolha_anterior=None):
    valor_primario = None
    valor_secundario = None
    ordem_planilhas = None
    ordem_planilhas2 = None

    chave_radio = f"lab_radio_{contador}"
    escolha = st.radio("Selecione o Laboratório", ["Cetesb", "EPA", "Lista Holandesa", "Conama-420"], key=chave_radio)

    if escolha == "Cetesb" or escolha != escolha_anterior:
        if escolha == "Cetesb":
            ordem_planilhas = "c"
            chave_radio_cetesb = f"cetesb_radio_{contador}"
            escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Cetesb", ["Solo Agrícola", "Solo Residencial", "Solo Industrial", "Água subterrânea"], key=chave_radio_cetesb)
            if escolha_matriz == "Solo Agrícola":
                valor_primario = 1
            elif escolha_matriz == "Solo Residencial":
                valor_primario = 2
            elif escolha_matriz == "Solo Industrial":
                valor_primario = 3
            elif escolha_matriz == "Água subterrânea":
                valor_primario = 4
        elif escolha == "EPA":
            chave_radio_epa = f"epa_radio_{contador}"
            ordem_planilhas = "e"
            escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da EPA", ["Res Solo", "Água subterrânea", "Res Ar", "Solo para GW 1123", "Ind Solo", "Ind Air"], key=chave_radio_epa)
            if escolha_matriz == "Res Solo":
                valor_primario = 1
            elif escolha_matriz == "Água subterrânea":
                valor_primario = 2
            elif escolha_matriz == "Res Ar":
                valor_primario = 3
            elif escolha_matriz == "Solo para GW 1123":
                valor_primario = 4
            elif escolha_matriz == "Ind Solo":
                valor_primario = 5
            elif escolha_matriz == "Ind Air":
                valor_primario = 6
        elif escolha == "Lista Holandesa":
            chave_radio_listaholandesa = f"listaholandesa_radio_{contador}"
            ordem_planilhas = "l"
            escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Lista Holandesa", ["Solo Agricola", "Solo Residencial", "Agua Subterranea"], key=chave_radio_listaholandesa)
            if escolha_matriz == "Solo Agricola":
                valor_primario = 1
            elif escolha_matriz == "Solo Residencial":
                valor_primario = 2
            elif escolha_matriz == "Agua Subterranea":
                valor_primario = 3
        elif escolha == "Conama-420":
            chave_radio_conama = f"conama_radio_{contador}"
            ordem_planilhas = "o"
            escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Conama-420", ["Solo Prevenção", "Solo Agricola", "Solo Residencial", "Solo Industrial", "Agua Subterranea"], key=chave_radio_conama)
            if escolha_matriz == "Solo Prevenção":
                valor_primario = 1
            elif escolha_matriz == "Solo Agricola":
                valor_primario = 2
            elif escolha_matriz == "Solo Residencial":
                valor_primario = 3
            elif escolha_matriz == "Solo Industrial":
                valor_primario = 4
            elif escolha_matriz == "Agua Subterranea":
                valor_primario = 5

    # Adicionar segunda seleção de laboratório
    # Restante do código continua a mesma lógica para a segunda seleção

    return valor_primario, valor_secundario, ordem_planilhas, ordem_planilhas2, escolha

def carregar_analise(file_path, novo_caminho, escolha, quantidade_analise,valor_primario, valor_secundario, ordem_planilhas, ordem_planilhas2):
    st.write("Rodando Verificador")
    Ceimic.main(file_path, novo_caminho)
    st.write("Rodando Organizador")
    Organizar.main(novo_caminho)
    st.write("Rodando Análise")
    if quantidade_analise == 3 and escolha == "Ceimic":
        Analise3.main(novo_caminho)
    elif quantidade_analise == 2 and escolha == "Ceimic":
        Analise2.main(novo_caminho,valor_primario, valor_secundario, ordem_planilhas, ordem_planilhas2)
    st.write("Terminou a Análise")

def main():
    st.title("SERVMAR")
    st.write("Projeto Canhadas")

    uploaded_file = st.file_uploader("Carregar Excel", type=["xlsx", "xls"])

    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.write("Dados do Excel:")
        st.write(df)

        diretório, _ = os.path.split(uploaded_file.name)
        novo_caminho = st.text_input("Digite o nome do novo arquivo:", key="novo_caminho", value=os.path.join(diretório, "novo_arquivo.xlsx"))

        quantidade_analise = st.radio("Escolha a quantidade de Valores Orientadores", [2, 3])

        escolha = st.radio("Escolha de qual laboratório a análise deve ser feita", ["Ceimic"])

        st.text("Escolha os Valores Orientadores")
        valor_primario, valor_secundario, ordem_planilhas, ordem_planilhas2, escolha = abrir_radiobutton_modal(2)
        carregar_analise(uploaded_file, novo_caminho, escolha, quantidade_analise,valor_primario, valor_secundario, ordem_planilhas, ordem_planilhas2)
        

        if st.button("Fazer Análise"):
            st.write("Rodando análise...")
            st.write("Pronto para rodar")

if __name__ == "__main__":
    main()
