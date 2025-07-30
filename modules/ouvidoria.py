"""
============================================================================
                        MÓDULO OUVIDORIA - DASHBOARD IFPB-CZ
============================================================================

Este módulo implementa análises completas sobre dados da Ouvidoria do 
Instituto Federal da Paraíba - Campus Cajazeiras (IFPB-CZ), apresentando 
métricas detalhadas sobre manifestações, tipos de usuários, tempo de 
atendimento e distribuição por unidades.

FUNCIONALIDADES PRINCIPAIS:
- Dashboard interativo com KPIs consolidados da ouvidoria
- Análises temporais de manifestações com periodicidade configurável
- Distribuição de manifestações por unidades organizacionais
- Classificação por tipos de manifestação (reclamação, sugestão, etc.)
- Análise de perfil de usuários e tempo de resposta
- Monitoramento da qualidade do atendimento institucional

ESTRUTURA DOS DADOS:
- Dados sintéticos gerados pelo DataGenerator
- Campos: ano, mes, unidade, tipo_manifestacao, tipo_usuario, quantidade, dias_atendimento
- Agregações por múltiplos níveis: temporal, organizacional, tipológico
- Cálculo automático de médias e percentuais

DEPENDÊNCIAS:
- streamlit: Interface web interativa e responsiva
- pandas: Manipulação e análise de dados estruturados
- plotly.express/graph_objects: Visualizações gráficas interativas
- utils: Funções auxiliares (cabeçalho, rodapé, formatação)

PADRÃO VISUAL:
- Cores institucionais IFPB: #1a8c73 (principal), #0d5a4e, #2db896
- Paleta qualitativa para gráficos de pizza (Set3)
- Layout responsivo com containers CSS personalizados
- Gráficos interativos com filtros temporais e organizacionais

============================================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def ouvidoria_module(data_gen):
    """
    Módulo principal de análise dos dados da Ouvidoria IFPB-CZ.
    
    Processa e apresenta dados da ouvidoria através de dashboards interativos,
    incluindo KPIs de atendimento, análises temporais, distribuições por 
    unidade e tipo, e métricas de qualidade do serviço de ouvidoria.
    
    SEÇÕES IMPLEMENTADAS:
    1. KPIs Consolidados - Total, usuário frequente e tempo médio
    2. Evolução Temporal - Análise mensal/semestral de manifestações
    3. Distribuição por Unidade - Análise organizacional
    4. Tipos de Manifestação - Classificação das demandas
    5. Perfil de Usuários - Análise do público atendido
    6. Tempo de Atendimento - Monitoramento da qualidade do serviço
    
    Args:
        data_gen (DataGenerator): Instância para geração de dados sintéticos
                                 da ouvidoria com estrutura padronizada
    
    Returns:
        None: Renderiza interface Streamlit com visualizações interativas
    """
    
    # ============= INICIALIZAÇÃO: CABEÇALHO E DADOS =============
    # Exibir cabeçalho institucional com logo IFPB
    display_header_with_logo("Ouvidoria")
    
    # Gerar dados sintéticos da ouvidoria usando DataGenerator
    dados_ouvidoria = data_gen.gerar_dados_ouvidoria()
    
    # ============= PROCESSAMENTO: CÁLCULO DE KPIs ANUAIS =============
    # Filtrar dados para o ano atual (2025) para métricas consolidadas
    dados_2025 = dados_ouvidoria[dados_ouvidoria['ano'] == 2025]
    
    # Calcular indicadores-chave (KPIs) da ouvidoria para o ano atual
    total_manifestacoes = dados_2025['quantidade'].sum()        # Total de manifestações recebidas
    
    # Identificar usuário mais frequente (perfil predominante)
    usuario_mais_frequente = dados_2025.groupby('tipo_usuario')['quantidade'].sum().idxmax()
    
    # Calcular média de dias para atendimento (indicador de eficiência)
    media_dias_atendimento = dados_2025['dias_atendimento'].mean()
    
    # ============= SEÇÃO 1: DISPLAY DE KPIs DA OUVIDORIA =============
    # Apresentar indicadores principais em formato de cartões visuais
    # Layout em 3 colunas para exibição dos KPIs consolidados
    col1, col2, col3 = st.columns(3)
    
    # KPI 1: Total de Manifestações (indicador de volume de demandas)
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TOTAL DE MANIFESTAÇÕES</div>
            <div class="kpi-value">{total_manifestacoes:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 2: Usuário Mais Frequente (perfil predominante)
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">USUÁRIO MAIS FREQUENTE</div>
            <div class="kpi-value">{usuario_mais_frequente}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 3: Média de Dias de Atendimento (indicador de eficiência)
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">MÉDIA DE DIAS DE ATENDIMENTO</div>
            <div class="kpi-value">{media_dias_atendimento:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Separador visual entre seções principais
    st.markdown("---")
    
    # ============= SEÇÃO 2: EVOLUÇÃO TEMPORAL DAS MANIFESTAÇÕES =============
    # Análise longitudinal das manifestações ao longo do tempo
    # Permite identificar tendências, sazonalidades e padrões temporais
    
    # Subsseção A: Gráfico de evolução temporal com filtros dinâmicos
    # Container com título estilizado para organização visual
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução Mensal de Manifestações")
    
    # Layout de filtros em duas colunas para melhor UX
    col1, col2 = st.columns(2)
    
    # Filtro 1: Seleção do ano de análise
    # Ordenado de forma decrescente para priorizar dados recentes
    with col1:
        ano_evolucao = st.selectbox(
            "Ano:",
            sorted(dados_ouvidoria['ano'].unique(), reverse=True),
            key="ano_evolucao_ouv"
        )
    
    # Filtro 2: Período de agrupamento temporal
    # Opções entre visualização mensal e semestral
    with col2:
        periodo_evolucao = st.selectbox(
            "Período:",
            ["Mensal", "Semestral"],
            key="periodo_evolucao"
        )
    
    # Aplicar filtro temporal nos dados
    # Subset dos dados baseado no ano selecionado
    dados_evolucao = dados_ouvidoria[dados_ouvidoria['ano'] == ano_evolucao]
    
    # Processamento condicional baseado no período selecionado
    if periodo_evolucao == "Mensal":
        # Agrupamento mensal: soma de manifestações por mês
        dados_evolucao_grafico = dados_evolucao.groupby('mes')['quantidade'].sum().reset_index()
        
        # Mapeamento de números para nomes dos meses (melhor legibilidade)
        meses_nomes = {
            1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
            7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
        }
        
        # Aplicar mapeamento para exibição amigável
        dados_evolucao_grafico['mes_nome'] = dados_evolucao_grafico['mes'].map(meses_nomes)
        
        # Criação do gráfico de linha temporal mensal
        # Visualização com marcadores para melhor identificação dos pontos
        fig = px.line(
            dados_evolucao_grafico,
            x='mes_nome',  # Eixo X com nomes dos meses
            y='quantidade',  # Eixo Y com quantidade de manifestações
            title=f"Evolução Mensal de Manifestações - {ano_evolucao}",
            markers=True,  # Habilitar marcadores nos pontos
            color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
        )
        
        # Customização do layout do gráfico mensal
        fig.update_layout(
            xaxis_title="Mês",
            yaxis_title="Quantidade de Manifestações",
            height=400,  # Altura padrão do gráfico
            plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        # Formatação da grade para melhor legibilidade
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
    else:  # Visualização Semestral
        # Processamento para agrupamento semestral
        # Classificação dos meses em semestres (1º: Jan-Jun, 2º: Jul-Dez)
        dados_evolucao['semestre'] = dados_evolucao['mes'].apply(lambda x: 1 if x <= 6 else 2)
        
        # Agrupamento semestral: soma de manifestações por semestre
        dados_evolucao_grafico = dados_evolucao.groupby('semestre')['quantidade'].sum().reset_index()
        
        # Formatação amigável dos rótulos semestrais
        dados_evolucao_grafico['semestre_nome'] = dados_evolucao_grafico['semestre'].apply(lambda x: f"{x}º Semestre")
        
        # Criação do gráfico de barras para visualização semestral
        # Gráfico de barras mais adequado para comparação de períodos discretos
        fig = px.bar(
            dados_evolucao_grafico,
            x='semestre_nome',  # Eixo X com rótulos semestrais
            y='quantidade',  # Eixo Y com quantidade de manifestações
            title=f"Manifestações por Semestre - {ano_evolucao}",
            color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
        )
        
        # Customização do layout do gráfico semestral
        fig.update_layout(
            xaxis_title="Semestre",
            yaxis_title="Quantidade de Manifestações",
            height=400,  # Altura padrão do gráfico
            plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        # Formatação da grade para melhor legibilidade
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    
    # Renderização do gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    # Informação sobre fonte dos dados (transparência e credibilidade)
    st.markdown('<div class="fonte-dados">Fonte de Dados: Ouvidoria IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 3: DISTRIBUIÇÃO DE MANIFESTAÇÕES POR UNIDADE =============
    # Análise espacial das manifestações entre diferentes unidades organizacionais
    # Permite identificar unidades com maior demanda e necessidades específicas
    
    # Subsseção A: Container para análise por unidade administrativa
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Manifestações por Unidade")
    
    # Layout de filtros em duas colunas para seleção de parâmetros
    col1, col2 = st.columns(2)
    
    # Filtro 1: Seleção do ano para análise por unidade
    # Priorização de dados recentes com ordenação decrescente
    with col1:
        ano_unidade = st.selectbox(
            "Ano:",
            sorted(dados_ouvidoria['ano'].unique(), reverse=True),
            key="ano_unidade_ouv"
        )
    
    # Filtro 2: Forma de exibição dos dados (absoluto vs relativo)
    # Opção entre valores absolutos e percentuais para diferentes perspectivas
    with col2:
        forma_exibicao = st.selectbox(
            "Forma de exibição:",
            ["Quantidade", "Percentual"],
            key="forma_exibicao_ouv"
        )
    
    # Aplicar filtro temporal e processar dados por unidade
    # Subset dos dados baseado no ano selecionado
    dados_unidade = dados_ouvidoria[dados_ouvidoria['ano'] == ano_unidade]
    
    # Agrupamento por unidade: soma de manifestações por unidade administrativa
    dados_unidade_grafico = dados_unidade.groupby('unidade')['quantidade'].sum().reset_index()
    
    # Processamento condicional baseado na forma de exibição
    if forma_exibicao == "Percentual":
        # Cálculo do percentual relativo ao total do ano
        total_manifestacoes_ano = dados_unidade_grafico['quantidade'].sum()
        dados_unidade_grafico['percentual'] = (dados_unidade_grafico['quantidade'] / total_manifestacoes_ano) * 100
        
        # Criação do gráfico de barras com percentuais
        # Visualização relativa para comparação proporcional
        fig2 = px.bar(
            dados_unidade_grafico,
            x='unidade',  # Eixo X com nomes das unidades
            y='percentual',  # Eixo Y com percentuais
            title=f"Manifestações por Unidade (%) - {ano_unidade}",
            color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
        )
        
        # Customização do layout para exibição percentual
        fig2.update_layout(
            xaxis_title="Unidade",
            yaxis_title="Percentual (%)",
            xaxis_tickangle=-45,  # Rotação dos rótulos para melhor legibilidade
            height=400,  # Altura padrão do gráfico
            plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        # Formatação da grade para melhor legibilidade
        fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
    else:  # Exibição por Quantidade Absoluta
        # Criação do gráfico de barras com valores absolutos
        # Visualização direta das quantidades por unidade
        fig2 = px.bar(
            dados_unidade_grafico,
            x='unidade',  # Eixo X com nomes das unidades
            y='quantidade',  # Eixo Y com quantidades absolutas
            title=f"Manifestações por Unidade - {ano_unidade}",
            color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
        )
        
        # Customização do layout para exibição de quantidade
        fig2.update_layout(
            xaxis_title="Unidade",
            yaxis_title="Quantidade",
            xaxis_tickangle=-45,  # Rotação dos rótulos para melhor legibilidade
            height=400,  # Altura padrão do gráfico
            plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        # Formatação da grade para melhor legibilidade
        fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    
    # Renderização do gráfico de unidades no Streamlit
    st.plotly_chart(fig2, use_container_width=True)
    
    # Informação sobre fonte dos dados (transparência e credibilidade)
    st.markdown('<div class="fonte-dados">Fonte de Dados: Ouvidoria IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 4: ANÁLISE DE TIPOS DE MANIFESTAÇÃO =============
    # Classificação das manifestações por natureza e categoria
    # Permite compreender a distribuição das demandas por tipo de solicitação
    
    # Subsseção A: Container para análise tipológica das manifestações
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Tipos de Manifestação")
    
    # Layout de filtros em duas colunas para seleção de parâmetros
    col1, col2 = st.columns(2)
    
    # Filtro 1: Seleção do ano para análise tipológica
    # Ordenação decrescente para priorizar dados recentes
    with col1:
        ano_tipo = st.selectbox(
            "Ano:",
            sorted(dados_ouvidoria['ano'].unique(), reverse=True),
            key="ano_tipo_ouv"
        )
    
    # Filtro 2: Seleção da unidade para análise específica ou geral
    # Opção "Todas" para visão institucional consolidada
    with col2:
        unidade_tipo = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_ouvidoria['unidade'].unique()),
            key="unidade_tipo_ouv"
        )
    
    # Aplicar filtros temporais e espaciais nos dados
    # Subset inicial baseado no ano selecionado
    dados_tipo = dados_ouvidoria[dados_ouvidoria['ano'] == ano_tipo]
    
    # Aplicar filtro de unidade se especificado
    # Refinamento adicional por unidade administrativa
    if unidade_tipo != "Todas":
        dados_tipo = dados_tipo[dados_tipo['unidade'] == unidade_tipo]
    
    # Agrupamento por tipo de manifestação: soma por categoria
    dados_tipo_grafico = dados_tipo.groupby('tipo_manifestacao')['quantidade'].sum().reset_index()
    
    # Criação do gráfico de pizza para visualização proporcional
    # Gráfico circular ideal para mostrar distribuição de categorias
    fig3 = px.pie(
        dados_tipo_grafico,
        values='quantidade',  # Valores para cálculo das fatias
        names='tipo_manifestacao',  # Rótulos das categorias
        title=f"Tipos de Manifestação - {ano_tipo}" + (f" - {unidade_tipo}" if unidade_tipo != "Todas" else ""),
        color_discrete_sequence=px.colors.qualitative.Set3  # Paleta de cores diversificada
    )
    
    # Customização das informações exibidas no gráfico
    # Exibir percentual e rótulo dentro das fatias
    fig3.update_traces(
        textposition='inside',  # Posicionamento interno do texto
        textinfo='percent+label',  # Informações a serem exibidas
        textfont_size=11  # Tamanho da fonte para legibilidade
    )
    
    # Customização do layout do gráfico de pizza
    fig3.update_layout(
        height=400,  # Altura padrão do gráfico
        font=dict(family="Arial", size=12)  # Fonte padrão para consistência
    )
    
    # Renderização do gráfico de tipos de manifestação
    st.plotly_chart(fig3, use_container_width=True)
    
    # Informação sobre fonte dos dados (transparência e credibilidade)
    st.markdown('<div class="fonte-dados">Fonte de Dados: Ouvidoria IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 5: ANÁLISE DE PERFIL DE USUÁRIOS =============
    # Caracterização dos usuários que procuram os serviços de ouvidoria
    # Permite compreender o público-alvo e suas demandas específicas
    
    # Subsseção A: Container para análise do perfil de usuários
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Tipos de Usuário")
    
    # Filtro único para seleção do ano de análise
    # Seleção temporal para análise de perfil de usuários
    ano_usuario = st.selectbox(
        "Ano:",
        sorted(dados_ouvidoria['ano'].unique(), reverse=True),
        key="ano_usuario_ouv"
    )
    
    # Aplicar filtro temporal nos dados
    # Subset dos dados baseado no ano selecionado
    dados_usuario = dados_ouvidoria[dados_ouvidoria['ano'] == ano_usuario]
    
    # Agrupamento por tipo de usuário: soma por perfil
    dados_usuario_grafico = dados_usuario.groupby('tipo_usuario')['quantidade'].sum().reset_index()
    
    # Criação do gráfico de barras para perfil de usuários
    # Visualização comparativa dos diferentes tipos de usuários
    fig4 = px.bar(
        dados_usuario_grafico,
        x='tipo_usuario',  # Eixo X com tipos de usuários
        y='quantidade',  # Eixo Y com quantidades
        title=f"Manifestações por Tipo de Usuário - {ano_usuario}",
        color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
    )
    
    # Customização do layout do gráfico de usuários
    fig4.update_layout(
        xaxis_title="Tipo de Usuário",
        yaxis_title="Quantidade",
        height=400,  # Altura padrão do gráfico
        xaxis_tickangle=-45,  # Rotação dos rótulos se necessário
        plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # Formatação da grade para melhor legibilidade
    fig4.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig4.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    
    # Renderização do gráfico de tipos de usuário
    st.plotly_chart(fig4, use_container_width=True)
    
    # Informação sobre fonte dos dados (transparência e credibilidade)
    st.markdown('<div class="fonte-dados">Fonte de Dados: Ouvidoria IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 6: ANÁLISE DE TEMPO DE ATENDIMENTO =============
    # Avaliação da eficiência temporal no processamento das manifestações
    # Permite monitorar qualidade do serviço e identificar gargalos operacionais
    
    # Subsseção A: Container para análise de tempo de resposta
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("⏱️ Tempo de Atendimento")
    
    # Layout de filtros em duas colunas para análise temporal
    col1, col2 = st.columns(2)
    
    # Filtro 1: Seleção do ano para análise de tempo de atendimento
    # Ordenação decrescente para priorizar dados recentes
    with col1:
        ano_tempo = st.selectbox(
            "Ano:",
            sorted(dados_ouvidoria['ano'].unique(), reverse=True),
            key="ano_tempo_ouv"
        )
    
    # Filtro 2: Seleção da unidade para análise específica ou geral
    # Opção "Todas" para visão institucional consolidada
    with col2:
        unidade_tempo = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_ouvidoria['unidade'].unique()),
            key="unidade_tempo_ouv"
        )
    
    # Aplicar filtros temporais e espaciais nos dados
    # Subset inicial baseado no ano selecionado
    dados_tempo = dados_ouvidoria[dados_ouvidoria['ano'] == ano_tempo]
    
    # Aplicar filtro de unidade se especificado
    # Refinamento adicional por unidade administrativa
    if unidade_tempo != "Todas":
        dados_tempo = dados_tempo[dados_tempo['unidade'] == unidade_tempo]
    
    # Calcular tempo médio de atendimento por mês
    # Agrupamento temporal com cálculo da média de dias para atendimento
    dados_tempo_grafico = dados_tempo.groupby('mes')['dias_atendimento'].mean().reset_index()
    
    # Mapeamento de números para nomes dos meses (melhor legibilidade)
    meses_nomes = {
        1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
    }
    
    # Aplicar mapeamento para exibição amigável
    dados_tempo_grafico['mes_nome'] = dados_tempo_grafico['mes'].map(meses_nomes)
    
    # Criação do gráfico de linha para evolução temporal do atendimento
    # Visualização da eficiência temporal ao longo dos meses
    fig5 = px.line(
        dados_tempo_grafico,
        x='mes_nome',  # Eixo X com nomes dos meses
        y='dias_atendimento',  # Eixo Y com tempo médio em dias
        title=f"Tempo Médio de Atendimento por Mês - {ano_tempo}" + (f" - {unidade_tempo}" if unidade_tempo != "Todas" else ""),
        markers=True,  # Habilitar marcadores nos pontos
        color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
    )
    
    # Customização do layout do gráfico de tempo de atendimento
    # Customização do layout do gráfico de tempo de atendimento
    fig5.update_layout(
        xaxis_title="Mês",
        yaxis_title="Dias de Atendimento",
        height=400,  # Altura padrão do gráfico
        plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # Formatação da grade para melhor legibilidade
    fig5.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig5.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    
    # Renderização do gráfico de tempo de atendimento
    st.plotly_chart(fig5, use_container_width=True)
    
    # Informação sobre fonte dos dados (transparência e credibilidade)
    st.markdown('<div class="fonte-dados">Fonte de Dados: Ouvidoria IFPB</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= RODAPÉ DA PÁGINA =============
    # Exibição do rodapé institucional padronizado
    # Componente final da interface para informações complementares
    display_footer()
