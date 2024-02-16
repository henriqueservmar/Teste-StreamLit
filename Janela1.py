import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth

def projeto():
    import ProjetoCanhadas
    ProjetoCanhadas.main()

def authenticate():
    nomes = ["Henrique Canhadas", "Vitor Lucas"]
    usernames = ["henrique.canhadas", "vitor.lucas"]

    file_path = Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

    authenticator = stauth.Authenticate(nomes, usernames, hashed_passwords,cookie_name="CookieLogin", cookie_expiry_days=0.0013888)

    
    authenticator.login("Login")

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
