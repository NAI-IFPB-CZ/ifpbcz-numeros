import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def ensino_module(data_gen):
    """
    Módulo de Ensino - Dashboard de Indicadores Educacionais
    
    Este módulo apresenta análises completas sobre dados educacionais do IFPB-CZ,
    incluindo métricas de matriculados, formados, desistentes e transferidos.
    
    Funcionalidades principais:
    - KPIs consolidados do ano atual
    - Gráficos interativos por campus, modalidade e curso
    - Análise temporal de evolução dos indicadores
    - Comparação entre campus com tabela detalhada
    
    Args:
        data_gen: Instância do DataGenerator para obter dados sintéticos
    """
    
    # Cabeçalho com logo institucional
    display_header_with_logo("Ensino")
    
    # Gerar dados sintéticos de ensino usando o DataGenerator
    dados_ensino = data_gen.gerar_dados_ensino()
    
    # Filtrar dados para o ano mais recente para cálculo dos KPIs
    ano_atual = dados_ensino['ano'].max()
    dados_ano_atual = dados_ensino[dados_ensino['ano'] == ano_atual]
    
    # Calcular indicadores-chave (KPIs) consolidados para o ano atual
    total_matriculados = dados_ano_atual['matriculados'].sum()    # Total de alunos matriculados
    total_formados = dados_ano_atual['formados'].sum()            # Total de alunos formados
    total_desistentes = dados_ano_atual['desistentes'].sum()      # Total de alunos desistentes
    total_transferidos = dados_ano_atual['transferidos'].sum()    # Total de alunos transferidos
    
    # ==================== SEÇÃO 1: CARTÕES DE KPIs ====================
    # Exibir indicadores principais em formato de cartões visuais
    # Utiliza CSS personalizado para estilização dos containers
    
    col1, col2, col3, col4 = st.columns(4)
    
    # KPI 1: Alunos Matriculados (indicador principal de capacidade)
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ALUNOS MATRICULADOS</div>
            <div class="kpi-value">{total_matriculados:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 2: Alunos Formados (indicador de sucesso acadêmico)
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ALUNOS FORMADOS</div>
            <div class="kpi-value">{total_formados:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 3: Desistentes (indicador de retenção - quanto menor, melhor)
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">DESISTENTES</div>
            <div class="kpi-value">{total_desistentes:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 4: Transferidos (indicador de mobilidade acadêmica)
    with col4:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TRANSFERIDOS</div>
            <div class="kpi-value">{total_transferidos:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")  # Separador visual entre seções
    
    # ==================== SEÇÃO 2: GRÁFICO DE ALUNOS POR CAMPUS ====================
    # Gráfico interativo com múltiplos filtros para análise detalhada por campus
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Número de Alunos por Campus")
    
    # Criar 4 colunas para organizar os controles de filtro
    col1, col2, col3, col4 = st.columns(4)
    
    # FILTRO 1: Seleção múltipla de campus
    with col1:
        # Preparar lista de campus disponíveis (incluindo opção "Todos")
        campus_disponivel = ["Todos"] + sorted(dados_ensino['campus'].unique())
        campus_selecionados = st.multiselect(
            "Selecione os Campus:",
            options=campus_disponivel,
            default=["Todos"],  # Padrão: todos os campus selecionados
            key="campus_multi_1"
        )
        
        # Lógica para processamento da seleção de campus
        # Se "Todos" estiver selecionado, incluir todos os campus automaticamente
        if "Todos" in campus_selecionados:
            campus_filtro = dados_ensino['campus'].unique()
        else:
            campus_filtro = campus_selecionados
    
    # FILTRO 2: Métrica a ser exibida no gráfico
    with col2:
        forma_exibicao = st.selectbox(
            "Escolha a forma de exibição:",
            ["Matriculados", "Formados", "Desistentes", "Transferidos"],
            key="forma_exib_1"
        )
    
    # FILTRO 3: Nível de detalhamento dos dados
    with col3:
        nivel_detalhe = st.selectbox(
            "Nível de detalhe:",
            ["Geral", "Por Modalidade", "Por Curso"],  # Três níveis de granularidade
            key="nivel_det_1"
        )
    
    # FILTRO 4: Ano de referência
    with col4:
        ano_selecionado = st.selectbox(
            "Ano:",
            sorted(dados_ensino['ano'].unique(), reverse=True),  # Anos em ordem decrescente
            key="ano_1"
        )
    
    # Aplicar filtros aos dados baseado nas seleções do usuário
    dados_filtrados = dados_ensino[
        (dados_ensino['ano'] == ano_selecionado) & 
        (dados_ensino['campus'].isin(campus_filtro))
    ]
    
    # Mapeamento das métricas para os nomes das colunas no DataFrame
    metrica_map = {
        "Matriculados": "matriculados",
        "Formados": "formados", 
        "Desistentes": "desistentes",
        "Transferidos": "transferidos"
    }
    
    # Processar dados baseado no nível de detalhe selecionado
    if nivel_detalhe == "Geral":
        # Agrupamento simples por campus (visão consolidada)
        dados_grafico = dados_filtrados.groupby('campus')[metrica_map[forma_exibicao]].sum().reset_index()
    elif nivel_detalhe == "Por Modalidade":
        # Agrupamento por campus e modalidade (presencial, EAD, etc.)
        dados_grafico = dados_filtrados.groupby(['campus', 'modalidade'])[metrica_map[forma_exibicao]].sum().reset_index()
    else:  # Por Curso
        # Agrupamento por campus e curso (maior nível de detalhamento)
        dados_grafico = dados_filtrados.groupby(['campus', 'curso'])[metrica_map[forma_exibicao]].sum().reset_index()
    
    # Criação do gráfico baseado no nível de detalhe
    if nivel_detalhe == "Geral":
        # Gráfico de barras simples (uma barra por campus)
        fig = px.bar(
            dados_grafico,
            x='campus',
            y=metrica_map[forma_exibicao],
            title=f"Nº de {forma_exibicao} por Campus - {ano_selecionado}",
            color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
        )
    elif nivel_detalhe == "Por Modalidade":
        # Gráfico de barras agrupadas por modalidade
        fig = px.bar(
            dados_grafico,
            x='campus',
            y=metrica_map[forma_exibicao],
            color='modalidade',  # Cores diferentes para cada modalidade
            title=f"Nº de {forma_exibicao} por Campus e Modalidade - {ano_selecionado}",
            color_discrete_sequence=['#1a8c73', '#0d5a4e', '#2db896']  # Paleta de cores institucional
        )
    else:  # Por Curso
        # Gráfico de barras agrupadas por curso (pode ter muitas cores)
        fig = px.bar(
            dados_grafico,
            x='campus',
            y=metrica_map[forma_exibicao],
            color='curso',  # Cores diferentes para cada curso
            title=f"Nº de {forma_exibicao} por Campus e Curso - {ano_selecionado}"
        )
    
    # Configurações de layout do gráfico
    fig.update_layout(
        xaxis_title="Campus",
        yaxis_title=f"Número de {forma_exibicao}",
        xaxis_tickangle=-45,  # Rotacionar labels do eixo X para melhor legibilidade
        height=500  # Altura fixa para consistência visual
    )
    
    # Renderizar o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: Sistema Acadêmico IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ==================== SEÇÃO 3: EVOLUÇÃO TEMPORAL ====================
    # Gráfico de séries temporais para análise de tendências ao longo dos anos
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução do Número de Alunos")
    
    # Controles de filtro para análise temporal
    col1, col2, col3 = st.columns(3)
    
    # FILTRO 1: Seleção de campus para análise temporal
    with col1:
        campus_evolucao = st.multiselect(
            "Escolha os Campus:",
            options=["Todos"] + sorted(dados_ensino['campus'].unique()),
            default=["Todos"],
            key="campus_evolucao"
        )
        
        # Processar seleção de campus (similar à seção anterior)
        if "Todos" in campus_evolucao:
            campus_filtro_evolucao = dados_ensino['campus'].unique()
        else:
            campus_filtro_evolucao = campus_evolucao
    
    # FILTRO 2: Métrica para análise temporal
    with col2:
        forma_exibicao_2 = st.selectbox(
            "Forma de exibição:",
            ["Matriculados", "Formados", "Desistentes", "Transferidos"],
            key="forma_exib_2"
        )
    
    # FILTRO 3: Tipo de visualização gráfica
    with col3:
        tipo_grafico = st.selectbox(
            "Tipo de gráfico:",
            ["Linha", "Área", "Barras"],  # Diferentes tipos de visualização temporal
            key="tipo_grafico_evolucao"
        )
    
    # Filtrar dados baseado nos campus selecionados
    dados_evolucao = dados_ensino[dados_ensino['campus'].isin(campus_filtro_evolucao)]
    
    # Lógica para processamento baseado na quantidade de campus selecionados
    if len(campus_filtro_evolucao) == 1 and "Todos" not in campus_evolucao:
        # CASO 1: Um campus específico selecionado
        # Agregar dados apenas por ano (série temporal simples)
        dados_evolucao = dados_evolucao.groupby('ano')[metrica_map[forma_exibicao_2]].sum().reset_index()
        titulo_grafico = f"Evolução do Nº de {forma_exibicao_2} - {campus_filtro_evolucao[0]}"
        
        # Criar gráfico baseado no tipo selecionado (campus único)
        if tipo_grafico == "Linha":
            fig2 = px.line(
                dados_evolucao,
                x='ano',
                y=metrica_map[forma_exibicao_2],
                title=titulo_grafico,
                markers=True,  # Mostrar pontos nos dados
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
        # CASO 2: Múltiplos campus ou "Todos" selecionado
        if "Todos" in campus_evolucao:
            # Agregar todos os campus em uma única série temporal
            dados_evolucao = dados_ensino.groupby('ano')[metrica_map[forma_exibicao_2]].sum().reset_index()
            titulo_grafico = f"Evolução do Nº de {forma_exibicao_2} - Todos os Campus"
        else:
            # Manter separação por campus (múltiplas séries temporais)
            dados_evolucao = dados_evolucao.groupby(['ano', 'campus'])[metrica_map[forma_exibicao_2]].sum().reset_index()
            titulo_grafico = f"Evolução do Nº de {forma_exibicao_2} - Campus Selecionados"
        
        # Criar gráfico baseado no tipo selecionado (múltiplos campus)
        if tipo_grafico == "Linha":
            if 'campus' in dados_evolucao.columns:
                # Múltiplas linhas (uma por campus)
                fig2 = px.line(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    color='campus',  # Cor diferente para cada campus
                    title=titulo_grafico,
                    markers=True
                )
            else:
                # Linha única (todos os campus agregados)
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
                # Múltiplas áreas empilhadas
                fig2 = px.area(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    color='campus',
                    title=titulo_grafico
                )
            else:
                # Área única
                fig2 = px.area(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    title=titulo_grafico,
                    color_discrete_sequence=['#1a8c73']
                )
        else:  # Barras
            if 'campus' in dados_evolucao.columns:
                # Barras agrupadas por campus
                fig2 = px.bar(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    color='campus',
                    title=titulo_grafico,
                    barmode='group'  # Barras lado a lado
                )
            else:
                # Barras simples
                fig2 = px.bar(
                    dados_evolucao,
                    x='ano',
                    y=metrica_map[forma_exibicao_2],
                    title=titulo_grafico,
                    color_discrete_sequence=['#1a8c73']
                )
    
    # Configurações de layout do gráfico temporal
    fig2.update_layout(
        xaxis_title="Ano",
        yaxis_title=f"Número de {forma_exibicao_2}",
        height=500
    )
    
    # Renderizar gráfico temporal
    st.plotly_chart(fig2, use_container_width=True)
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: Sistema Acadêmico IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ==================== SEÇÃO 4: COMPARAÇÃO ENTRE CAMPUS ====================
    # Análise comparativa com ranking de campus e tabela detalhada de indicadores
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("🏛️ Comparação entre Campus")
    
    # Controles de filtro para análise comparativa
    col1, col2, col3 = st.columns(3)
    
    # FILTRO 1: Seleção de campus para comparação (máximo 10 para visualização)
    with col1:
        campus_comparacao = st.multiselect(
            "Selecione até 10 Campus para comparar:",
            options=sorted(dados_ensino['campus'].unique()),
            default=sorted(dados_ensino['campus'].unique())[:5],  # Padrão: primeiros 5 campus
            max_selections=10,  # Limite para evitar poluição visual
            key="campus_comparacao"
        )
    
    # FILTRO 2: Métrica para comparação
    with col2:
        metrica_comparacao = st.selectbox(
            "Métrica para comparação:",
            ["Matriculados", "Formados", "Desistentes", "Transferidos"],
            key="metrica_comparacao"
        )
    
    # FILTRO 3: Período de análise
    with col3:
        periodo_comparacao = st.selectbox(
            "Período:",
            ["Último Ano", "Últimos 3 Anos", "Últimos 5 Anos", "Todos os Anos"],
            key="periodo_comparacao"
        )
    
    # Verificar se há campus selecionados para comparação
    if campus_comparacao:
        # Filtrar dados baseado no período selecionado
        if periodo_comparacao == "Último Ano":
            dados_comp = dados_ensino[dados_ensino['ano'] == dados_ensino['ano'].max()]
        elif periodo_comparacao == "Últimos 3 Anos":
            dados_comp = dados_ensino[dados_ensino['ano'] >= dados_ensino['ano'].max() - 2]
        elif periodo_comparacao == "Últimos 5 Anos":
            dados_comp = dados_ensino[dados_ensino['ano'] >= dados_ensino['ano'].max() - 4]
        else:  # Todos os anos
            dados_comp = dados_ensino.copy()
        
        # Aplicar filtro de campus selecionados
        dados_comp = dados_comp[dados_comp['campus'].isin(campus_comparacao)]
        
        # Agregar dados por campus para o período selecionado
        dados_comp_grouped = dados_comp.groupby('campus')[metrica_map[metrica_comparacao]].sum().reset_index()
        # Ordenar em ordem decrescente para criar ranking
        dados_comp_grouped = dados_comp_grouped.sort_values(metrica_map[metrica_comparacao], ascending=False)
        
        # Criar gráfico de barras horizontais para melhor visualização do ranking
        fig3 = px.bar(
            dados_comp_grouped,
            x=metrica_map[metrica_comparacao],
            y='campus',
            orientation='h',  # Barras horizontais
            title=f"Comparação: {metrica_comparacao} - {periodo_comparacao}",
            color=metrica_map[metrica_comparacao],  # Cor baseada no valor
            color_continuous_scale='Viridis',  # Escala de cores
            text=metrica_map[metrica_comparacao]  # Mostrar valores nas barras
        )
        
        # Configurações do gráfico comparativo
        fig3.update_layout(
            xaxis_title=f"Número de {metrica_comparacao}",
            yaxis_title="Campus",
            height=max(400, len(campus_comparacao) * 40),  # Altura dinâmica baseada no número de campus
            showlegend=False  # Remover legenda desnecessária
        )
        
        # Configurar posição dos textos nas barras
        fig3.update_traces(texttemplate='%{text}', textposition='outside')
        
        # Renderizar gráfico comparativo
        st.plotly_chart(fig3, use_container_width=True)
        
        # ==================== TABELA DETALHADA DE INDICADORES ====================
        st.subheader("📋 Dados Detalhados")
        
        # Criar tabela resumo com todos os indicadores e taxas calculadas
        dados_resumo = dados_comp.groupby('campus').agg({
            'matriculados': 'sum',
            'formados': 'sum',
            'desistentes': 'sum',
            'transferidos': 'sum'
        }).reset_index()
        
        # Calcular taxas percentuais para análise de desempenho
        dados_resumo['taxa_formacao'] = (dados_resumo['formados'] / dados_resumo['matriculados'] * 100).round(1)
        dados_resumo['taxa_desistencia'] = (dados_resumo['desistentes'] / dados_resumo['matriculados'] * 100).round(1)
        dados_resumo['taxa_transferencia'] = (dados_resumo['transferidos'] / dados_resumo['matriculados'] * 100).round(1)
        
        # Renomear colunas para melhor apresentação
        dados_resumo.columns = [
            'Campus', 'Matriculados', 'Formados', 'Desistentes', 'Transferidos',
            'Taxa Formação (%)', 'Taxa Desistência (%)', 'Taxa Transferência (%)'
        ]
        
        # Ordenar por número de matriculados (indicador de tamanho do campus)
        dados_resumo = dados_resumo.sort_values('Matriculados', ascending=False)
        
        # Renderizar tabela interativa
        st.dataframe(dados_resumo, use_container_width=True, hide_index=True)
    
    else:
        # Mensagem de aviso quando nenhum campus é selecionado
        st.warning("Selecione pelo menos um campus para comparação.")
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: Sistema Acadêmico IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ==================== RODAPÉ ====================
    # Exibir rodapé padrão com informações institucionais
    display_footer()
