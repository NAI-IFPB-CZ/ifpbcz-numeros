import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random
import base64
import os

# Função para converter imagem para base64
def get_base64_image(image_path):
    """Converte imagem para base64"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Função para exibir logo no cabeçalho
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

# Configuração da página
st.set_page_config(
    page_title="Sistema de Visualização de Dados Institucionais - IFPB-CZ",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# CSS customizado para tema verde e branco
st.markdown("""
<style>
    /* Esconder elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    .stAppDeployButton {display: none;}
    .stDecoration {display: none;}
    .stActionButton {display: none;}
    .stToolbar {display: none;}
    .stMenuItem {display: none;}
    .stApp > header {display: none;}
    .stApp > div[data-testid="stToolbar"] {display: none;}
    .stApp > div[data-testid="stDecoration"] {display: none;}
    .stApp > div[data-testid="stStatusWidget"] {display: none;}
    
    /* Preservar botão de controle da sidebar */
    button[data-testid="collapsedControl"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        z-index: 999999 !important;
        background-color: #1a8c73 !important;
        color: white !important;
        border: none !important;
        padding: 0.5rem !important;
        border-radius: 0 0 0.5rem 0 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
    }
    
    /* Estilo para quando a sidebar está expandida */
    .stSidebar button[data-testid="baseButton-header"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        background-color: #1a8c73 !important;
        color: white !important;
        border: none !important;
    }
    
    /* Esconder botão de fork */
    .stAppViewContainer > .main > div[data-testid="stToolbar"] {
        display: none;
    }
    
    /* Esconder watermark "Made with Streamlit" */
    a[href^="https://streamlit.io"] {
        display: none !important;
    }
    
    /* Esconder elementos de debug */
    .stException {display: none;}
    .stAlert {display: none;}
    
    /* Garantir que o botão de controle da sidebar sempre seja visível */
    .stSidebar .stButton button,
    [data-testid="collapsedControl"],
    [data-testid="baseButton-header"],
    .stSidebar button[kind="header"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: all !important;
    }
    
    /* Estilo específico para o botão de colapsar quando sidebar está fechada */
    [data-testid="collapsedControl"] {
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        z-index: 999999 !important;
        background-color: #1a8c73 !important;
        color: white !important;
        border: none !important;
        padding: 0.5rem 0.75rem !important;
        border-radius: 0 0 0.5rem 0 !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important;
    }
    
    /* Hover do botão de controle */
    [data-testid="collapsedControl"]:hover {
        background-color: #0d5a4e !important;
        transform: scale(1.05) !important;
        transition: all 0.2s ease !important;
    }
    
    /* Customizar aparência da página */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Garantir que todos os elementos de fundo sejam brancos */
    .main .block-container {
        background-color: #f8f9fa;
        padding: 2rem;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    
    .stSelectbox > div > div {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 4px;
    }
    
    /* Adicionar estilos para melhorar contraste */
    .stSelectbox > div > div > div {
        background-color: white !important;
        border: 1px solid #ddd !important;
        border-radius: 4px !important;
    }
    
    .stMultiSelect > div > div > div {
        background-color: white !important;
        border: 1px solid #ddd !important;
        border-radius: 4px !important;
    }
    
    .stSlider > div > div > div {
        background-color: white !important;
    }
    
    .stTextInput > div > div > input {
        background-color: white !important;
        border: 1px solid #ddd !important;
        border-radius: 4px !important;
    }
    
    .stNumberInput > div > div > input {
        background-color: white !important;
        border: 1px solid #ddd !important;
        border-radius: 4px !important;
    }
    
    /* Melhorar contraste dos botões */
    .stButton > button {
        background-color: #1a8c73 !important;
        color: white !important;
        border: 1px solid #0d5a4e !important;
        border-radius: 4px !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #0d5a4e !important;
        transform: translateY(-1px) !important;
    }
    
    /* Estilo principal */
    .main-header {
        background: linear-gradient(90deg, #0d5a4e, #1a8c73);
        color: white;
        padding: 2rem;
        margin: -1rem -1rem 2rem -1rem;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        position: relative;
    }
    
    .main-header::before {
        content: "";
        position: absolute;
        top: 1rem;
        left: 2rem;
        width: 60px;
        height: 60px;
        background: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMTMuMDkgOC4yNkwyMCA5TDEzLjA5IDE1Ljc0TDEyIDIyTDEwLjkxIDE1Ljc0TDQgOUwxMC45MSA4LjI2TDEyIDJaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K') no-repeat center;
        background-size: contain;
    }
    
    /* Logo no cabeçalho */
    .header-logo {
        position: absolute;
        top: 1rem;
        left: 2rem;
        width: 80px;
        height: 60px;
        background: white;
        border-radius: 8px;
        padding: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .header-logo img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }
    
    /* Cartões de KPI */
    .kpi-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #1a8c73;
        margin: 1rem 0;
        border: 1px solid #e0e0e0;
        transition: transform 0.2s ease;
    }
    
    .kpi-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .kpi-title {
        color: #0d5a4e;
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .kpi-value {
        color: #1a8c73;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
    }
    
    /* Sidebar */
    .sidebar .sidebar-content {
        background: white;
    }
    
    /* Filtros */
    .filter-container {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Gráficos */
    .chart-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border: 1px solid #e0e0e0;
    }
    
    .fonte-dados {
        color: #666;
        font-size: 0.9rem;
        font-style: italic;
        margin-top: 1rem;
        text-align: right;
    }
    
    /* Botões */
    .stButton > button {
        background-color: #1a8c73;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    
    /* CSS CRÍTICO: Garantir que o botão de controle da sidebar sempre seja visível */
    section[data-testid="stSidebar"] button[kind="header"],
    section[data-testid="stSidebar"] .stButton button,
    .stSidebar button[data-testid="baseButton-header"],
    button[data-testid="collapsedControl"],
    .css-1d391kg button,
    .css-1544g2n button {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: all !important;
        position: relative !important;
    }
    
    /* Forçar visibilidade do botão quando sidebar está colapsada */
    .stApp > div > div > div > div > button[data-testid="collapsedControl"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        z-index: 999999 !important;
        background-color: #1a8c73 !important;
        color: white !important;
        border: 2px solid #0d5a4e !important;
        padding: 0.5rem 0.75rem !important;
        border-radius: 0 0 0.5rem 0 !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important;
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
    }
    
    .stButton > button:hover {
        background-color: #0d5a4e;
    }
</style>

<script>
// JavaScript para garantir que o botão da sidebar sempre seja visível
function ensureSidebarButtonVisible() {
    // Procurar pelo botão de controle da sidebar
    const selectors = [
        '[data-testid="collapsedControl"]',
        '.stSidebar button[kind="header"]',
        '.stSidebar .stButton button',
        'button[data-testid="baseButton-header"]',
        '.css-1d391kg button',
        '.css-1544g2n button',
        '[data-testid="stSidebar"] button',
        'section[data-testid="stSidebar"] button'
    ];
    
    selectors.forEach(selector => {
        const button = document.querySelector(selector);
        if (button) {
            button.style.display = 'block';
            button.style.visibility = 'visible';
            button.style.opacity = '1';
            button.style.pointerEvents = 'all';
            button.style.zIndex = '999999';
            
            // Se for o botão colapsado, posicionar no canto superior esquerdo
            if (button.dataset.testid === 'collapsedControl') {
                button.style.position = 'fixed';
                button.style.left = '0';
                button.style.top = '0';
                button.style.backgroundColor = '#1a8c73';
                button.style.color = 'white';
                button.style.border = '2px solid #0d5a4e';
                button.style.padding = '0.5rem 0.75rem';
                button.style.borderRadius = '0 0 0.5rem 0';
                button.style.boxShadow = '0 2px 6px rgba(0,0,0,0.3)';
            }
        }
    });
}

// Função para forçar a abertura da sidebar
function forceSidebarOpen() {
    const sidebar = document.querySelector('[data-testid="stSidebar"]');
    if (sidebar) {
        sidebar.style.display = 'block';
        sidebar.style.visibility = 'visible';
        sidebar.style.opacity = '1';
        sidebar.style.transform = 'translateX(0)';
        sidebar.style.marginLeft = '0';
        sidebar.style.width = '21rem';
        sidebar.style.minWidth = '21rem';
        sidebar.style.maxWidth = '21rem';
        sidebar.style.position = 'relative';
        sidebar.style.zIndex = '999';
    }
}

// Executar quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    ensureSidebarButtonVisible();
    forceSidebarOpen();
});

// Executar a cada 100ms para garantir que o botão permaneça visível
setInterval(ensureSidebarButtonVisible, 100);

// Observar mudanças no DOM
const observer = new MutationObserver(function() {
    ensureSidebarButtonVisible();
});
observer.observe(document.body, { childList: true, subtree: true });
</script>
""", unsafe_allow_html=True)

# Importar módulos
from modules.data_generator import DataGenerator
from modules.ensino import ensino_module
from modules.assistencia_estudantil import assistencia_estudantil_module
from modules.pesquisa import pesquisa_module
from modules.extensao import extensao_module
from modules.orcamento import orcamento_module
from modules.servidores import servidores_module
from modules.ouvidoria import ouvidoria_module
from modules.auditoria import auditoria_module
from modules.mundo_trabalho import mundo_trabalho_module
from modules.help_page import show_help

def main():
    # Inicializar estado da sessão para controle da sidebar
    if 'sidebar_state' not in st.session_state:
        st.session_state.sidebar_state = 'expanded'
    
    # CSS para controle da sidebar baseado no estado da sessão
    if st.session_state.sidebar_state == 'collapsed':
        st.markdown("""
        <style>
        .stSidebar {
            display: none !important;
        }
        .main .block-container {
            margin-left: 0 !important;
            max-width: 100% !important;
        }
        /* Estilo do botão Menu */
        div[data-testid="column"]:first-child button[key="toggle_sidebar"] {
            background-color: #1a8c73 !important;
            color: white !important;
            border: 2px solid #0d5a4e !important;
            font-weight: bold !important;
            border-radius: 0.375rem !important;
        }
        div[data-testid="column"]:first-child button[key="toggle_sidebar"]:hover {
            background-color: #0d5a4e !important;
            transform: scale(1.05) !important;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        .stSidebar {
            display: block !important;
        }
        .main .block-container {
            margin-left: 21rem !important;
            max-width: calc(100% - 21rem) !important;
        }
        /* Estilo do botão Menu */
        div[data-testid="column"]:first-child button[key="toggle_sidebar"] {
            background-color: #1a8c73 !important;
            color: white !important;
            border: 2px solid #0d5a4e !important;
            font-weight: bold !important;
            border-radius: 0.375rem !important;
        }
        div[data-testid="column"]:first-child button[key="toggle_sidebar"]:hover {
            background-color: #0d5a4e !important;
            transform: scale(1.05) !important;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # CSS adicional para estilizar o botão Menu
    st.markdown("""
    <style>
    /* Estilo específico para o botão Menu */
    button[data-testid="baseButton-secondary"] {
        background-color: #1a8c73 !important;
        color: white !important;
        border: 2px solid #0d5a4e !important;
        font-weight: bold !important;
        border-radius: 0.375rem !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.2s ease !important;
    }
    button[data-testid="baseButton-secondary"]:hover {
        background-color: #0d5a4e !important;
        transform: scale(1.05) !important;
    }
    button[data-testid="baseButton-secondary"]:focus {
        background-color: #0d5a4e !important;
        box-shadow: 0 0 0 2px rgba(26, 140, 115, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Botão para controle da sidebar
    col1, col2, col3 = st.columns([2, 10, 1])
    with col1:
        if st.button("☰ Menu", help="Mostrar/ocultar menu", key="toggle_sidebar"):
            if st.session_state.sidebar_state == 'expanded':
                st.session_state.sidebar_state = 'collapsed'
            else:
                st.session_state.sidebar_state = 'expanded'
            st.rerun()
    
    # Gerar dados
    data_gen = DataGenerator()
    
    # Sidebar - Menu Principal
    logo_path = os.path.join("logo-ifpb", "IFPB-cz.png")
    logo_base64 = get_base64_image(logo_path)
    
    # Adicionar logo na sidebar
    if logo_base64:
        st.sidebar.markdown(f"""
        <div style="text-align: center; margin-bottom: 2rem;">
            <img src="data:image/png;base64,{logo_base64}" 
                 alt="IFPB Logo" 
                 style="width: 120px; height: auto; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    
    st.sidebar.title("📊 Sistema Institucional")
    st.sidebar.markdown("---")
    
    # Placeholders no topo
    st.sidebar.markdown("### 📋 Navegação")
    apresentacao = st.sidebar.button("📖 Apresentação")
    mapa = st.sidebar.button("🗺️ Mapa")
    ajuda = st.sidebar.button("❓ Ajuda")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Dashboards")
    
    # Menu principal com ordem específica
    opcoes_menu = [
        ("🎓 Ensino", "ensino"),
        ("🤝 Assistência Estudantil", "assistencia"),
        ("🔬 Pesquisa", "pesquisa"),
        ("🌟 Extensão", "extensao"),
        ("💰 Orçamento", "orcamento"),
        ("👥 Servidores", "servidores"),
        ("📢 Ouvidoria", "ouvidoria"),
        ("🔍 Auditoria", "auditoria"),
        ("💼 Mundo do Trabalho", "mundo_trabalho")
    ]
    
    # Seleção do módulo
    modulo_selecionado = st.sidebar.selectbox(
        "Selecione o módulo:",
        options=[opcao[1] for opcao in opcoes_menu],
        format_func=lambda x: next(opcao[0] for opcao in opcoes_menu if opcao[1] == x),
        index=0
    )
    
    # Rodar o módulo selecionado
    if modulo_selecionado == "ensino":
        ensino_module(data_gen)
    elif modulo_selecionado == "assistencia":
        assistencia_estudantil_module(data_gen)
    elif modulo_selecionado == "pesquisa":
        pesquisa_module(data_gen)
    elif modulo_selecionado == "extensao":
        extensao_module(data_gen)
    elif modulo_selecionado == "orcamento":
        orcamento_module(data_gen)
    elif modulo_selecionado == "servidores":
        servidores_module(data_gen)
    elif modulo_selecionado == "ouvidoria":
        ouvidoria_module(data_gen)
    elif modulo_selecionado == "auditoria":
        auditoria_module(data_gen)
    elif modulo_selecionado == "mundo_trabalho":
        mundo_trabalho_module(data_gen)
    
    # Handlers para placeholders
    if apresentacao:
        st.info("🚧 Módulo de Apresentação em desenvolvimento")
    if mapa:
        st.info("🚧 Módulo de Mapa em desenvolvimento")
    if ajuda:
        show_help()

if __name__ == "__main__":
    main()
