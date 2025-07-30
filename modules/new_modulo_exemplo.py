#!/usr/bin/env python3
"""
=============================================================================
MÓDULO EXEMPLO - TEMPLATE PARA NOVOS MÓDULOS - SISTEMA DASHBOARD IFPB-CZ
=============================================================================

Este arquivo serve como template e guia de referência para criação de novos
módulos no Sistema Dashboard IFPB-CZ, demonstrando estrutura padrão,
convenções de nomenclatura, organização de código e implementação de
funcionalidades essenciais seguindo os padrões estabelecidos no sistema.

ESTRUTURA PADRÃO DE UM MÓDULO:
------------------------------
1. Cabeçalho com documentação completa
2. Importação de bibliotecas necessárias
3. Configuração de constantes e cores institucionais
4. Função de carregamento de dados
5. Funções auxiliares específicas do módulo
6. Funções de criação de visualizações
7. Função principal do dashboard
8. Ponto de entrada para execução independente

CONVENÇÕES OBRIGATÓRIAS:
------------------------
- Nome do arquivo: nome_do_modulo.py (snake_case)
- Função principal: mostrar_dashboard_[nome_modulo]()
- Cores institucionais: usar CORES_IFPB do utils.py
- Estrutura de dados: sempre usar DataFrames do pandas
- Tratamento de erros: implementar try/except apropriados
- Documentação: docstrings detalhadas para todas as funções

FUNCIONALIDADES ESSENCIAIS:
---------------------------
- Carregamento de dados (reais ou sintéticos)
- Filtros interativos na sidebar
- Múltiplas visualizações (KPIs, gráficos, tabelas)
- Responsividade e layout adaptativo
- Tratamento de casos sem dados
- Informações de atualização e fonte

DEPENDÊNCIAS PADRÃO:
--------------------
- streamlit: interface web
- pandas: manipulação de dados
- plotly: visualizações interativas
- datetime: manipulação de datas
- modules.utils: utilitários compartilhados

AUTOR: Sistema Dashboard IFPB-CZ - NAI
DATA: 2024
=============================================================================
"""

# =============================================================================
# IMPORTAÇÕES NECESSÁRIAS
# =============================================================================

# Biblioteca principal para interface web interativa
import streamlit as st

# Bibliotecas para manipulação e análise de dados
import pandas as pd                    # Manipulação de DataFrames
import numpy as np                     # Operações numéricas e arrays

# Bibliotecas para visualizações interativas
import plotly.express as px            # Gráficos rápidos e intuitivos
import plotly.graph_objects as go      # Gráficos customizados avançados

# Bibliotecas para manipulação de datas e tempo
from datetime import datetime, date    # Operações com datas

# Importar utilitários compartilhados do sistema IFPB-CZ
from modules.utils import (
    CORES_IFPB,                       # Paleta de cores institucional IFPB
    aplicar_estilo_personalizado,     # CSS customizado para interface
    criar_card_metrica,               # Componente para exibir KPIs
    formatar_numero,                  # Formatação de números brasileira
    gerar_dados_ficticios,           # Gerador de dados para testes
    exibir_info_atualizacao          # Rodapé com informações de atualização
)

# =============================================================================
# CONFIGURAÇÕES ESPECÍFICAS DO MÓDULO
# =============================================================================

# Nome do módulo para identificação interna e logs
NOME_MODULO = "Exemplo"

# Descrição exibida no cabeçalho do dashboard
DESCRICAO_MODULO = "Módulo de exemplo demonstrando estrutura padrão para novos desenvolvimentos"

# Identificação da origem dos dados para rastreabilidade
FONTE_DADOS = "Sistema de Gestão Exemplo / Dados Sintéticos"

# Dicionário com configurações centralizadas do módulo
# Facilita manutenção e customização de parâmetros
CONFIGURACOES = {
    'periodo_padrao': datetime.now().year,  # Ano atual como padrão
    # Lista de categorias possíveis para classificação
    'categorias_exemplo': ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D'],
    # Estados possíveis para controle de workflow
    'status_possiveis': ['Ativo', 'Inativo', 'Pendente', 'Concluído'],
    # Tipos de indicadores para análise multidimensional
    'tipos_indicadores': ['Indicador 1', 'Indicador 2', 'Indicador 3']
}

# =============================================================================
# FUNÇÃO DE CARREGAMENTO DE DADOS
# =============================================================================

