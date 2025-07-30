"""
============================================================================
                        MÓDULO DE ENSINO - DASHBOARD IFPB-CZ
============================================================================

Este módulo implementa análises completas sobre indicadores educacionais do 
Instituto Federal da Paraíba - Campus Cajazeiras (IFPB-CZ), apresentando 
métricas detalhadas sobre alunos matriculados, formados, desistentes e 
transferidos.

FUNCIONALIDADES PRINCIPAIS:
- Dashboard interativo com KPIs consolidados do ensino
- Análises por campus, modalidade e curso com filtros dinâmicos  
- Visualizações temporais de evolução dos indicadores educacionais
- Comparação rankings entre campus com tabelas detalhadas
- Cálculo automático de taxas de formação, desistência e transferência

ESTRUTURA DOS DADOS:
- Dados sintéticos gerados pelo DataGenerator
- Campos: campus, ano, modalidade, curso, matriculados, formados, desistentes, transferidos
- Agregações por múltiplos níveis: campus, modalidade, curso, período temporal

DEPENDÊNCIAS:
- streamlit: Interface web interativa
- pandas: Manipulação e análise de dados
- plotly.express/graph_objects: Visualizações gráficas interativas
- utils: Funções auxiliares (cabeçalho, rodapé, formatação)

PADRÃO VISUAL:
- Cores institucionais IFPB: #1a8c73 (principal), #0d5a4e, #2db896
- Layout responsivo com containers CSS personalizados
- Gráficos interativos com filtros dinâmicos

============================================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def ensino_module(data_gen):
    """
    Módulo principal de análise dos indicadores educacionais do IFPB-CZ.
    
    Processa e apresenta dados educacionais através de dashboards interativos,
    incluindo KPIs consolidados, análises temporais, comparações entre campus
    e visualizações detalhadas por modalidade e curso.
    
    SEÇÕES IMPLEMENTADAS:
    1. KPIs Consolidados - Cartões com indicadores principais
    2. Análise por Campus - Gráficos com múltiplos filtros
    3. Evolução Temporal - Séries históricas com tendências
    4. Comparação Campus - Rankings e tabelas detalhadas
    
    Args:
        data_gen (DataGenerator): Instância para geração de dados sintéticos
                                 educacionais com estrutura padronizada
    
    Returns:
        None: Renderiza interface Streamlit com visualizações interativas
    """
    
    # ============= INICIALIZAÇÃO: CABEÇALHO E DADOS =============
    # Exibir cabeçalho institucional com logo IFPB
    display_header_with_logo("Ensino")
    
    # Gerar dados sintéticos educacionais usando DataGenerator
    dados_ensino = data_gen.gerar_dados_ensino()
    
    # ============= PROCESSAMENTO: CÁLCULO DE KPIs =============
    # Filtrar dados para o ano mais recente para métricas consolidadas
    ano_atual = dados_ensino['ano'].max()                         # Último ano disponível
    dados_ano_atual = dados_ensino[dados_ensino['ano'] == ano_atual]  # Dados do ano atual
    
    # Calcular indicadores-chave (KPIs) consolidados para o ano atual
    total_matriculados = dados_ano_atual['matriculados'].sum()    # Total de alunos matriculados
    total_formados = dados_ano_atual['formados'].sum()            # Total de alunos formados  
    total_desistentes = dados_ano_atual['desistentes'].sum()      # Total de alunos desistentes
    total_transferidos = dados_ano_atual['transferidos'].sum()    # Total de alunos transferidos
    
    # ============= SEÇÃO 1: DISPLAY DE KPIs EDUCACIONAIS =============
    # Apresentar indicadores principais em formato de cartões visuais
    # Utiliza CSS personalizado para estilização consistente dos containers
    
    # Criar layout em 4 colunas para exibição dos KPIs principais
    col1, col2, col3, col4 = st.columns(4)
    
    # KPI 1: Alunos Matriculados (indicador de capacidade institucional)
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
    
    # Separador visual entre seções principais
    st.markdown("---")
    
    # ============= SEÇÃO 2: ANÁLISE DETALHADA POR CAMPUS =============
    # Gráfico interativo com múltiplos filtros para análise granular por campus
    
    # Container CSS para estilização consistente dos gráficos
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Número de Alunos por Campus")
    st.write("**Análise detalhada com filtros por campus, modalidade e curso**")
    
    # ============= CONTROLES: FILTROS INTERATIVOS =============
    # Criar 4 colunas para organizar os controles de filtro de forma intuitiva
    col1, col2, col3, col4 = st.columns(4)
    
    # FILTRO 1: Seleção múltipla de campus com opção "Todos"
    with col1:
        # Preparar lista de campus disponíveis (incluindo opção "Todos")
        campus_disponivel = ["Todos"] + sorted(dados_ensino['campus'].unique())
        campus_selecionados = st.multiselect(
            "Selecione os Campus:",                        # Label descritivo
            options=campus_disponivel,                     # Opções disponíveis
            default=["Todos"],                             # Padrão: todos selecionados
            key="campus_multi_1"                           # Chave única para estado
        )
        
        # Lógica para processamento da seleção de campus
        # Se "Todos" estiver selecionado, incluir todos os campus automaticamente
        if "Todos" in campus_selecionados:
            campus_filtro = dados_ensino['campus'].unique()
        else:
            campus_filtro = campus_selecionados
    
    # FILTRO 2: Métrica específica a ser exibida no gráfico
    with col2:
        forma_exibicao = st.selectbox(
            "Escolha a forma de exibição:",               # Label descritivo
            ["Matriculados", "Formados", "Desistentes", "Transferidos"],  # Métricas disponíveis
            key="forma_exib_1"                            # Chave única para estado
        )
    
    # FILTRO 3: Nível de detalhamento/granularidade dos dados
    with col3:
        nivel_detalhe = st.selectbox(
            "Nível de detalhe:",                          # Label descritivo
            ["Geral", "Por Modalidade", "Por Curso"],    # Três níveis de granularidade
            key="nivel_det_1"                             # Chave única para estado
        )
    
    # FILTRO 4: Ano de referência para análise temporal
    with col4:
        ano_selecionado = st.selectbox(
            "Ano:",                                       # Label descritivo
            sorted(dados_ensino['ano'].unique(), reverse=True),  # Anos em ordem decrescente
            key="ano_1"                                   # Chave única para estado
        )
    
    # ============= PROCESSAMENTO: APLICAÇÃO DE FILTROS =============
    # Aplicar filtros aos dados baseado nas seleções interativas do usuário
    dados_filtrados = dados_ensino[
        (dados_ensino['ano'] == ano_selecionado) &       # Filtro temporal
        (dados_ensino['campus'].isin(campus_filtro))      # Filtro por campus
    ]
    
    # ============= MAPEAMENTO: MÉTRICAS PARA COLUNAS =============
    # Mapear nomes amigáveis das métricas para nomes das colunas no DataFrame
    metrica_map = {
        "Matriculados": "matriculados",                   # Alunos matriculados
        "Formados": "formados",                           # Alunos formados
        "Desistentes": "desistentes",                     # Alunos desistentes
        "Transferidos": "transferidos"                    # Alunos transferidos
    }
    
    # ============= PROCESSAMENTO: AGRUPAMENTO POR NÍVEL DE DETALHE =============
    # Processar dados baseado no nível de granularidade selecionado
    if nivel_detalhe == "Geral":
        # Agrupamento simples por campus (visão consolidada)
        dados_grafico = dados_filtrados.groupby('campus')[metrica_map[forma_exibicao]].sum().reset_index()
    elif nivel_detalhe == "Por Modalidade":
        # Agrupamento por campus e modalidade (presencial, EAD, etc.)
        dados_grafico = dados_filtrados.groupby(['campus', 'modalidade'])[metrica_map[forma_exibicao]].sum().reset_index()
    else:  # Por Curso
        # Agrupamento por campus e curso (maior nível de detalhamento)
        dados_grafico = dados_filtrados.groupby(['campus', 'curso'])[metrica_map[forma_exibicao]].sum().reset_index()
    
    # ============= VISUALIZAÇÃO: CRIAÇÃO DOS GRÁFICOS =============
    # Criar gráfico baseado no nível de detalhe selecionado
    if nivel_detalhe == "Geral":
        # Gráfico de barras simples (uma barra por campus)
        fig = px.bar(
            dados_grafico,
            x='campus',                                   # Eixo X: campus
            y=metrica_map[forma_exibicao],               # Eixo Y: métrica selecionada
            title=f"Nº de {forma_exibicao} por Campus - {ano_selecionado}",  # Título dinâmico
            color_discrete_sequence=['#1a8c73']          # Cor institucional IFPB
        )
    elif nivel_detalhe == "Por Modalidade":
        # Gráfico de barras agrupadas por modalidade de ensino
        fig = px.bar(
            dados_grafico,
            x='campus',                                   # Eixo X: campus
            y=metrica_map[forma_exibicao],               # Eixo Y: métrica selecionada
            color='modalidade',                           # Agrupamento por modalidade
            title=f"Nº de {forma_exibicao} por Campus e Modalidade - {ano_selecionado}",  # Título dinâmico
            color_discrete_sequence=['#1a8c73', '#0d5a4e', '#2db896']  # Paleta institucional
        )
    else:  # Por Curso
        # Gráfico de barras agrupadas por curso (maior detalhamento)
        fig = px.bar(
            dados_grafico,
            x='campus',                                   # Eixo X: campus
            y=metrica_map[forma_exibicao],               # Eixo Y: métrica selecionada
            color='curso',                                # Agrupamento por curso
            title=f"Nº de {forma_exibicao} por Campus e Curso - {ano_selecionado}"  # Título dinâmico
        )
    
    # ============= CONFIGURAÇÃO: LAYOUT E FORMATAÇÃO =============
    # Configurar layout do gráfico para melhor apresentação
    fig.update_layout(
        xaxis_title="Campus",                            # Título eixo X
        yaxis_title=f"Número de {forma_exibicao}",      # Título eixo Y dinâmico
        xaxis_tickangle=-45,                             # Rotacionar labels para legibilidade
        height=500,                                      # Altura fixa para consistência
        showlegend=True                                  # Exibir legenda quando aplicável
    )
    
    # Renderizar gráfico interativo no Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: Sistema Acadêmico IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 3: EVOLUÇÃO TEMPORAL DOS INDICADORES =============
    # Análise de séries temporais para identificar tendências ao longo dos anos
    
    # Container CSS para estilização consistente
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução do Número de Alunos")
    st.write("**Análise temporal com múltiplas opções de visualização**")
    
    # ============= CONTROLES: FILTROS PARA ANÁLISE TEMPORAL =============
    # Organizar controles em 3 colunas para análise temporal
    col1, col2, col3 = st.columns(3)
    
    # FILTRO 1: Seleção de campus para análise temporal
    with col1:
        campus_evolucao = st.multiselect(
            "Escolha os Campus:",                         # Label descritivo
            options=["Todos"] + sorted(dados_ensino['campus'].unique()),  # Opções disponíveis
            default=["Todos"],                            # Padrão: todos selecionados
            key="campus_evolucao"                         # Chave única para estado
        )
        
        # Processar seleção de campus (lógica similar à seção anterior)
        if "Todos" in campus_evolucao:
            campus_filtro_evolucao = dados_ensino['campus'].unique()
        else:
            campus_filtro_evolucao = campus_evolucao
    
    # FILTRO 2: Métrica específica para análise temporal
    with col2:
        forma_exibicao_2 = st.selectbox(
            "Forma de exibição:",                         # Label descritivo
            ["Matriculados", "Formados", "Desistentes", "Transferidos"],  # Métricas disponíveis
            key="forma_exib_2"                            # Chave única para estado
        )
    
    # FILTRO 3: Tipo de visualização gráfica temporal
    with col3:
        tipo_grafico = st.selectbox(
            "Tipo de gráfico:",                           # Label descritivo
            ["Linha", "Área", "Barras"],                 # Tipos de visualização temporal
            key="tipo_grafico_evolucao"                   # Chave única para estado
        )
    
    # ============= PROCESSAMENTO: FILTRAR DADOS TEMPORAIS =============
    # Filtrar dados baseado nos campus selecionados para análise temporal
    dados_evolucao = dados_ensino[dados_ensino['campus'].isin(campus_filtro_evolucao)]
    
    # ============= LÓGICA: PROCESSAMENTO BASEADO NA SELEÇÃO =============
    # Processar dados de forma diferente baseado na quantidade de campus
    if len(campus_filtro_evolucao) == 1 and "Todos" not in campus_evolucao:
        # CASO 1: Campus específico único selecionado
        # Agregar dados apenas por ano (série temporal simples)
        dados_evolucao = dados_evolucao.groupby('ano')[metrica_map[forma_exibicao_2]].sum().reset_index()
        titulo_grafico = f"Evolução do Nº de {forma_exibicao_2} - {campus_filtro_evolucao[0]}"
        
        # Criar gráfico baseado no tipo selecionado (campus único)
        if tipo_grafico == "Linha":
            fig2 = px.line(
                dados_evolucao,
                x='ano',                                  # Eixo X: anos
                y=metrica_map[forma_exibicao_2],         # Eixo Y: métrica selecionada
                title=titulo_grafico,                     # Título específico do campus
                markers=True,                             # Exibir marcadores nos pontos
                color_discrete_sequence=['#1a8c73']      # Cor institucional IFPB
            )
        elif tipo_grafico == "Área":
            fig2 = px.area(
                dados_evolucao,
                x='ano',                                  # Eixo X: anos
                y=metrica_map[forma_exibicao_2],         # Eixo Y: métrica selecionada
                title=titulo_grafico,                     # Título específico do campus
                color_discrete_sequence=['#1a8c73']      # Cor institucional IFPB
            )
        else:  # Barras
            fig2 = px.bar(
                dados_evolucao,
                x='ano',                                  # Eixo X: anos
                y=metrica_map[forma_exibicao_2],         # Eixo Y: métrica selecionada
                title=titulo_grafico,                     # Título específico do campus
                color_discrete_sequence=['#1a8c73']      # Cor institucional IFPB
            )
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
            # Agregar todos os campus em uma única série temporal consolidada
            dados_evolucao = dados_ensino.groupby('ano')[metrica_map[forma_exibicao_2]].sum().reset_index()
            titulo_grafico = f"Evolução do Nº de {forma_exibicao_2} - Todos os Campus"
        else:
            # Manter separação por campus (múltiplas séries temporais)
            dados_evolucao = dados_evolucao.groupby(['ano', 'campus'])[metrica_map[forma_exibicao_2]].sum().reset_index()
            titulo_grafico = f"Evolução do Nº de {forma_exibicao_2} - Campus Selecionados"
        
        # ============= VISUALIZAÇÃO: GRÁFICOS PARA MÚLTIPLOS CAMPUS =============
        # Criar gráfico baseado no tipo selecionado (múltiplos campus)
        if tipo_grafico == "Linha":
            if 'campus' in dados_evolucao.columns:
                # Múltiplas linhas (uma linha por campus)
                fig2 = px.line(
                    dados_evolucao,
                    x='ano',                              # Eixo X: anos
                    y=metrica_map[forma_exibicao_2],     # Eixo Y: métrica selecionada
                    color='campus',                       # Cor diferente para cada campus
                    title=titulo_grafico,                 # Título dinâmico
                    markers=True                          # Exibir marcadores nos pontos
                )
            else:
                # Linha única (todos os campus agregados)
                fig2 = px.line(
                    dados_evolucao,
                    x='ano',                              # Eixo X: anos
                    y=metrica_map[forma_exibicao_2],     # Eixo Y: métrica selecionada
                    title=titulo_grafico,                 # Título dinâmico
                    markers=True,                         # Exibir marcadores nos pontos
                    color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
                )
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
                # Múltiplas áreas empilhadas por campus
                fig2 = px.area(
                    dados_evolucao,
                    x='ano',                              # Eixo X: anos
                    y=metrica_map[forma_exibicao_2],     # Eixo Y: métrica selecionada
                    color='campus',                       # Empilhamento por campus
                    title=titulo_grafico                  # Título dinâmico
                )
            else:
                # Área única (todos os campus agregados)
                fig2 = px.area(
                    dados_evolucao,
                    x='ano',                              # Eixo X: anos
                    y=metrica_map[forma_exibicao_2],     # Eixo Y: métrica selecionada
                    title=titulo_grafico,                 # Título dinâmico
                    color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
                )
        else:  # Barras
            if 'campus' in dados_evolucao.columns:
                # Barras agrupadas por campus
                fig2 = px.bar(
                    dados_evolucao,
                    x='ano',                              # Eixo X: anos
                    y=metrica_map[forma_exibicao_2],     # Eixo Y: métrica selecionada
                    color='campus',                       # Agrupamento por campus
                    title=titulo_grafico,                 # Título dinâmico
                    barmode='group'                       # Barras lado a lado
                )
            else:
                # Barras simples (todos os campus agregados)
                fig2 = px.bar(
                    dados_evolucao,
                    x='ano',                              # Eixo X: anos
                    y=metrica_map[forma_exibicao_2],     # Eixo Y: métrica selecionada
                    title=titulo_grafico,                 # Título dinâmico
                    color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
                )
    # ============= CONFIGURAÇÃO: LAYOUT DO GRÁFICO TEMPORAL =============
    # Configurar layout para melhor apresentação da evolução temporal
    fig2.update_layout(
        xaxis_title="Ano",                               # Título eixo X
        yaxis_title=f"Número de {forma_exibicao_2}",    # Título eixo Y dinâmico
        height=500,                                      # Altura fixa para consistência
        showlegend=True                                  # Exibir legenda quando aplicável
    )
    
    # Renderizar gráfico temporal interativo
    st.plotly_chart(fig2, use_container_width=True)
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: Sistema Acadêmico IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ============= SEÇÃO 4: ANÁLISE COMPARATIVA ENTRE CAMPUS =============
    # Ranking de campus com tabelas detalhadas e cálculo de indicadores
    
    # Container CSS para estilização consistente
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("🏛️ Comparação entre Campus")
    st.write("**Análise comparativa com rankings e indicadores de desempenho**")
    
    # ============= CONTROLES: FILTROS PARA ANÁLISE COMPARATIVA =============
    # Organizar controles em 3 colunas para seleção de parâmetros
    col1, col2, col3 = st.columns(3)
    
    # FILTRO 1: Seleção limitada de campus para evitar poluição visual
    with col1:
        campus_comparacao = st.multiselect(
            "Selecione até 10 Campus para comparar:",     # Label com orientação
            options=sorted(dados_ensino['campus'].unique()),  # Campus ordenados alfabeticamente
            default=sorted(dados_ensino['campus'].unique())[:5],  # Padrão: primeiros 5
            max_selections=10,                            # Limite máximo para visualização
            key="campus_comparacao"                       # Chave única para estado
        )
    
    # FILTRO 2: Métrica específica para base da comparação
    with col2:
        metrica_comparacao = st.selectbox(
            "Métrica para comparação:",                   # Label descritivo
            ["Matriculados", "Formados", "Desistentes", "Transferidos"],  # Métricas disponíveis
            key="metrica_comparacao"                      # Chave única para estado
        )
    
    # FILTRO 3: Período temporal para análise agregada
    with col3:
        periodo_comparacao = st.selectbox(
            "Período:",                                   # Label descritivo
            ["Último Ano", "Últimos 3 Anos", "Últimos 5 Anos", "Todos os Anos"],  # Períodos
            key="periodo_comparacao"                      # Chave única para estado
        )
    
    # ============= VALIDAÇÃO: VERIFICAR CAMPUS SELECIONADOS =============
    # Verificar se há campus selecionados para realizar comparação
    if campus_comparacao:
        # ============= PROCESSAMENTO: FILTRAR DADOS POR PERÍODO =============
        # Aplicar filtro temporal baseado no período selecionado
        if periodo_comparacao == "Último Ano":
            dados_comp = dados_ensino[dados_ensino['ano'] == dados_ensino['ano'].max()]
        elif periodo_comparacao == "Últimos 3 Anos":
            dados_comp = dados_ensino[dados_ensino['ano'] >= dados_ensino['ano'].max() - 2]
        elif periodo_comparacao == "Últimos 5 Anos":
            dados_comp = dados_ensino[dados_ensino['ano'] >= dados_ensino['ano'].max() - 4]
        else:  # Todos os anos
            dados_comp = dados_ensino.copy()
        
        # Aplicar filtro de campus selecionados para comparação
        dados_comp = dados_comp[dados_comp['campus'].isin(campus_comparacao)]
        
        # ============= PROCESSAMENTO: AGREGAÇÃO E RANKING =============
        # Agregar dados por campus para o período selecionado
        dados_comp_grouped = dados_comp.groupby('campus')[metrica_map[metrica_comparacao]].sum().reset_index()
        # Ordenar em ordem decrescente para criar ranking automático
        dados_comp_grouped = dados_comp_grouped.sort_values(metrica_map[metrica_comparacao], ascending=False)
        
        # ============= VISUALIZAÇÃO: GRÁFICO DE RANKING =============
        # Criar gráfico de barras horizontais para melhor visualização do ranking
        fig3 = px.bar(
            dados_comp_grouped,
            x=metrica_map[metrica_comparacao],               # Eixo X: valores da métrica
            y='campus',                                      # Eixo Y: nomes dos campus
            orientation='h',                                 # Barras horizontais para ranking
            title=f"Comparação: {metrica_comparacao} - {periodo_comparacao}",  # Título dinâmico
            color=metrica_map[metrica_comparacao],          # Cor baseada no valor
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
        
        # ============= FORMATAÇÃO: RENOMEAR COLUNAS PARA APRESENTAÇÃO =============
        # Renomear colunas para nomes amigáveis na interface do usuário
        dados_resumo.columns = [
            'Campus', 'Matriculados', 'Formados', 'Desistentes', 'Transferidos',
            'Taxa Formação (%)', 'Taxa Desistência (%)', 'Taxa Transferência (%)'
        ]
        
        # Ordenar tabela por número de matriculados (indicador de tamanho do campus)
        dados_resumo = dados_resumo.sort_values('Matriculados', ascending=False)
        
        # ============= EXIBIÇÃO: TABELA INTERATIVA =============
        # Renderizar tabela interativa com dados detalhados
        st.dataframe(dados_resumo, use_container_width=True, hide_index=True)
    
    else:
        # ============= AVISO: NENHUM CAMPUS SELECIONADO =============
        # Exibir mensagem de orientação quando nenhum campus é selecionado
        st.warning("⚠️ Selecione pelo menos um campus para realizar a comparação.")
    
    # Fonte dos dados e fechamento do container CSS
    st.markdown('<div class="fonte-dados">Fonte de Dados: Sistema Acadêmico IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ============= RODAPÉ: INFORMAÇÕES INSTITUCIONAIS =============
    # Exibir rodapé padrão do sistema com informações gerais
    display_footer()
