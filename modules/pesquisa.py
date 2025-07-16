import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from .utils import display_header_with_logo, display_footer

def pesquisa_module(data_gen):
    """Módulo de Pesquisa"""
    
    # Cabeçalho com logo
    display_header_with_logo("Pesquisa")
    
    # Gerar dados
    dados_pesquisa = data_gen.gerar_dados_pesquisa()
    
    # Verificar se os dados foram gerados corretamente
    if dados_pesquisa is None or dados_pesquisa.empty:
        st.error("Erro ao gerar dados de pesquisa. Verifique o arquivo de dados.")
        return
    
    # Verificar se as colunas necessárias existem
    required_columns = ['ano', 'tipo_publicacao', 'quantidade', 'area_conhecimento']
    missing_columns = [col for col in required_columns if col not in dados_pesquisa.columns]
    
    if missing_columns:
        st.error(f"Colunas ausentes nos dados: {missing_columns}")
        st.write(f"Colunas disponíveis: {list(dados_pesquisa.columns)}")
        return
    
    # Filtrar dados para 2025
    dados_2025 = dados_pesquisa[dados_pesquisa['ano'] == 2025]
    
    # Verificar se existem dados para 2025
    if dados_2025.empty:
        st.warning("Nenhum dado encontrado para 2025.")
        # Usar dados do ano mais recente disponível
        ano_mais_recente = dados_pesquisa['ano'].max()
        dados_2025 = dados_pesquisa[dados_pesquisa['ano'] == ano_mais_recente]
        st.info(f"Usando dados de {ano_mais_recente} como referência.")
    
    # Calcular KPIs
    artigos_publicados = dados_2025[dados_2025['tipo_publicacao'] == 'Artigos']['quantidade'].sum()
    capitulos_livros = dados_2025[dados_2025['tipo_publicacao'] == 'Capítulos de Livros']['quantidade'].sum()
    trabalhos_eventos = dados_2025[dados_2025['tipo_publicacao'] == 'Trabalhos em Eventos']['quantidade'].sum()
    
    # Cartões de KPI
    st.markdown("### 📊 Indicadores Principais")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ARTIGOS PUBLICADOS</div>
            <div class="kpi-value">{artigos_publicados:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">CAPÍTULOS DE LIVROS</div>
            <div class="kpi-value">{capitulos_livros:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TRABALHOS EM EVENTOS</div>
            <div class="kpi-value">{trabalhos_eventos:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Gráfico 1: Publicações por Tipo
    st.markdown("### 📊 Análise de Publicações")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("Publicações por Tipo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        modo_grafico = st.selectbox(
            "📊 Modo de Exibição:",
            ["Pizza", "Barras", "Nuvem de Palavras"],
            key="modo_grafico"
        )
    
    with col2:
        ano_selecionado = st.selectbox(
            "📅 Ano:",
            sorted(dados_pesquisa['ano'].unique(), reverse=True),
            key="ano_publicacoes"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Filtrar dados
    dados_filtrados = dados_pesquisa[dados_pesquisa['ano'] == ano_selecionado]
    dados_grafico = dados_filtrados.groupby('tipo_publicacao')['quantidade'].sum().reset_index()
    
    # Criar gráfico baseado no modo selecionado
    if modo_grafico == "Pizza":
        fig = px.pie(
            dados_grafico,
            values='quantidade',
            names='tipo_publicacao',
            title=f"Distribuição de Publicações por Tipo - {ano_selecionado}",
            color_discrete_sequence=['#1a8c73', '#0d5a4e', '#4CAF50']
        )
        fig.update_layout(height=400)
        fig.update_traces(textposition='inside', textinfo='percent+label')
    elif modo_grafico == "Barras":
        fig = px.bar(
            dados_grafico,
            x='tipo_publicacao',
            y='quantidade',
            title=f"Publicações por Tipo - {ano_selecionado}",
            color_discrete_sequence=['#1a8c73'],
            text='quantidade'
        )
        fig.update_layout(
            xaxis_title="Tipo de Publicação",
            yaxis_title="Quantidade",
            height=400,
            showlegend=False
        )
        fig.update_traces(textposition='outside')
    else:  # Nuvem de palavras
        if not dados_grafico.empty:
            # Criar dados para nuvem de palavras
            text_data = []
            for _, row in dados_grafico.iterrows():
                text_data.extend([row['tipo_publicacao']] * int(row['quantidade']))
            
            if text_data:
                wordcloud = WordCloud(
                    width=800,
                    height=400,
                    background_color='white',
                    colormap='Greens'
                ).generate(' '.join(text_data))
                
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                ax.set_title(f"Nuvem de Palavras - Publicações {ano_selecionado}")
                st.pyplot(fig)
            else:
                st.info("Não há dados suficientes para gerar a nuvem de palavras.")
        else:
            st.info("Não há dados para o ano selecionado.")
    
    if modo_grafico != "Nuvem de Palavras":
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: Plataforma Lattes</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gráfico 2: Evolução das Publicações
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução Temporal das Publicações")
    
    tipo_publicacao_evolucao = st.selectbox(
        "📄 Tipo de Publicação:",
        ["Todos"] + list(dados_pesquisa['tipo_publicacao'].unique()),
        key="tipo_evolucao"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Filtrar dados para evolução
    if tipo_publicacao_evolucao == "Todos":
        dados_evolucao = dados_pesquisa.groupby('ano')['quantidade'].sum().reset_index()
        titulo_evolucao = "Evolução das Publicações - Todos os Tipos"
    else:
        dados_evolucao = dados_pesquisa[dados_pesquisa['tipo_publicacao'] == tipo_publicacao_evolucao]
        dados_evolucao = dados_evolucao.groupby('ano')['quantidade'].sum().reset_index()
        titulo_evolucao = f"Evolução das Publicações - {tipo_publicacao_evolucao}"
    
    fig2 = px.line(
        dados_evolucao,
        x='ano',
        y='quantidade',
        title=titulo_evolucao,
        markers=True,
        color_discrete_sequence=['#1a8c73']
    )
    
    fig2.update_layout(
        xaxis_title="Ano",
        yaxis_title="Quantidade",
        height=400,
        showlegend=False
    )
    
    fig2.update_traces(
        mode='lines+markers+text',
        textposition='top center',
        texttemplate='%{y}'
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: Plataforma Lattes</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gráfico 3: Produção por Área de Conhecimento com seleção múltipla de anos
    st.markdown("### 📊 Análise por Área de Conhecimento")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("Produção por Área de Conhecimento")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        anos_selecionados = st.multiselect(
            "📅 Selecione os Anos:",
            sorted(dados_pesquisa['ano'].unique(), reverse=True),
            default=[dados_pesquisa['ano'].max()],
            key="anos_area"
        )
    
    with col2:
        tipo_area = st.selectbox(
            "📄 Tipo de Publicação:",
            ["Todos"] + list(dados_pesquisa['tipo_publicacao'].unique()),
            key="tipo_area"
        )
    
    with col3:
        modo_exibicao = st.selectbox(
            "📊 Modo de Exibição:",
            ["Por Ano", "Total Acumulado"],
            key="modo_area"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Verificar se há anos selecionados
    if not anos_selecionados:
        st.warning("Selecione pelo menos um ano para visualizar os dados.")
    else:
        # Filtrar dados
        dados_area = dados_pesquisa[dados_pesquisa['ano'].isin(anos_selecionados)]
        
        if tipo_area != "Todos":
            dados_area = dados_area[dados_area['tipo_publicacao'] == tipo_area]
        
        if modo_exibicao == "Por Ano":
            # Mostrar evolução por ano
            dados_grafico_area = dados_area.groupby(['ano', 'area_conhecimento'])['quantidade'].sum().reset_index()
            
            fig_area = px.bar(
                dados_grafico_area,
                x='area_conhecimento',
                y='quantidade',
                color='ano',
                title=f"Evolução da Produção por Área de Conhecimento ({min(anos_selecionados)}-{max(anos_selecionados)})",
                color_discrete_sequence=px.colors.qualitative.Set3,
                barmode='group'
            )
            
            fig_area.update_layout(
                xaxis_title="Área de Conhecimento",
                yaxis_title="Quantidade",
                xaxis_tickangle=-45,
                height=500,
                legend_title="Ano"
            )
        else:  # modo_exibicao == "Total Acumulado"
            # Mostrar total acumulado
            dados_grafico_area = dados_area.groupby('area_conhecimento')['quantidade'].sum().reset_index()
            
            fig_area = px.bar(
                dados_grafico_area,
                x='area_conhecimento',
                y='quantidade',
                title=f"Produção Acumulada por Área de Conhecimento ({min(anos_selecionados)}-{max(anos_selecionados)})",
                color_discrete_sequence=['#1a8c73'],
                text='quantidade'
            )
            
            fig_area.update_layout(
                xaxis_title="Área de Conhecimento",
                yaxis_title="Quantidade Total",
                xaxis_tickangle=-45,
                height=450,
                showlegend=False
            )
            
            fig_area.update_traces(textposition='outside')
        
        st.plotly_chart(fig_area, use_container_width=True)
        
        # Adicionar gráfico de linhas para mostrar evolução temporal quando múltiplos anos são selecionados
        if len(anos_selecionados) > 1:
            st.subheader("📈 Evolução Temporal por Área de Conhecimento")
            
            # Dados para o gráfico de linhas
            dados_linha = dados_area.groupby(['ano', 'area_conhecimento'])['quantidade'].sum().reset_index()
            
            fig_linha = px.line(
                dados_linha,
                x='ano',
                y='quantidade',
                color='area_conhecimento',
                title="Evolução Temporal da Produção por Área",
                markers=True,
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            
            fig_linha.update_layout(
                xaxis_title="Ano",
                yaxis_title="Quantidade",
                height=400,
                legend_title="Área de Conhecimento"
            )
            
            st.plotly_chart(fig_linha, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">📋 Fonte de Dados: Plataforma Lattes</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ARTIGOS PUBLICADOS</div>
            <div class="kpi-value">{artigos_publicados:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">CAPÍTULOS DE LIVROS PUBLICADOS</div>
            <div class="kpi-value">{capitulos_livros:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TRABALHOS EM EVENTOS PUBLICADOS</div>
            <div class="kpi-value">{trabalhos_eventos:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Seções expandíveis por tipo de publicação
    tipos_publicacao = dados_pesquisa['tipo_publicacao'].unique()
    
    for tipo in tipos_publicacao:
        with st.expander(f"📚 {tipo}", expanded=(tipo == "Artigos")):
            
            col1, col2 = st.columns(2)
            
            with col1:
                ano_selecionado = st.selectbox(
                    "Ano:",
                    sorted(dados_pesquisa['ano'].unique(), reverse=True),
                    key=f"ano_{tipo}"
                )
            
            with col2:
                forma_exibicao = st.radio(
                    "Forma de exibição:",
                    ["Publicados no ano", "Evolução", "Nuvem de palavras"],
                    key=f"forma_{tipo}"
                )
            
            # Filtrar dados por tipo
            dados_tipo = dados_pesquisa[dados_pesquisa['tipo_publicacao'] == tipo]
            
            if forma_exibicao == "Publicados no ano":
                # Gráfico de barras por unidade
                dados_filtrados = dados_tipo[dados_tipo['ano'] == ano_selecionado]
                dados_grafico = dados_filtrados.groupby('unidade')['quantidade'].sum().reset_index()
                
                fig = px.bar(
                    dados_grafico,
                    x='unidade',
                    y='quantidade',
                    title=f"{tipo} por Unidade - {ano_selecionado}",
                    color_discrete_sequence=['#1a8c73']
                )
                
                fig.update_layout(
                    xaxis_title="Unidade",
                    yaxis_title="Quantidade",
                    xaxis_tickangle=-45,
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
            elif forma_exibicao == "Evolução":
                # Gráfico de linha evolutiva
                dados_evolucao = dados_tipo.groupby('ano')['quantidade'].sum().reset_index()
                
                fig = px.line(
                    dados_evolucao,
                    x='ano',
                    y='quantidade',
                    title=f"Evolução de {tipo}",
                    markers=True,
                    color_discrete_sequence=['#1a8c73']
                )
                
                fig.update_layout(
                    xaxis_title="Ano",
                    yaxis_title="Quantidade",
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
            else:  # Nuvem de palavras
                # Coletar todas as palavras-chave
                dados_filtrados = dados_tipo[dados_tipo['ano'] == ano_selecionado]
                
                if not dados_filtrados.empty:
                    todas_palavras = []
                    for _, row in dados_filtrados.iterrows():
                        if pd.notna(row['palavras_chave']):
                            palavras = row['palavras_chave'].split(', ')
                            todas_palavras.extend(palavras * int(row['quantidade']))
                    
                    # Criar nuvem de palavras
                    if todas_palavras:
                        wordcloud = WordCloud(
                            width=800,
                            height=400,
                            background_color='white',
                            colormap='Greens',
                            max_words=100,
                            relative_scaling=0.5,
                            min_font_size=10
                        ).generate(' '.join(todas_palavras))
                        
                        fig, ax = plt.subplots(figsize=(10, 5))
                        ax.imshow(wordcloud, interpolation='bilinear')
                        ax.axis('off')
                        ax.set_title(f"Nuvem de Palavras - {tipo} - {ano_selecionado}", fontsize=16, pad=20)
                        
                        st.pyplot(fig)
                    else:
                        st.info("Não há palavras-chave suficientes para gerar a nuvem de palavras.")
                else:
                    st.info("Não há dados para o ano selecionado.")
            
            st.markdown('<div class="fonte-dados">Fonte de Dados: Plataforma Lattes</div>', unsafe_allow_html=True)
    
    # Gráfico adicional: Produção por Área de Conhecimento
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Produção por Área de Conhecimento")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        anos_disponiveis = sorted(dados_pesquisa['ano'].unique(), reverse=True)
        anos_selecionados = st.multiselect(
            "Anos:",
            anos_disponiveis,
            default=[anos_disponiveis[0]] if anos_disponiveis else [],
            key="anos_area"
        )
    
    with col2:
        tipo_area = st.selectbox(
            "Tipo de Publicação:",
            ["Todos"] + list(dados_pesquisa['tipo_publicacao'].unique()),
            key="tipo_area"
        )
    
    with col3:
        modo_exibicao = st.selectbox(
            "Modo de Exibição:",
            ["Por Ano", "Total Acumulado"],
            key="modo_area"
        )
    
    # Verificar se há anos selecionados
    if not anos_selecionados:
        st.warning("Selecione pelo menos um ano para visualizar os dados.")
    else:
        # Filtrar dados
        dados_area = dados_pesquisa[dados_pesquisa['ano'].isin(anos_selecionados)]
        
        if tipo_area != "Todos":
            dados_area = dados_area[dados_area['tipo_publicacao'] == tipo_area]
        
        if modo_exibicao == "Por Ano":
            # Mostrar evolução por ano
            dados_grafico_area = dados_area.groupby(['ano', 'area_conhecimento'])['quantidade'].sum().reset_index()
            
            fig_area = px.bar(
                dados_grafico_area,
                x='area_conhecimento',
                y='quantidade',
                color='ano',
                title=f"Evolução da Produção por Área de Conhecimento ({min(anos_selecionados)}-{max(anos_selecionados)})",
                color_discrete_sequence=px.colors.qualitative.Set3,
                barmode='group'
            )
            
            fig_area.update_layout(
                xaxis_title="Área de Conhecimento",
                yaxis_title="Quantidade",
                xaxis_tickangle=-45,
                height=500,
                legend_title="Ano"
            )
        elif modo_exibicao == "Total Acumulado":
            # Mostrar total acumulado
            dados_grafico_area = dados_area.groupby('area_conhecimento')['quantidade'].sum().reset_index()
            
            fig_area = px.bar(
                dados_grafico_area,
                x='area_conhecimento',
                y='quantidade',
                title=f"Produção Acumulada por Área de Conhecimento ({min(anos_selecionados)}-{max(anos_selecionados)})",
                color_discrete_sequence=['#1a8c73']
            )
            
            fig_area.update_layout(
                xaxis_title="Área de Conhecimento",
                yaxis_title="Quantidade Total",
                xaxis_tickangle=-45,
                height=400
            )
        
        st.plotly_chart(fig_area, use_container_width=True)
        
        # Adicionar gráfico de linhas para mostrar evolução temporal quando múltiplos anos são selecionados
        if len(anos_selecionados) > 1:
            st.subheader("📈 Evolução Temporal por Área de Conhecimento")
            
            # Dados para o gráfico de linhas
            dados_linha = dados_area.groupby(['ano', 'area_conhecimento'])['quantidade'].sum().reset_index()
            
            fig_linha = px.line(
                dados_linha,
                x='ano',
                y='quantidade',
                color='area_conhecimento',
                title="Evolução Temporal da Produção por Área",
                markers=True,
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            
            fig_linha.update_layout(
                xaxis_title="Ano",
                yaxis_title="Quantidade",
                height=400,
                legend_title="Área de Conhecimento"
            )
            
            st.plotly_chart(fig_linha, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Plataforma Lattes</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
