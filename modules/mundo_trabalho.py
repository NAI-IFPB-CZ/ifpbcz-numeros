import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def mundo_trabalho_module(data_gen):
    """Módulo de Mundo do Trabalho"""
    
    # Cabeçalho com logo
    display_header_with_logo("Mundo do Trabalho")
    
    # Gerar dados
    dados_trabalho = data_gen.gerar_dados_mundo_trabalho()
    
    # Filtrar dados para 2025
    dados_2025 = dados_trabalho[dados_trabalho['ano'] == 2025]
    
    # Calcular KPIs (assumindo que DF se refere ao Distrito Federal ou a dados federais)
    total_admissoes = dados_2025['admissoes'].sum()
    total_desligamentos = dados_2025['desligamentos'].sum()
    saldo_admissoes = dados_2025['saldo'].sum()
    
    # Cartões de KPI
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ADMISSÕES DF 2025</div>
            <div class="kpi-value">{total_admissoes:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">DESLIGAMENTOS DF 2025</div>
            <div class="kpi-value">{total_desligamentos:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        cor_saldo = "#1a8c73" if saldo_admissoes >= 0 else "#d32f2f"
        sinal_saldo = "+" if saldo_admissoes >= 0 else ""
        
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">SALDO DE ADMISSÕES DF 2025</div>
            <div class="kpi-value" style="color: {cor_saldo};">{sinal_saldo}{saldo_admissoes:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Renderizar gráficos sintéticos
    render_graficos_sinteticos(dados_trabalho)
    


def render_graficos_sinteticos(dados_trabalho):
    """Renderiza gráficos para dados sintéticos antigos"""
    
    # Gráfico 1: Evolução de Admissões/Desligamentos
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução de Admissões/Desligamentos")
    
    regiao_evolucao = st.selectbox(
        "Região:",
        ["Todas"] + list(dados_trabalho['regiao'].unique()),
        key="regiao_evolucao_trab"
    )
    
    # Filtrar dados
    if regiao_evolucao == "Todas":
        dados_evolucao = dados_trabalho.groupby('ano').agg({
            'admissoes': 'sum',
            'desligamentos': 'sum',
            'saldo': 'sum'
        }).reset_index()
        titulo_evolucao = "Evolução de Admissões/Desligamentos - Todas as Regiões"
    else:
        dados_evolucao = dados_trabalho[dados_trabalho['regiao'] == regiao_evolucao]
        dados_evolucao = dados_evolucao.groupby('ano').agg({
            'admissoes': 'sum',
            'desligamentos': 'sum',
            'saldo': 'sum'
        }).reset_index()
        titulo_evolucao = f"Evolução de Admissões/Desligamentos - {regiao_evolucao}"
    
    # Criar gráfico de linha
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dados_evolucao['ano'],
        y=dados_evolucao['admissoes'],
        mode='lines+markers',
        name='Admissões',
        line=dict(color='#1a8c73', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=dados_evolucao['ano'],
        y=dados_evolucao['desligamentos'],
        mode='lines+markers',
        name='Desligamentos',
        line=dict(color='#d32f2f', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=dados_evolucao['ano'],
        y=dados_evolucao['saldo'],
        mode='lines+markers',
        name='SALDO',
        line=dict(color='#0d5a4e', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title=titulo_evolucao,
        xaxis_title="Ano",
        yaxis_title="Número de Pessoas",
        height=500,
        hovermode='x unified'
    )
    
    # Adicionar linha de referência no zero
    fig.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Saldo Zero")
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 2: Top 10 Setores de Atividade (Treemap)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Top 10 Setores de Atividade")
    
    col1, col2 = st.columns(2)
    
    with col1:
        forma_exibicao_setor = st.selectbox(
            "Forma de exibição:",
            ["Admissões", "Desligamentos"],
            key="forma_exibicao_setor"
        )
    
    with col2:
        ano_setor = st.selectbox(
            "Ano:",
            sorted(dados_trabalho['ano'].unique(), reverse=True),
            key="ano_setor"
        )
    
    # Filtrar dados
    dados_setor = dados_trabalho[dados_trabalho['ano'] == ano_setor]
    
    # Escolher métrica
    metrica_setor = 'admissoes' if forma_exibicao_setor == "Admissões" else 'desligamentos'
    
    # Agrupar por setor e pegar top 10
    dados_setor_grafico = dados_setor.groupby('setor_atividade')[metrica_setor].sum().reset_index()
    dados_setor_grafico = dados_setor_grafico.sort_values(metrica_setor, ascending=False).head(10)
    
    # Criar treemap
    fig2 = go.Figure(go.Treemap(
        labels=dados_setor_grafico['setor_atividade'],
        values=dados_setor_grafico[metrica_setor],
        parents=[""] * len(dados_setor_grafico),
        textinfo="label+value",
        hovertemplate='<b>%{label}</b><br>%{value}<extra></extra>',
        maxdepth=1,
        marker=dict(
            colorscale="Greens",
            colorbar=dict(title=f"Número de {forma_exibicao_setor}")
        )
    ))
    
    fig2.update_layout(
        title=f"Top 10 Setores de Atividade - {forma_exibicao_setor} - {ano_setor}",
        height=500
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 3: Comparação Regional
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Comparação Regional")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_regional = st.selectbox(
            "Ano:",
            sorted(dados_trabalho['ano'].unique(), reverse=True),
            key="ano_regional"
        )
    
    with col2:
        metrica_regional = st.selectbox(
            "Métrica:",
            ["Admissões", "Desligamentos", "Saldo"],
            key="metrica_regional"
        )
    
    # Filtrar dados
    dados_regional = dados_trabalho[dados_trabalho['ano'] == ano_regional]
    
    # Mapear métrica
    mapeamento_metrica = {
        "Admissões": "admissoes",
        "Desligamentos": "desligamentos",
        "Saldo": "saldo"
    }
    
    coluna_metrica = mapeamento_metrica[metrica_regional]
    
    # Agrupar por região
    dados_regional_grafico = dados_regional.groupby('regiao')[coluna_metrica].sum().reset_index()
    
    # Definir cores baseadas no valor (para saldo)
    if metrica_regional == "Saldo":
        colors = ['#1a8c73' if x >= 0 else '#d32f2f' for x in dados_regional_grafico[coluna_metrica]]
        color_discrete_map = None
    else:
        colors = None
        color_discrete_map = None
    
    fig3 = px.bar(
        dados_regional_grafico,
        x='regiao',
        y=coluna_metrica,
        title=f"{metrica_regional} por Região - {ano_regional}",
        color=colors if colors else None,
        color_discrete_sequence=['#1a8c73'] if not colors else None
    )
    
    fig3.update_layout(
        xaxis_title="Região",
        yaxis_title=f"Número de {metrica_regional}",
        height=400,
        showlegend=False
    )
    
    # Adicionar linha de referência no zero para saldo
    if metrica_regional == "Saldo":
        fig3.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Saldo Zero")
    
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 4: Setores com Maior Crescimento
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Setores com Maior Crescimento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        periodo_crescimento = st.selectbox(
            "Período:",
            ["Últimos 5 anos", "Últimos 10 anos", "Todos os anos"],
            key="periodo_crescimento"
        )
    
    with col2:
        tipo_crescimento = st.selectbox(
            "Tipo:",
            ["Admissões", "Saldo"],
            key="tipo_crescimento"
        )
    
    # Filtrar dados por período
    ano_atual = dados_trabalho['ano'].max()
    
    if periodo_crescimento == "Últimos 5 anos":
        dados_crescimento = dados_trabalho[dados_trabalho['ano'] >= (ano_atual - 4)]
    elif periodo_crescimento == "Últimos 10 anos":
        dados_crescimento = dados_trabalho[dados_trabalho['ano'] >= (ano_atual - 9)]
    else:  # Todos os anos
        dados_crescimento = dados_trabalho
    
    # Calcular crescimento por setor
    metrica_crescimento = 'admissoes' if tipo_crescimento == "Admissões" else 'saldo'
    
    # Agrupar por setor e calcular total
    dados_crescimento_setor = dados_crescimento.groupby('setor_atividade')[metrica_crescimento].sum().reset_index()
    dados_crescimento_setor = dados_crescimento_setor.sort_values(metrica_crescimento, ascending=False).head(10)
    
    # Criar gráfico horizontal
    fig4 = px.bar(
        dados_crescimento_setor,
        x=metrica_crescimento,
        y='setor_atividade',
        title=f"Top 10 Setores - {tipo_crescimento} - {periodo_crescimento}",
        color=metrica_crescimento,
        color_continuous_scale='Greens',
        orientation='h'
    )
    
    fig4.update_layout(
        xaxis_title=f"Total de {tipo_crescimento}",
        yaxis_title="Setor de Atividade",
        height=500
    )
    
    st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 5: Análise de Tendências por Setor
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Análise de Tendências por Setor")
    
    col1, col2 = st.columns(2)
    
    with col1:
        setores_selecionados = st.multiselect(
            "Selecione até 5 setores:",
            dados_trabalho['setor_atividade'].unique(),
            default=dados_trabalho['setor_atividade'].unique()[:3],
            max_selections=5,
            key="setores_tendencia"
        )
    
    with col2:
        metrica_tendencia = st.selectbox(
            "Métrica:",
            ["Admissões", "Desligamentos", "Saldo"],
            key="metrica_tendencia"
        )
    
    if setores_selecionados:
        # Filtrar dados
        dados_tendencia = dados_trabalho[dados_trabalho['setor_atividade'].isin(setores_selecionados)]
        
        # Mapear métrica
        coluna_tendencia = mapeamento_metrica[metrica_tendencia]
        
        # Agrupar por ano e setor
        dados_tendencia_grafico = dados_tendencia.groupby(['ano', 'setor_atividade'])[coluna_tendencia].sum().reset_index()
        
        # Criar gráfico
        fig5 = px.line(
            dados_tendencia_grafico,
            x='ano',
            y=coluna_tendencia,
            color='setor_atividade',
            title=f"Tendência de {metrica_tendencia} por Setor",
            markers=True
        )
        
        fig5.update_layout(
            xaxis_title="Ano",
            yaxis_title=f"Número de {metrica_tendencia}",
            height=400,
            legend_title="Setor de Atividade"
        )
        
        st.plotly_chart(fig5, use_container_width=True)
    else:
        st.info("Selecione pelo menos um setor para visualizar a tendência.")
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