def carregar_dados_exemplo():
    """
    Carrega dados do módulo exemplo (reais ou sintéticos).
    
    Esta função implementa o carregamento de dados específicos do módulo,
    seguindo o padrão estabelecido no sistema para integração com fontes
    de dados reais ou geração de dados sintéticos para demonstração.
    
    ESTRATÉGIA DE CARREGAMENTO:
    1. Tentar carregar dados reais de arquivo/API
    2. Em caso de falha, gerar dados sintéticos
    3. Aplicar validações e tratamentos necessários
    4. Retornar DataFrame padronizado
    
    ESTRUTURA DE DADOS ESPERADA:
    - data: data do registro (formato datetime)
    - categoria: categoria do item
    - valor: valor numérico principal
    - quantidade: quantidade relacionada
    - status: status atual do item
    - tipo: tipo/classificação do item
    - descricao: descrição textual
    
    RETORNO:
    --------
    pd.DataFrame
        DataFrame com dados do módulo, estruturado conforme especificação
        
    TRATAMENTO DE ERROS:
    --------------------
    - Captura exceções de carregamento
    - Fallback para dados sintéticos
    - Logging de erros quando necessário
    """
    try:
        # =============================================================================
        # TENTATIVA DE CARREGAMENTO DE DADOS REAIS
        # =============================================================================
        
        # SUBSTITUIR ESTA SEÇÃO PELA LÓGICA REAL DE CARREGAMENTO
        # Exemplos possíveis:
        # - pd.read_excel('dados/dados_modulo_exemplo.xlsx')
        # - Consulta a API: requests.get('api_endpoint')
        # - Consulta a banco de dados: pd.read_sql(query, connection)
        
        # Para demonstração, simular falha para usar dados sintéticos
        raise FileNotFoundError("Arquivo de dados reais não encontrado")
        
    except Exception as e:
        # =============================================================================
        # GERAÇÃO DE DADOS SINTÉTICOS PARA DEMONSTRAÇÃO
        # =============================================================================
        
        # Informar ao usuário sobre o uso de dados sintéticos
        st.info(f"📊 Usando dados sintéticos para demonstração do módulo {NOME_MODULO}")
        
        # Lista para armazenar registros gerados
        dados_sinteticos = []
        
        # Definir período de dados (últimos 24 meses para ter volume representativo)
        periodo_inicio = datetime.now().replace(day=1, month=1) - pd.DateOffset(years=1)
        # Gerar 500 datas distribuídas no período (aproximadamente 1.5 registros por dia)
        datas = pd.date_range(start=periodo_inicio, periods=500, freq='D')
        
        # Gerar registros sintéticos combinando datas com categorias
        for data in datas:
            for categoria in CONFIGURACOES['categorias_exemplo']:
                # Gerar valores usando distribuição normal para realismo
                # Valor base centrado em R$ 1.000 com desvio de R$ 200
                valor_base = np.random.normal(1000, 200)
                
                # Quantidade segue distribuição de Poisson (típica para contagens)
                # Lambda = 10 gera média de 10 itens por registro
                quantidade = np.random.poisson(10)
                
                # Criar registro individual com estrutura padronizada
                registro = {
                    'data': data,                                                    # Data do registro
                    'categoria': categoria,                                          # Categoria de classificação
                    'valor': max(0, valor_base + np.random.normal(0, 100)),        # Valor monetário (sempre positivo)
                    'quantidade': max(0, quantidade),                               # Quantidade (sempre positiva)
                    'status': np.random.choice(CONFIGURACOES['status_possiveis']), # Status aleatório
                    'tipo': np.random.choice(CONFIGURACOES['tipos_indicadores']),  # Tipo de indicador
                    'descricao': f"Registro exemplo para {categoria} em {data.strftime('%d/%m/%Y')}"  # Descrição descritiva
                }
                # Adicionar registro à lista de dados sintéticos
                dados_sinteticos.append(registro)
        
        # Converter lista de dicionários para DataFrame pandas
        df = pd.DataFrame(dados_sinteticos)
        
        # Aplicar tratamentos e validações dos dados
        df['data'] = pd.to_datetime(df['data'])    # Garantir formato datetime
        df['ano'] = df['data'].dt.year             # Extrair ano para filtros
        df['mes'] = df['data'].dt.month            # Extrair mês para agregações
        df['valor'] = df['valor'].round(2)         # Arredondar valores para 2 decimais
        
        return df

# =============================================================================
# FUNÇÕES AUXILIARES ESPECÍFICAS DO MÓDULO
# =============================================================================

