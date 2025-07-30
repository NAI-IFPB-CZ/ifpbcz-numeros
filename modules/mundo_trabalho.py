"""
============================================================================
                    MÓDULO MUNDO DO TRABALHO - DASHBOARD IFPB-CZ
============================================================================

Este módulo implementa análises completas sobre indicadores do mercado de 
trabalho relacionados aos egressos do Instituto Federal da Paraíba - Campus 
Cajazeiras (IFPB-CZ), apresentando métricas de admissões, desligamentos e 
saldo de vagas no mercado de trabalho.

FUNCIONALIDADES PRINCIPAIS:
- Dashboard interativo com KPIs de mercado de trabalho
- Análises de evolução temporal de admissões e desligamentos
- Rankings de setores de atividade com treemaps interativos
- Comparações regionais com visualizações dinâmicas
- Análise de crescimento setorial e tendências temporais
- Monitoramento de inserção profissional dos egressos

ESTRUTURA DOS DADOS:
- Dados sintéticos gerados pelo DataGenerator
- Campos: ano, regiao, setor_atividade, admissoes, desligamentos, saldo
- Agregações por múltiplos níveis: temporal, regional, setorial
- Cálculo automático de saldos e crescimentos

DEPENDÊNCIAS:
- streamlit: Interface web interativa e responsiva
- pandas: Manipulação e análise de dados estruturados
- plotly.express/graph_objects: Visualizações gráficas avançadas
- utils: Funções auxiliares (cabeçalho, rodapé, formatação)

PADRÃO VISUAL:
- Cores institucionais IFPB: #1a8c73 (principal), #0d5a4e, #2db896
- Cores para saldo: verde (#1a8c73) positivo, vermelho (#d32f2f) negativo
- Layout responsivo com containers CSS personalizados
- Gráficos interativos com múltiplos tipos de visualização

============================================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def mundo_trabalho_module(data_gen):
    """
    Módulo principal de análise do mercado de trabalho dos egressos IFPB-CZ.
    
    Processa e apresenta dados do mercado de trabalho através de dashboards
    interativos, incluindo KPIs de inserção profissional, análises setoriais,
    comparações regionais e tendências temporais de empregabilidade.
    
    SEÇÕES IMPLEMENTADAS:
    1. KPIs Consolidados - Admissões, desligamentos e saldo do ano atual
    2. Evolução Temporal - Séries históricas de movimentação no mercado
    3. Top Setores - Rankings de atividades econômicas (treemaps)
    4. Comparação Regional - Análise por regiões geográficas
    5. Crescimento Setorial - Identificação de setores em expansão
    6. Tendências Setoriais - Análise temporal por atividade econômica
    
    Args:
        data_gen (DataGenerator): Instância para geração de dados sintéticos
                                 do mercado de trabalho com estrutura padronizada
    
    Returns:
        None: Renderiza interface Streamlit com visualizações interativas
    """
    
    # ============= INICIALIZAÇÃO: CABEÇALHO E DADOS =============
    # Exibir cabeçalho institucional com logo IFPB
    display_header_with_logo("Mundo do Trabalho")
    
    # Gerar dados sintéticos do mercado de trabalho usando DataGenerator
    dados_trabalho = data_gen.gerar_dados_mundo_trabalho()
    
    # ============= PROCESSAMENTO: CÁLCULO DE KPIs ANUAIS =============
    # Filtrar dados para o ano atual (2025) para métricas consolidadas
    dados_2025 = dados_trabalho[dados_trabalho['ano'] == 2025]
    
    # Calcular indicadores-chave (KPIs) do mercado de trabalho para o ano atual
    total_admissoes = dados_2025['admissoes'].sum()        # Total de admissões no ano
    total_desligamentos = dados_2025['desligamentos'].sum()  # Total de desligamentos no ano
    saldo_admissoes = dados_2025['saldo'].sum()            # Saldo líquido (admissões - desligamentos)
    
    # ============= SEÇÃO 1: DISPLAY DE KPIs DO MERCADO DE TRABALHO =============
    # Apresentar indicadores principais em formato de cartões visuais
    # Layout em 3 colunas para exibição dos KPIs consolidados
    col1, col2, col3 = st.columns(3)
    
    # KPI 1: Total de Admissões no ano atual
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ADMISSÕES DF 2025</div>
            <div class="kpi-value">{total_admissoes:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 2: Total de Desligamentos no ano atual
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">DESLIGAMENTOS DF 2025</div>
            <div class="kpi-value">{total_desligamentos:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 3: Saldo de Admissões (indicador de crescimento do emprego)
    with col3:
        # Definir cor baseada no sinal do saldo (verde para positivo, vermelho para negativo)
        cor_saldo = "#1a8c73" if saldo_admissoes >= 0 else "#d32f2f"
        sinal_saldo = "+" if saldo_admissoes >= 0 else ""
        
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">SALDO DE ADMISSÕES DF 2025</div>
            <div class="kpi-value" style="color: {cor_saldo};">{sinal_saldo}{saldo_admissoes:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Separador visual entre seções principais
    st.markdown("---")
    
    # ============= DELEGAÇÃO: RENDERIZAR GRÁFICOS DETALHADOS =============
    # Chamar função específica para renderizar todos os gráficos analíticos
    render_graficos_sinteticos(dados_trabalho)
    


def render_graficos_sinteticos(dados_trabalho):
    """
    Renderiza todos os gráficos analíticos do módulo mundo do trabalho.
    
    Esta função concentra a lógica de visualização de dados do mercado de
    trabalho, organizando múltiplas seções com diferentes tipos de análises:
    evolução temporal, rankings setoriais, comparações regionais e tendências.
    
    SEÇÕES DE VISUALIZAÇÃO:
    1. Evolução Admissões/Desligamentos - Séries temporais com filtro regional
    2. Top 10 Setores - Treemap interativo dos principais setores
    3. Comparação Regional - Análise por regiões geográficas
    4. Setores em Crescimento - Rankings de crescimento setorial
    5. Tendências Setoriais - Análise temporal multi-setorial
    
    Args:
        dados_trabalho (DataFrame): Dataset completo com dados do mercado
                                   de trabalho por ano, região e setor
    
    Returns:
        None: Renderiza visualizações diretamente no Streamlit
    """
    
    # ============= SEÇÃO 2: EVOLUÇÃO TEMPORAL ADMISSÕES/DESLIGAMENTOS =============
    # Análise de séries temporais com filtros regionais interativos
    
    # Container CSS para estilização consistente dos gráficos
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução de Admissões/Desligamentos")
    st.write("**Análise temporal da movimentação no mercado de trabalho**")
    
    # ============= CONTROLES: FILTRO REGIONAL =============
    # Seletor para escolher região específica ou visualizar todas
    regiao_evolucao = st.selectbox(
        "Região:",                                        # Label descritivo
        ["Todas"] + list(dados_trabalho['regiao'].unique()),  # Opções: todas + específicas
        key="regiao_evolucao_trab"                        # Chave única para estado
    )
    
    # ============= PROCESSAMENTO: FILTRAR E AGREGAR DADOS =============
    # Aplicar filtro regional e agregar dados por ano
    if regiao_evolucao == "Todas":
        # Agregar todas as regiões em uma única série temporal
        dados_evolucao = dados_trabalho.groupby('ano').agg({
            'admissoes': 'sum',                           # Somar admissões de todas as regiões
            'desligamentos': 'sum',                       # Somar desligamentos de todas as regiões
            'saldo': 'sum'                                # Somar saldo de todas as regiões
        }).reset_index()
        titulo_evolucao = "Evolução de Admissões/Desligamentos - Todas as Regiões"
    else:
        # Filtrar dados para região específica
        dados_evolucao = dados_trabalho[dados_trabalho['regiao'] == regiao_evolucao]
        dados_evolucao = dados_evolucao.groupby('ano').agg({
            'admissoes': 'sum',                           # Somar admissões da região selecionada
            'desligamentos': 'sum',                       # Somar desligamentos da região selecionada
            'saldo': 'sum'                                # Somar saldo da região selecionada
        }).reset_index()
        titulo_evolucao = f"Evolução de Admissões/Desligamentos - {regiao_evolucao}"
    
    # ============= VISUALIZAÇÃO: GRÁFICO DE LINHA TRIPLO =============
    # Criar gráfico interativo com três séries temporais
    fig = go.Figure()
    
    # Série 1: Admissões (linha verde - indicador positivo)
    fig.add_trace(go.Scatter(
        x=dados_evolucao['ano'],                          # Eixo X: anos
        y=dados_evolucao['admissoes'],                    # Eixo Y: número de admissões
        mode='lines+markers',                             # Linha com marcadores
        name='Admissões',                                 # Nome da série na legenda
        line=dict(color='#1a8c73', width=3),            # Cor institucional IFPB, espessura 3
        marker=dict(size=8)                               # Tamanho dos marcadores
    ))
    
    # Série 2: Desligamentos (linha vermelha - indicador de saída)
    fig.add_trace(go.Scatter(
        x=dados_evolucao['ano'],                          # Eixo X: anos
        y=dados_evolucao['desligamentos'],                # Eixo Y: número de desligamentos
        mode='lines+markers',                             # Linha com marcadores
        name='Desligamentos',                             # Nome da série na legenda
        line=dict(color='#d32f2f', width=3),            # Cor vermelha para indicar saída
        marker=dict(size=8)                               # Tamanho dos marcadores
    ))
    
    # Série 3: Saldo (linha azul escura - indicador líquido)
    fig.add_trace(go.Scatter(
        x=dados_evolucao['ano'],                          # Eixo X: anos
        y=dados_evolucao['saldo'],                        # Eixo Y: saldo líquido
        mode='lines+markers',                             # Linha com marcadores
        name='SALDO',                                     # Nome da série na legenda (destaque)
        line=dict(color='#0d5a4e', width=3),            # Cor secundária IFPB
        marker=dict(size=8)                               # Tamanho dos marcadores
    ))
    
    # ============= CONFIGURAÇÃO: LAYOUT DO GRÁFICO =============
    # Configurar layout para melhor apresentação da evolução temporal
    fig.update_layout(
        title=titulo_evolucao,                            # Título dinâmico baseado na seleção
        xaxis_title="Ano",                                # Título eixo X
        yaxis_title="Número de Pessoas",                 # Título eixo Y
        height=500,                                       # Altura fixa para consistência
        hovermode='x unified'                             # Hover unificado no eixo X
    )
    
    # Adicionar linha de referência no zero para destacar saldo neutro
    fig.add_hline(
        y=0,                                              # Posição da linha horizontal
        line_dash="dash",                                 # Linha tracejada
        line_color="gray",                                # Cor cinza para discrição
        annotation_text="Saldo Zero"                     # Texto explicativo
    )
    
    # Renderizar gráfico de evolução temporal
    st.plotly_chart(fig, use_container_width=True)
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 3: TOP 10 SETORES DE ATIVIDADE =============
    # Análise setorial com visualização em treemap para melhor compreensão hierárquica
    
    # Container CSS para nova seção
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Top 10 Setores de Atividade")
    st.write("**Ranking dos principais setores econômicos por volume de movimentação**")
    
    # ============= CONTROLES: FILTROS DE MÉTRICA E PERÍODO =============
    # Organizar controles em 2 colunas para seleção de parâmetros
    col1, col2 = st.columns(2)
    
    # FILTRO 1: Métrica para análise setorial
    with col1:
        forma_exibicao_setor = st.selectbox(
            "Forma de exibição:",                         # Label descritivo
            ["Admissões", "Desligamentos"],              # Métricas disponíveis
            key="forma_exibicao_setor"                    # Chave única para estado
        )
    
    # FILTRO 2: Ano específico para análise
    with col2:
        ano_setor = st.selectbox(
            "Ano:",                                       # Label descritivo
            sorted(dados_trabalho['ano'].unique(), reverse=True),  # Anos em ordem decrescente
            key="ano_setor"                               # Chave única para estado
        )
    
    # ============= PROCESSAMENTO: FILTRAR E RANKING SETORIAL =============
    # Filtrar dados para o ano selecionado
    dados_setor = dados_trabalho[dados_trabalho['ano'] == ano_setor]
    
    # Determinar métrica baseada na seleção do usuário
    metrica_setor = 'admissoes' if forma_exibicao_setor == "Admissões" else 'desligamentos'
    
    # Agrupar por setor de atividade e selecionar top 10
    dados_setor_grafico = dados_setor.groupby('setor_atividade')[metrica_setor].sum().reset_index()
    dados_setor_grafico = dados_setor_grafico.sort_values(metrica_setor, ascending=False).head(10)
    
    # ============= VISUALIZAÇÃO: TREEMAP HIERÁRQUICO =============
    # Criar treemap interativo para visualização hierárquica dos setores
    fig2 = go.Figure(go.Treemap(
        labels=dados_setor_grafico['setor_atividade'],   # Rótulos dos setores
        values=dados_setor_grafico[metrica_setor],       # Valores para dimensionamento
        parents=[""] * len(dados_setor_grafico),         # Estrutura plana (sem hierarquia)
        textinfo="label+value",                          # Exibir rótulo e valor
        hovertemplate='<b>%{label}</b><br>%{value}<extra></extra>',  # Template de hover
        maxdepth=1,                                      # Profundidade máxima
        marker=dict(
            colorscale="Greens",                         # Escala de cores verde
            colorbar=dict(title=f"Número de {forma_exibicao_setor}")  # Título da barra de cores
        )
    ))
    
    # Configurar layout do treemap
    fig2.update_layout(
        title=f"Top 10 Setores de Atividade - {forma_exibicao_setor} - {ano_setor}",  # Título dinâmico
        height=500                                        # Altura fixa
    )
    
    # Renderizar treemap setorial
    st.plotly_chart(fig2, use_container_width=True)
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 4: COMPARAÇÃO REGIONAL =============
    # Análise comparativa entre regiões geográficas
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Comparação Regional")
    st.write("**Análise comparativa do mercado de trabalho por regiões**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_regional = st.selectbox(
            "Ano:",                                       # Ano para análise regional
            sorted(dados_trabalho['ano'].unique(), reverse=True),
            key="ano_regional"
        )
    
    with col2:
        metrica_regional = st.selectbox(
            "Métrica:",                                   # Métrica para comparação
            ["Admissões", "Desligamentos", "Saldo"],
            key="metrica_regional"
        )
    
    # ============= PROCESSAMENTO: DADOS REGIONAIS =============
    dados_regional = dados_trabalho[dados_trabalho['ano'] == ano_regional]
    
    # Mapear métrica selecionada para coluna correspondente
    mapeamento_metrica = {
        "Admissões": "admissoes",
        "Desligamentos": "desligamentos", 
        "Saldo": "saldo"
    }
    
    coluna_metrica = mapeamento_metrica[metrica_regional]
    dados_regional_grafico = dados_regional.groupby('regiao')[coluna_metrica].sum().reset_index()
    
    # ============= VISUALIZAÇÃO: GRÁFICO REGIONAL COM CORES CONDICIONAIS =============
    # Definir cores baseadas no valor (especialmente para saldo)
    if metrica_regional == "Saldo":
        colors = ['#1a8c73' if x >= 0 else '#d32f2f' for x in dados_regional_grafico[coluna_metrica]]
        color_discrete_map = None
    else:
        colors = None
        color_discrete_map = None
    
    fig3 = px.bar(
        dados_regional_grafico,
        x='regiao',
        y=coluna_metrica,
        title=f"{metrica_regional} por Região - {ano_regional}",
        color=colors if colors else None,
        color_discrete_sequence=['#1a8c73'] if not colors else None
    )
    
    fig3.update_layout(
        xaxis_title="Região",
        yaxis_title=f"Número de {metrica_regional}",
        height=400,
        showlegend=False
    )
    
    # Adicionar linha de referência para saldo zero
    if metrica_regional == "Saldo":
        fig3.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Saldo Zero")
    
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 5: SETORES COM MAIOR CRESCIMENTO =============
    # Análise de crescimento setorial por períodos configuráveis
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Setores com Maior Crescimento")
    st.write("**Identificação de setores em expansão por período temporal**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        periodo_crescimento = st.selectbox(
            "Período:",                                   # Período para análise de crescimento
            ["Últimos 5 anos", "Últimos 10 anos", "Todos os anos"],
            key="periodo_crescimento"
        )
    
    with col2:
        tipo_crescimento = st.selectbox(
            "Tipo:",                                      # Tipo de métrica para crescimento
            ["Admissões", "Saldo"],
            key="tipo_crescimento"
        )
    
    # ============= PROCESSAMENTO: FILTRAR POR PERÍODO =============
    ano_atual = dados_trabalho['ano'].max()
    
    if periodo_crescimento == "Últimos 5 anos":
        dados_crescimento = dados_trabalho[dados_trabalho['ano'] >= (ano_atual - 4)]
    elif periodo_crescimento == "Últimos 10 anos":
        dados_crescimento = dados_trabalho[dados_trabalho['ano'] >= (ano_atual - 9)]
    else:  # Todos os anos
        dados_crescimento = dados_trabalho
    
    # Calcular crescimento acumulado por setor
    metrica_crescimento = 'admissoes' if tipo_crescimento == "Admissões" else 'saldo'
    dados_crescimento_setor = dados_crescimento.groupby('setor_atividade')[metrica_crescimento].sum().reset_index()
    dados_crescimento_setor = dados_crescimento_setor.sort_values(metrica_crescimento, ascending=False).head(10)
    
    # ============= VISUALIZAÇÃO: GRÁFICO HORIZONTAL DE CRESCIMENTO =============
    fig4 = px.bar(
        dados_crescimento_setor,
        x=metrica_crescimento,
        y='setor_atividade',
        title=f"Top 10 Setores - {tipo_crescimento} - {periodo_crescimento}",
        color=metrica_crescimento,
        color_continuous_scale='Greens',
        orientation='h'                                   # Orientação horizontal para melhor leitura
    )
    
    fig4.update_layout(
        xaxis_title=f"Total de {tipo_crescimento}",
        yaxis_title="Setor de Atividade",
        height=500
    )
    
    st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO 6: ANÁLISE DE TENDÊNCIAS POR SETOR =============
    # Análise temporal multi-setorial com seleção interativa
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Análise de Tendências por Setor")
    st.write("**Evolução temporal comparativa entre setores selecionados**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        setores_selecionados = st.multiselect(
            "Selecione até 5 setores:",                  # Limitação para melhor visualização
            dados_trabalho['setor_atividade'].unique(),
            default=dados_trabalho['setor_atividade'].unique()[:3],  # Padrão: primeiros 3
            max_selections=5,                             # Máximo 5 setores
            key="setores_tendencia"
        )
    
    with col2:
        metrica_tendencia = st.selectbox(
            "Métrica:",                                   # Métrica para análise temporal
            ["Admissões", "Desligamentos", "Saldo"],
            key="metrica_tendencia"
        )
    
    # ============= VALIDAÇÃO E PROCESSAMENTO: DADOS DE TENDÊNCIA =============
    if setores_selecionados:
        # Filtrar dados pelos setores selecionados
        dados_tendencia = dados_trabalho[dados_trabalho['setor_atividade'].isin(setores_selecionados)]
        
        # Mapear métrica selecionada
        coluna_tendencia = mapeamento_metrica[metrica_tendencia]
        
        # Agrupar por ano e setor para análise temporal
        dados_tendencia_grafico = dados_tendencia.groupby(['ano', 'setor_atividade'])[coluna_tendencia].sum().reset_index()
        
        # ============= VISUALIZAÇÃO: GRÁFICO DE LINHAS MULTI-SETORIAL =============
        fig5 = px.line(
            dados_tendencia_grafico,
            x='ano',                                      # Eixo temporal
            y=coluna_tendencia,                          # Métrica selecionada
            color='setor_atividade',                     # Separação por setor (cores diferentes)
            title=f"Tendência de {metrica_tendencia} por Setor",
            markers=True                                  # Marcadores nos pontos
        )
        
        fig5.update_layout(
            xaxis_title="Ano",
            yaxis_title=f"Número de {metrica_tendencia}",
            height=400,
            legend_title="Setor de Atividade"
        )
        
        st.plotly_chart(fig5, use_container_width=True)
    else:
        # ============= AVISO: NENHUM SETOR SELECIONADO =============
        st.info("📌 Selecione pelo menos um setor para visualizar a tendência.")
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= RODAPÉ: INFORMAÇÕES INSTITUCIONAIS =============
    # Exibir rodapé padrão do sistema
    display_footer()
