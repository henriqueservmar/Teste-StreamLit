import streamlit as st
import os
import pandas as pd
from pathlib import Path


def abrir_radiobutton_modal_3_valores(contador, escolha_anterior=None,):
    valor_primario = None
    ordem_planilhas = None
    valor_secundario = None
    ordem_planilhas2 = None
    valor_terceario = None
    ordem_planilhas3 = None

    col1, col2, col3 = st.columns(3)
    with col1:
        # Gerar uma chave única para o widget radio
        chave_radio = f"lab_radio_{contador}"
        escolha1 = st.radio("Primeiro Valor de Referencia:", ["Cetesb", "EPA", "Lista Holandesa", "Conama-420"], key=chave_radio, index=None)
    with col1:
        if escolha1 == "Cetesb" or escolha1 != escolha_anterior:
            if escolha1 == "Cetesb":
                ordem_planilhas = "c"
                # Gerar uma chave única para o widget radio dentro do if
                chave_radio_cetesb = f"cetesb_radio_{contador}"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Cetesb", ["Solo Agrícola", "Solo Residencial", "Solo Industrial", "Água subterrânea"], key=chave_radio_cetesb, index=None)
                if escolha_matriz == "Solo Agrícola":
                    valor_primario = 1
                elif escolha_matriz == "Solo Residencial":
                    valor_primario = 2
                elif escolha_matriz == "Solo Industrial":
                    valor_primario = 3
                elif escolha_matriz == "Água subterrânea":
                    valor_primario = 4
            elif escolha1 == "EPA":
                # Gerar uma chave única para o widget radio dentro do if
                chave_radio_epa = f"epa_radio_{contador}"
                ordem_planilhas = "e"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da EPA", ["Res Solo", "Água subterrânea", "Res Ar", "Solo para GW 1123", "Ind Solo", "Ind Air"], key=chave_radio_epa, index=None)
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
            elif escolha1 == "Lista Holandesa":
                chave_radio_listaholandesa = f"listaholandesa_radio_{contador}"
                ordem_planilhas = "l"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Lista Holandesa", ["Solo Agricola", "Solo Residencial", "Agua Subterranea"], key=chave_radio_listaholandesa, index=None)
                if escolha_matriz == "Solo Agricola":
                    valor_primario = 1
                elif escolha_matriz == "Solo Residencial":
                    valor_primario = 2
                elif escolha_matriz == "Agua Subterranea":
                    valor_primario = 3
            elif escolha1 == "Conama-420":
                chave_radio_conama = f"conama_radio_{contador}"
                ordem_planilhas = "o"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Conama-420", ["Solo Prevenção", "Solo Agricola", "Solo Residencial", "Solo Industrial", "Agua Subterranea"], key=chave_radio_conama, index=None)
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

    contador = 3

    with col2:
        chave_radio = f"lab_radio_{contador}"
        escolha = st.radio("Segundo Valor de Referencia:", ["Cetesb", "EPA", "Lista Holandesa", "Conama-420"], key=chave_radio, index=None)
    with col2:
        if escolha == "Cetesb" or escolha != escolha_anterior:
            if escolha == "Cetesb":
                ordem_planilhas2 = "c"
                # Gerar uma chave única para o widget radio dentro do if
                chave_radio_cetesb = f"cetesb_radio_{contador}"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Cetesb", ["Solo Agrícola", "Solo Residencial", "Solo Industrial", "Água subterrânea"], key=chave_radio_cetesb,index=None)
                if escolha_matriz == "Solo Agrícola":
                    valor_secundario = 1
                elif escolha_matriz == "Solo Residencial":
                    valor_secundario = 2
                elif escolha_matriz == "Solo Industrial":
                    valor_secundario = 3
                elif escolha_matriz == "Água subterrânea":
                    valor_secundario = 4
            elif escolha == "EPA":
                # Gerar uma chave única para o widget radio dentro do if
                chave_radio_epa = f"epa_radio_{contador}"
                ordem_planilhas2 = "e"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da EPA", ["Res Solo", "Água subterrânea", "Res Ar", "Solo para GW 1123", "Ind Solo", "Ind Air"], key=chave_radio_epa, index=None)
                if escolha_matriz == "Res Solo":
                    valor_secundario = 1
                elif escolha_matriz == "Água subterrânea":
                    valor_secundario = 2
                elif escolha_matriz == "Res Ar":
                    valor_secundario = 3
                elif escolha_matriz == "Solo para GW 1123":
                    valor_secundario = 4
                elif escolha_matriz == "Ind Solo":
                    valor_secundario = 5
                elif escolha_matriz == "Ind Air":
                    valor_secundario = 6
            elif escolha == "Lista Holandesa":
                chave_radio_listaholandesa = f"listaholandesa_radio_{contador}"
                ordem_planilhas2 = "l"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Lista Holandesa", ["Solo Agricola", "Solo Residencial", "Agua Subterranea"], key=chave_radio_listaholandesa, index=None)
                if escolha_matriz == "Solo Agricola":
                    valor_secundario = 1
                elif escolha_matriz == "Solo Residencial":
                    valor_secundario = 2
                elif escolha_matriz == "Agua Subterranea":
                    valor_secundario = 3
            elif escolha == "Conama-420":
                chave_radio_conama = f"conama_radio_{contador}"
                ordem_planilhas2 = "o"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Conama-420", ["Solo Prevenção", "Solo Agricola", "Solo Residencial", "Solo Industrial", "Agua Subterranea"], key=chave_radio_conama, index=None)
                if escolha_matriz == "Solo Prevenção":
                    valor_secundario = 1
                elif escolha_matriz == "Solo Agricola":
                    valor_secundario = 2
                elif escolha_matriz == "Solo Residencial":
                    valor_secundario = 3
                elif escolha_matriz == "Solo Industrial":
                    valor_secundario = 4
                elif escolha_matriz == "Agua Subterranea":
                    valor_secundario = 5

    contador = 4

    with col3:
        chave_radio = f"lab_radio_{contador}"
        escolha2 = st.radio("Terceiro Valor de Referencia:", ["Cetesb", "EPA", "Lista Holandesa", "Conama-420"], key=chave_radio, index=None)
    
    with col3:
        if escolha2 == "Cetesb" or escolha2 != escolha_anterior:
            if escolha2 == "Cetesb":
                ordem_planilhas3 = "c"
                # Gerar uma chave única para o widget radio dentro do if
                chave_radio_cetesb = f"cetesb_radio_{contador}"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Cetesb", ["Solo Agrícola", "Solo Residencial", "Solo Industrial", "Água subterrânea"], key=chave_radio_cetesb, index=None)
                if escolha_matriz == "Solo Agrícola":
                    valor_terceario = 1
                elif escolha_matriz == "Solo Residencial":
                    valor_terceario = 2
                elif escolha_matriz == "Solo Industrial":
                    valor_terceario = 3
                elif escolha_matriz == "Água subterrânea":
                    valor_terceario = 4
            elif escolha2 == "EPA":
                # Gerar uma chave única para o widget radio dentro do if
                chave_radio_epa = f"epa_radio_{contador}"
                ordem_planilhas3 = "e"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da EPA", ["Res Solo", "Água subterrânea", "Res Ar", "Solo para GW 1123", "Ind Solo", "Ind Air"], key=chave_radio_epa, index=None)
                if escolha_matriz == "Res Solo":
                    valor_terceario = 1
                elif escolha_matriz == "Água subterrânea":
                    valor_terceario = 2
                elif escolha_matriz == "Res Ar":
                    valor_terceario = 3
                elif escolha_matriz == "Solo para GW 1123":
                    valor_terceario = 4
                elif escolha_matriz == "Ind Solo":
                    valor_terceario = 5
                elif escolha_matriz == "Ind Air":
                    valor_terceario = 6
            elif escolha2 == "Lista Holandesa":
                chave_radio_listaholandesa = f"listaholandesa_radio_{contador}"
                ordem_planilhas3 = "l"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Lista Holandesa", ["Solo Agricola", "Solo Residencial", "Agua Subterranea"], key=chave_radio_listaholandesa, index=None)
                if escolha_matriz == "Solo Agricola":
                    valor_terceario = 1
                elif escolha_matriz == "Solo Residencial":
                    valor_terceario = 2
                elif escolha_matriz == "Agua Subterranea":
                    valor_terceario = 3
            elif escolha2 == "Conama-420":
                chave_radio_conama = f"conama_radio_{contador}"
                ordem_planilhas3 = "o"
                escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Conama-420", ["Solo Prevenção", "Solo Agricola", "Solo Residencial", "Solo Industrial", "Agua Subterranea"], key=chave_radio_conama, index=None)
                if escolha_matriz == "Solo Prevenção":
                    valor_terceario = 1
                elif escolha_matriz == "Solo Agricola":
                    valor_terceario = 2
                elif escolha_matriz == "Solo Residencial":
                    valor_terceario = 3
                elif escolha_matriz == "Solo Industrial":
                    valor_terceario = 4
                elif escolha_matriz == "Agua Subterranea":
                    valor_terceario = 5
    
        return valor_primario, ordem_planilhas, valor_secundario, ordem_planilhas2, valor_terceario, ordem_planilhas3
    
