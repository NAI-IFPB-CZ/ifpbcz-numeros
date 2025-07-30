# ============================================================================
# MÓDULO DE ANÁLISE DE SERVIDORES - DASHBOARD IFPB CAMPUS CAJAZEIRAS
# ============================================================================
"""
DESCRIÇÃO DO MÓDULO:
Este módulo fornece análises abrangentes sobre o quadro de servidores do IFPB Campus Cajazeiras,
incluindo evolução temporal, distribuição por unidades, proporções funcionais e taxas de crescimento.

FUNCIONALIDADES PRINCIPAIS:
1. Indicadores consolidados (KPIs) do quadro de pessoal
2. Evolução temporal do número de servidores por categoria
3. Distribuição de servidores entre unidades organizacionais
4. Análise proporcional entre docentes e técnicos administrativos
5. Cálculo e visualização de taxas de crescimento anual

ESTRUTURA DE DADOS:
- Dados de servidores por ano, unidade e categoria profissional
- Métricas: total de servidores, docentes, técnicos administrativos
- Dimensões temporais: 2013-2025 (dados históricos e projeções)
- Dimensões espaciais: unidades administrativas do campus

DEPENDÊNCIAS:
- Streamlit: Interface web e componentes interativos
- Pandas: Manipulação e processamento de dados
- Plotly Express/Graph Objects: Visualizações interativas
- Utils: Componentes visuais padronizados (cabeçalho, rodapé)

PADRÕES VISUAIS:
- Cores institucionais IFPB: #1a8c73 (principal), #0d5a4e, #2db896
- Gráficos responsivos com interatividade Plotly
- Layout em containers estilizados com CSS personalizado
- KPIs em formato de cartões visuais destacados
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def servidores_module(data_gen):
    """
    Módulo principal para análise do quadro de servidores do IFPB Campus Cajazeiras.
    
    Este módulo apresenta uma visão abrangente do quadro de pessoal da instituição,
    oferecendo análises temporais, distribucionais e comparativas através de 
    visualizações interativas e indicadores consolidados.
    
    SEÇÕES PRINCIPAIS:
    1. KPIs Consolidados - Indicadores principais do quadro atual
    2. Evolução Temporal - Análise longitudinal do crescimento de pessoal
    3. Distribuição por Unidade - Análise espacial entre setores
    4. Proporção Funcional - Comparação entre categorias profissionais
    5. Taxa de Crescimento - Indicadores de expansão anual
    
    PARÂMETROS:
    -----------
    data_gen : object
        Gerador de dados contendo informações dos servidores
        Estrutura esperada: ano, unidade, total_servidores, docentes, tecnicos
    
    RETORNO:
    --------
    None
        Renderiza interface Streamlit com visualizações e análises interativas
    
    FUNCIONALIDADES INTERATIVAS:
    - Filtros por unidade e período temporal
    - Seleção de categorias profissionais para análise específica
    - Gráficos responsivos com hover e zoom
    - Exportação de dados através de componentes Plotly
    """
    
    # ============= CONFIGURAÇÃO INICIAL E CARREGAMENTO DE DADOS =============
    # Exibição do cabeçalho institucional padronizado
    display_header_with_logo("Servidores")
    
    # Geração/carregamento dos dados de servidores
    # Obtém dataset completo com informações históricas e atuais
    dados_servidores = data_gen.gerar_dados_servidores()
    
    # Filtro para dados do ano corrente (2025) para cálculo de KPIs
    # Subset específico para indicadores consolidados atuais
    dados_2025 = dados_servidores[dados_servidores['ano'] == 2025]
    
    # ============= CÁLCULO DE INDICADORES-CHAVE (KPIs) =============
    # Consolidação dos principais indicadores do quadro de pessoal atual
    # Agregação de dados para visão institucional consolidada
    
    # KPI 1: Total geral de servidores ativos no campus
    total_servidores = dados_2025['total_servidores'].sum()
    
    # KPI 2: Total de servidores técnicos administrativos
    total_tecnicos = dados_2025['tecnicos'].sum()
    
    # KPI 3: Total de servidores docentes (professores)
    total_docentes = dados_2025['docentes'].sum()
    
    # ============= SEÇÃO 1: DISPLAY DE KPIs DO QUADRO DE SERVIDORES =============
    # Apresentar indicadores principais em formato de cartões visuais
    # Layout em 3 colunas para exibição equilibrada dos KPIs
    # Layout em 3 colunas para exibição equilibrada dos KPIs
    col1, col2, col3 = st.columns(3)
    
    # KPI 1: Total de Servidores (indicador global de força de trabalho)
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">SERVIDORES</div>
            <div class="kpi-value">{total_servidores:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 2: Servidores Técnicos (pessoal de apoio administrativo)
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TÉCNICOS</div>
            <div class="kpi-value">{total_tecnicos:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 3: Servidores Docentes (corpo professoral ativo)
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">DOCENTES</div>
            <div class="kpi-value">{total_docentes:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Separador visual entre seções principais
    st.markdown("---")
    
    # ============= SEÇÃO 2: EVOLUÇÃO TEMPORAL DO QUADRO DE SERVIDORES =============
    # Análise longitudinal da evolução do pessoal ao longo dos anos
    # Visualização da tendência de crescimento e distribuição por categoria
    
    # Subsseção A: Container principal para evolução temporal
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução do Número de Servidores")
    
    # Filtro interativo para seleção de unidade específica ou visão geral
    # Permite análise tanto institucional quanto setorial
    unidade_selecionada = st.selectbox(
        "Selecione a unidade:",
        ["Todas"] + list(dados_servidores['unidade'].unique()),
        key="unidade_servidores"
    )
    
    # Processamento condicional dos dados baseado na seleção
    # Agregação institucional ou filtro específico por unidade
    if unidade_selecionada == "Todas":
        # Visão consolidada: agregar dados de todas as unidades por ano
        dados_filtrados = dados_servidores.groupby('ano').agg({
            'total_servidores': 'sum',  # Soma total de servidores
            'docentes': 'sum',          # Soma de docentes
            'tecnicos': 'sum'           # Soma de técnicos
        }).reset_index()
        titulo_grafico = "Evolução do Número de Servidores - Todas as Unidades"
    else:
        # Visão específica: filtrar dados da unidade selecionada
        dados_filtrados = dados_servidores[dados_servidores['unidade'] == unidade_selecionada]
        titulo_grafico = f"Evolução do Número de Servidores - {unidade_selecionada}"
    
    # Criação do gráfico de área empilhada para visualização temporal
    # Uso do Plotly Graph Objects para maior controle de customização
    fig = go.Figure()
    
    # Série 1: Total de Servidores (linha principal de referência)
    # Linha mais destacada representando o conjunto total
    fig.add_trace(go.Scatter(
        x=dados_filtrados['ano'],                    # Eixo temporal
        y=dados_filtrados['total_servidores'],       # Total de servidores
        mode='lines+markers',                        # Linha com marcadores
        name='Total Servidores',                     # Legenda da série
        line=dict(color='#1a8c73', width=3),        # Cor institucional, linha espessa
        fill='tonexty'                               # Preenchimento até próxima série
    ))
    
    # Série 2: Servidores Docentes (professores)
    # Visualização da componente docente do quadro
    fig.add_trace(go.Scatter(
        x=dados_filtrados['ano'],                    # Eixo temporal
        y=dados_filtrados['docentes'],               # Número de docentes
        mode='lines+markers',                        # Linha com marcadores
        name='Servidores Professores',               # Legenda da série
        line=dict(color='#0d5a4e', width=2),        # Cor secundária institucional
        fill='tonexty'                               # Preenchimento até próxima série
    ))
    
    # Série 3: Servidores Técnicos (pessoal administrativo)
    # Visualização da componente técnica do quadro
    fig.add_trace(go.Scatter(
        x=dados_filtrados['ano'],                    # Eixo temporal
        y=dados_filtrados['tecnicos'],               # Número de técnicos
        mode='lines+markers',                        # Linha com marcadores
        name='Servidores Técnicos',                  # Legenda da série
        line=dict(color='#2db896', width=2),        # Cor terciária institucional
        fill='tozeroy'                               # Preenchimento até zero
    ))
    
    # Customização do layout e formatação do gráfico
    fig.update_layout(
        title=titulo_grafico,                        # Título dinâmico baseado na seleção
        xaxis_title="Ano",                           # Rótulo do eixo X
        yaxis_title="Número de Servidores",          # Rótulo do eixo Y
        height=500,                                  # Altura do gráfico
        hovermode='x unified',                       # Modo de hover unificado
        plot_bgcolor='rgba(0,0,0,0)',               # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)',              # Papel transparente
        font=dict(family="Arial", size=12)           # Fonte padrão
    )
    
    # Formatação da grade para melhor legibilidade
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    
    # Renderização do gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    # Informação sobre fonte dos dados (transparência e credibilidade)
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 3: DISTRIBUIÇÃO DE SERVIDORES POR UNIDADE =============
    # Análise espacial da distribuição do quadro entre unidades organizacionais
    # Permite identificar concentração de pessoal e necessidades setoriais
    
    # Subsseção A: Container para análise distributiva por unidade
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Distribuição de Servidores por Unidade")
    
    # Layout de filtros em duas colunas para seleção de parâmetros
    col1, col2 = st.columns(2)
    
    # Filtro 1: Seleção do ano para análise distributiva
    # Ordenação decrescente para priorizar dados recentes
    with col1:
        ano_distribuicao = st.selectbox(
            "Ano:",
            sorted(dados_servidores['ano'].unique(), reverse=True),
            key="ano_distribuicao"
        )
    
    # Filtro 2: Seleção do tipo de servidor para análise específica
    # Opções entre total, docentes ou técnicos para visões direcionadas
    with col2:
        tipo_servidor = st.selectbox(
            "Tipo de Servidor:",
            ["Total", "Docentes", "Técnicos"],
            key="tipo_servidor"
        )
    
    # Aplicar filtro temporal nos dados
    # Subset dos dados baseado no ano selecionado
    dados_distribuicao = dados_servidores[dados_servidores['ano'] == ano_distribuicao]
    
    # Mapeamento do tipo selecionado para coluna correspondente
    # Dicionário de correspondência entre interface e dados
    mapeamento_tipo = {
        "Total": "total_servidores",  # Coluna para total de servidores
        "Docentes": "docentes",       # Coluna para docentes
        "Técnicos": "tecnicos"        # Coluna para técnicos
    }
    
    # Obter a coluna correspondente ao tipo selecionado
    coluna_tipo = mapeamento_tipo[tipo_servidor]
    
    # Criação do gráfico de barras para distribuição por unidade
    # Visualização comparativa entre unidades organizacionais
    fig2 = px.bar(
        dados_distribuicao,
        x='unidade',                                  # Eixo X com nomes das unidades
        y=coluna_tipo,                                # Eixo Y com quantidade selecionada
        title=f"Distribuição de {tipo_servidor} por Unidade - {ano_distribuicao}",
        color_discrete_sequence=['#1a8c73']          # Cor institucional IFPB
    )
    
    # Customização do layout do gráfico distributivo
    fig2.update_layout(
        xaxis_title="Unidade",
        yaxis_title=f"Número de {tipo_servidor}",    # Rótulo dinâmico baseado no tipo
        xaxis_tickangle=-45,                          # Rotação dos rótulos para legibilidade
        height=400,                                   # Altura padrão do gráfico
        plot_bgcolor='rgba(0,0,0,0)',                # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)',               # Papel transparente
        font=dict(family="Arial", size=12)            # Fonte padrão
    )
    
    # Formatação da grade para melhor legibilidade
    fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    
    # Renderização do gráfico de distribuição
    st.plotly_chart(fig2, use_container_width=True)
    
    # Informação sobre fonte dos dados (transparência e credibilidade)
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 4: PROPORÇÃO ENTRE CATEGORIAS PROFISSIONAIS =============
    # Análise comparativa entre docentes e técnicos administrativos
    # Permite avaliar equilibrio e composição do quadro de pessoal
    
    # Subsseção A: Container para análise proporcional
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Proporção Docentes vs Técnicos")
    
    # Layout de filtros em duas colunas para seleção de parâmetros
    col1, col2 = st.columns(2)
    
    # Filtro 1: Seleção do ano para análise proporcional
    # Ordenação decrescente para priorizar dados recentes
    with col1:
        ano_proporcao = st.selectbox(
            "Ano:",
            sorted(dados_servidores['ano'].unique(), reverse=True),
            key="ano_proporcao"
        )
    
    # Filtro 2: Seleção da unidade para análise específica ou geral
    # Opção "Todas" para visão institucional consolidada
    with col2:
        unidade_proporcao = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_servidores['unidade'].unique()),
            key="unidade_proporcao"
        )
    
    # Aplicar filtros temporais e espaciais nos dados
    # Subset inicial baseado no ano selecionado
    dados_proporcao = dados_servidores[dados_servidores['ano'] == ano_proporcao]
    
    # Aplicar filtro de unidade se especificado
    # Refinamento adicional por unidade administrativa
    if unidade_proporcao != "Todas":
        dados_proporcao = dados_proporcao[dados_proporcao['unidade'] == unidade_proporcao]
    
    # Calcular totais agregados para análise proporcional
    # Somatória de cada categoria profissional
    total_docentes_prop = dados_proporcao['docentes'].sum()
    total_tecnicos_prop = dados_proporcao['tecnicos'].sum()
    
    # Preparar dados estruturados para o gráfico de pizza
    # DataFrame específico para visualização proporcional
    dados_pizza = pd.DataFrame({
        'Tipo': ['Docentes', 'Técnicos'],             # Categorias profissionais
        'Quantidade': [total_docentes_prop, total_tecnicos_prop]  # Valores correspondentes
    })
    
    # Criação do gráfico de pizza para visualização proporcional
    # Gráfico circular ideal para mostrar distribuição entre duas categorias
    fig3 = px.pie(
        dados_pizza,
        values='Quantidade',                          # Valores para cálculo das fatias
        names='Tipo',                                 # Rótulos das categorias
        title=f"Proporção Docentes vs Técnicos - {ano_proporcao}" + (f" - {unidade_proporcao}" if unidade_proporcao != "Todas" else ""),
        color_discrete_sequence=['#1a8c73', '#0d5a4e']  # Cores institucionais IFPB
    )
    
    # Customização das informações exibidas no gráfico
    # Exibir percentual e rótulo dentro das fatias
    fig3.update_traces(
        textposition='inside',                        # Posicionamento interno do texto
        textinfo='percent+label',                     # Informações a serem exibidas
        textfont_size=14                              # Tamanho da fonte para legibilidade
    )
    
    # Customização do layout do gráfico de pizza
    fig3.update_layout(
        height=400,                                   # Altura padrão do gráfico
        font=dict(family="Arial", size=12)            # Fonte padrão para consistência
    )
    
    # Renderização do gráfico de proporção
    st.plotly_chart(fig3, use_container_width=True)
    
    # Informação sobre fonte dos dados (transparência e credibilidade)
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 5: ANÁLISE DE TAXAS DE CRESCIMENTO ANUAL =============
    # Cálculo e visualização de indicadores de expansão do quadro de pessoal
    # Permite monitorar tendências de contratação e crescimento institucional
    
    # Subsseção A: Container para análise de crescimento
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Taxa de Crescimento Anual")
    
    # Agregação temporal para cálculo de crescimento institucional
    # Consolidação de dados anuais para todas as unidades
    dados_crescimento = dados_servidores.groupby('ano').agg({
        'total_servidores': 'sum',  # Soma total de servidores por ano
        'docentes': 'sum',          # Soma de docentes por ano
        'tecnicos': 'sum'           # Soma de técnicos por ano
    }).reset_index()
    
    # Cálculo de percentuais de crescimento ano a ano
    # Uso da função pct_change() para variação percentual
    dados_crescimento['crescimento_total'] = dados_crescimento['total_servidores'].pct_change() * 100
    dados_crescimento['crescimento_docentes'] = dados_crescimento['docentes'].pct_change() * 100
    dados_crescimento['crescimento_tecnicos'] = dados_crescimento['tecnicos'].pct_change() * 100
    
    # Remoção do primeiro ano (sem crescimento calculável)
    # Filtro para anos com dados de crescimento válidos
    dados_crescimento = dados_crescimento[dados_crescimento['ano'] > 2013]
    
    # Criação do gráfico de linhas múltiplas para crescimento
    # Uso do Plotly Graph Objects para controle avançado
    fig4 = go.Figure()
    
    # Série 1: Crescimento total de servidores (linha principal)
    fig4.add_trace(go.Scatter(
        x=dados_crescimento['ano'],                   # Eixo temporal
        y=dados_crescimento['crescimento_total'],     # Taxa de crescimento total
        mode='lines+markers',                         # Linha com marcadores
        name='Total Servidores',                      # Legenda da série
        line=dict(color='#1a8c73', width=3)          # Cor institucional, linha espessa
    ))
    
    # Série 2: Crescimento de docentes
    fig4.add_trace(go.Scatter(
        x=dados_crescimento['ano'],                   # Eixo temporal
        y=dados_crescimento['crescimento_docentes'],  # Taxa de crescimento de docentes
        mode='lines+markers',                         # Linha com marcadores
        name='Docentes',                              # Legenda da série
        line=dict(color='#0d5a4e', width=2)          # Cor secundária institucional
    ))
    
    # Série 3: Crescimento de técnicos
    fig4.add_trace(go.Scatter(
        x=dados_crescimento['ano'],                   # Eixo temporal
        y=dados_crescimento['crescimento_tecnicos'],  # Taxa de crescimento de técnicos
        mode='lines+markers',                         # Linha com marcadores
        name='Técnicos',                              # Legenda da série
        line=dict(color='#2db896', width=2)          # Cor terciária institucional
    ))
    
    # Customização do layout do gráfico de crescimento
    fig4.update_layout(
        title="Taxa de Crescimento Anual de Servidores",
        xaxis_title="Ano",                           # Rótulo do eixo X
        yaxis_title="Taxa de Crescimento (%)",       # Rótulo do eixo Y
        height=400,                                  # Altura padrão do gráfico
        plot_bgcolor='rgba(0,0,0,0)',               # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)',              # Papel transparente
        font=dict(family="Arial", size=12)           # Fonte padrão
    )
    
    # Formatação da grade para melhor legibilidade
    fig4.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig4.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    
    # Linha de referência horizontal em 0% (marco de crescimento neutro)
    # Indicador visual para separar crescimento positivo e negativo
    fig4.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="0%")
    
    # Renderização do gráfico de crescimento
    st.plotly_chart(fig4, use_container_width=True)
    
    # Informação sobre fonte dos dados (transparência e credibilidade)
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= RODAPÉ DA PÁGINA =============
    # Exibição do rodapé institucional padronizado
    # Componente final da interface para informações complementares
    display_footer()