def calcular_indicadores_exemplo(df):
    """
    Calcula indicadores específicos do módulo exemplo.
    
    PARÂMETROS:
    -----------
    df : pd.DataFrame
        DataFrame com dados do módulo
        
    RETORNO:
    --------
    dict
        Dicionário com indicadores calculados
    """
    # Verificar se DataFrame está vazio para evitar erros de cálculo
    if df.empty:
        # Retornar indicadores zerados quando não há dados
        return {
            'total_registros': 0,
            'valor_total': 0,
            'media_valor': 0,
            'quantidade_total': 0,
            'crescimento_mensal': 0
        }
    
    # =============================================================================
    # CÁLCULO DE INDICADORES BÁSICOS
    # =============================================================================
    
    # Contar total de registros no DataFrame filtrado
    total_registros = len(df)
    
    # Somar todos os valores monetários
    valor_total = df['valor'].sum()
    
    # Calcular valor médio por registro
    media_valor = df['valor'].mean()
    
    # Somar todas as quantidades
    quantidade_total = df['quantidade'].sum()
    
    # =============================================================================
    # CÁLCULO DE CRESCIMENTO MENSAL
    # =============================================================================
    
    # Filtrar dados do mês atual (último mês com dados)
    df_atual = df[df['data'] >= df['data'].max() - pd.DateOffset(months=1)]
    
    # Filtrar dados do mês anterior (penúltimo mês)
    df_anterior = df[(df['data'] >= df['data'].max() - pd.DateOffset(months=2)) & 
                     (df['data'] < df['data'].max() - pd.DateOffset(months=1))]
    
    # Calcular valores totais de cada período
    valor_atual = df_atual['valor'].sum() if not df_atual.empty else 0
    valor_anterior = df_anterior['valor'].sum() if not df_anterior.empty else 1  # Evitar divisão por zero
    
    # Calcular percentual de crescimento mensal
    crescimento_mensal = ((valor_atual - valor_anterior) / valor_anterior * 100) if valor_anterior > 0 else 0
    
    # =============================================================================
    # RETORNO DOS INDICADORES CALCULADOS
    # =============================================================================
    
    # Retornar dicionário com todos os indicadores calculados
    return {
        'total_registros': total_registros,      # Quantidade total de registros
        'valor_total': valor_total,              # Soma de todos os valores
        'media_valor': media_valor,              # Valor médio por registro
        'quantidade_total': quantidade_total,    # Soma de todas as quantidades
        'crescimento_mensal': crescimento_mensal # Percentual de crescimento mensal
    }

def filtrar_dados_exemplo(df, filtros):
    """
    Aplica filtros aos dados do módulo exemplo.
    
    Esta função implementa a lógica de filtragem dos dados baseada
    nas seleções do usuário na interface, permitindo análises
    específicas por período, categoria e status.
    
    PARÂMETROS:
    -----------
    df : pd.DataFrame
        DataFrame original com todos os dados carregados
    filtros : dict
        Dicionário com filtros selecionados pelo usuário contendo:
        - 'periodo': ano selecionado para análise
        - 'categorias': lista de categorias selecionadas
        - 'status': lista de status selecionados
        
    RETORNO:
    --------
    pd.DataFrame
        DataFrame filtrado conforme seleções do usuário
        
    LÓGICA DE FILTRAGEM:
    -------------------
    1. Criar cópia do DataFrame original para preservar dados
    2. Aplicar filtro de período (ano) se especificado
    3. Aplicar filtro de categorias se especificado
    4. Aplicar filtro de status se especificado
    5. Retornar DataFrame resultante
    """
    # Criar cópia do DataFrame original para não modificar os dados fonte
    df_filtrado = df.copy()
    
    # =============================================================================
    # APLICAÇÃO DE FILTROS SEQUENCIAIS
    # =============================================================================
    
    # Filtro por período (ano)
    # Aplicar apenas se período foi especificado
    if filtros.get('periodo'):
        df_filtrado = df_filtrado[df_filtrado['ano'] == filtros['periodo']]
    
    # Filtro por categorias
    # Aplicar apenas se categorias foram especificadas
    if filtros.get('categorias'):
        df_filtrado = df_filtrado[df_filtrado['categoria'].isin(filtros['categorias'])]
    
    # Filtro por status
    # Aplicar apenas se status foram especificados
    if filtros.get('status'):
        df_filtrado = df_filtrado[df_filtrado['status'].isin(filtros['status'])]
    
    return df_filtrado

# =============================================================================
# FUNÇÕES DE CRIAÇÃO DE VISUALIZAÇÕES
# =============================================================================