def abrir_radiobutton_modal_2_valores(contador, escolha_anterior=None,):
    valor_primario = None
    ordem_planilhas = None
    valor_secundario = None
    ordem_planilhas2 = None

    col1, col2 = st.columns(2)
    # Gerar uma chave única para o widget radio

    with st.container(border=True):  
        with col1:
            chave_radio = f"lab_radio_{contador}"
            escolha1 = st.radio("Primeiro Valor de Referencia:", ["Cetesb", "EPA", "Lista Holandesa", "Conama-420"], key=chave_radio, index=None)

        with col1:
            if escolha1 == "Cetesb" or escolha1 != escolha_anterior:
                with col1:
                    if escolha1 == "Cetesb":
                        ordem_planilhas = "c"
                        # Gerar uma chave única para o widget radio dentro do if
                        chave_radio_cetesb = f"cetesb_radio_{contador}"
                        escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Cetesb", ["Solo Agrícola", "Solo Residencial", "Solo Industrial", "Água subterrânea"], key=chave_radio_cetesb, index=None)
                        if escolha_matriz == "Solo Agrícola":
                            valor_primario = 1
                        elif escolha_matriz == "Solo Residencial":
                            valor_primario = 2
                        elif escolha_matriz == "Solo Industrial":
                            valor_primario = 3
                        elif escolha_matriz == "Água subterrânea":
                            valor_primario = 4
                    elif escolha1 == "EPA":
                        # Gerar uma chave única para o widget radio dentro do if
                        chave_radio_epa = f"epa_radio_{contador}"
                        ordem_planilhas = "e"
                        escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da EPA", ["Res Solo", "Água subterrânea", "Res Ar", "Solo para GW 1123", "Ind Solo", "Ind Air"], key=chave_radio_epa, index=None)
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
                    elif escolha1 == "Lista Holandesa":
                        chave_radio_listaholandesa = f"listaholandesa_radio_{contador}"
                        ordem_planilhas = "l"
                        escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Lista Holandesa", ["Solo Agricola", "Solo Residencial", "Agua Subterranea"], key=chave_radio_listaholandesa, index=None)
                        if escolha_matriz == "Solo Agricola":
                            valor_primario = 1
                        elif escolha_matriz == "Solo Residencial":
                            valor_primario = 2
                        elif escolha_matriz == "Agua Subterranea":
                            valor_primario = 3
                    elif escolha1 == "Conama-420":
                        chave_radio_conama = f"conama_radio_{contador}"
                        ordem_planilhas = "o"
                        escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Conama-420", ["Solo Prevenção", "Solo Agricola", "Solo Residencial", "Solo Industrial", "Agua Subterranea"], key=chave_radio_conama, index=None)
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

    contador = 3
    
    with st.container(border=True):  
        with col2:
            chave_radio = f"lab_radio_{contador}"
            escolha = st.radio("Segundo Valor de Referencia:", ["Cetesb", "EPA", "Lista Holandesa", "Conama-420"], key=chave_radio, index=None)

        if escolha == "Cetesb" or escolha != escolha_anterior:
            with col2:
                if escolha == "Cetesb":
                    ordem_planilhas2 = "c"
                    # Gerar uma chave única para o widget radio dentro do if
                    chave_radio_cetesb = f"cetesb_radio_{contador}"
                    escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Cetesb", ["Solo Agrícola", "Solo Residencial", "Solo Industrial", "Água subterrânea"], key=chave_radio_cetesb,index=None)
                    if escolha_matriz == "Solo Agrícola":
                        valor_secundario = 1
                    elif escolha_matriz == "Solo Residencial":
                        valor_secundario = 2
                    elif escolha_matriz == "Solo Industrial":
                        valor_secundario = 3
                    elif escolha_matriz == "Água subterrânea":
                        valor_secundario = 4
                elif escolha == "EPA":
                    # Gerar uma chave única para o widget radio dentro do if
                    chave_radio_epa = f"epa_radio_{contador}"
                    ordem_planilhas2 = "e"
                    escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da EPA", ["Res Solo", "Água subterrânea", "Res Ar", "Solo para GW 1123", "Ind Solo", "Ind Air"], key=chave_radio_epa, index=None)
                    if escolha_matriz == "Res Solo":
                        valor_secundario = 1
                    elif escolha_matriz == "Água subterrânea":
                        valor_secundario = 2
                    elif escolha_matriz == "Res Ar":
                        valor_secundario = 3
                    elif escolha_matriz == "Solo para GW 1123":
                        valor_secundario = 4
                    elif escolha_matriz == "Ind Solo":
                        valor_secundario = 5
                    elif escolha_matriz == "Ind Air":
                        valor_secundario = 6
                elif escolha == "Lista Holandesa":
                    chave_radio_listaholandesa = f"listaholandesa_radio_{contador}"
                    ordem_planilhas2 = "l"
                    escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Lista Holandesa", ["Solo Agricola", "Solo Residencial", "Agua Subterranea"], key=chave_radio_listaholandesa, index=None)
                    if escolha_matriz == "Solo Agricola":
                        valor_secundario = 1
                    elif escolha_matriz == "Solo Residencial":
                        valor_secundario = 2
                    elif escolha_matriz == "Agua Subterranea":
                        valor_secundario = 3
                elif escolha == "Conama-420":
                    chave_radio_conama = f"conama_radio_{contador}"
                    ordem_planilhas2 = "o"
                    escolha_matriz = st.radio("Selecione a matriz e/ou o cenário ambiental da Conama-420", ["Solo Prevenção", "Solo Agricola", "Solo Residencial", "Solo Industrial", "Agua Subterranea"], key=chave_radio_conama, index=None)
                    if escolha_matriz == "Solo Prevenção":
                        valor_secundario = 1
                    elif escolha_matriz == "Solo Agricola":
                        valor_secundario = 2
                    elif escolha_matriz == "Solo Residencial":
                        valor_secundario = 3
                    elif escolha_matriz == "Solo Industrial":
                        valor_secundario = 4
                    elif escolha_matriz == "Agua Subterranea":
                        valor_secundario = 5

    return valor_primario, ordem_planilhas, valor_secundario, ordem_planilhas2

