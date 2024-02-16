import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import time

def projeto():
    import ProjetoCanhadas
    ProjetoCanhadas.main()

def authenticate():
    st.session_state["authentication_status"] = None  # Definir sempre como None para solicitar login
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    autenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    autenticator.login()

def main():
    st.set_page_config(page_title="Projeto Canhadas", page_icon="servmarico.ico") 
    st.session_state["authentication_status"] = None 
    authenticate()

    if st.session_state.get("authentication_status"):
        success_message = st.success("Login Feito, Seja Bem Vindo")
        time.sleep(3) 
        projeto()
        success_message.empty()  # Remove a mensagem após 3 segundos
    elif st.session_state["authentication_status"] is False:
        st.error("Usuário/Senha Inválidos")
    elif st.session_state["authentication_status"] is None:
        st.warning("Digite um usuário e uma senha")

if __name__ == "__main__":
    main()