def criar_grafico_evolucao_temporal(df):
    """
    Cria gráfico de evolução temporal dos dados.
    
    Esta função gera um gráfico de linha mostrando a evolução
    dos valores ao longo do tempo, agregando dados mensalmente
    para facilitar visualização de tendências.
    
    PARÂMETROS:
    -----------
    df : pd.DataFrame
        DataFrame com dados filtrados contendo colunas:
        - 'data': datas dos registros
        - 'valor': valores monetários
        - 'quantidade': quantidades associadas
        
    RETORNO:
    --------
    plotly.graph_objects.Figure
        Gráfico de linha interativo com evolução temporal
        
    CARACTERÍSTICAS DO GRÁFICO:
    ---------------------------
    - Agregação mensal dos dados
    - Linha com marcadores para melhor visualização
    - Cores institucionais IFPB
    - Hover interativo
    - Tratamento para casos sem dados
    """
    # =============================================================================
    # VALIDAÇÃO DE DADOS DISPONÍVEIS
    # =============================================================================
    
    # Verificar se há dados para processar
    if df.empty:
        # Criar gráfico vazio com mensagem informativa
        fig = go.Figure()
        fig.add_annotation(
            text="Nenhum dado disponível para o período selecionado",
            xref="paper", yref="paper",              # Referências relativas ao papel
            x=0.5, y=0.5,                            # Posição central
            xanchor='center', yanchor='middle',      # Âncoras centralizadas
            showarrow=False, font_size=16            # Sem seta, fonte legível
        )
        return fig
    
    # =============================================================================
    # AGREGAÇÃO DE DADOS POR PERÍODO MENSAL
    # =============================================================================
    
    # Agrupar dados por mês para suavizar visualização
    # to_period('M') agrupa por mês, ignorando o dia
    df_mensal = df.groupby(df['data'].dt.to_period('M')).agg({
        'valor': 'sum',        # Somar valores do mês
        'quantidade': 'sum'    # Somar quantidades do mês
    }).reset_index()
    
    # Converter período de volta para timestamp para usar no gráfico
    df_mensal['data'] = df_mensal['data'].dt.to_timestamp()
    
    # =============================================================================
    # CRIAÇÃO DO GRÁFICO DE LINHA
    # =============================================================================
    
    # Inicializar figura Plotly
    fig = go.Figure()
    
    # Adicionar linha principal com valores mensais
    fig.add_trace(go.Scatter(
        x=df_mensal['data'],                          # Eixo X: datas mensais
        y=df_mensal['valor'],                         # Eixo Y: valores agregados
        mode='lines+markers',                         # Linha contínua + marcadores
        name='Valor Total',                           # Nome da série
        line=dict(color=CORES_IFPB['primary'], width=3),  # Estilo da linha
        marker=dict(size=8)                           # Tamanho dos marcadores
    ))
    
    # =============================================================================
    # CONFIGURAÇÃO DE LAYOUT E ESTILO
    # =============================================================================
    
    # Configurar aparência e interatividade do gráfico
    fig.update_layout(
        title="Evolução Temporal dos Valores",       # Título descritivo
        xaxis_title="Período",                       # Rótulo do eixo X
        yaxis_title="Valor Total",                   # Rótulo do eixo Y
        hovermode='x unified',                       # Hover unificado no eixo X
        plot_bgcolor='white',                        # Fundo do gráfico branco
        paper_bgcolor='white',                       # Fundo do papel branco
        font=dict(size=12)                           # Tamanho da fonte
    )
    
    return fig