def carregar_analise_3_valores(uploaded_file, novo_caminho, escolha, quantidade_analise, valor_primario, ordem_planilhas, valor_secundario, ordem_planilhas2, valor_terceario, ordem_planilhas3):
    progresso = 0
    
    if quantidade_analise == 3 and escolha == "Ceimic":
        # Etapa 1: Importar Ceimic
        import Ceimic
        Ceimic.main(uploaded_file, novo_caminho)
        progresso += 33
        yield progresso
        
        # Etapa 2: Organizar
        import Organizar
        Organizar.main(novo_caminho)
        progresso += 33
        yield progresso
        
        # Etapa 3: Analise3
        import Analise3
        Analise3.main(novo_caminho, valor_primario, ordem_planilhas, valor_secundario, ordem_planilhas2, valor_terceario, ordem_planilhas3)
        progresso += 34
        yield progresso

def carregar_analise_2_valores(uploaded_file, novo_caminho, escolha, quantidade_analise, valor_primario, ordem_planilhas, valor_secundario, ordem_planilhas2):
    progresso = 0
    

    if quantidade_analise == 2 and escolha == "Ceimic":
        # Etapa 1: Importar Ceimic
        import Ceimic
        Ceimic.main(uploaded_file, novo_caminho)
        progresso += 25
        yield progresso


        # Etapa 2: Organizar
        import Organizar
        Organizar.main(novo_caminho)
        progresso += 40
        yield progresso
        df = pd.read_excel(novo_caminho)
        st.write(df)


        # Etapa 3: Analise2
        import Analise2
        Analise2.main(novo_caminho, valor_primario, ordem_planilhas, valor_secundario, ordem_planilhas2)
        progresso += 35
        yield progresso
        df = pd.read_excel(novo_caminho)
        st.write(df)
        


