"""
==============================================================================
SISTEMA DASHBOARD IFPB-CZ - APLICAÇÃO PRINCIPAL
==============================================================================

Aplicação Streamlit para visualização de dados institucionais do
Instituto Federal da Paraíba - Campus Cajazeiras (IFPB-CZ).

Este sistema oferece dashboards interativos para acompanhamento de:
- Dados de Ensino (matrículas, evasão, conclusões)
- Assistência Estudantil (programas de auxílio e bolsas)
- Pesquisa Científica (produção acadêmica e projetos)
- Extensão Universitária (projetos e eventos comunitários)
- Gestão Orçamentária (execução e planejamento financeiro)
- Recursos Humanos (servidores docentes e técnicos)
- Ouvidoria (manifestações e atendimento ao público)
- Auditoria Interna (conformidade e controle)
- Mundo do Trabalho (empregabilidade de egressos)
- Mapeamento dos Campus (localização geográfica)

Funcionalidades principais:
- Interface responsiva com tema institucional verde/branco
- Navegação por sidebar colapsível 
- Gráficos interativos com Plotly
- Dados sintéticos realistas para demonstração
- Sistema de cache para otimização de performance
- Configurações de segurança e controle de acesso

Autor: Sistema NAI/IFPB-CZ
Versão: 2.0 - Dashboard Institucional Completo
Data: Julho 2025
==============================================================================
"""

# ==============================================================================
# IMPORTAÇÕES E DEPENDÊNCIAS
# ==============================================================================
import streamlit as st               # Framework principal da aplicação web
import pandas as pd                  # Manipulação e análise de dados
import numpy as np                   # Operações numéricas e arrays
import plotly.express as px          # Gráficos interativos simplificados
import plotly.graph_objects as go    # Gráficos interativos avançados
from wordcloud import WordCloud      # Geração de nuvens de palavras
import matplotlib.pyplot as plt      # Gráficos estáticos complementares
from datetime import datetime, timedelta  # Manipulação de datas e períodos
import random                        # Geração de números aleatórios
import base64                        # Codificação de imagens para HTML
import os                           # Operações do sistema operacional

# ==============================================================================
# FUNÇÕES UTILITÁRIAS PARA INTERFACE
# ==============================================================================

def get_base64_image(image_path):
    """
    Converte imagem para formato base64 para incorporação em HTML.
    
    Esta função é essencial para exibir logos e imagens diretamente
    no HTML gerado pelo Streamlit, evitando problemas de caminho
    de arquivos em diferentes ambientes de deploy.
    
    Args:
        image_path (str): Caminho para o arquivo de imagem
        
    Returns:
        str: String base64 da imagem ou None se houver erro
        
    Example:
        >>> base64_img = get_base64_image("logo-ifpb/IFPB-cz.png")
        >>> # Usar em HTML: f'<img src="data:image/png;base64,{base64_img}">'
    """
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

def display_header_with_logo(title):
    """
    Exibe cabeçalho estilizado com logo institucional do IFPB.
    
    Cria um cabeçalho visualmente atrativo com gradiente verde
    (cores institucionais) e incorpora o logo do IFPB quando disponível.
    Função preparada para uso futuro em páginas específicas.
    
    Args:
        title (str): Título a ser exibido no cabeçalho
        
    Note:
        Atualmente não utilizada na interface principal, mas mantida
        para uso em módulos específicos que necessitem de cabeçalho customizado.
    """
    logo_path = os.path.join("logo-ifpb", "IFPB-cz.png")
    
    # Tentar carregar o logo do IFPB
    logo_base64 = get_base64_image(logo_path)
    
    if logo_base64:
        # Cabeçalho com logo incorporado
        st.markdown(f"""
        <div class="main-header">
            <div class="header-logo">
                <img src="data:image/png;base64,{logo_base64}" alt="IFPB Logo">
            </div>
            {title}
        </div>
        """, unsafe_allow_html=True)
    else:
        # Cabeçalho sem logo (fallback)
        st.markdown(f'<div class="main-header">{title}</div>', unsafe_allow_html=True)

# ==============================================================================
# CONFIGURAÇÃO INICIAL DA APLICAÇÃO STREAMLIT
# ==============================================================================

