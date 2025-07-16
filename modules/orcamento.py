import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def orcamento_module(data_gen):
    """Módulo de Orçamento"""
    
    # Cabeçalho com logo
    display_header_with_logo("Orçamento")
    
    # Gerar dados
    dados_orcamento = data_gen.gerar_dados_orcamento()
    
    # Filtrar dados para 2025
    dados_2025 = dados_orcamento[dados_orcamento['ano'] == 2025]
    
    # Calcular KPIs
    total_dotacao = dados_2025['dotacao'].sum()
    total_empenhado = dados_2025['empenhado'].sum()
    total_pago = dados_2025['pago'].sum()
    
    # Cartões de KPI
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ORÇAMENTO DOTAÇÃO</div>
            <div class="kpi-value">{data_gen.formatar_valor_monetario(total_dotacao)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ORÇAMENTO EMPENHADO</div>
            <div class="kpi-value">{data_gen.formatar_valor_monetario(total_empenhado)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ORÇAMENTO PAGO</div>
            <div class="kpi-value">{data_gen.formatar_valor_monetario(total_pago)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Painel de Gastos
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("💰 Painel de Gastos por Categoria")
    
    col1, col2 = st.columns(2)
    
    with col1:
        unidade_selecionada = st.selectbox(
            "Selecione uma unidade:",
            ["Todas"] + list(dados_orcamento['unidade'].unique()),
            key="unidade_orcamento"
        )
    
    with col2:
        ano_selecionado = st.selectbox(
            "Selecione um ano:",
            sorted(dados_orcamento['ano'].unique(), reverse=True),
            key="ano_orcamento"
        )
    
    # Filtrar dados
    dados_filtrados = dados_orcamento[dados_orcamento['ano'] == ano_selecionado]
    
    if unidade_selecionada != "Todas":
        dados_filtrados = dados_filtrados[dados_filtrados['unidade'] == unidade_selecionada]
    
    # Agrupar por categoria
    dados_categorias = dados_filtrados.groupby('categoria').agg({
        'dotacao': 'sum',
        'empenhado': 'sum',
        'pago': 'sum'
    }).reset_index()
    
    # Ícones para cada categoria
    icones_categorias = {
        "Pessoal e Encargos Sociais": "👥",
        "Custeio": "🏢",
        "Investimentos": "💎",
        "Manutenção": "🔧",
        "Equipamentos": "💻",
        "Obras": "🏗️"
    }
    
    # Criar layout em grid para categorias
    num_colunas = 3
    colunas = st.columns(num_colunas)
    
    for idx, (_, row) in enumerate(dados_categorias.iterrows()):
        col_idx = idx % num_colunas
        categoria = row['categoria']
        icone = icones_categorias.get(categoria, "📊")
        
        with colunas[col_idx]:
            st.markdown(f"""
            <div class="kpi-container">
                <div style="text-align: center; font-size: 2rem; margin-bottom: 1rem;">
                    {icone}
                </div>
                <div class="kpi-title">{categoria}</div>
                <div style="color: #1a8c73; font-size: 1.2rem; margin: 0.5rem 0;">
                    <strong>Dotação:</strong> {data_gen.formatar_valor_monetario(row['dotacao'])}
                </div>
                <div style="color: #0d5a4e; font-size: 1.2rem; margin: 0.5rem 0;">
                    <strong>Empenhado:</strong> {data_gen.formatar_valor_monetario(row['empenhado'])}
                </div>
                <div style="color: #2db896; font-size: 1.2rem; margin: 0.5rem 0;">
                    <strong>Pago:</strong> {data_gen.formatar_valor_monetario(row['pago'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 1: Comparação Dotação vs Empenhado vs Pago
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Comparação Orçamentária por Categoria")
    
    # Reorganizar dados para o gráfico
    dados_melted = dados_categorias.melt(
        id_vars=['categoria'],
        value_vars=['dotacao', 'empenhado', 'pago'],
        var_name='tipo',
        value_name='valor'
    )
    
    # Mapear nomes
    mapeamento_tipos = {
        'dotacao': 'Dotação',
        'empenhado': 'Empenhado',
        'pago': 'Pago'
    }
    
    dados_melted['tipo'] = dados_melted['tipo'].map(mapeamento_tipos)
    
    fig = px.bar(
        dados_melted,
        x='categoria',
        y='valor',
        color='tipo',
        title=f"Comparação Orçamentária por Categoria - {ano_selecionado}",
        color_discrete_sequence=['#1a8c73', '#0d5a4e', '#2db896'],
        barmode='group'
    )
    
    fig.update_layout(
        xaxis_title="Categoria",
        yaxis_title="Valor (R$)",
        xaxis_tickangle=-45,
        height=500
    )
    
    # Formatar valores no eixo Y
    fig.update_yaxes(tickformat='.0f')
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 2: Evolução Orçamentária
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução Orçamentária")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tipo_evolucao = st.selectbox(
            "Tipo de Orçamento:",
            ["Dotação", "Empenhado", "Pago"],
            key="tipo_evolucao"
        )
    
    with col2:
        unidade_evolucao = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_orcamento['unidade'].unique()),
            key="unidade_evolucao"
        )
    
    # Filtrar dados para evolução
    dados_evolucao = dados_orcamento.copy()
    
    if unidade_evolucao != "Todas":
        dados_evolucao = dados_evolucao[dados_evolucao['unidade'] == unidade_evolucao]
    
    # Mapear tipo selecionado
    mapeamento_tipo = {
        "Dotação": "dotacao",
        "Empenhado": "empenhado",
        "Pago": "pago"
    }
    
    tipo_coluna = mapeamento_tipo[tipo_evolucao]
    
    # Agrupar por ano
    dados_evolucao_grafico = dados_evolucao.groupby('ano')[tipo_coluna].sum().reset_index()
    
    fig2 = px.line(
        dados_evolucao_grafico,
        x='ano',
        y=tipo_coluna,
        title=f"Evolução do Orçamento {tipo_evolucao} - {unidade_evolucao}",
        markers=True,
        color_discrete_sequence=['#1a8c73']
    )
    
    fig2.update_layout(
        xaxis_title="Ano",
        yaxis_title=f"Valor {tipo_evolucao} (R$)",
        height=400
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 3: Eficiência Orçamentária (Percentual de Execução)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Eficiência Orçamentária")
    
    # Calcular percentuais
    dados_eficiencia = dados_filtrados.copy()
    dados_eficiencia['percentual_empenhado'] = (dados_eficiencia['empenhado'] / dados_eficiencia['dotacao']) * 100
    dados_eficiencia['percentual_pago'] = (dados_eficiencia['pago'] / dados_eficiencia['dotacao']) * 100
    
    # Agrupar por categoria
    dados_eficiencia_grafico = dados_eficiencia.groupby('categoria').agg({
        'percentual_empenhado': 'mean',
        'percentual_pago': 'mean'
    }).reset_index()
    
    # Reorganizar dados
    dados_eficiencia_melted = dados_eficiencia_grafico.melt(
        id_vars=['categoria'],
        value_vars=['percentual_empenhado', 'percentual_pago'],
        var_name='tipo',
        value_name='percentual'
    )
    
    # Mapear nomes
    mapeamento_eficiencia = {
        'percentual_empenhado': '% Empenhado',
        'percentual_pago': '% Pago'
    }
    
    dados_eficiencia_melted['tipo'] = dados_eficiencia_melted['tipo'].map(mapeamento_eficiencia)
    
    fig3 = px.bar(
        dados_eficiencia_melted,
        x='categoria',
        y='percentual',
        color='tipo',
        title=f"Eficiência Orçamentária por Categoria - {ano_selecionado}",
        color_discrete_sequence=['#1a8c73', '#0d5a4e'],
        barmode='group'
    )
    
    fig3.update_layout(
        xaxis_title="Categoria",
        yaxis_title="Percentual (%)",
        xaxis_tickangle=-45,
        height=400
    )
    
    # Adicionar linha de referência em 100%
    fig3.add_hline(y=100, line_dash="dash", line_color="red", annotation_text="100%")
    
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
