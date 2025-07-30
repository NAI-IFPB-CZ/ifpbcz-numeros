# ==============================================================================
# MÓDULO DE PESQUISA - SISTEMA DASHBOARD IFPB-CZ
# ==============================================================================
"""
Módulo responsável pela análise e visualização de dados de pesquisa científica.

FUNCIONALIDADES PRINCIPAIS:
• Indicadores de publicações científicas (artigos, capítulos, trabalhos em eventos)
• Análise temporal da evolução das publicações
• Distribuição por área de conhecimento
• Visualizações interativas (gráficos de barras, pizza, linha)
• Nuvem de palavras para análise de palavras-chave
• Filtros dinâmicos por ano, tipo de publicação e unidade

DADOS PROCESSADOS:
• Artigos publicados em periódicos
• Capítulos de livros publicados
• Trabalhos apresentados em eventos científicos
• Distribuição por área de conhecimento
• Palavras-chave das publicações

VISUALIZAÇÕES GERADAS:
• KPIs principais de produção científica
• Gráficos de distribuição por tipo de publicação
• Evolução temporal das publicações
• Análise por área de conhecimento
• Seções expandíveis por tipo específico

TECNOLOGIAS UTILIZADAS:
• Streamlit para interface web
• Plotly para gráficos interativos
• WordCloud para nuvem de palavras
• Pandas para manipulação de dados
• Matplotlib para visualizações especiais
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from .utils import display_header_with_logo, display_footer

def pesquisa_module(data_gen):
    """
    Módulo principal de análise de pesquisa científica.
    
    Este módulo processa e visualiza dados de produção científica do IFPB-CZ,
    incluindo artigos, capítulos de livros e trabalhos em eventos.
    
    Args:
        data_gen: Gerador de dados para obtenção das informações de pesquisa
    
    Returns:
        None: Renderiza a interface Streamlit com as visualizações
    """
    
    # ==============================================================================
    # INICIALIZAÇÃO E CONFIGURAÇÃO
    # ==============================================================================
    
    # Exibir cabeçalho institucional com logo
    display_header_with_logo("Pesquisa")
    
    # ==============================================================================
    # CARREGAMENTO E VALIDAÇÃO DOS DADOS
    # ==============================================================================
    
    # Gerar dados de pesquisa (real ou simulado conforme configuração)
    dados_pesquisa = data_gen.gerar_dados_pesquisa()
    
    # Verificar se os dados foram carregados corretamente
    if dados_pesquisa is None or dados_pesquisa.empty:
        st.error("Erro ao gerar dados de pesquisa. Verifique o arquivo de dados.")
        return
    
    # Definir colunas obrigatórias para funcionamento do módulo
    required_columns = ['ano', 'tipo_publicacao', 'quantidade', 'area_conhecimento']
    missing_columns = [col for col in required_columns if col not in dados_pesquisa.columns]
    
    # Validar estrutura dos dados
    if missing_columns:
        st.error(f"Colunas ausentes nos dados: {missing_columns}")
        st.write(f"Colunas disponíveis: {list(dados_pesquisa.columns)}")
        return
    
    # ==============================================================================
    # PREPARAÇÃO DOS DADOS PARA ANÁLISE
    # ==============================================================================
    
    # Filtrar dados para o ano atual (2025) como base para KPIs
    dados_2025 = dados_pesquisa[dados_pesquisa['ano'] == 2025]
    
    # Verificar disponibilidade de dados para 2025
    if dados_2025.empty:
        st.warning("Nenhum dado encontrado para 2025.")
        # Usar dados do ano mais recente como fallback
        ano_mais_recente = dados_pesquisa['ano'].max()
        dados_2025 = dados_pesquisa[dados_pesquisa['ano'] == ano_mais_recente]
        st.info(f"Usando dados de {ano_mais_recente} como referência.")
    
    # ==============================================================================
    # CÁLCULO DOS KPIS PRINCIPAIS
    # ==============================================================================
    
    # KPI 1: Total de artigos publicados em periódicos
    artigos_publicados = dados_2025[dados_2025['tipo_publicacao'] == 'Artigos']['quantidade'].sum()
    
    # KPI 2: Total de capítulos de livros publicados
    capitulos_livros = dados_2025[dados_2025['tipo_publicacao'] == 'Capítulos de Livros']['quantidade'].sum()
    
    # KPI 3: Total de trabalhos apresentados em eventos científicos
    trabalhos_eventos = dados_2025[dados_2025['tipo_publicacao'] == 'Trabalhos em Eventos']['quantidade'].sum()
    
    # ==============================================================================
    # EXIBIÇÃO DOS KPIS PRINCIPAIS
    # ==============================================================================
    
    # Cartões de KPI para indicadores principais
    st.markdown("### 📊 Indicadores Principais")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Layout em 3 colunas para os KPIs
    col1, col2, col3 = st.columns(3)
    
    # KPI Card 1: Artigos Publicados
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ARTIGOS PUBLICADOS</div>
            <div class="kpi-value">{artigos_publicados:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI Card 2: Capítulos de Livros
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">CAPÍTULOS DE LIVROS</div>
            <div class="kpi-value">{capitulos_livros:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI Card 3: Trabalhos em Eventos
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TRABALHOS EM EVENTOS</div>
            <div class="kpi-value">{trabalhos_eventos:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Separadores visuais
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # ==============================================================================
    # GRÁFICO 1: PUBLICAÇÕES POR TIPO
    # ==============================================================================
    
    # Gráfico 1: Publicações por Tipo com múltiplos modos de visualização
    st.markdown("### 📊 Análise de Publicações")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("Publicações por Tipo")
    
    # Controles de filtro em duas colunas
    col1, col2 = st.columns(2)
    
    # Seletor de modo de exibição (Pizza, Barras, Nuvem de Palavras)
    with col1:
        modo_grafico = st.selectbox(
            "📊 Modo de Exibição:",
            ["Pizza", "Barras", "Nuvem de Palavras"],
            key="modo_grafico"
        )
    
    # Seletor de ano para análise
    with col2:
        ano_selecionado = st.selectbox(
            "📅 Ano:",
            sorted(dados_pesquisa['ano'].unique(), reverse=True),
            key="ano_publicacoes"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Filtrar e agrupar dados por tipo de publicação
    dados_filtrados = dados_pesquisa[dados_pesquisa['ano'] == ano_selecionado]
    dados_grafico = dados_filtrados.groupby('tipo_publicacao')['quantidade'].sum().reset_index()
    
    # Criar gráfico baseado no modo selecionado pelo usuário
    if modo_grafico == "Pizza":
        # Modo Pizza: Gráfico de setores para distribuição percentual
        fig = px.pie(
            dados_grafico,
            values='quantidade',
            names='tipo_publicacao',
            title=f"Distribuição de Publicações por Tipo - {ano_selecionado}",
            color_discrete_sequence=['#1a8c73', '#0d5a4e', '#4CAF50']  # Paleta verde institucional
        )
        fig.update_layout(height=400)
        fig.update_traces(
            textposition='inside',     # Texto dentro das fatias
            textinfo='percent+label'   # Mostrar percentual e rótulo
        )
        
    elif modo_grafico == "Barras":
        # Modo Barras: Gráfico de barras para comparação quantitativa
        fig = px.bar(
            dados_grafico,
            x='tipo_publicacao',
            y='quantidade',
            title=f"Publicações por Tipo - {ano_selecionado}",
            color_discrete_sequence=['#1a8c73'],  # Cor institucional IFPB
            text='quantidade'
        )
        fig.update_layout(
            xaxis_title="Tipo de Publicação",
            yaxis_title="Quantidade",
            height=400,
            showlegend=False
        )
        fig.update_traces(textposition='outside')  # Valores acima das barras
        
    else:  # modo_grafico == "Nuvem de Palavras"
        # Modo Nuvem de Palavras: Visualização textual baseada em frequência
        if not dados_grafico.empty:
            # Criar dados para nuvem de palavras baseada na quantidade
            text_data = []
            for _, row in dados_grafico.iterrows():
                # Repetir tipo de publicação proporcionalmente à quantidade
                text_data.extend([row['tipo_publicacao']] * int(row['quantidade']))
            
            # Gerar nuvem de palavras se há dados suficientes
            if text_data:
                wordcloud = WordCloud(
                    width=800,
                    height=400,
                    background_color='white',
                    colormap='Greens'  # Paleta verde institucional
                ).generate(' '.join(text_data))
                
                # Criar figura matplotlib para a nuvem
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')  # Remover eixos
                ax.set_title(f"Nuvem de Palavras - Publicações {ano_selecionado}")
                st.pyplot(fig)
            else:
                st.info("Não há dados suficientes para gerar a nuvem de palavras.")
        else:
            st.info("Não há dados para o ano selecionado.")
    
    # Renderizar gráfico (exceto para nuvem de palavras que já foi renderizada)
    if modo_grafico != "Nuvem de Palavras":
        st.plotly_chart(fig, use_container_width=True)
    
    # Fonte dos dados
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: Plataforma Lattes</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==============================================================================
    # GRÁFICO 2: EVOLUÇÃO TEMPORAL DAS PUBLICAÇÕES
    # ==============================================================================
    
    # Gráfico 2: Evolução das Publicações ao longo do tempo
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução Temporal das Publicações")
    
    # Filtro para seleção de tipo de publicação específico ou todos
    tipo_publicacao_evolucao = st.selectbox(
        "📄 Tipo de Publicação:",
        ["Todos"] + list(dados_pesquisa['tipo_publicacao'].unique()),
        key="tipo_evolucao"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Filtrar e agrupar dados para evolução temporal
    if tipo_publicacao_evolucao == "Todos":
        # Agrupar todos os tipos de publicação por ano
        dados_evolucao = dados_pesquisa.groupby('ano')['quantidade'].sum().reset_index()
        titulo_evolucao = "Evolução das Publicações - Todos os Tipos"
    else:
        # Filtrar tipo específico e agrupar por ano
        dados_evolucao = dados_pesquisa[dados_pesquisa['tipo_publicacao'] == tipo_publicacao_evolucao]
        dados_evolucao = dados_evolucao.groupby('ano')['quantidade'].sum().reset_index()
        titulo_evolucao = f"Evolução das Publicações - {tipo_publicacao_evolucao}"
    
    # Criar gráfico de linha para mostrar evolução temporal
    fig2 = px.line(
        dados_evolucao,
        x='ano',
        y='quantidade',
        title=titulo_evolucao,
        markers=True,  # Adicionar marcadores nos pontos
        color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
    )
    
    # Personalizar layout do gráfico de evolução
    fig2.update_layout(
        xaxis_title="Ano",
        yaxis_title="Quantidade",
        height=400,
        showlegend=False
    )
    
    # Adicionar valores nos pontos da linha
    fig2.update_traces(
        mode='lines+markers+text',  # Linha com marcadores e texto
        textposition='top center',   # Posição do texto acima dos pontos
        texttemplate='%{y}'         # Template para exibir o valor de y
    )
    
    # Renderizar gráfico de evolução temporal
    st.plotly_chart(fig2, use_container_width=True)
    
    # Fonte dos dados
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: Plataforma Lattes</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==============================================================================
    # GRÁFICO 3: ANÁLISE POR ÁREA DE CONHECIMENTO
    # ==============================================================================
    
    # Gráfico 3: Produção por Área de Conhecimento com seleção múltipla de anos
    st.markdown("### 📊 Análise por Área de Conhecimento")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("Produção por Área de Conhecimento")
    
    # Controles de filtro em três colunas
    col1, col2, col3 = st.columns(3)
    
    # Seletor múltiplo de anos
    with col1:
        anos_selecionados = st.multiselect(
            "📅 Selecione os Anos:",
            sorted(dados_pesquisa['ano'].unique(), reverse=True),
            default=[dados_pesquisa['ano'].max()],  # Ano mais recente como padrão
            key="anos_area"
        )
    
    # Filtro de tipo de publicação
    with col2:
        tipo_area = st.selectbox(
            "📄 Tipo de Publicação:",
            ["Todos"] + list(dados_pesquisa['tipo_publicacao'].unique()),
            key="tipo_area"
        )
    
    # Modo de exibição dos dados
    with col3:
        modo_exibicao = st.selectbox(
            "📊 Modo de Exibição:",
            ["Por Ano", "Total Acumulado"],
            key="modo_area"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Verificar se pelo menos um ano foi selecionado
    if not anos_selecionados:
        st.warning("Selecione pelo menos um ano para visualizar os dados.")
    else:
        # Filtrar dados pelos anos selecionados
        dados_area = dados_pesquisa[dados_pesquisa['ano'].isin(anos_selecionados)]
        
        # Aplicar filtro de tipo de publicação se especificado
        if tipo_area != "Todos":
            dados_area = dados_area[dados_area['tipo_publicacao'] == tipo_area]
        
        # Gerar visualização baseada no modo selecionado
        if modo_exibicao == "Por Ano":
            # Mostrar evolução por ano com agrupamento duplo
            dados_grafico_area = dados_area.groupby(['ano', 'area_conhecimento'])['quantidade'].sum().reset_index()
            
            # Criar gráfico de barras agrupadas por ano
            fig_area = px.bar(
                dados_grafico_area,
                x='area_conhecimento',
                y='quantidade',
                color='ano',  # Agrupar barras por ano
                title=f"Evolução da Produção por Área de Conhecimento ({min(anos_selecionados)}-{max(anos_selecionados)})",
                color_discrete_sequence=px.colors.qualitative.Set3,  # Paleta de cores variadas
                barmode='group'  # Barras agrupadas lado a lado
            )
            
            # Personalizar layout do gráfico agrupado
            fig_area.update_layout(
                xaxis_title="Área de Conhecimento",
                yaxis_title="Quantidade",
                xaxis_tickangle=-45,  # Rotacionar labels para melhor legibilidade
                height=500,
                legend_title="Ano"
            )
            
        else:  # modo_exibicao == "Total Acumulado"
            # Mostrar total acumulado para o período selecionado
            dados_grafico_area = dados_area.groupby('area_conhecimento')['quantidade'].sum().reset_index()
            
            # Criar gráfico de barras simples com total acumulado
            fig_area = px.bar(
                dados_grafico_area,
                x='area_conhecimento',
                y='quantidade',
                title=f"Produção Acumulada por Área de Conhecimento ({min(anos_selecionados)}-{max(anos_selecionados)})",
                color_discrete_sequence=['#1a8c73'],  # Cor institucional IFPB
                text='quantidade'
            )
            
            # Personalizar layout do gráfico acumulado
            fig_area.update_layout(
                xaxis_title="Área de Conhecimento",
                yaxis_title="Quantidade Total",
                xaxis_tickangle=-45,  # Rotacionar labels para melhor legibilidade
                height=450,
                showlegend=False
            )
            
            # Posicionar valores nas barras
            fig_area.update_traces(textposition='outside')
        
        # Renderizar gráfico principal de área de conhecimento
        st.plotly_chart(fig_area, use_container_width=True)
        
        # Adicionar gráfico de linha complementar para evolução temporal (quando múltiplos anos)
        if len(anos_selecionados) > 1:
            st.subheader("📈 Evolução Temporal por Área de Conhecimento")
            
            # Dados para o gráfico de linhas temporal
            dados_linha = dados_area.groupby(['ano', 'area_conhecimento'])['quantidade'].sum().reset_index()
            
            # Criar gráfico de linha para mostrar tendências
            fig_linha = px.line(
                dados_linha,
                x='ano',
                y='quantidade',
                color='area_conhecimento',  # Linha diferente para cada área
                title="Evolução Temporal da Produção por Área",
                markers=True,  # Adicionar marcadores nos pontos
                color_discrete_sequence=px.colors.qualitative.Set3  # Paleta de cores variadas
            )
            
            # Personalizar layout do gráfico de linha
            fig_linha.update_layout(
                xaxis_title="Ano",
                yaxis_title="Quantidade",
                height=400,
                legend_title="Área de Conhecimento"
            )
            
            # Renderizar gráfico de evolução temporal
            st.plotly_chart(fig_linha, use_container_width=True)
    
    # Fonte dos dados
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: Plataforma Lattes</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==============================================================================
    # SEÇÕES EXPANDÍVEIS POR TIPO DE PUBLICAÇÃO
    # ==============================================================================
    
    # Seções expandíveis detalhadas para cada tipo de publicação
    tipos_publicacao = dados_pesquisa['tipo_publicacao'].unique()
    
    # Iterar por cada tipo de publicação para criar seções detalhadas
    for tipo in tipos_publicacao:
        # Criar seção expandível (artigos expandido por padrão)
        with st.expander(f"📚 {tipo}", expanded=(tipo == "Artigos")):
            
            # Controles de filtro em duas colunas
            col1, col2 = st.columns(2)
            
            # Seletor de ano específico para o tipo
            with col1:
                ano_selecionado = st.selectbox(
                    "Ano:",
                    sorted(dados_pesquisa['ano'].unique(), reverse=True),
                    key=f"ano_{tipo}"
                )
            
            # Seletor de forma de exibição
            with col2:
                forma_exibicao = st.radio(
                    "Forma de exibição:",
                    ["Publicados no ano", "Evolução", "Nuvem de palavras"],
                    key=f"forma_{tipo}"
                )
            
            # Filtrar dados específicos do tipo de publicação
            dados_tipo = dados_pesquisa[dados_pesquisa['tipo_publicacao'] == tipo]
            
            # Gerar visualização baseada na forma selecionada
            if forma_exibicao == "Publicados no ano":
                # Modo 1: Gráfico de barras por unidade para o ano selecionado
                dados_filtrados = dados_tipo[dados_tipo['ano'] == ano_selecionado]
                dados_grafico = dados_filtrados.groupby('unidade')['quantidade'].sum().reset_index()
                
                # Criar gráfico de barras por unidade
                fig = px.bar(
                    dados_grafico,
                    x='unidade',
                    y='quantidade',
                    title=f"{tipo} por Unidade - {ano_selecionado}",
                    color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
                )
                
                # Personalizar layout do gráfico por unidade
                fig.update_layout(
                    xaxis_title="Unidade",
                    yaxis_title="Quantidade",
                    xaxis_tickangle=-45,  # Rotacionar labels
                    height=400
                )
                
                # Renderizar gráfico por unidade
                st.plotly_chart(fig, use_container_width=True)
                
            elif forma_exibicao == "Evolução":
                # Modo 2: Gráfico de linha evolutiva temporal
                dados_evolucao = dados_tipo.groupby('ano')['quantidade'].sum().reset_index()
                
                # Criar gráfico de linha para evolução temporal
                fig = px.line(
                    dados_evolucao,
                    x='ano',
                    y='quantidade',
                    title=f"Evolução de {tipo}",
                    markers=True,  # Adicionar marcadores nos pontos
                    color_discrete_sequence=['#1a8c73']  # Cor institucional IFPB
                )
                
                # Personalizar layout do gráfico de evolução
                fig.update_layout(
                    xaxis_title="Ano",
                    yaxis_title="Quantidade",
                    height=400
                )
                
                # Renderizar gráfico de evolução
                st.plotly_chart(fig, use_container_width=True)
                
            else:  # forma_exibicao == "Nuvem de palavras"
                # Modo 3: Nuvem de palavras baseada em palavras-chave
                dados_filtrados = dados_tipo[dados_tipo['ano'] == ano_selecionado]
                
                # Verificar se há dados para processar
                if not dados_filtrados.empty:
                    # Coletar todas as palavras-chave do tipo e ano selecionados
                    todas_palavras = []
                    for _, row in dados_filtrados.iterrows():
                        # Verificar se a coluna palavras_chave existe e não é nula
                        if pd.notna(row['palavras_chave']):
                            palavras = row['palavras_chave'].split(', ')
                            # Repetir palavras proporcionalmente à quantidade
                            todas_palavras.extend(palavras * int(row['quantidade']))
                    
                    # Gerar nuvem de palavras se há palavras suficientes
                    if todas_palavras:
                        wordcloud = WordCloud(
                            width=800,
                            height=400,
                            background_color='white',
                            colormap='Greens',  # Paleta verde institucional
                            max_words=100,      # Máximo de palavras a exibir
                            relative_scaling=0.5,  # Escala relativa dos tamanhos
                            min_font_size=10    # Tamanho mínimo da fonte
                        ).generate(' '.join(todas_palavras))
                        
                        # Criar figura matplotlib para a nuvem
                        fig, ax = plt.subplots(figsize=(10, 5))
                        ax.imshow(wordcloud, interpolation='bilinear')
                        ax.axis('off')  # Remover eixos
                        ax.set_title(f"Nuvem de Palavras - {tipo} - {ano_selecionado}", fontsize=16, pad=20)
                        
                        # Renderizar nuvem de palavras
                        st.pyplot(fig)
                    else:
                        st.info("Não há palavras-chave suficientes para gerar a nuvem de palavras.")
                else:
                    st.info("Não há dados para o ano selecionado.")
            
            # Fonte dos dados para seção específica
            st.markdown('<div class="fonte-dados">Fonte de Dados: Plataforma Lattes</div>', unsafe_allow_html=True)
    
    # ==============================================================================
    # RODAPÉ DO SISTEMA
    # ==============================================================================
    
    # Rodapé com informações institucionais
    display_footer()
