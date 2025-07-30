"""
==============================================================================
MÓDULO DE EXTENSÃO - Sistema Dashboard IFPB-CZ
==============================================================================

Este módulo implementa o dashboard de extensão universitária, exibindo
indicadores e análises sobre estágios supervisionados e inclusão de
pessoas com necessidades especiais (PNE).

Funcionalidades principais:
- KPIs de estágios concluídos e ingressantes PNE
- Análise temporal da evolução dos estágios
- Distribuição por unidades, cursos e gênero
- Acessibilidade e inclusão de pessoas com necessidades especiais
- Filtros interativos para análise personalizada

Dados analisados:
- Estágios supervisionados concluídos
- Ingressantes com necessidades especiais
- Distribuição por curso, unidade e gênero
- Tipos de necessidades especiais atendidas

Autor: Sistema NAI/IFPB-CZ
Versão: 2.0 - Dashboard Institucional Completo
Data: Julho 2025
==============================================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def extensao_module(data_gen):
    """
    Módulo principal de Extensão Universitária.
    
    Exibe dashboard completo com indicadores de estágios supervisionados,
    inclusão de pessoas com necessidades especiais e análises temporais.
    
    Args:
        data_gen: Instância do gerador de dados para extensão
        
    Returns:
        None: Renderiza a interface diretamente no Streamlit
    """
    
    # Cabeçalho com logo institucional
    display_header_with_logo("Extensão")
    
    # ==============================================================================
    # CARREGAMENTO E VALIDAÇÃO DOS DADOS
    # ==============================================================================
    
    # Gerar dados de extensão através do data generator
    dados_extensao = data_gen.gerar_dados_extensao()
    
    # Verificar se os dados foram gerados corretamente
    if dados_extensao is None or dados_extensao.empty:
        st.error("Erro ao gerar dados de extensão. Verifique o arquivo de dados.")
        return
    
    # Verificar se as colunas necessárias existem no dataset
    required_columns = ['ano', 'estagios_concluidos', 'pne_ingressantes', 'tipo_necessidade']
    missing_columns = [col for col in required_columns if col not in dados_extensao.columns]
    
    if missing_columns:
        st.error(f"Colunas ausentes nos dados: {missing_columns}")
        st.write(f"Colunas disponíveis: {list(dados_extensao.columns)}")
        return
    
    # ==============================================================================
    # PREPARAÇÃO DOS DADOS PARA ANÁLISE
    # ==============================================================================
    
    # Filtrar dados para o ano mais recente (preferencialmente 2025)
    dados_2025 = dados_extensao[dados_extensao['ano'] == 2025]
    
    # Verificar se existem dados para 2025
    if dados_2025.empty:
        st.warning("Nenhum dado encontrado para 2025.")
        # Usar dados do ano mais recente disponível como fallback
        ano_mais_recente = dados_extensao['ano'].max()
        dados_2025 = dados_extensao[dados_extensao['ano'] == ano_mais_recente]
        st.info(f"Usando dados de {ano_mais_recente} como referência.")
    
    # ==============================================================================
    # CÁLCULO DOS INDICADORES PRINCIPAIS (KPIs)
    # ==============================================================================
    
    # Calcular total de estágios concluídos no ano
    total_estagios = dados_2025['estagios_concluidos'].sum()
    
    # Calcular total de ingressantes com necessidades especiais
    total_pne = dados_2025['pne_ingressantes'].sum()
    
    # Identificar o tipo de necessidade especial mais frequente
    if total_pne > 0:
        tipo_mais_frequente = dados_2025[dados_2025['tipo_necessidade'].notna()].groupby('tipo_necessidade')['pne_ingressantes'].sum().idxmax()
    else:
        tipo_mais_frequente = "N/A"
    
    # ==============================================================================
    # SEÇÃO DE INDICADORES PRINCIPAIS (KPIs)
    # ==============================================================================
    
    # Cartões de KPI com design institucional
    st.markdown("### 📊 Indicadores Principais")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Criar três colunas para os KPIs principais
    col1, col2, col3 = st.columns(3)
    
    # KPI 1: Total de Estágios Concluídos
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ESTÁGIOS CONCLUÍDOS</div>
            <div class="kpi-value">{total_estagios:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 2: Total de Ingressantes com Necessidades Especiais
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">INGRESSANTES PNE</div>
            <div class="kpi-value">{total_pne:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 3: Tipo de Necessidade Mais Frequente
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TIPO MAIS FREQUENTE</div>
            <div class="kpi-value">{tipo_mais_frequente}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Separadores visuais para melhor organização
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # ==============================================================================
    # GRÁFICO 1: ESTÁGIOS CONCLUÍDOS POR UNIDADE
    # ==============================================================================
    
    # Gráfico 1: Estágios Concluídos por Unidade
    st.markdown("### 📊 Análise de Estágios")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("Estágios Concluídos por Unidade")
    
    # Filtros organizados para melhor UX
    st.markdown("**Filtros:**")
    col1, col2 = st.columns(2)
    
    # Filtro de ano (dropdown com anos disponíveis em ordem decrescente)
    with col1:
        ano_selecionado = st.selectbox(
            "📅 Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_ext_1"
        )
    
    # Filtro de unidade (incluindo opção "Todas")
    with col2:
        unidade_selecionada = st.selectbox(
            "🏢 Unidade:",
            ["Todas"] + list(dados_extensao['unidade'].unique()),
            key="unidade_ext_1"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Aplicar filtros selecionados aos dados
    dados_filtrados = dados_extensao[dados_extensao['ano'] == ano_selecionado]
    
    if unidade_selecionada != "Todas":
        dados_filtrados = dados_filtrados[dados_filtrados['unidade'] == unidade_selecionada]
    
    # Agrupar dados por unidade para criação do gráfico
    dados_grafico = dados_filtrados.groupby('unidade')['estagios_concluidos'].sum().reset_index()
    
    # Criar gráfico de barras com Plotly
    fig = px.bar(
        dados_grafico,
        x='unidade',
        y='estagios_concluidos',
        title=f"Estágios Concluídos por Unidade - {ano_selecionado}",
        color_discrete_sequence=['#1a8c73'],  # Cor institucional IFPB
        text='estagios_concluidos'
    )
    
    # Personalizar layout do gráfico
    fig.update_layout(
        xaxis_title="Unidade",
        yaxis_title="Número de Estágios Concluídos",
        xaxis_tickangle=-45,  # Rotacionar labels do eixo X para melhor legibilidade
        height=450,
        showlegend=False
    )
    
    # Posicionar valores nas barras
    fig.update_traces(textposition='outside')
    
    # Renderizar gráfico
    st.plotly_chart(fig, use_container_width=True)
    
    # Fonte dos dados
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==============================================================================
    # GRÁFICO 2: EVOLUÇÃO TEMPORAL DOS ESTÁGIOS
    # ==============================================================================
    
    # Gráfico 2: Evolução do Número de Estágios Concluídos
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução Temporal dos Estágios")
    
    # Filtro para seleção de unidade específica ou todas
    st.markdown("**Filtros:**")
    unidade_evolucao = st.selectbox(
        "🏢 Unidade:",
        ["Todas"] + list(dados_extensao['unidade'].unique()),
        key="unidade_ext_evolucao"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Filtrar e agrupar dados para evolução temporal
    if unidade_evolucao == "Todas":
        # Agrupar todos os dados por ano
        dados_evolucao = dados_extensao.groupby('ano')['estagios_concluidos'].sum().reset_index()
        titulo_evolucao = "Evolução dos Estágios Concluídos - Todas as Unidades"
    else:
        # Filtrar dados da unidade específica e agrupar por ano
        dados_evolucao = dados_extensao[dados_extensao['unidade'] == unidade_evolucao]
        dados_evolucao = dados_evolucao.groupby('ano')['estagios_concluidos'].sum().reset_index()
        titulo_evolucao = f"Evolução dos Estágios Concluídos - {unidade_evolucao}"
    
    # Criar gráfico de linha para mostrar evolução temporal
    fig2 = px.line(
        dados_evolucao,
        x='ano',
        y='estagios_concluidos',
        title=titulo_evolucao,
        markers=True,  # Adicionar marcadores nos pontos
        color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
    )
    
    # Personalizar layout do gráfico de evolução
    fig2.update_layout(
        xaxis_title="Ano",
        yaxis_title="Número de Estágios Concluídos",
        height=450,
        showlegend=False
    )
    
    # Adicionar valores nos pontos da linha
    fig2.update_traces(
        mode='lines+markers+text',  # Linha com marcadores e texto
        textposition='top center',   # Posição do texto acima dos pontos
        texttemplate='%{y}'         # Template para exibir o valor de y
    )
    
    # Renderizar gráfico de evolução
    st.plotly_chart(fig2, use_container_width=True)
    
    # Fonte dos dados
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==============================================================================
    # GRÁFICOS DE DISTRIBUIÇÃO (PIZZA)
    # ==============================================================================
    
    # Gráficos de Pizza para distribuição por categorias
    st.markdown("### 📊 Distribuição por Categorias")
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de pizza: Distribuição de estágios por curso
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("🎓 Estágios por Curso")
        
        # Filtro de ano para o gráfico de curso
        st.markdown("**Filtros:**")
        ano_pizza = st.selectbox(
            "📅 Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_pizza_curso"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Filtrar dados por ano e agrupar por curso
        dados_pizza_curso = dados_extensao[dados_extensao['ano'] == ano_pizza]
        dados_pizza_curso = dados_pizza_curso.groupby('curso')['estagios_concluidos'].sum().reset_index()
        
        # Criar gráfico de pizza para distribuição por curso
        fig3 = px.pie(
            dados_pizza_curso,
            values='estagios_concluidos',
            names='curso',
            title=f"Distribuição por Curso - {ano_pizza}",
            color_discrete_sequence=px.colors.qualitative.Set3  # Paleta de cores variadas
        )
        
        # Personalizar layout do gráfico de pizza
        fig3.update_layout(height=400)
        fig3.update_traces(
            textposition='inside',      # Posição do texto dentro das fatias
            textinfo='percent+label'    # Mostrar porcentagem e rótulo
        )
        
        # Renderizar gráfico de distribuição por curso
        st.plotly_chart(fig3, use_container_width=True)
        
        # Fonte dos dados
        st.markdown('<div class="fonte-dados">📋 Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Gráfico de pizza: Distribuição de estágios por gênero
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("👫 Estágios por Gênero")
        
        # Filtro de ano para o gráfico de gênero
        st.markdown("**Filtros:**")
        ano_pizza_genero = st.selectbox(
            "📅 Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_pizza_genero"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Filtrar dados por ano e agrupar por gênero
        dados_pizza_genero = dados_extensao[dados_extensao['ano'] == ano_pizza_genero]
        dados_pizza_genero = dados_pizza_genero.groupby('genero')['estagios_concluidos'].sum().reset_index()
        
        # Criar gráfico de pizza para distribuição por gênero
        fig4 = px.pie(
            dados_pizza_genero,
            values='estagios_concluidos',
            names='genero',
            title=f"Distribuição por Gênero - {ano_pizza_genero}",
            color_discrete_sequence=['#1a8c73', '#0d5a4e', '#4CAF50']  # Cores na paleta verde institucional
        )
        
        # Personalizar layout do gráfico de pizza
        fig4.update_layout(height=400)
        fig4.update_traces(
            textposition='inside',      # Posição do texto dentro das fatias
            textinfo='percent+label'    # Mostrar porcentagem e rótulo
        )
        
        # Renderizar gráfico de distribuição por gênero
        st.plotly_chart(fig4, use_container_width=True)
        
        # Fonte dos dados
        st.markdown('<div class="fonte-dados">📋 Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==============================================================================
    # SEÇÃO DE INCLUSÃO E ACESSIBILIDADE
    # ==============================================================================
    
    # Gráfico adicional: Necessidades Especiais
    st.markdown("### ♿ Inclusão e Acessibilidade")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("Ingressantes com Necessidades Especiais")
    
    # Filtros para análise de inclusão
    st.markdown("**Filtros:**")
    col1, col2 = st.columns(2)
    
    # Filtro de ano para dados PNE
    with col1:
        ano_pne = st.selectbox(
            "📅 Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_pne"
        )
    
    # Filtro de unidade para dados PNE
    with col2:
        unidade_pne = st.selectbox(
            "🏢 Unidade:",
            ["Todas"] + list(dados_extensao['unidade'].unique()),
            key="unidade_pne"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Filtrar e processar dados de necessidades especiais
    dados_pne = dados_extensao[dados_extensao['ano'] == ano_pne]
    dados_pne = dados_pne[dados_pne['tipo_necessidade'].notna()]  # Remover valores nulos
    
    # Aplicar filtro de unidade se especificado
    if unidade_pne != "Todas":
        dados_pne = dados_pne[dados_pne['unidade'] == unidade_pne]
    
    # Verificar se existem dados para exibir
    if not dados_pne.empty:
        # Agrupar dados por tipo de necessidade
        dados_grafico_pne = dados_pne.groupby('tipo_necessidade')['pne_ingressantes'].sum().reset_index()
        
        # Criar gráfico de barras para necessidades especiais
        fig5 = px.bar(
            dados_grafico_pne,
            x='tipo_necessidade',
            y='pne_ingressantes',
            title=f"Ingressantes PNE por Tipo de Necessidade - {ano_pne}",
            color_discrete_sequence=['#1a8c73'],  # Cor institucional IFPB
            text='pne_ingressantes'
        )
        
        # Personalizar layout do gráfico PNE
        fig5.update_layout(
            xaxis_title="Tipo de Necessidade",
            yaxis_title="Número de Ingressantes",
            height=450,
            showlegend=False,
            xaxis_tickangle=-45  # Rotacionar labels para melhor legibilidade
        )
        
        # Posicionar valores nas barras
        fig5.update_traces(textposition='outside')
        
        # Renderizar gráfico de necessidades especiais
        st.plotly_chart(fig5, use_container_width=True)
    else:
        # Exibir mensagem informativa quando não há dados
        st.info("ℹ️ Não há dados de necessidades especiais para os filtros selecionados.")
    
    # Fonte dos dados
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==============================================================================
    # RODAPÉ DO SISTEMA
    # ==============================================================================
    
    # Rodapé com informações institucionais
    display_footer()
