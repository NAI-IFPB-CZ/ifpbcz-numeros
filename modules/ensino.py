import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def ensino_module(data_gen):
    """Módulo de Ensino"""
    
    # Cabeçalho com logo
    display_header_with_logo("Ensino")
    
    # Gerar dados
    dados_ensino = data_gen.gerar_dados_ensino()
    
    # Filtrar dados para o ano mais recente
    ano_atual = dados_ensino['ano'].max()
    dados_ano_atual = dados_ensino[dados_ensino['ano'] == ano_atual]
    
    # Calcular KPIs
    total_matriculados = dados_ano_atual['matriculados'].sum()
    total_formados = dados_ano_atual['formados'].sum()
    total_desistentes = dados_ano_atual['desistentes'].sum()
    total_transferidos = dados_ano_atual['transferidos'].sum()
    
    # Cartões de KPI
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ALUNOS MATRICULADOS</div>
            <div class="kpi-value">{total_matriculados:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ALUNOS FORMADOS</div>
            <div class="kpi-value">{total_formados:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">DESISTENTES</div>
            <div class="kpi-value">{total_desistentes:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TRANSFERIDOS</div>
            <div class="kpi-value">{total_transferidos:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Gráfico 1: Número de Alunos por Campus
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Número de Alunos por Campus")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        # Seleção de campus
        campus_disponivel = ["Todos"] + sorted(dados_ensino['campus'].unique())
        campus_selecionados = st.multiselect(
            "Selecione os Campus:",
            options=campus_disponivel,
            default=["Todos"],
            key="campus_multi_1"
        )
        
        # Se "Todos" estiver selecionado, incluir todos os campus
        if "Todos" in campus_selecionados:
            campus_filtro = dados_ensino['campus'].unique()
        else:
            campus_filtro = campus_selecionados
    
    with col2:
        forma_exibicao = st.selectbox(
            "Escolha a forma de exibição:",
            ["Matriculados", "Formados", "Desistentes", "Transferidos"],
            key="forma_exib_1"
        )
    
    with col3:
        nivel_detalhe = st.selectbox(
            "Nível de detalhe:",
            ["Geral", "Por Modalidade", "Por Curso"],
            key="nivel_det_1"
        )
    
    with col4:
        ano_selecionado = st.selectbox(
            "Ano:",
            sorted(dados_ensino['ano'].unique(), reverse=True),
            key="ano_1"
        )
    
    # Filtrar dados
    dados_filtrados = dados_ensino[
        (dados_ensino['ano'] == ano_selecionado) & 
        (dados_ensino['campus'].isin(campus_filtro))
    ]
    
    # Preparar dados para o gráfico
    metrica_map = {
        "Matriculados": "matriculados",
        "Formados": "formados", 
        "Desistentes": "desistentes",
        "Transferidos": "transferidos"
    }
    
    if nivel_detalhe == "Geral":
        dados_grafico = dados_filtrados.groupby('campus')[metrica_map[forma_exibicao]].sum().reset_index()
    elif nivel_detalhe == "Por Modalidade":
        dados_grafico = dados_filtrados.groupby(['campus', 'modalidade'])[metrica_map[forma_exibicao]].sum().reset_index()
    else:  # Por Curso
        dados_grafico = dados_filtrados.groupby(['campus', 'curso'])[metrica_map[forma_exibicao]].sum().reset_index()
    
    # Criar gráfico
    if nivel_detalhe == "Geral":
        fig = px.bar(
            dados_grafico,
            x='campus',
            y=metrica_map[forma_exibicao],
            title=f"Nº de {forma_exibicao} por Campus - {ano_selecionado}",
            color_discrete_sequence=['#1a8c73']
        )
    elif nivel_detalhe == "Por Modalidade":
        fig = px.bar(
            dados_grafico,
            x='campus',
            y=metrica_map[forma_exibicao],
            color='modalidade',
            title=f"Nº de {forma_exibicao} por Campus e Modalidade - {ano_selecionado}",
            color_discrete_sequence=['#1a8c73', '#0d5a4e', '#2db896']
        )
    else:  # Por Curso
        fig = px.bar(
            dados_grafico,
            x='campus',
            y=metrica_map[forma_exibicao],
            color='curso',
            title=f"Nº de {forma_exibicao} por Campus e Curso - {ano_selecionado}"
        )
    
    fig.update_layout(
        xaxis_title="Campus",
        yaxis_title=f"Número de {forma_exibicao}",
        xaxis_tickangle=-45,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Sistema Acadêmico IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 2: Evolução do Número de Alunos
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução do Número de Alunos")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Seleção de campus para evolução
        campus_evolucao = st.multiselect(
            "Escolha os Campus:",
            options=["Todos"] + sorted(dados_ensino['campus'].unique()),
            default=["Todos"],
            key="campus_evolucao"
        )
        
        # Se "Todos" estiver selecionado, incluir todos os campus
        if "Todos" in campus_evolucao:
            campus_filtro_evolucao = dados_ensino['campus'].unique()
        else:
            campus_filtro_evolucao = campus_evolucao
    
    with col2:
        forma_exibicao_2 = st.selectbox(
            "Forma de exibição:",
            ["Matriculados", "Formados", "Desistentes", "Transferidos"],
            key="forma_exib_2"
        )
    
    with col3:
        tipo_grafico = st.selectbox(
            "Tipo de gráfico:",
            ["Linha", "Área", "Barras"],
            key="tipo_grafico_evolucao"
        )
    
    # Filtrar dados para evolução
    dados_evolucao = dados_ensino[dados_ensino['campus'].isin(campus_filtro_evolucao)]
    
    if len(campus_filtro_evolucao) == 1 and "Todos" not in campus_evolucao:
        # Um campus específico
        dados_evolucao = dados_evolucao.groupby('ano')[metrica_map[forma_exibicao_2]].sum().reset_index()
        titulo_grafico = f"Evolução do Nº de {forma_exibicao_2} - {campus_filtro_evolucao[0]}"
        
        # Criar gráfico baseado no tipo selecionado
        if tipo_grafico == "Linha":
            fig2 = px.line(
                dados_evolucao,
                x='ano',
                y=metrica_map[forma_exibicao_2],
                title=titulo_grafico,
                markers=True,
                color_discrete_sequence=['#1a8c73']
            )
        elif tipo_grafico == "Área":
            fig2 = px.area(
                dados_evolucao,
                x='ano',
                y=metrica_map[forma_exibicao_2],
                title=titulo_grafico,
                color_discrete_sequence=['#1a8c73']
            )
        else:  # Barras
            fig2 = px.bar(
                dados_evolucao,
                x='ano',
                y=metrica_map[forma_exibicao_2],
                title=titulo_grafico,
                color_discrete_sequence=['#1a8c73']
            )
    else:
        # Múltiplos campus ou todos
        if "Todos" in campus_evolucao:
            dados_evolucao = dados_ensino.groupby('ano')[metrica_map[forma_exibicao_2]].sum().reset_index()
            titulo_grafico = f"Evolução do Nº de {forma_exibicao_2} - Todos os Campus"
        else:
            dados_evolucao = dados_evolucao.groupby(['ano', 'campus'])[metrica_map[forma_exibicao_2]].sum().reset_index()
            titulo_grafico = f"Evolução do Nº de {forma_exibicao_2} - Campus Selecionados"
        
        # Criar gráfico baseado no tipo selecionado
        if tipo_grafico == "Linha":
            if 'campus' in dados_evolucao.columns:
                fig2 = px.line(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    color='campus',
                    title=titulo_grafico,
                    markers=True
                )
            else:
                fig2 = px.line(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    title=titulo_grafico,
                    markers=True,
                    color_discrete_sequence=['#1a8c73']
                )
        elif tipo_grafico == "Área":
            if 'campus' in dados_evolucao.columns:
                fig2 = px.area(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    color='campus',
                    title=titulo_grafico
                )
            else:
                fig2 = px.area(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    title=titulo_grafico,
                    color_discrete_sequence=['#1a8c73']
                )
        else:  # Barras
            if 'campus' in dados_evolucao.columns:
                fig2 = px.bar(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    color='campus',
                    title=titulo_grafico,
                    barmode='group'
                )
            else:
                fig2 = px.bar(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    title=titulo_grafico,
                    color_discrete_sequence=['#1a8c73']
                )
    
    fig2.update_layout(
        xaxis_title="Ano",
        yaxis_title=f"Número de {forma_exibicao_2}",
        height=500
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Sistema Acadêmico IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Gráfico 3: Comparação entre Campus
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("🏛️ Comparação entre Campus")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Seleção de campus para comparação
        campus_comparacao = st.multiselect(
            "Selecione até 10 Campus para comparar:",
            options=sorted(dados_ensino['campus'].unique()),
            default=sorted(dados_ensino['campus'].unique())[:5],
            max_selections=10,
            key="campus_comparacao"
        )
    
    with col2:
        metrica_comparacao = st.selectbox(
            "Métrica para comparação:",
            ["Matriculados", "Formados", "Desistentes", "Transferidos"],
            key="metrica_comparacao"
        )
    
    with col3:
        periodo_comparacao = st.selectbox(
            "Período:",
            ["Último Ano", "Últimos 3 Anos", "Últimos 5 Anos", "Todos os Anos"],
            key="periodo_comparacao"
        )
    
    if campus_comparacao:
        # Filtrar dados por período
        if periodo_comparacao == "Último Ano":
            dados_comp = dados_ensino[dados_ensino['ano'] == dados_ensino['ano'].max()]
        elif periodo_comparacao == "Últimos 3 Anos":
            dados_comp = dados_ensino[dados_ensino['ano'] >= dados_ensino['ano'].max() - 2]
        elif periodo_comparacao == "Últimos 5 Anos":
            dados_comp = dados_ensino[dados_ensino['ano'] >= dados_ensino['ano'].max() - 4]
        else:  # Todos os anos
            dados_comp = dados_ensino.copy()
        
        # Filtrar por campus selecionados
        dados_comp = dados_comp[dados_comp['campus'].isin(campus_comparacao)]
        
        # Agrupar dados
        dados_comp_grouped = dados_comp.groupby('campus')[metrica_map[metrica_comparacao]].sum().reset_index()
        dados_comp_grouped = dados_comp_grouped.sort_values(metrica_map[metrica_comparacao], ascending=False)
        
        # Criar gráfico de barras horizontais
        fig3 = px.bar(
            dados_comp_grouped,
            x=metrica_map[metrica_comparacao],
            y='campus',
            orientation='h',
            title=f"Comparação: {metrica_comparacao} - {periodo_comparacao}",
            color=metrica_map[metrica_comparacao],
            color_continuous_scale='Viridis',
            text=metrica_map[metrica_comparacao]
        )
        
        fig3.update_layout(
            xaxis_title=f"Número de {metrica_comparacao}",
            yaxis_title="Campus",
            height=max(400, len(campus_comparacao) * 40),
            showlegend=False
        )
        
        fig3.update_traces(texttemplate='%{text}', textposition='outside')
        
        st.plotly_chart(fig3, use_container_width=True)
        
        # Tabela com dados detalhados
        st.subheader("📋 Dados Detalhados")
        
        # Criar tabela resumo
        dados_resumo = dados_comp.groupby('campus').agg({
            'matriculados': 'sum',
            'formados': 'sum',
            'desistentes': 'sum',
            'transferidos': 'sum'
        }).reset_index()
        
        # Calcular percentuais
        dados_resumo['taxa_formacao'] = (dados_resumo['formados'] / dados_resumo['matriculados'] * 100).round(1)
        dados_resumo['taxa_desistencia'] = (dados_resumo['desistentes'] / dados_resumo['matriculados'] * 100).round(1)
        dados_resumo['taxa_transferencia'] = (dados_resumo['transferidos'] / dados_resumo['matriculados'] * 100).round(1)
        
        # Renomear colunas
        dados_resumo.columns = [
            'Campus', 'Matriculados', 'Formados', 'Desistentes', 'Transferidos',
            'Taxa Formação (%)', 'Taxa Desistência (%)', 'Taxa Transferência (%)'
        ]
        
        # Ordenar por número de matriculados
        dados_resumo = dados_resumo.sort_values('Matriculados', ascending=False)
        
        st.dataframe(dados_resumo, use_container_width=True, hide_index=True)
    
    else:
        st.warning("Selecione pelo menos um campus para comparação.")
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Sistema Acadêmico IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Rodapé
    display_footer()
