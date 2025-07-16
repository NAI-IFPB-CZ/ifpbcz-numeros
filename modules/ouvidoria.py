import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def ouvidoria_module(data_gen):
    """Módulo de Ouvidoria"""
    
    # Cabeçalho com logo
    display_header_with_logo("Ouvidoria")
    
    # Gerar dados
    dados_ouvidoria = data_gen.gerar_dados_ouvidoria()
    
    # Filtrar dados para 2025
    dados_2025 = dados_ouvidoria[dados_ouvidoria['ano'] == 2025]
    
    # Calcular KPIs
    total_manifestacoes = dados_2025['quantidade'].sum()
    
    # Usuário mais frequente
    usuario_mais_frequente = dados_2025.groupby('tipo_usuario')['quantidade'].sum().idxmax()
    
    # Média de dias de atendimento
    media_dias_atendimento = dados_2025['dias_atendimento'].mean()
    
    # Cartões de KPI
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TOTAL DE MANIFESTAÇÕES</div>
            <div class="kpi-value">{total_manifestacoes:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">USUÁRIO MAIS FREQUENTE</div>
            <div class="kpi-value">{usuario_mais_frequente}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">MÉDIA DE DIAS DE ATENDIMENTO</div>
            <div class="kpi-value">{media_dias_atendimento:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Gráfico 1: Evolução Mensal de Manifestações
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução Mensal de Manifestações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_evolucao = st.selectbox(
            "Ano:",
            sorted(dados_ouvidoria['ano'].unique(), reverse=True),
            key="ano_evolucao_ouv"
        )
    
    with col2:
        periodo_evolucao = st.selectbox(
            "Período:",
            ["Mensal", "Semestral"],
            key="periodo_evolucao"
        )
    
    # Filtrar dados
    dados_evolucao = dados_ouvidoria[dados_ouvidoria['ano'] == ano_evolucao]
    
    if periodo_evolucao == "Mensal":
        dados_evolucao_grafico = dados_evolucao.groupby('mes')['quantidade'].sum().reset_index()
        
        # Mapear nomes dos meses
        meses_nomes = {
            1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
            7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
        }
        
        dados_evolucao_grafico['mes_nome'] = dados_evolucao_grafico['mes'].map(meses_nomes)
        
        fig = px.line(
            dados_evolucao_grafico,
            x='mes_nome',
            y='quantidade',
            title=f"Evolução Mensal de Manifestações - {ano_evolucao}",
            markers=True,
            color_discrete_sequence=['#1a8c73']
        )
        
        fig.update_layout(
            xaxis_title="Mês",
            yaxis_title="Quantidade de Manifestações",
            height=400
        )
        
    else:  # Semestral
        dados_evolucao['semestre'] = dados_evolucao['mes'].apply(lambda x: 1 if x <= 6 else 2)
        dados_evolucao_grafico = dados_evolucao.groupby('semestre')['quantidade'].sum().reset_index()
        dados_evolucao_grafico['semestre_nome'] = dados_evolucao_grafico['semestre'].apply(lambda x: f"{x}º Semestre")
        
        fig = px.bar(
            dados_evolucao_grafico,
            x='semestre_nome',
            y='quantidade',
            title=f"Manifestações por Semestre - {ano_evolucao}",
            color_discrete_sequence=['#1a8c73']
        )
        
        fig.update_layout(
            xaxis_title="Semestre",
            yaxis_title="Quantidade de Manifestações",
            height=400
        )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Ouvidoria IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 2: Manifestações por Unidade
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Manifestações por Unidade")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_unidade = st.selectbox(
            "Ano:",
            sorted(dados_ouvidoria['ano'].unique(), reverse=True),
            key="ano_unidade_ouv"
        )
    
    with col2:
        forma_exibicao = st.selectbox(
            "Forma de exibição:",
            ["Quantidade", "Percentual"],
            key="forma_exibicao_ouv"
        )
    
    # Filtrar dados
    dados_unidade = dados_ouvidoria[dados_ouvidoria['ano'] == ano_unidade]
    dados_unidade_grafico = dados_unidade.groupby('unidade')['quantidade'].sum().reset_index()
    
    if forma_exibicao == "Percentual":
        total_manifestacoes_ano = dados_unidade_grafico['quantidade'].sum()
        dados_unidade_grafico['percentual'] = (dados_unidade_grafico['quantidade'] / total_manifestacoes_ano) * 100
        
        fig2 = px.bar(
            dados_unidade_grafico,
            x='unidade',
            y='percentual',
            title=f"Manifestações por Unidade (%) - {ano_unidade}",
            color_discrete_sequence=['#1a8c73']
        )
        
        fig2.update_layout(
            xaxis_title="Unidade",
            yaxis_title="Percentual (%)",
            xaxis_tickangle=-45,
            height=400
        )
        
    else:  # Quantidade
        fig2 = px.bar(
            dados_unidade_grafico,
            x='unidade',
            y='quantidade',
            title=f"Manifestações por Unidade - {ano_unidade}",
            color_discrete_sequence=['#1a8c73']
        )
        
        fig2.update_layout(
            xaxis_title="Unidade",
            yaxis_title="Quantidade",
            xaxis_tickangle=-45,
            height=400
        )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Ouvidoria IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 3: Tipos de Manifestação
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Tipos de Manifestação")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_tipo = st.selectbox(
            "Ano:",
            sorted(dados_ouvidoria['ano'].unique(), reverse=True),
            key="ano_tipo_ouv"
        )
    
    with col2:
        unidade_tipo = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_ouvidoria['unidade'].unique()),
            key="unidade_tipo_ouv"
        )
    
    # Filtrar dados
    dados_tipo = dados_ouvidoria[dados_ouvidoria['ano'] == ano_tipo]
    
    if unidade_tipo != "Todas":
        dados_tipo = dados_tipo[dados_tipo['unidade'] == unidade_tipo]
    
    dados_tipo_grafico = dados_tipo.groupby('tipo_manifestacao')['quantidade'].sum().reset_index()
    
    fig3 = px.pie(
        dados_tipo_grafico,
        values='quantidade',
        names='tipo_manifestacao',
        title=f"Tipos de Manifestação - {ano_tipo}",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig3.update_traces(textposition='inside', textinfo='percent+label')
    
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Ouvidoria IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 4: Tipos de Usuário
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Tipos de Usuário")
    
    ano_usuario = st.selectbox(
        "Ano:",
        sorted(dados_ouvidoria['ano'].unique(), reverse=True),
        key="ano_usuario_ouv"
    )
    
    # Filtrar dados
    dados_usuario = dados_ouvidoria[dados_ouvidoria['ano'] == ano_usuario]
    dados_usuario_grafico = dados_usuario.groupby('tipo_usuario')['quantidade'].sum().reset_index()
    
    fig4 = px.bar(
        dados_usuario_grafico,
        x='tipo_usuario',
        y='quantidade',
        title=f"Manifestações por Tipo de Usuário - {ano_usuario}",
        color_discrete_sequence=['#1a8c73']
    )
    
    fig4.update_layout(
        xaxis_title="Tipo de Usuário",
        yaxis_title="Quantidade",
        height=400
    )
    
    st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Ouvidoria IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 5: Tempo de Atendimento
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("⏱️ Tempo de Atendimento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_tempo = st.selectbox(
            "Ano:",
            sorted(dados_ouvidoria['ano'].unique(), reverse=True),
            key="ano_tempo_ouv"
        )
    
    with col2:
        unidade_tempo = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_ouvidoria['unidade'].unique()),
            key="unidade_tempo_ouv"
        )
    
    # Filtrar dados
    dados_tempo = dados_ouvidoria[dados_ouvidoria['ano'] == ano_tempo]
    
    if unidade_tempo != "Todas":
        dados_tempo = dados_tempo[dados_tempo['unidade'] == unidade_tempo]
    
    # Calcular média por mês
    dados_tempo_grafico = dados_tempo.groupby('mes')['dias_atendimento'].mean().reset_index()
    
    # Mapear nomes dos meses
    meses_nomes = {
        1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
    }
    
    dados_tempo_grafico['mes_nome'] = dados_tempo_grafico['mes'].map(meses_nomes)
    
    fig5 = px.line(
        dados_tempo_grafico,
        x='mes_nome',
        y='dias_atendimento',
        title=f"Tempo Médio de Atendimento por Mês - {ano_tempo}",
        markers=True,
        color_discrete_sequence=['#1a8c73']
    )
    
    fig5.update_layout(
        xaxis_title="Mês",
        yaxis_title="Dias de Atendimento",
        height=400
    )
    
    st.plotly_chart(fig5, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Ouvidoria IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