def criar_grafico_distribuicao_categoria(df):
    """
    Cria gráfico de distribuição por categoria.
    
    Esta função gera um gráfico de barras horizontais mostrando
    a distribuição de valores entre diferentes categorias,
    facilitando comparação visual entre categorias.
    
    PARÂMETROS:
    -----------
    df : pd.DataFrame
        DataFrame com dados filtrados contendo colunas:
        - 'categoria': categorias para agrupamento
        - 'valor': valores para agregação
        - 'quantidade': quantidades para agregação
        
    RETORNO:
    --------
    plotly.graph_objects.Figure
        Gráfico de barras horizontais interativo
        
    CARACTERÍSTICAS DO GRÁFICO:
    ---------------------------
    - Barras horizontais para melhor legibilidade de categorias
    - Ordenação crescente por valor
    - Cores institucionais IFPB
    - Rótulos de valores formatados
    - Tratamento para casos sem dados
    """
    # =============================================================================
    # VALIDAÇÃO DE DADOS DISPONÍVEIS
    # =============================================================================
    
    # Verificar se há dados para processar
    if df.empty:
        # Criar gráfico vazio com mensagem informativa
        fig = go.Figure()
        fig.add_annotation(
            text="Nenhum dado disponível",
            xref="paper", yref="paper",              # Referências relativas
            x=0.5, y=0.5,                            # Posição central
            xanchor='center', yanchor='middle',      # Âncoras centralizadas
            showarrow=False, font_size=16            # Sem seta, fonte legível
        )
        return fig
    
    # =============================================================================
    # AGREGAÇÃO E ORDENAÇÃO DOS DADOS
    # =============================================================================
    
    # Agrupar dados por categoria e calcular totais
    df_categoria = df.groupby('categoria').agg({
        'valor': 'sum',        # Somar valores por categoria
        'quantidade': 'sum'    # Somar quantidades por categoria
    }).reset_index()
    
    # Ordenar por valor crescente para facilitar leitura do gráfico
    df_categoria = df_categoria.sort_values('valor', ascending=True)
    
    # =============================================================================
    # CRIAÇÃO DO GRÁFICO DE BARRAS HORIZONTAIS
    # =============================================================================
    
    # Inicializar figura Plotly
    fig = go.Figure()
    
    # Adicionar barras horizontais
    fig.add_trace(go.Bar(
        x=df_categoria['valor'],                     # Eixo X: valores agregados
        y=df_categoria['categoria'],                 # Eixo Y: categorias
        orientation='h',                             # Orientação horizontal
        marker_color=CORES_IFPB['secondary'],       # Cor institucional secundária
        # Formatar números nos rótulos das barras
        text=df_categoria['valor'].apply(lambda x: formatar_numero(x)),
        textposition='auto'                          # Posição automática do texto
    ))
    
    # =============================================================================
    # CONFIGURAÇÃO DE LAYOUT E ESTILO
    # =============================================================================
    
    # Configurar aparência do gráfico de barras
    fig.update_layout(
        title="Distribuição de Valores por Categoria",  # Título descritivo
        xaxis_title="Valor Total",                      # Rótulo eixo X
        yaxis_title="Categoria",                        # Rótulo eixo Y
        plot_bgcolor='white',                           # Fundo branco
        paper_bgcolor='white',                          # Papel branco
        font=dict(size=12)                              # Fonte legível
    )
    
    return fig

def criar_grafico_status_pizza(df):
    """
    Cria gráfico de pizza com distribuição por status.
    
    Esta função gera um gráfico de pizza (donut) mostrando
    a distribuição proporcional dos diferentes status,
    ideal para visualizar composição de categorias.
    
    PARÂMETROS:
    -----------
    df : pd.DataFrame
        DataFrame com dados filtrados contendo coluna:
        - 'status': status dos registros para contagem
        
    RETORNO:
    --------
    plotly.graph_objects.Figure
        Gráfico de pizza interativo com distribuição de status
        
    CARACTERÍSTICAS DO GRÁFICO:
    ---------------------------
    - Formato donut (com buraco central)
    - Cores institucionais IFPB
    - Percentuais automáticos
    - Interatividade com hover
    - Tratamento para casos sem dados
    """
    # =============================================================================
    # VALIDAÇÃO DE DADOS DISPONÍVEIS
    # =============================================================================
    
    # Verificar se há dados para processar
    if df.empty:
        # Criar gráfico vazio com mensagem informativa
        fig = go.Figure()
        fig.add_annotation(
            text="Nenhum dado disponível",
            xref="paper", yref="paper",              # Referências relativas
            x=0.5, y=0.5,                            # Posição central
            xanchor='center', yanchor='middle',      # Âncoras centralizadas
            showarrow=False, font_size=16            # Sem seta, fonte legível
        )
        return fig
    
    # =============================================================================
    # CONTAGEM E PREPARAÇÃO DOS DADOS
    # =============================================================================
    
    # Contar ocorrências de cada status
    df_status = df['status'].value_counts().reset_index()
    df_status.columns = ['status', 'count']      # Renomear colunas para clareza
    
    # =============================================================================
    # CRIAÇÃO DO GRÁFICO DE PIZZA
    # =============================================================================
    
    # Inicializar figura Plotly
    fig = go.Figure()
    
    # Adicionar gráfico de pizza com estilo donut
    fig.add_trace(go.Pie(
        labels=df_status['status'],              # Rótulos das fatias
        values=df_status['count'],               # Valores para proporção
        hole=0.4,                                # Buraco central (estilo donut)
        # Array de cores institucionais IFPB para as fatias
        marker_colors=[CORES_IFPB['primary'], CORES_IFPB['secondary'], 
                      CORES_IFPB['accent'], CORES_IFPB['highlight']]
    ))
    
    # =============================================================================
    # CONFIGURAÇÃO DE LAYOUT E ESTILO
    # =============================================================================
    
    # Configurar aparência do gráfico de pizza
    fig.update_layout(
        title="Distribuição por Status",            # Título descritivo
        plot_bgcolor='white',                       # Fundo branco
        paper_bgcolor='white',                      # Papel branco
        font=dict(size=12)                          # Fonte legível
    )
    
    return fig

