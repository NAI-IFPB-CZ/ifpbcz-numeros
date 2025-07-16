import streamlit as st
import base64
import os

def get_base64_image(image_path):
    """Converte imagem para base64"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

def display_header_with_logo(title):
    """Exibe cabeçalho com logo do IFPB"""
    logo_path = os.path.join("logo-ifpb", "IFPB-cz.png")
    
    # Tentar carregar o logo
    logo_base64 = get_base64_image(logo_path)
    
    if logo_base64:
        st.markdown(f"""
        <div class="main-header">
            <div class="header-logo">
                <img src="data:image/png;base64,{logo_base64}" alt="IFPB Logo">
            </div>
            {title}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="main-header">{title}</div>', unsafe_allow_html=True)

def display_footer():
    """Exibe rodapé customizado"""
    st.markdown("""
    <div style="
        background: linear-gradient(90deg, #0d5a4e, #1a8c73);
        color: white;
        padding: 1rem;
        text-align: center;
        margin-top: 3rem;
        border-radius: 10px;
        font-size: 0.9rem;
    ">
        <p style="margin: 0;">
            <strong>Sistema de Visualização de Dados Institucionais - IFPB Campus Cajazeiras</strong><br>
            Desenvolvido com ❤️ pela equipe NAI | 2025
        </p>
    </div>
    """, unsafe_allow_html=True)
