# ==============================================================================
# MÓDULO DE ORÇAMENTO - SISTEMA DASHBOARD IFPB-CZ
# ==============================================================================
"""
Módulo responsável pela análise e visualização de dados orçamentários da instituição.

FUNCIONALIDADES PRINCIPAIS:
• Monitoramento de dotação orçamentária, valores empenhados e pagos
• Análise por categorias orçamentárias (pessoal, custeio, investimentos, etc.)
• Visualização de evolução temporal dos gastos públicos
• Cálculo de eficiência orçamentária e percentuais de execução
• Comparação entre diferentes unidades e anos
• Filtros dinâmicos para análise detalhada

DADOS PROCESSADOS:
• Dotação orçamentária autorizada por categoria
• Valores empenhados (comprometidos) por período
• Valores efetivamente pagos pela instituição
• Distribuição por unidades organizacionais
• Histórico temporal de execução orçamentária

VISUALIZAÇÕES GERADAS:
• KPIs principais de execução orçamentária
• Painel de gastos por categoria com ícones visuais
• Gráficos comparativos de dotação vs empenhado vs pago
• Evolução temporal dos diferentes tipos orçamentários
• Análise de eficiência com percentuais de execução

CATEGORIAS ORÇAMENTÁRIAS:
• Pessoal e Encargos Sociais: folha de pagamento e benefícios
• Custeio: despesas operacionais e manutenção corrente
• Investimentos: aquisições de bens de capital
• Manutenção: conservação de bens e equipamentos
• Equipamentos: aquisição de materiais permanentes
• Obras: construções e reformas de infraestrutura

TECNOLOGIAS UTILIZADAS:
• Streamlit para interface web responsiva
• Plotly para gráficos interativos avançados
• Pandas para manipulação de dados financeiros
• Formatação monetária brasileira (R$)
• Sistema de cores institucional para categorização
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def orcamento_module(data_gen):
    """
    Módulo principal de análise orçamentária institucional.
    
    Este módulo processa e apresenta informações financeiras da instituição,
    incluindo dotação orçamentária, valores empenhados, pagos e análises
    de eficiência de execução orçamentária.
    
    Args:
        data_gen: Gerador de dados para obtenção das informações orçamentárias
    
    Returns:
        None: Renderiza a interface Streamlit com análises financeiras
    """
    
    # ==============================================================================
    # INICIALIZAÇÃO E CONFIGURAÇÃO
    # ==============================================================================
    
    # Exibir cabeçalho institucional com logo
    display_header_with_logo("Orçamento")
    
    # ==============================================================================
    # CARREGAMENTO E PROCESSAMENTO DOS DADOS ORÇAMENTÁRIOS
    # ==============================================================================
    
    # Gerar dados orçamentários (real ou simulado conforme configuração)
    dados_orcamento = data_gen.gerar_dados_orcamento()
    
    # Filtrar dados para o ano atual (2025) para cálculo dos KPIs principais
    dados_2025 = dados_orcamento[dados_orcamento['ano'] == 2025]
    
    # ==============================================================================
    # CÁLCULO DOS KPIS ORÇAMENTÁRIOS PRINCIPAIS
    # ==============================================================================
    
    # KPI 1: Total da dotação orçamentária autorizada
    total_dotacao = dados_2025['dotacao'].sum()
    
    # KPI 2: Total de valores empenhados (comprometidos)
    total_empenhado = dados_2025['empenhado'].sum()
    
    # KPI 3: Total de valores efetivamente pagos
    total_pago = dados_2025['pago'].sum()
    
    # ==============================================================================
    # EXIBIÇÃO DOS KPIS ORÇAMENTÁRIOS
    # ==============================================================================
    
    # Cartões de KPI em layout de três colunas
    col1, col2, col3 = st.columns(3)
    
    # KPI Card 1: Dotação Orçamentária
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ORÇAMENTO DOTAÇÃO</div>
            <div class="kpi-value">{data_gen.formatar_valor_monetario(total_dotacao)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI Card 2: Orçamento Empenhado
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ORÇAMENTO EMPENHADO</div>
            <div class="kpi-value">{data_gen.formatar_valor_monetario(total_empenhado)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI Card 3: Orçamento Pago
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ORÇAMENTO PAGO</div>
            <div class="kpi-value">{data_gen.formatar_valor_monetario(total_pago)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Separador visual entre seções
    st.markdown("---")
    
    # ==============================================================================
    # PAINEL DE GASTOS POR CATEGORIA
    # ==============================================================================
    
    # Painel de Gastos com visualização por categorias
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("💰 Painel de Gastos por Categoria")
    
    # Controles de filtro em duas colunas
    col1, col2 = st.columns(2)
    
    # Filtro de unidade organizacional
    with col1:
        unidade_selecionada = st.selectbox(
            "Selecione uma unidade:",
            ["Todas"] + list(dados_orcamento['unidade'].unique()),
            key="unidade_orcamento"
        )
    
    # Filtro de ano para análise temporal
    with col2:
        ano_selecionado = st.selectbox(
            "Selecione um ano:",
            sorted(dados_orcamento['ano'].unique(), reverse=True),
            key="ano_orcamento"
        )
    
    # ==============================================================================
    # PROCESSAMENTO E FILTRAGEM DOS DADOS
    # ==============================================================================
    
    # Aplicar filtros selecionados pelo usuário
    dados_filtrados = dados_orcamento[dados_orcamento['ano'] == ano_selecionado]
    
    # Aplicar filtro de unidade se especificado
    if unidade_selecionada != "Todas":
        dados_filtrados = dados_filtrados[dados_filtrados['unidade'] == unidade_selecionada]
    
    # Agrupar dados por categoria orçamentária
    dados_categorias = dados_filtrados.groupby('categoria').agg({
        'dotacao': 'sum',      # Soma da dotação autorizada
        'empenhado': 'sum',    # Soma dos valores empenhados
        'pago': 'sum'          # Soma dos valores pagos
    }).reset_index()
    
    # ==============================================================================
    # CONFIGURAÇÃO DE ÍCONES POR CATEGORIA
    # ==============================================================================
    
    # Ícones visuais para cada categoria orçamentária
    icones_categorias = {
        "Pessoal e Encargos Sociais": "👥",  # Recursos humanos
        "Custeio": "🏢",                     # Despesas operacionais
        "Investimentos": "💎",               # Bens de capital
        "Manutenção": "🔧",                  # Conservação e reparos
        "Equipamentos": "💻",                # Material permanente
        "Obras": "🏗️"                       # Construções e reformas
    }
    
    # ==============================================================================
    # GRID DE CATEGORIAS ORÇAMENTÁRIAS
    # ==============================================================================
    
    # Criar layout em grid de 3 colunas para exibir categorias
    num_colunas = 3
    colunas = st.columns(num_colunas)
    
    # Iterar por cada categoria para criar cards informativos
    for idx, (_, row) in enumerate(dados_categorias.iterrows()):
        # Calcular posição da coluna no grid
        col_idx = idx % num_colunas
        categoria = row['categoria']
        
        # Obter ícone correspondente ou usar padrão
        icone = icones_categorias.get(categoria, "📊")
        
        # Criar card da categoria na coluna correspondente
        with colunas[col_idx]:
            # Card HTML com ícone e informações financeiras formatadas
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
    
    # Fechar container do painel de categorias
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ==============================================================================
    # GRÁFICO 1: COMPARAÇÃO ORÇAMENTÁRIA POR CATEGORIA
    # ==============================================================================
    
    # Gráfico 1: Comparação Dotação vs Empenhado vs Pago
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Comparação Orçamentária por Categoria")
    
    # Reorganizar dados para formato adequado ao gráfico (pivot/melt)
    dados_melted = dados_categorias.melt(
        id_vars=['categoria'],                              # Coluna identificadora
        value_vars=['dotacao', 'empenhado', 'pago'],       # Colunas de valores
        var_name='tipo',                                    # Nome da nova coluna categoria
        value_name='valor'                                  # Nome da nova coluna valores
    )
    
    # Mapear nomes técnicos para nomes amigáveis
    mapeamento_tipos = {
        'dotacao': 'Dotação',       # Orçamento autorizado
        'empenhado': 'Empenhado',   # Valores comprometidos
        'pago': 'Pago'              # Valores efetivamente pagos
    }
    
    # Aplicar mapeamento aos dados
    dados_melted['tipo'] = dados_melted['tipo'].map(mapeamento_tipos)
    
    # Criar gráfico de barras agrupadas para comparação
    fig = px.bar(
        dados_melted,
        x='categoria',
        y='valor',
        color='tipo',                                       # Agrupar por tipo orçamentário
        title=f"Comparação Orçamentária por Categoria - {ano_selecionado}",
        color_discrete_sequence=['#1a8c73', '#0d5a4e', '#2db896'],  # Cores institucionais
        barmode='group'                                     # Barras agrupadas lado a lado
    )
    
    # Personalizar layout do gráfico
    fig.update_layout(
        xaxis_title="Categoria",                           # Título eixo X
        yaxis_title="Valor (R$)",                          # Título eixo Y
        xaxis_tickangle=-45,                               # Inclinar labels para melhor leitura
        height=500,                                        # Altura do gráfico
        showlegend=True,                                   # Exibir legenda
        legend=dict(
            orientation="h",                               # Legenda horizontal
            yanchor="bottom",                              # Ancoragem inferior
            y=1.02,                                        # Posição acima do gráfico
            xanchor="right",                               # Ancoragem direita
            x=1                                            # Posição completa à direita
        )
    )
    
    # Formatar valores no eixo Y com separadores
    fig.update_yaxes(tickformat='.0f')
    
    # Exibir gráfico de comparação orçamentária
    st.plotly_chart(fig, use_container_width=True)
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO: EVOLUÇÃO TEMPORAL DO ORÇAMENTO =============
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução Orçamentária")
    st.write("**Análise da evolução do orçamento ao longo dos anos disponíveis**")
    
    # Criar colunas para seletores de filtros da evolução temporal
    col1, col2 = st.columns(2)
    
    # Coluna 1: Seletor de tipo de análise temporal
    with col1:
        # Opções para visualização temporal dos tipos orçamentários
        tipo_evolucao = st.selectbox(
            "Tipo de Orçamento:",                          # Label do seletor
            ["Dotação", "Empenhado", "Pago"],             # Opções disponíveis
            key="tipo_evolucao"                            # Chave única para controle estado
        )
    
    # Coluna 2: Informações contextuais sobre a análise temporal
    
    # Coluna 2: Seletor de unidade organizacional
    with col2:
        # Permitir filtrar por unidade específica ou visualizar todas
        unidade_evolucao = st.selectbox(
            "Unidade:",                                    # Label do seletor
            ["Todas"] + list(dados_orcamento['unidade'].unique()),  # Opções: todas + unidades específicas
            key="unidade_evolucao"                         # Chave única para controle estado
        )
    
    # ============= PROCESSAMENTO: FILTRAR DADOS PARA EVOLUÇÃO =============
    # Criar cópia dos dados para manipulação
    dados_evolucao = dados_orcamento.copy()
    
    # Aplicar filtro de unidade se selecionada uma específica
    if unidade_evolucao != "Todas":
        dados_evolucao = dados_evolucao[dados_evolucao['unidade'] == unidade_evolucao]
    
    # Mapear tipo selecionado para nome da coluna nos dados
    mapeamento_tipo = {
        "Dotação": "dotacao",                              # Orçamento autorizado
        "Empenhado": "empenhado",                          # Valores comprometidos  
        "Pago": "pago"                                     # Valores efetivamente pagos
    }
    
    # Obter nome da coluna correspondente ao tipo selecionado
    tipo_coluna = mapeamento_tipo[tipo_evolucao]
    
    # ============= PROCESSAMENTO: AGRUPAR DADOS POR ANO =============
    # Agrupar dados por ano e somar valores do tipo selecionado
    dados_evolucao_grafico = dados_evolucao.groupby('ano')[tipo_coluna].sum().reset_index()
    
    # ============= VISUALIZAÇÃO: GRÁFICO DE EVOLUÇÃO TEMPORAL =============
    # Criar gráfico de linha para mostrar evolução temporal
    fig2 = px.line(
        dados_evolucao_grafico,
        x='ano',                                           # Eixo X: anos
        y=tipo_coluna,                                     # Eixo Y: valores do tipo selecionado
        title=f"Evolução do Orçamento {tipo_evolucao} - {unidade_evolucao}",  # Título dinâmico
        markers=True,                                      # Exibir marcadores nos pontos
        color_discrete_sequence=['#1a8c73']               # Cor institucional IFPB
    )
    
    # Personalizar layout do gráfico de evolução
    fig2.update_layout(
        xaxis_title="Ano",                                 # Título eixo X
        yaxis_title=f"Valor {tipo_evolucao} (R$)",        # Título eixo Y dinâmico
        height=400,                                        # Altura do gráfico
        showlegend=False                                   # Ocultar legenda (apenas uma linha)
    )
    
    # Exibir gráfico de evolução temporal
    st.plotly_chart(fig2, use_container_width=True)
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= SEÇÃO: ANÁLISE DE EFICIÊNCIA ORÇAMENTÁRIA =============
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Eficiência Orçamentária")
    st.write("**Análise dos percentuais de execução orçamentária por categoria**")
    
    # ============= PROCESSAMENTO: CALCULAR PERCENTUAIS DE EXECUÇÃO =============
    # Criar cópia dos dados para cálculos de eficiência
    dados_eficiencia = dados_filtrados.copy()
    
    # Calcular percentual de empenhamento (compromisso dos recursos)
    dados_eficiencia['percentual_empenhado'] = (dados_eficiencia['empenhado'] / dados_eficiencia['dotacao']) * 100
    
    # Calcular percentual de pagamento (execução efetiva)
    dados_eficiencia['percentual_pago'] = (dados_eficiencia['pago'] / dados_eficiencia['dotacao']) * 100
    
    # ============= PROCESSAMENTO: AGRUPAR DADOS POR CATEGORIA =============
    # Agrupar por categoria e calcular médias dos percentuais
    dados_eficiencia_grafico = dados_eficiencia.groupby('categoria').agg({
        'percentual_empenhado': 'mean',                    # Média do percentual empenhado por categoria
        'percentual_pago': 'mean'                          # Média do percentual pago por categoria
    }).reset_index()
    
    # ============= PROCESSAMENTO: REORGANIZAR DADOS PARA VISUALIZAÇÃO =============
    # Transformar dados para formato adequado ao gráfico (pivot/melt)
    dados_eficiencia_melted = dados_eficiencia_grafico.melt(
        id_vars=['categoria'],                             # Coluna identificadora
        value_vars=['percentual_empenhado', 'percentual_pago'],  # Colunas de percentuais
        var_name='tipo',                                   # Nome da nova coluna categoria
        value_name='percentual'                            # Nome da nova coluna valores
    )
    
    # Mapear nomes técnicos para nomes amigáveis na visualização
    mapeamento_eficiencia = {
        'percentual_empenhado': 'Percentual Empenhado',   # Recursos comprometidos
        'percentual_pago': 'Percentual Pago'              # Recursos efetivamente pagos
    }
    
    # Aplicar mapeamento aos dados
    dados_eficiencia_melted['tipo'] = dados_eficiencia_melted['tipo'].map(mapeamento_eficiencia)
    
    # ============= VISUALIZAÇÃO: GRÁFICO DE EFICIÊNCIA ORÇAMENTÁRIA =============
    # Criar gráfico de barras para mostrar eficiência por categoria
    fig3 = px.bar(
        dados_eficiencia_melted,
        x='categoria',                                     # Eixo X: categorias orçamentárias
        y='percentual',                                    # Eixo Y: percentuais de execução
        color='tipo',                                      # Agrupar por tipo de eficiência
        title=f"Eficiência Orçamentária por Categoria - {ano_selecionado}",  # Título dinâmico
        color_discrete_sequence=['#1a8c73', '#0d5a4e'],   # Cores institucionais IFPB
        barmode='group'                                    # Barras agrupadas lado a lado
    )
    
    # Personalizar layout do gráfico de eficiência
    fig3.update_layout(
        xaxis_title="Categoria",                           # Título eixo X
        yaxis_title="Percentual (%)",                     # Título eixo Y
        xaxis_tickangle=-45,                               # Inclinar labels para melhor leitura
        height=400,                                        # Altura do gráfico
        showlegend=True                                    # Exibir legenda
    )
    
    # Adicionar linha de referência em 100% (execução completa)
    fig3.add_hline(
        y=100,                                             # Valor da linha horizontal
        line_dash="dash",                                  # Linha tracejada
        line_color="red",                                  # Cor vermelha para destaque
        annotation_text="100% - Execução Completa"        # Texto explicativo
    )
    
    # Exibir gráfico de eficiência orçamentária
    st.plotly_chart(fig3, use_container_width=True)
    
    # Fonte dos dados e fechamento do container
    st.markdown('<div class="fonte-dados">Fonte de Dados: Portal da Transparência</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ============= RODAPÉ: INFORMAÇÕES GERAIS =============
    # Exibir rodapé padrão do sistema
    display_footer()
