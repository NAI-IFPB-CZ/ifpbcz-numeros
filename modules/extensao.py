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
    
    # Verificar se os dados foram gerados corretamente
    if dados_extensao is None or dados_extensao.empty:
        st.error("Erro ao gerar dados de extensão. Verifique o arquivo de dados.")
        return
    
    # Verificar se as colunas necessárias existem
    required_columns = ['ano', 'estagios_concluidos', 'pne_ingressantes', 'tipo_necessidade']
    missing_columns = [col for col in required_columns if col not in dados_extensao.columns]
    
    if missing_columns:
        st.error(f"Colunas ausentes nos dados: {missing_columns}")
        st.write(f"Colunas disponíveis: {list(dados_extensao.columns)}")
        return
    
    # Filtrar dados para 2025
    dados_2025 = dados_extensao[dados_extensao['ano'] == 2025]
    
    # Verificar se existem dados para 2025
    if dados_2025.empty:
        st.warning("Nenhum dado encontrado para 2025.")
        # Usar dados do ano mais recente disponível
        ano_mais_recente = dados_extensao['ano'].max()
        dados_2025 = dados_extensao[dados_extensao['ano'] == ano_mais_recente]
        st.info(f"Usando dados de {ano_mais_recente} como referência.")
    
    # Calcular KPIs
    total_estagios = dados_2025['estagios_concluidos'].sum()
    total_pne = dados_2025['pne_ingressantes'].sum()
    
    # Tipo mais frequente de necessidade especial
    if total_pne > 0:
        tipo_mais_frequente = dados_2025[dados_2025['tipo_necessidade'].notna()].groupby('tipo_necessidade')['pne_ingressantes'].sum().idxmax()
    else:
        tipo_mais_frequente = "N/A"
    
    # Cartões de KPI
    st.markdown("### 📊 Indicadores Principais")
    st.markdown("<br>", unsafe_allow_html=True)
    
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
            <div class="kpi-title">INGRESSANTES PNE</div>
            <div class="kpi-value">{total_pne:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TIPO MAIS FREQUENTE</div>
            <div class="kpi-value">{tipo_mais_frequente}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Gráfico 1: Estágios Concluídos por Unidade
    st.markdown("### 📊 Análise de Estágios")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("Estágios Concluídos por Unidade")
    
    # Filtros organizados
    st.markdown("**Filtros:**")
    col1, col2 = st.columns(2)
    
    with col1:
        ano_selecionado = st.selectbox(
            "📅 Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_ext_1"
        )
    
    with col2:
        unidade_selecionada = st.selectbox(
            "🏢 Unidade:",
            ["Todas"] + list(dados_extensao['unidade'].unique()),
            key="unidade_ext_1"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
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
        color_discrete_sequence=['#1a8c73'],
        text='estagios_concluidos'
    )
    
    fig.update_layout(
        xaxis_title="Unidade",
        yaxis_title="Número de Estágios Concluídos",
        xaxis_tickangle=-45,
        height=450,
        showlegend=False
    )
    
    fig.update_traces(textposition='outside')
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gráfico 2: Evolução do Número de Estágios Concluídos
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução Temporal dos Estágios")
    
    st.markdown("**Filtros:**")
    unidade_evolucao = st.selectbox(
        "🏢 Unidade:",
        ["Todas"] + list(dados_extensao['unidade'].unique()),
        key="unidade_ext_evolucao"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
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
        yaxis_title="Número de Estágios Concluídos",
        height=450,
        showlegend=False
    )
    
    fig2.update_traces(
        mode='lines+markers+text',
        textposition='top center',
        texttemplate='%{y}'
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gráficos de Pizza
    st.markdown("### 📊 Distribuição por Categorias")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("🎓 Estágios por Curso")
        
        st.markdown("**Filtros:**")
        ano_pizza = st.selectbox(
            "📅 Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_pizza_curso"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        dados_pizza_curso = dados_extensao[dados_extensao['ano'] == ano_pizza]
        dados_pizza_curso = dados_pizza_curso.groupby('curso')['estagios_concluidos'].sum().reset_index()
        
        fig3 = px.pie(
            dados_pizza_curso,
            values='estagios_concluidos',
            names='curso',
            title=f"Distribuição por Curso - {ano_pizza}",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig3.update_layout(height=400)
        fig3.update_traces(textposition='inside', textinfo='percent+label')
        
        st.plotly_chart(fig3, use_container_width=True)
        
        st.markdown('<div class="fonte-dados">📋 Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("� Estágios por Gênero")
        
        st.markdown("**Filtros:**")
        ano_pizza_genero = st.selectbox(
            "📅 Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_pizza_genero"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        dados_pizza_genero = dados_extensao[dados_extensao['ano'] == ano_pizza_genero]
        dados_pizza_genero = dados_pizza_genero.groupby('genero')['estagios_concluidos'].sum().reset_index()
        
        fig4 = px.pie(
            dados_pizza_genero,
            values='estagios_concluidos',
            names='genero',
            title=f"Distribuição por Gênero - {ano_pizza_genero}",
            color_discrete_sequence=['#1a8c73', '#0d5a4e', '#4CAF50']
        )
        
        fig4.update_layout(height=400)
        fig4.update_traces(textposition='inside', textinfo='percent+label')
        
        st.plotly_chart(fig4, use_container_width=True)
        
        st.markdown('<div class="fonte-dados">📋 Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gráfico adicional: Necessidades Especiais
    st.markdown("### ♿ Inclusão e Acessibilidade")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("Ingressantes com Necessidades Especiais")
    
    st.markdown("**Filtros:**")
    col1, col2 = st.columns(2)
    
    with col1:
        ano_pne = st.selectbox(
            "📅 Ano:",
            sorted(dados_extensao['ano'].unique(), reverse=True),
            key="ano_pne"
        )
    
    with col2:
        unidade_pne = st.selectbox(
            "🏢 Unidade:",
            ["Todas"] + list(dados_extensao['unidade'].unique()),
            key="unidade_pne"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
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
            color_discrete_sequence=['#1a8c73'],
            text='pne_ingressantes'
        )
        
        fig5.update_layout(
            xaxis_title="Tipo de Necessidade",
            yaxis_title="Número de Ingressantes",
            height=450,
            showlegend=False,
            xaxis_tickangle=-45
        )
        
        fig5.update_traces(textposition='outside')
        
        st.plotly_chart(fig5, use_container_width=True)
    else:
        st.info("ℹ️ Não há dados de necessidades especiais para os filtros selecionados.")
    
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
