import hashlib
import pickle
from pathlib import Path
import bcrypt
import streamlit as st
import streamlit_authenticator as stauth

def projeto():
    import ProjetoCanhadas
    ProjetoCanhadas.main()

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    print(hashed)
    return hashed

def verify_password(password, hashed_password):
    # Converte a senha hash-ada de string para bytes
    hashed_password_bytes = hashed_password.encode()
    return bcrypt.checkpw(password.encode(), hashed_password_bytes)


def authenticate():
    nomes = ["Henrique Canhadas", "Vitor Lucas"]
    usernames = ["henrique.canhadas", "vitor.lucas"]

    file_path = Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

    # Captura de dados de entrada do usuário
    username_input = st.text_input("Usuário")
    password_input = st.text_input("Senha", type="password")

    # Verifica se as credenciais são válidas
    if st.button("Login"):
        if username_input in usernames:
            print(username_input)
            index = usernames.index(username_input)
            # Verifica se a senha digitada corresponde à senha armazenada
            if verify_password(password_input, hashed_passwords[index]):
                # Se as credenciais estiverem corretas, define o status de autenticação como True
                st.session_state["authentication_status"] = True
                return
        # Se as credenciais estiverem incorretas, define o status de autenticação como False
        st.session_state["authentication_status"] = False

def main():
    st.set_page_config(page_title="Projeto Canhadas", page_icon="servmarico.ico")
        
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    titulo = st.title("SERVMAR")

    st.session_state["authentication_status"] = None 
    authenticate()
    
    if st.session_state.get("authentication_status"):
        titulo.empty()
        success_message = st.success("Login Feito, Seja Bem Vindo!")
        projeto()
        success_message.empty()  # Remove a mensagem após 3 segundos
    elif st.session_state.get("authentication_status") is False:
        st.error("Usuário e/ou Senha Incorretos")
    elif st.session_state.get("authentication_status") is None:
        st.warning("Digite um usuário e uma senha")

if __name__ == "__main__":
    main()
