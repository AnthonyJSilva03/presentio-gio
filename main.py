import streamlit as st
from app import mostrar_presente

st.set_page_config(page_title="Meu Amor", layout="wide")

if 'entrou' not in st.session_state:
    st.session_state['entrou'] = False

# 1. Criamos um "espaço reservado" que pode ser apagado na hora
tela_inicial = st.empty()

# 2. A Página Inicial
if not st.session_state['entrou']:
    
    # Colocamos TUDO da capa dentro desse espaço reservado
    with tela_inicial.container():
        
        fundo_capa_css = """
        <style>
        .stApp {
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        div[data-testid="stVerticalBlock"] > div {
            animation: surgirSuave 1.2s ease-out forwards;
            opacity: 0;
        }

        @keyframes surgirSuave {
            0% { opacity: 0; transform: translateY(40px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        div[data-testid="stVerticalBlock"] > div:nth-child(1) { animation-delay: 0.2s; }
        div[data-testid="stVerticalBlock"] > div:nth-child(2) { animation-delay: 0.5s; }
        div[data-testid="stVerticalBlock"] > div:nth-child(3) { animation-delay: 0.8s; }
        div[data-testid="stVerticalBlock"] > div:nth-child(4) { animation-delay: 1.1s; }
        div[data-testid="stVerticalBlock"] > div:nth-child(5) { animation-delay: 1.5s; }
        </style>
        """
        st.markdown(fundo_capa_css, unsafe_allow_html=True)
        
        for _ in range(5):
            st.write("")
        
        col_texto1, col_texto2, col_texto3 = st.columns([0.2, 0.6, 0.2])
        col_btn1, col_btn2, col_btn3 = st.columns([0.4, 0.2, 0.4])
        with col_btn2:
            if st.button("Abrir o Presente 🎁", use_container_width=True):
                st.session_state['entrou'] = True
                tela_inicial.empty()
                st.rerun()

if st.session_state['entrou']:
    mostrar_presente()