#    hide_menu_style = """
#            <style>
#            #MainMenu {visibility: hidden;}
#                footer {visibility: hidden;}
#                header {visibility: hidden;}
#            </style>
#            """
#    st.markdown(hide_menu_style, unsafe_allow_html=True)

def main():
    st.title("SERVMAR")
    st.subheader("Projeto Canhadas")
    
    uploaded_file = st.file_uploader("Carregue seu arquivo Excel:", type=["xlsx", "xls"], key="excel_uploader_1", label_visibility="visible")

    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.write("Dados do arquivo Excel:")
        st.write(df)

        nome_arquivo = st.text_input("Digite o nome do novo arquivo:", key="nome_arquivo1")

        if nome_arquivo:
            novo_caminho = criar_excel_vazio(nome_arquivo, uploaded_file)
        else:
            st.warning("Por favor, insira um nome para o novo arquivo.") 
            novo_caminho = None

        col1, col2 = st.columns(2)

        with col1:
            escolha = st.radio("Escolha de qual laboratório a análise deve ser feita:", ["Ceimic"], key="escolha_laboratorio_1")
        
        with col2:
            quantidade_analise_options = {"2 Valores Orientadores": 2, "3 Valores Orientadores": 3}
            quantidade_analise_texto = st.radio("Escolha a quantidade de Valores Orientadores:", list(quantidade_analise_options.keys()), key="quantidade_analise_1", index=None)

        if quantidade_analise_texto in quantidade_analise_options:
            quantidade_analise = quantidade_analise_options[quantidade_analise_texto]
        else:
            st.warning("Por favor, insira um nome para o novo arquivo.")
            quantidade_analise = None

        if quantidade_analise == 2:
            valor_primario = None
            ordem_planilhas = None
            valor_secundario = None
            ordem_planilhas2 = None

            valor_primario, ordem_planilhas, valor_secundario, ordem_planilhas2 = abrir_radiobutton_modal_2_valores(2)

        elif quantidade_analise == 3:
            valor_primario = None
            ordem_planilhas = None
            valor_secundario = None
            ordem_planilhas2 = None
            valor_terceario = None
            ordem_planilhas3 = None

            col1, col2 = st.columns(2)

            valor_primario, ordem_planilhas, valor_secundario, ordem_planilhas2, valor_terceario, ordem_planilhas3 = abrir_radiobutton_modal_3_valores(2)

        if (quantidade_analise == 2 and (valor_primario is not None and ordem_planilhas is not None and valor_secundario is not None and ordem_planilhas2 is not None)) or (quantidade_analise == 3 and (valor_primario is not None and ordem_planilhas is not None and valor_secundario is not None and ordem_planilhas2 is not None and valor_terceario is not None and ordem_planilhas3 is not None)):
           
            st.divider()  
    
            if st.button("Fazer Análise", type="primary"):
                if novo_caminho:
                    progresso_placeholder = st.empty()
                    progresso_bar = progresso_placeholder.progress(0)
                    if quantidade_analise == 2:
                        for progresso in carregar_analise_2_valores(uploaded_file, novo_caminho, escolha, quantidade_analise, valor_primario, ordem_planilhas, valor_secundario, ordem_planilhas2):
                            progresso_bar.progress(progresso)
                    elif quantidade_analise == 3:
                        for progresso in carregar_analise_3_valores(uploaded_file, novo_caminho, escolha, quantidade_analise, valor_primario, ordem_planilhas, valor_secundario, ordem_planilhas2, valor_terceario, ordem_planilhas3):
                            progresso_bar.progress(progresso)
                    download_excel(novo_caminho)
                    df = pd.read_excel(novo_caminho)
                    st.write(df)
                else:
                    st.error("Erro ao criar o novo arquivo. Verifique o nome e tente novamente.")

def criar_excel_vazio(nome_arquivo, uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        downloads_path = str(Path.home() / "Downloads")
        novo_caminho_download = os.path.join(downloads_path, nome_arquivo + ".xlsx")
        df.to_excel(novo_caminho_download, index=False)
        return novo_caminho_download
    except Exception as e:
        st.error(f"Erro ao criar o novo arquivo: {e}")
        return None

def download_excel(novo_caminho):
    # Configurar o nome do arquivo para download
    nome_arquivo = os.path.basename(novo_caminho)
    
    with open(novo_caminho, "rb") as file:
        # Ler os bytes do arquivo
        file_bytes = file.read()
    
    # Configurar o botão de download
    with st.spinner("Baixando Excel..."):
        st.success("Download concluído. Clique abaixo para baixar.")
        st.download_button(
            label="Baixar Resultado da Análise",
            data=file_bytes,
            file_name=nome_arquivo,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                
    
if __name__ == "__main__":
    main()
