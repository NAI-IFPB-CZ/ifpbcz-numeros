import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def servidores_module(data_gen):
    """Módulo de Servidores"""
    
    # Cabeçalho com logo
    display_header_with_logo("Servidores")
    
    # Gerar dados
    dados_servidores = data_gen.gerar_dados_servidores()
    
    # Filtrar dados para 2025
    dados_2025 = dados_servidores[dados_servidores['ano'] == 2025]
    
    # Calcular KPIs
    total_servidores = dados_2025['total_servidores'].sum()
    total_tecnicos = dados_2025['tecnicos'].sum()
    total_docentes = dados_2025['docentes'].sum()
    
    # Cartões de KPI
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">SERVIDORES</div>
            <div class="kpi-value">{total_servidores:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TÉCNICOS</div>
            <div class="kpi-value">{total_tecnicos:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">DOCENTES</div>
            <div class="kpi-value">{total_docentes:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Gráfico Principal: Evolução do Número de Servidores
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução do Número de Servidores")
    
    unidade_selecionada = st.selectbox(
        "Selecione a unidade:",
        ["Todas"] + list(dados_servidores['unidade'].unique()),
        key="unidade_servidores"
    )
    
    # Filtrar dados
    if unidade_selecionada == "Todas":
        dados_filtrados = dados_servidores.groupby('ano').agg({
            'total_servidores': 'sum',
            'docentes': 'sum',
            'tecnicos': 'sum'
        }).reset_index()
        titulo_grafico = "Evolução do Número de Servidores - Todas as Unidades"
    else:
        dados_filtrados = dados_servidores[dados_servidores['unidade'] == unidade_selecionada]
        titulo_grafico = f"Evolução do Número de Servidores - {unidade_selecionada}"
    
    # Criar gráfico de área
    fig = go.Figure()
    
    # Adicionar séries
    fig.add_trace(go.Scatter(
        x=dados_filtrados['ano'],
        y=dados_filtrados['total_servidores'],
        mode='lines+markers',
        name='Total Servidores',
        line=dict(color='#1a8c73', width=3),
        fill='tonexty'
    ))
    
    fig.add_trace(go.Scatter(
        x=dados_filtrados['ano'],
        y=dados_filtrados['docentes'],
        mode='lines+markers',
        name='Servidores Professores',
        line=dict(color='#0d5a4e', width=2),
        fill='tonexty'
    ))
    
    fig.add_trace(go.Scatter(
        x=dados_filtrados['ano'],
        y=dados_filtrados['tecnicos'],
        mode='lines+markers',
        name='Servidores Técnicos',
        line=dict(color='#2db896', width=2),
        fill='tozeroy'
    ))
    
    fig.update_layout(
        title=titulo_grafico,
        xaxis_title="Ano",
        yaxis_title="Número de Servidores",
        height=500,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 2: Distribuição por Unidade
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Distribuição de Servidores por Unidade")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_distribuicao = st.selectbox(
            "Ano:",
            sorted(dados_servidores['ano'].unique(), reverse=True),
            key="ano_distribuicao"
        )
    
    with col2:
        tipo_servidor = st.selectbox(
            "Tipo de Servidor:",
            ["Total", "Docentes", "Técnicos"],
            key="tipo_servidor"
        )
    
    # Filtrar dados
    dados_distribuicao = dados_servidores[dados_servidores['ano'] == ano_distribuicao]
    
    # Mapear tipo selecionado
    mapeamento_tipo = {
        "Total": "total_servidores",
        "Docentes": "docentes",
        "Técnicos": "tecnicos"
    }
    
    coluna_tipo = mapeamento_tipo[tipo_servidor]
    
    # Criar gráfico
    fig2 = px.bar(
        dados_distribuicao,
        x='unidade',
        y=coluna_tipo,
        title=f"Distribuição de {tipo_servidor} por Unidade - {ano_distribuicao}",
        color_discrete_sequence=['#1a8c73']
    )
    
    fig2.update_layout(
        xaxis_title="Unidade",
        yaxis_title=f"Número de {tipo_servidor}",
        xaxis_tickangle=-45,
        height=400
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 3: Proporção Docentes vs Técnicos
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Proporção Docentes vs Técnicos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_proporcao = st.selectbox(
            "Ano:",
            sorted(dados_servidores['ano'].unique(), reverse=True),
            key="ano_proporcao"
        )
    
    with col2:
        unidade_proporcao = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_servidores['unidade'].unique()),
            key="unidade_proporcao"
        )
    
    # Filtrar dados
    dados_proporcao = dados_servidores[dados_servidores['ano'] == ano_proporcao]
    
    if unidade_proporcao != "Todas":
        dados_proporcao = dados_proporcao[dados_proporcao['unidade'] == unidade_proporcao]
    
    # Calcular totais
    total_docentes_prop = dados_proporcao['docentes'].sum()
    total_tecnicos_prop = dados_proporcao['tecnicos'].sum()
    
    # Criar dados para pizza
    dados_pizza = pd.DataFrame({
        'Tipo': ['Docentes', 'Técnicos'],
        'Quantidade': [total_docentes_prop, total_tecnicos_prop]
    })
    
    fig3 = px.pie(
        dados_pizza,
        values='Quantidade',
        names='Tipo',
        title=f"Proporção Docentes vs Técnicos - {ano_proporcao}",
        color_discrete_sequence=['#1a8c73', '#0d5a4e']
    )
    
    # Adicionar percentuais
    fig3.update_traces(textposition='inside', textinfo='percent+label')
    
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 4: Crescimento Anual
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Taxa de Crescimento Anual")
    
    # Calcular crescimento
    dados_crescimento = dados_servidores.groupby('ano').agg({
        'total_servidores': 'sum',
        'docentes': 'sum',
        'tecnicos': 'sum'
    }).reset_index()
    
    # Calcular percentual de crescimento
    dados_crescimento['crescimento_total'] = dados_crescimento['total_servidores'].pct_change() * 100
    dados_crescimento['crescimento_docentes'] = dados_crescimento['docentes'].pct_change() * 100
    dados_crescimento['crescimento_tecnicos'] = dados_crescimento['tecnicos'].pct_change() * 100
    
    # Remover primeiro ano (sem crescimento)
    dados_crescimento = dados_crescimento[dados_crescimento['ano'] > 2013]
    
    # Criar gráfico
    fig4 = go.Figure()
    
    fig4.add_trace(go.Scatter(
        x=dados_crescimento['ano'],
        y=dados_crescimento['crescimento_total'],
        mode='lines+markers',
        name='Total Servidores',
        line=dict(color='#1a8c73', width=3)
    ))
    
    fig4.add_trace(go.Scatter(
        x=dados_crescimento['ano'],
        y=dados_crescimento['crescimento_docentes'],
        mode='lines+markers',
        name='Docentes',
        line=dict(color='#0d5a4e', width=2)
    ))
    
    fig4.add_trace(go.Scatter(
        x=dados_crescimento['ano'],
        y=dados_crescimento['crescimento_tecnicos'],
        mode='lines+markers',
        name='Técnicos',
        line=dict(color='#2db896', width=2)
    ))
    
    fig4.update_layout(
        title="Taxa de Crescimento Anual de Servidores",
        xaxis_title="Ano",
        yaxis_title="Taxa de Crescimento (%)",
        height=400
    )
    
    # Adicionar linha de referência em 0%
    fig4.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="0%")
    
    st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
