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
    
    # Filtrar dados para 2025
    dados_2025 = dados_pesquisa[dados_pesquisa['ano'] == 2025]
    
    # Calcular KPIs
    artigos_publicados = dados_2025[dados_2025['tipo_publicacao'] == 'Artigos']['publicacoes'].sum()
    capitulos_livros = dados_2025[dados_2025['tipo_publicacao'] == 'Capítulos de Livros']['publicacoes'].sum()
    trabalhos_eventos = dados_2025[dados_2025['tipo_publicacao'] == 'Trabalhos em Eventos']['publicacoes'].sum()
    
    # Cartões de KPI
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
                dados_grafico = dados_filtrados.groupby('unidade')['publicacoes'].sum().reset_index()
                
                fig = px.bar(
                    dados_grafico,
                    x='unidade',
                    y='publicacoes',
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
                dados_evolucao = dados_tipo.groupby('ano')['publicacoes'].sum().reset_index()
                
                fig = px.line(
                    dados_evolucao,
                    x='ano',
                    y='publicacoes',
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
                            todas_palavras.extend(palavras * int(row['publicacoes']))
                    
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
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_area = st.selectbox(
            "Ano:",
            sorted(dados_pesquisa['ano'].unique(), reverse=True),
            key="ano_area"
        )
    
    with col2:
        tipo_area = st.selectbox(
            "Tipo de Publicação:",
            ["Todos"] + list(dados_pesquisa['tipo_publicacao'].unique()),
            key="tipo_area"
        )
    
    # Filtrar dados
    dados_area = dados_pesquisa[dados_pesquisa['ano'] == ano_area]
    
    if tipo_area != "Todos":
        dados_area = dados_area[dados_area['tipo_publicacao'] == tipo_area]
    
    # Agrupar por área
    dados_grafico_area = dados_area.groupby('area_pesquisa')['publicacoes'].sum().reset_index()
    
    fig_area = px.bar(
        dados_grafico_area,
        x='area_pesquisa',
        y='publicacoes',
        title=f"Produção por Área de Conhecimento - {ano_area}",
        color_discrete_sequence=['#1a8c73']
    )
    
    fig_area.update_layout(
        xaxis_title="Área de Conhecimento",
        yaxis_title="Quantidade",
        xaxis_tickangle=-45,
        height=400
    )
    
    st.plotly_chart(fig_area, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: Plataforma Lattes</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