# =============================================================================
# FUNÇÃO PRINCIPAL DO DASHBOARD
# =============================================================================

def mostrar_dashboard_exemplo():
    """
    Função principal do dashboard do módulo exemplo.
    
    Esta função implementa toda a interface e funcionalidade do dashboard,
    seguindo o padrão estabelecido no sistema para garantir consistência
    visual e funcional entre todos os módulos.
    
    ESTRUTURA IMPLEMENTADA:
    1. Aplicação de estilos personalizados
    2. Criação de título e descrição
    3. Carregamento de dados
    4. Criação de filtros na sidebar
    5. Aplicação de filtros aos dados
    6. Cálculo de indicadores
    7. Exibição de KPIs principais
    8. Criação de visualizações
    9. Informações de atualização
    
    LAYOUT RESPONSIVO:
    - Uso de colunas para organização
    - Adaptação automática a diferentes tamanhos de tela
    - Elementos visuais consistentes com identidade IFPB
    
    INTERATIVIDADE:
    - Filtros dinâmicos na sidebar
    - Gráficos interativos com Plotly
    - Atualização automática baseada em filtros
    """
    # =============================================================================
    # CONFIGURAÇÃO INICIAL E ESTILOS
    # =============================================================================
    
    # Aplicar CSS customizado e tema institucional IFPB
    aplicar_estilo_personalizado()
    
    # Criar cabeçalho principal com ícone e título do módulo
    st.title(f"📊 Dashboard {NOME_MODULO}")
    # Exibir descrição detalhada do módulo
    st.markdown(f"**{DESCRICAO_MODULO}**")
    # Separador visual para organizar conteúdo
    st.markdown("---")
    
    # =============================================================================
    # CARREGAMENTO DE DADOS
    # =============================================================================
    
    # Carregar dados com indicador visual de progresso
    # Spinner melhora experiência do usuário durante carregamento
    with st.spinner("Carregando dados..."):
        df = carregar_dados_exemplo()
    
    # Validação crítica: verificar se dados foram carregados com sucesso
    if df.empty:
        # Exibir mensagens de erro informativas ao usuário
        st.error("❌ Nenhum dado disponível para exibição.")
        st.info("Verifique a conexão com a fonte de dados ou entre em contato com o suporte.")
        return  # Interromper execução se não há dados
    
    # =============================================================================
    # FILTROS INTERATIVOS NA SIDEBAR
    # =============================================================================
    
    # Criar seção de filtros na barra lateral para interatividade
    st.sidebar.header("🔍 Filtros")
    
    # -------------------------------------------------------------------------
    # FILTRO DE PERÍODO (ANO)
    # -------------------------------------------------------------------------
    
    # Extrair anos únicos disponíveis nos dados e ordenar
    anos_disponiveis = sorted(df['ano'].unique())
    # Selectbox para escolha única do período de análise
    ano_selecionado = st.sidebar.selectbox(
        "📅 Período",                                      # Rótulo com ícone
        options=anos_disponiveis,                         # Opções disponíveis
        index=len(anos_disponiveis)-1 if anos_disponiveis else 0,  # Último ano como padrão
        help="Selecione o ano para análise"               # Tooltip de ajuda
    )
    
    # -------------------------------------------------------------------------
    # FILTRO DE CATEGORIAS
    # -------------------------------------------------------------------------
    
    # Extrair categorias únicas e ordenar alfabeticamente
    categorias_disponiveis = sorted(df['categoria'].unique())
    # Multiselect permite seleção múltipla de categorias
    categorias_selecionadas = st.sidebar.multiselect(
        "📂 Categorias",                                  # Rótulo com ícone
        options=categorias_disponiveis,                   # Todas as categorias
        default=categorias_disponiveis,                   # Todas selecionadas por padrão
        help="Selecione uma ou mais categorias"          # Tooltip explicativo
    )
    
    # -------------------------------------------------------------------------
    # FILTRO DE STATUS
    # -------------------------------------------------------------------------
    
    # Extrair status únicos e ordenar alfabeticamente
    status_disponiveis = sorted(df['status'].unique())
    # Multiselect para seleção múltipla de status
    # Multiselect para seleção múltipla de status
    status_selecionados = st.sidebar.multiselect(
        "📋 Status",                                      # Rótulo com ícone
        options=status_disponiveis,                       # Todos os status
        default=status_disponiveis,                       # Todos selecionados por padrão
        help="Selecione um ou mais status"                # Tooltip explicativo
    )
    
    # =============================================================================
    # APLICAÇÃO DE FILTROS AOS DADOS
    # =============================================================================
    
    # Organizar filtros selecionados em dicionário estruturado
    filtros = {
        'periodo': ano_selecionado,                       # Ano selecionado
        'categorias': categorias_selecionadas,            # Lista de categorias
        'status': status_selecionados                     # Lista de status
    }
    
    # Aplicar filtros aos dados usando função específica
    df_filtrado = filtrar_dados_exemplo(df, filtros)
    
    # Validação crítica: verificar se ainda há dados após filtragem
    if df_filtrado.empty:
        # Avisar usuário sobre filtros muito restritivos
        st.warning("⚠️ Nenhum dado encontrado para os filtros selecionados.")
        st.info("Tente ajustar os filtros na barra lateral.")
        return  # Interromper execução se não há dados filtrados
    
    # =============================================================================
    # CÁLCULO DE INDICADORES PRINCIPAIS
    # =============================================================================
    
    # Processar dados filtrados para extrair KPIs essenciais
    indicadores = calcular_indicadores_exemplo(df_filtrado)
    
    # =============================================================================
    # EXIBIÇÃO DE KPIs PRINCIPAIS
    # =============================================================================
    
    # Criar seção de indicadores principais com título
    st.subheader("📈 Indicadores Principais")
    
    # Layout responsivo: 4 colunas para métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    # -------------------------------------------------------------------------
    # KPI 1: TOTAL DE REGISTROS
    # -------------------------------------------------------------------------
    with col1:
        criar_card_metrica(
            "Total de Registros",                         # Título da métrica
            formatar_numero(indicadores['total_registros']),  # Valor formatado
            "📊"                                          # Ícone representativo
        )
    
    # -------------------------------------------------------------------------
    # KPI 2: VALOR TOTAL MONETÁRIO
    # -------------------------------------------------------------------------
    with col2:
        criar_card_metrica(
            "Valor Total",                                # Título da métrica
            f"R$ {formatar_numero(indicadores['valor_total'])}",  # Valor em reais
            "💰"                                          # Ícone de dinheiro
        )
    
    # -------------------------------------------------------------------------
    # KPI 3: VALOR MÉDIO POR REGISTRO
    # -------------------------------------------------------------------------
    with col3:
        criar_card_metrica(
            "Média por Registro",                         # Título da métrica
            f"R$ {formatar_numero(indicadores['media_valor'])}",  # Média formatada
            "📊"                                          # Ícone de estatística
        )
    
    # -------------------------------------------------------------------------
    # KPI 4: CRESCIMENTO MENSAL (COM INDICADOR VISUAL)
    # -------------------------------------------------------------------------
    with col4:
        # Determinar ícone baseado em crescimento positivo/negativo
        icone_crescimento = "📈" if indicadores['crescimento_mensal'] >= 0 else "📉"
        criar_card_metrica(
            "Crescimento Mensal",                         # Título da métrica
            f"{indicadores['crescimento_mensal']:.1f}%",  # Percentual com 1 decimal
            icone_crescimento                             # Ícone dinâmico
        )
    
    # Separador visual entre seções
    st.markdown("---")
    
    # =============================================================================
    # VISUALIZAÇÕES PRINCIPAIS
    # =============================================================================
    
    # -------------------------------------------------------------------------
    # PRIMEIRA LINHA: GRÁFICOS TEMPORAIS E CATEGÓRICOS
    # -------------------------------------------------------------------------
    
    # Layout responsivo: 2 colunas para gráficos lado a lado
    col1, col2 = st.columns(2)
    
    # Gráfico de evolução temporal na primeira coluna
    with col1:
        st.subheader("📈 Evolução Temporal")
        # Criar e exibir gráfico de linha com evolução mensal
        fig_evolucao = criar_grafico_evolucao_temporal(df_filtrado)
        # use_container_width=True torna gráfico responsivo
        st.plotly_chart(fig_evolucao, use_container_width=True)
    
    # Gráfico de distribuição por categoria na segunda coluna
    with col2:
        st.subheader("📊 Distribuição por Categoria")
        # Criar e exibir gráfico de barras horizontais
        fig_categoria = criar_grafico_distribuicao_categoria(df_filtrado)
        st.plotly_chart(fig_categoria, use_container_width=True)
    
    # -------------------------------------------------------------------------
    # SEGUNDA LINHA: GRÁFICO DE PIZZA E TABELA DETALHADA
    # -------------------------------------------------------------------------
    
    # Layout responsivo: 2 colunas com proporção igual
    col1, col2 = st.columns([1, 1])
    
    # Gráfico de pizza na primeira coluna
    with col1:
        st.subheader("🎯 Distribuição por Status")
        # Criar e exibir gráfico de pizza para status
        fig_status = criar_grafico_status_pizza(df_filtrado)
        st.plotly_chart(fig_status, use_container_width=True)
    
    # Tabela detalhada na segunda coluna
    with col2:
        st.subheader("📋 Dados Detalhados")
        
        # Criar tabela resumo com múltiplas agregações
        # Agrupar por categoria e status para análise cruzada
        df_resumo = df_filtrado.groupby(['categoria', 'status']).agg({
            'valor': ['sum', 'mean', 'count'],   # Soma, média e contagem de valores
            'quantidade': 'sum'                  # Soma das quantidades
        }).round(2)  # Arredondar para 2 casas decimais
        
        # Renomear colunas para melhor legibilidade
        df_resumo.columns = ['Valor Total', 'Valor Médio', 'Registros', 'Quantidade Total']
        df_resumo = df_resumo.reset_index()  # Transformar índices em colunas
        
        # Exibir tabela interativa responsiva
        st.dataframe(df_resumo, use_container_width=True)
    
    # =============================================================================
    # INFORMAÇÕES COMPLEMENTARES
    # =============================================================================
    
    # Separador visual para seção final
    st.markdown("---")
    
    # Exibir rodapé padrão com informações de fonte e atualização
    exibir_info_atualizacao(FONTE_DADOS)
    
    # -------------------------------------------------------------------------
    # SEÇÃO EXPANSÍVEL COM INFORMAÇÕES TÉCNICAS DETALHADAS
    # -------------------------------------------------------------------------
    
    # Expander oculta informações técnicas para não poluir interface
    with st.expander("ℹ️ Informações Técnicas"):
        # Layout em 2 colunas para organizar informações
        col1, col2 = st.columns(2)
        
        # Coluna 1: Informações temporais e quantitativas
        with col1:
            st.write("**Período dos dados:**")
            # Formatar datas em formato brasileiro (dd/mm/yyyy)
            data_inicio = df['data'].min().strftime('%d/%m/%Y')
            data_fim = df['data'].max().strftime('%d/%m/%Y')
            st.write(f"De {data_inicio} até {data_fim}")
            
            st.write("**Total de registros:**")
            # Mostrar volume total de dados disponíveis
            st.write(f"{len(df)} registros no dataset completo")
        
        # Coluna 2: Informações categóricas e estruturais
        with col2:
            st.write("**Categorias disponíveis:**")
            # Listar todas as categorias únicas ordenadas
            for categoria in sorted(df['categoria'].unique()):
                st.write(f"• {categoria}")
            
            st.write("**Status possíveis:**")
            # Listar todos os status únicos ordenados
            for status in sorted(df['status'].unique()):
                st.write(f"• {status}")

