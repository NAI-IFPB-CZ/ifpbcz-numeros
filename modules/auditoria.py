import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def auditoria_module(data_gen):
    """Módulo de Auditoria"""
    
    # Cabeçalho com logo
    display_header_with_logo("Auditoria")
    
    # Gerar dados
    dados_auditoria = data_gen.gerar_dados_auditoria()
    
    # Filtrar dados para 2025
    dados_2025 = dados_auditoria[dados_auditoria['ano'] == 2025]
    
    # Calcular KPIs
    total_recomendacoes_emitidas = dados_2025['recomendacoes_emitidas'].sum()
    total_recomendacoes_atendidas = dados_2025['recomendacoes_atendidas'].sum()
    
    # Percentual de recomendações atendidas
    if total_recomendacoes_emitidas > 0:
        percentual_atendidas = (total_recomendacoes_atendidas / total_recomendacoes_emitidas) * 100
    else:
        percentual_atendidas = 0
    
    # Órgão com maior número de recomendações
    orgao_maior_recomendacoes = dados_2025.groupby('unidade')['recomendacoes_emitidas'].sum().idxmax()
    
    # Cartões de KPI
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ESTOQUE DE RECOMENDAÇÕES EMITIDAS</div>
            <div class="kpi-value">{total_recomendacoes_emitidas:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">PERCENTUAL DE RECOMENDAÇÕES ATENDIDAS</div>
            <div class="kpi-value">{percentual_atendidas:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ÓRGÃO DE 2025 TEVE O MAIOR Nº DE RECOMENDAÇÕES</div>
            <div class="kpi-value" style="font-size: 1.5rem;">{orgao_maior_recomendacoes}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Gráfico 1: Evolução das Recomendações por Unidade
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução das Recomendações por Unidade")
    
    unidade_evolucao = st.selectbox(
        "Unidade:",
        ["Todas"] + list(dados_auditoria['unidade'].unique()),
        key="unidade_evolucao_aud"
    )
    
    # Filtrar dados
    if unidade_evolucao == "Todas":
        dados_evolucao = dados_auditoria.groupby('ano').agg({
            'recomendacoes_emitidas': 'sum',
            'recomendacoes_atendidas': 'sum'
        }).reset_index()
        titulo_evolucao = "Evolução das Recomendações - Todas as Unidades"
    else:
        dados_evolucao = dados_auditoria[dados_auditoria['unidade'] == unidade_evolucao]
        titulo_evolucao = f"Evolução das Recomendações - {unidade_evolucao}"
    
    # Criar gráfico de linha
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dados_evolucao['ano'],
        y=dados_evolucao['recomendacoes_emitidas'],
        mode='lines+markers',
        name='Recomendações Emitidas',
        line=dict(color='#1a8c73', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=dados_evolucao['ano'],
        y=dados_evolucao['recomendacoes_atendidas'],
        mode='lines+markers',
        name='Recomendações Atendidas',
        line=dict(color='#0d5a4e', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title=titulo_evolucao,
        xaxis_title="Ano",
        yaxis_title="Número de Recomendações",
        height=500,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 2: Recomendações por Unidade (Acumulado)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Recomendações por Unidade (Acumulado)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        periodo_acumulado = st.selectbox(
            "Período:",
            ["Todos os anos", "Últimos 5 anos", "Últimos 10 anos"],
            key="periodo_acumulado"
        )
    
    with col2:
        forma_exibicao_acum = st.selectbox(
            "Forma de exibição:",
            ["Quantidade", "Percentual"],
            key="forma_exibicao_acum"
        )
    
    # Filtrar dados por período
    ano_atual = dados_auditoria['ano'].max()
    
    if periodo_acumulado == "Últimos 5 anos":
        dados_acumulado = dados_auditoria[dados_auditoria['ano'] >= (ano_atual - 4)]
    elif periodo_acumulado == "Últimos 10 anos":
        dados_acumulado = dados_auditoria[dados_auditoria['ano'] >= (ano_atual - 9)]
    else:  # Todos os anos
        dados_acumulado = dados_auditoria
    
    # Agrupar por unidade
    dados_acumulado_grafico = dados_acumulado.groupby('unidade').agg({
        'recomendacoes_emitidas': 'sum',
        'recomendacoes_atendidas': 'sum'
    }).reset_index()
    
    if forma_exibicao_acum == "Percentual":
        total_emitidas = dados_acumulado_grafico['recomendacoes_emitidas'].sum()
        dados_acumulado_grafico['percentual_emitidas'] = (dados_acumulado_grafico['recomendacoes_emitidas'] / total_emitidas) * 100
        
        fig2 = px.bar(
            dados_acumulado_grafico,
            x='unidade',
            y='percentual_emitidas',
            title=f"Recomendações por Unidade (%) - {periodo_acumulado}",
            color_discrete_sequence=['#1a8c73']
        )
        
        fig2.update_layout(
            xaxis_title="Unidade",
            yaxis_title="Percentual (%)",
            xaxis_tickangle=-45,
            height=500
        )
        
    else:  # Quantidade
        # Reorganizar dados para gráfico agrupado
        dados_melted = dados_acumulado_grafico.melt(
            id_vars=['unidade'],
            value_vars=['recomendacoes_emitidas', 'recomendacoes_atendidas'],
            var_name='tipo',
            value_name='quantidade'
        )
        
        # Mapear nomes
        mapeamento_tipos = {
            'recomendacoes_emitidas': 'Emitidas',
            'recomendacoes_atendidas': 'Atendidas'
        }
        
        dados_melted['tipo'] = dados_melted['tipo'].map(mapeamento_tipos)
        
        fig2 = px.bar(
            dados_melted,
            x='unidade',
            y='quantidade',
            color='tipo',
            title=f"Recomendações por Unidade - {periodo_acumulado}",
            color_discrete_sequence=['#1a8c73', '#0d5a4e'],
            barmode='group'
        )
        
        fig2.update_layout(
            xaxis_title="Unidade",
            yaxis_title="Quantidade",
            xaxis_tickangle=-45,
            height=500
        )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 3: Taxa de Atendimento por Unidade
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Taxa de Atendimento por Unidade")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_taxa = st.selectbox(
            "Ano:",
            sorted(dados_auditoria['ano'].unique(), reverse=True),
            key="ano_taxa_aud"
        )
    
    with col2:
        ordenacao = st.selectbox(
            "Ordenar por:",
            ["Taxa de Atendimento", "Número de Recomendações"],
            key="ordenacao_taxa"
        )
    
    # Filtrar dados
    dados_taxa = dados_auditoria[dados_auditoria['ano'] == ano_taxa]
    dados_taxa_grafico = dados_taxa.groupby('unidade').agg({
        'recomendacoes_emitidas': 'sum',
        'recomendacoes_atendidas': 'sum'
    }).reset_index()
    
    # Calcular taxa de atendimento
    dados_taxa_grafico['taxa_atendimento'] = (dados_taxa_grafico['recomendacoes_atendidas'] / dados_taxa_grafico['recomendacoes_emitidas']) * 100
    
    # Ordenar dados
    if ordenacao == "Taxa de Atendimento":
        dados_taxa_grafico = dados_taxa_grafico.sort_values('taxa_atendimento', ascending=True)
    else:  # Número de Recomendações
        dados_taxa_grafico = dados_taxa_grafico.sort_values('recomendacoes_emitidas', ascending=True)
    
    # Criar gráfico horizontal
    fig3 = px.bar(
        dados_taxa_grafico,
        x='taxa_atendimento',
        y='unidade',
        title=f"Taxa de Atendimento por Unidade - {ano_taxa}",
        color='taxa_atendimento',
        color_continuous_scale='Greens',
        orientation='h'
    )
    
    fig3.update_layout(
        xaxis_title="Taxa de Atendimento (%)",
        yaxis_title="Unidade",
        height=500
    )
    
    # Adicionar linha de referência
    fig3.add_vline(x=75, line_dash="dash", line_color="red", annotation_text="Meta: 75%")
    
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 4: Distribuição das Recomendações
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Distribuição das Recomendações")
    
    ano_distribuicao = st.selectbox(
        "Ano:",
        sorted(dados_auditoria['ano'].unique(), reverse=True),
        key="ano_distribuicao_aud"
    )
    
    # Filtrar dados
    dados_distribuicao = dados_auditoria[dados_auditoria['ano'] == ano_distribuicao]
    dados_distribuicao_grafico = dados_distribuicao.groupby('unidade')['recomendacoes_emitidas'].sum().reset_index()
    
    fig4 = px.pie(
        dados_distribuicao_grafico,
        values='recomendacoes_emitidas',
        names='unidade',
        title=f"Distribuição das Recomendações por Unidade - {ano_distribuicao}",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig4.update_traces(textposition='inside', textinfo='percent+label')
    
    st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 5: Tendência Geral
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Tendência Geral das Recomendações")
    
    # Calcular dados agregados
    dados_tendencia = dados_auditoria.groupby('ano').agg({
        'recomendacoes_emitidas': 'sum',
        'recomendacoes_atendidas': 'sum'
    }).reset_index()
    
    # Calcular taxa de atendimento anual
    dados_tendencia['taxa_atendimento_anual'] = (dados_tendencia['recomendacoes_atendidas'] / dados_tendencia['recomendacoes_emitidas']) * 100
    
    # Criar gráfico com dois eixos Y
    fig5 = go.Figure()
    
    # Barras para recomendações
    fig5.add_trace(go.Bar(
        x=dados_tendencia['ano'],
        y=dados_tendencia['recomendacoes_emitidas'],
        name='Emitidas',
        marker_color='#1a8c73',
        yaxis='y'
    ))
    
    fig5.add_trace(go.Bar(
        x=dados_tendencia['ano'],
        y=dados_tendencia['recomendacoes_atendidas'],
        name='Atendidas',
        marker_color='#0d5a4e',
        yaxis='y'
    ))
    
    # Linha para taxa de atendimento
    fig5.add_trace(go.Scatter(
        x=dados_tendencia['ano'],
        y=dados_tendencia['taxa_atendimento_anual'],
        mode='lines+markers',
        name='Taxa de Atendimento (%)',
        line=dict(color='#2db896', width=3),
        marker=dict(size=8),
        yaxis='y2'
    ))
    
    # Configurar layout com dois eixos Y
    fig5.update_layout(
        title="Tendência Geral das Recomendações",
        xaxis_title="Ano",
        yaxis=dict(
            title="Número de Recomendações",
            side="left"
        ),
        yaxis2=dict(
            title="Taxa de Atendimento (%)",
            side="right",
            overlaying="y"
        ),
        height=500,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig5, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
