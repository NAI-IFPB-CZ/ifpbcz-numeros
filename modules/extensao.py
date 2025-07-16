import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def extensao_module(data_gen):
    """Módulo de Extensão"""
    
    # Cabeçalho com logo
    display_header_with_logo("Extensão")
    
    # Gerar dados
    dados_extensao = data_gen.gerar_dados_extensao()
    
    # Filtrar dados para 2025
    dados_2025 = dados_extensao[dados_extensao['ano'] == 2025]
    
    # Calcular KPIs
    total_estagios = dados_2025['estagios_concluidos'].sum()
    total_pne = dados_2025['pne_ingressantes'].sum()
    
    # Tipo mais frequente de necessidade especial
    if total_pne > 0:
        tipo_mais_frequente = dados_2025[dados_2025['tipo_necessidade'].notna()].groupby('tipo_necessidade')['pne_ingressantes'].sum().idxmax()
    else:
        tipo_mais_frequente = "N/A"
    
    # Cartões de KPI
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ESTÁGIOS CONCLUÍDOS</div>
            <div class="kpi-value">{total_estagios:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">INGRESSANTES PORTADORES DE NECESSIDADES ESPECIAIS</div>
            <div class="kpi-value">{total_pne:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TIPO MAIS FREQUENTE DE NECESSIDADE ESPECIAL</div>
            <div class="kpi-value">{tipo_mais_frequente}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Gráfico 1: Estágios Concluídos por Unidade
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Estágios Concluídos por Unidade")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_selecionado = st.selectbox(
            "Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_ext_1"
        )
    
    with col2:
        unidade_selecionada = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_extensao['unidade'].unique()),
            key="unidade_ext_1"
        )
    
    # Filtrar dados
    dados_filtrados = dados_extensao[dados_extensao['ano'] == ano_selecionado]
    
    if unidade_selecionada != "Todas":
        dados_filtrados = dados_filtrados[dados_filtrados['unidade'] == unidade_selecionada]
    
    # Agrupar por unidade
    dados_grafico = dados_filtrados.groupby('unidade')['estagios_concluidos'].sum().reset_index()
    
    fig = px.bar(
        dados_grafico,
        x='unidade',
        y='estagios_concluidos',
        title=f"Estágios Concluídos por Unidade - {ano_selecionado}",
        color_discrete_sequence=['#1a8c73']
    )
    
    fig.update_layout(
        xaxis_title="Unidade",
        yaxis_title="Estágios Concluídos",
        xaxis_tickangle=-45,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 2: Evolução do Número de Estágios Concluídos
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução do Número de Estágios Concluídos")
    
    unidade_evolucao = st.selectbox(
        "Unidade:",
        ["Todas"] + list(dados_extensao['unidade'].unique()),
        key="unidade_ext_evolucao"
    )
    
    # Filtrar dados para evolução
    if unidade_evolucao == "Todas":
        dados_evolucao = dados_extensao.groupby('ano')['estagios_concluidos'].sum().reset_index()
        titulo_evolucao = "Evolução dos Estágios Concluídos - Todas as Unidades"
    else:
        dados_evolucao = dados_extensao[dados_extensao['unidade'] == unidade_evolucao]
        dados_evolucao = dados_evolucao.groupby('ano')['estagios_concluidos'].sum().reset_index()
        titulo_evolucao = f"Evolução dos Estágios Concluídos - {unidade_evolucao}"
    
    fig2 = px.line(
        dados_evolucao,
        x='ano',
        y='estagios_concluidos',
        title=titulo_evolucao,
        markers=True,
        color_discrete_sequence=['#1a8c73']
    )
    
    fig2.update_layout(
        xaxis_title="Ano",
        yaxis_title="Estágios Concluídos",
        height=400
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráficos de Pizza
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("📊 Estágios Concluídos por Curso")
        
        ano_pizza = st.selectbox(
            "Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_pizza_curso"
        )
        
        dados_pizza_curso = dados_extensao[dados_extensao['ano'] == ano_pizza]
        dados_pizza_curso = dados_pizza_curso.groupby('curso')['estagios_concluidos'].sum().reset_index()
        
        fig3 = px.pie(
            dados_pizza_curso,
            values='estagios_concluidos',
            names='curso',
            title=f"Estágios por Curso - {ano_pizza}",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        st.plotly_chart(fig3, use_container_width=True)
        
        st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("📊 Estágios Concluídos por Gênero")
        
        ano_pizza_genero = st.selectbox(
            "Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_pizza_genero"
        )
        
        dados_pizza_genero = dados_extensao[dados_extensao['ano'] == ano_pizza_genero]
        dados_pizza_genero = dados_pizza_genero.groupby('genero')['estagios_concluidos'].sum().reset_index()
        
        fig4 = px.pie(
            dados_pizza_genero,
            values='estagios_concluidos',
            names='genero',
            title=f"Estágios por Gênero - {ano_pizza_genero}",
            color_discrete_sequence=['#1a8c73', '#0d5a4e']
        )
        
        st.plotly_chart(fig4, use_container_width=True)
        
        st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico adicional: Necessidades Especiais
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Ingressantes com Necessidades Especiais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_pne = st.selectbox(
            "Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_pne"
        )
    
    with col2:
        unidade_pne = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_extensao['unidade'].unique()),
            key="unidade_pne"
        )
    
    # Filtrar dados
    dados_pne = dados_extensao[dados_extensao['ano'] == ano_pne]
    dados_pne = dados_pne[dados_pne['tipo_necessidade'].notna()]
    
    if unidade_pne != "Todas":
        dados_pne = dados_pne[dados_pne['unidade'] == unidade_pne]
    
    if not dados_pne.empty:
        dados_grafico_pne = dados_pne.groupby('tipo_necessidade')['pne_ingressantes'].sum().reset_index()
        
        fig5 = px.bar(
            dados_grafico_pne,
            x='tipo_necessidade',
            y='pne_ingressantes',
            title=f"Ingressantes PNE por Tipo de Necessidade - {ano_pne}",
            color_discrete_sequence=['#1a8c73']
        )
        
        fig5.update_layout(
            xaxis_title="Tipo de Necessidade",
            yaxis_title="Número de Ingressantes",
            height=400
        )
        
        st.plotly_chart(fig5, use_container_width=True)
    else:
        st.info("Não há dados de necessidades especiais para os filtros selecionados.")
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