# =============================================================================
# PONTO DE ENTRADA PARA EXECUÇÃO INDEPENDENTE
# =============================================================================

if __name__ == "__main__":
    """
    Ponto de entrada para execução independente do módulo.
    
    Este bloco permite executar o módulo de forma standalone,
    facilitando desenvolvimento, testes e debug sem depender
    do sistema principal do dashboard IFPB-CZ.
    
    COMANDO PARA EXECUÇÃO:
    ---------------------
    streamlit run modules/new_modulo_exemplo.py
    
    UTILIDADE:
    ----------
    - Desenvolvimento isolado do módulo
    - Testes de funcionalidade específica
    - Debug de visualizações e lógica
    - Demonstração independente para stakeholders
    """
    # -------------------------------------------------------------------------
    # CONFIGURAÇÃO DA PÁGINA PARA EXECUÇÃO STANDALONE
    # -------------------------------------------------------------------------
    
    # Configurar metadados e layout da página Streamlit
    st.set_page_config(
        page_title=f"Dashboard {NOME_MODULO} - IFPB-CZ",  # Título da aba do navegador
        page_icon="📊",                                     # Ícone da aba
        layout="wide",                                      # Layout amplo para dashboards
        initial_sidebar_state="expanded"                    # Sidebar aberta por padrão
    )
    
    # Executar função principal do dashboard
    mostrar_dashboard_exemplo()