# Configurar propriedades básicas da página web
st.set_page_config(
    page_title="Sistema de Visualização de Dados Institucionais - IFPB-CZ",
    page_icon="📊",                    # Ícone que aparece na aba do navegador
    layout="wide",                     # Layout amplo para melhor uso do espaço
    initial_sidebar_state="expanded",  # Sidebar aberta por padrão
    menu_items={                       # Remover itens do menu padrão do Streamlit
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# ==============================================================================
# ESTILOS CSS CUSTOMIZADOS - TEMA INSTITUCIONAL
# ==============================================================================
# Este bloco contém todo o CSS necessário para:
# 1. Aplicar cores institucionais (verde IFPB)
# 2. Remover elementos indesejados do Streamlit
# 3. Garantir visibilidade do controle da sidebar
# 4. Estilizar componentes (botões, inputs, cards)
# 5. Criar responsividade e transições suaves

st.markdown("""
<style>
    /* =================================================================
       LIMPEZA DE INTERFACE - Remover elementos padrão do Streamlit
       ================================================================= */
    
    /* Esconder menu hambúrguer e elementos de navegação padrão */
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
    
    /* =================================================================
       CONTROLE DA SIDEBAR - Garantir funcionalidade do botão
       ================================================================= */
    
    /* Preservar botão de controle da sidebar (quando colapsada) */
    button[data-testid="collapsedControl"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        z-index: 999999 !important;
        background-color: #1a8c73 !important;  /* Verde institucional */
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
    
    /* Esconder elementos desnecessários */
    .stAppViewContainer > .main > div[data-testid="stToolbar"] {
        display: none;
    }
    
    /* Esconder watermark "Made with Streamlit" */
    a[href^="https://streamlit.io"] {
        display: none !important;
    }
    
    /* =================================================================
       TEMA VISUAL - Cores institucionais e layout
       ================================================================= */
    
    /* =================================================================
       TEMA VISUAL - Cores institucionais e layout
       ================================================================= */
    
    /* Fundo principal da aplicação */
    .stApp {
        background-color: #f8f9fa;  /* Cinza muito claro para contraste */
    }
    
    /* Container principal */
    .main .block-container {
        background-color: #f8f9fa;
        padding: 2rem;
    }
    
    /* Sidebar com fundo branco */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    
    /* =================================================================
       COMPONENTES DE FORMULÁRIO - Inputs, selects, botões
       ================================================================= */
    
    /* Caixas de seleção (selectbox) */
    .stSelectbox > div > div {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 4px;
    }
    
    /* Seleção múltipla (multiselect) */
    .stMultiSelect > div > div > div {
        background-color: white !important;
        border: 1px solid #ddd !important;
        border-radius: 4px !important;
    }
    
    /* Campos de entrada de texto */
    .stTextInput > div > div > input {
        background-color: white !important;
        border: 1px solid #ddd !important;
        border-radius: 4px !important;
    }
    
    /* Campos numéricos */
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

# ==============================================================================
# IMPORTAÇÃO DOS MÓDULOS DA APLICAÇÃO
# ==============================================================================
# Importar o gerador de dados e todos os módulos de dashboard específicos

# Gerador de dados sintéticos para todos os módulos
from modules.data_generator import DataGenerator

# Módulos de dashboard por área institucional
from modules.ensino import ensino_module                           # Dados acadêmicos
from modules.assistencia_estudantil import assistencia_estudantil_module  # Programas de auxílio
from modules.pesquisa import pesquisa_module                       # Produção científica
from modules.extensao import extensao_module                       # Projetos de extensão
from modules.orcamento import orcamento_module                     # Gestão financeira
from modules.servidores import servidores_module                   # Recursos humanos
from modules.ouvidoria import ouvidoria_module                     # Atendimento público
from modules.auditoria import auditoria_module                     # Controle interno
from modules.mundo_trabalho import mundo_trabalho_module           # Empregabilidade
from modules.mapa import mapa_module                               # Localização geográfica
from modules.help_page import show_help                            # Página de ajuda

# ==============================================================================
# FUNÇÃO PRINCIPAL DA APLICAÇÃO
# ==============================================================================

def main():
    """
    Função principal que controla toda a aplicação dashboard.
    
    Responsabilidades:
    1. Gerenciar estado da sidebar (expandida/colapsada)
    2. Aplicar estilos CSS dinâmicos
    3. Controlar navegação entre módulos
    4. Inicializar gerador de dados
    5. Renderizar interface da sidebar
    6. Rotear para módulo selecionado
    7. Gerenciar ações de botões especiais (apresentação, ajuda)
    
    A função utiliza st.session_state para manter persistência
    de configurações entre recarregamentos da página.
    """
    
    # Inicializar controle de estado da sidebar
    # Permite alternar entre sidebar expandida/colapsada
    if 'sidebar_state' not in st.session_state:
        st.session_state.sidebar_state = 'expanded'
    
    # ==================================================================
    # APLICAÇÃO DE ESTILOS CSS DINÂMICOS BASEADOS NO ESTADO DA SIDEBAR
    # ==================================================================
    
    # Aplicar CSS específico quando sidebar está colapsada
    if st.session_state.sidebar_state == 'collapsed':
        st.markdown("""
        <style>
        /* Esconder sidebar completamente */
        .stSidebar {
            display: none !important;
        }
        /* Expandir área principal para ocupar toda a largura */
        .main .block-container {
            margin-left: 0 !important;
            max-width: 100% !important;
        }
        /* Estilizar botão Menu quando sidebar está escondida */
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
        # CSS quando sidebar está expandida (estado normal)
        st.markdown("""
        <style>
        /* Mostrar sidebar normalmente */
        .stSidebar {
            display: block !important;
        }
        /* Ajustar margem da área principal para acomodar sidebar */
        .main .block-container {
            margin-left: 21rem !important;
            max-width: calc(100% - 21rem) !important;
        }
        /* Estilizar botão Menu quando sidebar está visível */
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
    
    # CSS adicional para garantir estilização consistente do botão Menu
    # Independente do estado da sidebar
    st.markdown("""
    <style>
    /* Estilo específico para o botão Menu em todos os estados */
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
    
    # ==================================================================
    # CONTROLE DE INTERFACE - Botão de toggle da sidebar
    # ==================================================================
    
    # Criar layout de 3 colunas para posicionar o botão Menu
    col1, col2, col3 = st.columns([2, 10, 1])
    with col1:
        # Botão para alternar visibilidade da sidebar
        if st.button("☰ Menu/Home", help="Mostrar/ocultar menu", key="toggle_sidebar"):
            # Alternar estado da sidebar
            if st.session_state.sidebar_state == 'expanded':
                st.session_state.sidebar_state = 'collapsed'
            else:
                st.session_state.sidebar_state = 'expanded'
            # Forçar recarregamento da página para aplicar mudanças
            st.rerun()
    
    # ==================================================================
    # INICIALIZAÇÃO DO GERADOR DE DADOS
    # ==================================================================
    
    # Instanciar o gerador de dados sintéticos para todos os módulos
    data_gen = DataGenerator()
    
    # ==================================================================
    # CONFIGURAÇÃO E CONTEÚDO DA SIDEBAR
    # ==================================================================
    
    # Preparar logo institucional para exibição
    logo_path = os.path.join("logo-ifpb", "IFPB-cz.png")
    logo_base64 = get_base64_image(logo_path)
    
    # Exibir logo do IFPB na sidebar quando disponível
    if logo_base64:
        st.sidebar.markdown(f"""
        <div style="text-align: center; margin-bottom: 2rem;">
            <img src="data:image/png;base64,{logo_base64}" 
                 alt="IFPB Logo" 
                 style="width: 120px; height: auto; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)
    
    # Título principal da sidebar
    st.sidebar.title("📊 Sistema Institucional")
    st.sidebar.markdown("---")
    
    # ==================================================================
    # SEÇÃO DE NAVEGAÇÃO ESPECIAL - Botões de ação rápida
    # ==================================================================
    
    st.sidebar.markdown("### 📋 Navegação")
    # Botões para funcionalidades especiais (ainda em desenvolvimento)
    apresentacao = st.sidebar.button("📖 Apresentação")
    mapa_button = st.sidebar.button("🗺️ Mapa dos Campus") 
    ajuda = st.sidebar.button("❓ Ajuda")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Dashboards")
    
    # ==================================================================
    # DEFINIÇÃO DOS MÓDULOS DISPONÍVEIS
    # ==================================================================
    
    # Lista ordenada de todos os módulos de dashboard com ícones e identificadores
    opcoes_menu = [
        ("🎓 Ensino", "ensino"),                    # Dados acadêmicos
        ("🤝 Assistência Estudantil", "assistencia"), # Programas de auxílio
        ("🔬 Pesquisa", "pesquisa"),                # Produção científica
        ("🌟 Extensão", "extensao"),                # Projetos comunitários
        ("💰 Orçamento", "orcamento"),              # Gestão financeira
        ("👥 Servidores", "servidores"),            # Recursos humanos
        ("📢 Ouvidoria", "ouvidoria"),              # Atendimento público
        ("🔍 Auditoria", "auditoria"),              # Controle interno
        ("💼 Mundo do Trabalho", "mundo_trabalho"), # Empregabilidade
        ("🗺️ Mapa dos Campus", "mapa")             # Localização geográfica
    ]
    
    # ==================================================================
    # CONTROLE DE ESTADO DE NAVEGAÇÃO
    # ==================================================================
    
    # Inicializar módulo padrão se não existir no estado da sessão
    if 'modulo_selecionado' not in st.session_state:
        st.session_state.modulo_selecionado = "ensino"  # Módulo de Ensino como padrão
    
    # Verificar se botão direto do mapa foi clicado (navegação especial)
    if mapa_button and st.session_state.modulo_selecionado != "mapa":
        st.session_state.modulo_selecionado = "mapa"
    
    # Widget de seleção principal de módulos na sidebar
    modulo_selecionado = st.sidebar.selectbox(
        "Selecione o módulo:",
        options=[opcao[1] for opcao in opcoes_menu],  # IDs dos módulos
        format_func=lambda x: next(opcao[0] for opcao in opcoes_menu if opcao[1] == x),  # Nomes com ícones
        index=[opcao[1] for opcao in opcoes_menu].index(st.session_state.modulo_selecionado) if st.session_state.modulo_selecionado in [opcao[1] for opcao in opcoes_menu] else 0,
        key="selector_modulo"
    )
    
    # Atualizar estado da sessão apenas se módulo mudou via selectbox
    if modulo_selecionado != st.session_state.modulo_selecionado:
        st.session_state.modulo_selecionado = modulo_selecionado
    
    # ==================================================================
    # ROTEAMENTO PARA MÓDULOS - Executar módulo selecionado
    # ==================================================================
    
    # Usar estado da sessão para garantir persistência entre recarregamentos
    modulo_ativo = st.session_state.modulo_selecionado
    
    # Router principal - direcionar para função específica de cada módulo
    if modulo_ativo == "ensino":
        ensino_module(data_gen)                    # Dashboard de dados acadêmicos
    elif modulo_ativo == "assistencia":
        assistencia_estudantil_module(data_gen)    # Dashboard de assistência estudantil
    elif modulo_ativo == "pesquisa":
        pesquisa_module(data_gen)                  # Dashboard de pesquisa científica
    elif modulo_ativo == "extensao":
        extensao_module(data_gen)                  # Dashboard de extensão universitária
    elif modulo_ativo == "orcamento":
        orcamento_module(data_gen)                 # Dashboard de gestão orçamentária
    elif modulo_ativo == "servidores":
        servidores_module(data_gen)                # Dashboard de recursos humanos
    elif modulo_ativo == "ouvidoria":
        ouvidoria_module(data_gen)                 # Dashboard de ouvidoria
    elif modulo_ativo == "auditoria":
        auditoria_module(data_gen)                 # Dashboard de auditoria interna
    elif modulo_ativo == "mundo_trabalho":
        mundo_trabalho_module(data_gen)            # Dashboard de empregabilidade
    elif modulo_ativo == "mapa":
        mapa_module(data_gen)                      # Visualização geográfica dos campus
    
    # ==================================================================
    # HANDLERS PARA AÇÕES ESPECIAIS DA SIDEBAR
    # ==================================================================
    
    # Processar cliques nos botões de navegação especial
    if apresentacao:
        # Módulo de apresentação ainda em desenvolvimento
        st.info("🚧 Módulo de Apresentação em desenvolvimento")
        
    if ajuda:
        # Exibir página de ajuda do sistema
        show_help()

# ==============================================================================
# PONTO DE ENTRADA DA APLICAÇÃO
# ==============================================================================
# PONTO DE ENTRADA DA APLICAÇÃO
# ==============================================================================

if __name__ == "__main__":
    # Ponto de entrada principal da aplicação.
    # Executa a função main() apenas quando o script é executado diretamente,
    # não quando importado como módulo. Esta é uma boa prática em Python
    # para permitir que o código seja tanto executável quanto importável.
    # Para executar a aplicação: streamlit run app.py
    main()
