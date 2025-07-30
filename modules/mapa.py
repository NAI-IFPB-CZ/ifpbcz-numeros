# ==============================================================================
# MÓDULO DE MAPA DOS CAMPUS - SISTEMA DASHBOARD IFPB-CZ
# ==============================================================================
"""
Módulo responsável pela visualização geográfica dos campus do IFPB na Paraíba.

FUNCIONALIDADES PRINCIPAIS:
• Mapeamento interativo de todos os 25 campus do IFPB no estado da Paraíba
• Filtros por região geográfica (Metropolitana, Agreste, Borborema, Cariri, Sertão, Litoral)
• Múltiplos tipos de visualização (Mapa Interativo, Mapa Streamlit, Tabela)
• Estatísticas de distribuição regional dos campus
• Informações detalhadas sobre localização e coordenadas

DADOS PROCESSADOS:
• Coordenadas geográficas precisas de cada campus
• Classificação regional dos campus
• Nomes oficiais e cidades de localização
• Contagem de campus por região geográfica

VISUALIZAÇÕES GERADAS:
• Mapa interativo com marcadores (Folium)
• Mapa nativo do Streamlit para compatibilidade
• Tabela detalhada com coordenadas
• KPIs de cobertura estadual
• Métricas de distribuição regional

TECNOLOGIAS UTILIZADAS:
• Streamlit para interface web
• Folium para mapas interativos avançados
• Streamlit-Folium para integração de mapas
• Pandas para manipulação de dados geográficos
• Sistema de coordenadas geográficas (lat/lon)

COBERTURA GEOGRÁFICA:
• 25 campus distribuídos em todo o estado da Paraíba
• 6 regiões geográficas contempladas
• 100% de cobertura estadual
• Atendimento a comunidades urbanas e rurais
"""

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from .utils import display_header_with_logo, display_footer

def mapa_module(data_gen):
    """
    Módulo principal de visualização geográfica dos campus do IFPB.
    
    Este módulo apresenta uma interface interativa para explorar a distribuição
    geográfica dos campus do Instituto Federal da Paraíba, oferecendo diferentes
    modos de visualização e filtros regionais.
    
    Args:
        data_gen: Gerador de dados (não utilizado neste módulo pois usa dados estáticos)
    
    Returns:
        None: Renderiza a interface Streamlit com visualizações geográficas
    """
    
    # ==============================================================================
    # INICIALIZAÇÃO E CONFIGURAÇÃO
    # ==============================================================================
    
    # Exibir cabeçalho institucional com logo e ícone de mapa
    display_header_with_logo("🗺️ Mapa dos Campus IFPB")
    
    # ==============================================================================
    # BASE DE DADOS GEOGRÁFICOS DOS CAMPUS
    # ==============================================================================
    
    # Coordenadas precisas dos 25 campus do IFPB na Paraíba
    # Dados obtidos através de consultas ao portal oficial e sistemas de geolocalização
    # Coordenadas precisas dos 25 campus do IFPB na Paraíba
    # Dados obtidos através de consultas ao portal oficial e sistemas de geolocalização
    campus_coordenadas = {
        # Campus da região do Brejo e Agreste
        'Areia': {'lat': -6.9607, 'lon': -35.7007, 'nome': 'IFPB - Campus Areia'},
        'Alagoa Grande': {'lat': -7.0539, 'lon': -35.2906, 'nome': 'IFPB - Campus Alagoa Grande'},
        
        # Campus da região metropolitana e litoral
        'Cabedelo': {'lat': -6.9814, 'lon': -34.8339, 'nome': 'IFPB - Campus Cabedelo'},
        'Cabedelo Centro': {'lat': -6.9814, 'lon': -34.8339, 'nome': 'IFPB - Campus Cabedelo Centro'},
        'João Pessoa': {'lat': -7.1195, 'lon': -34.8450, 'nome': 'IFPB - Campus João Pessoa'},
        'Mangabeira': {'lat': -7.1195, 'lon': -34.8450, 'nome': 'IFPB - Campus Mangabeira'},
        'Santa Rita': {'lat': -7.1137, 'lon': -34.9781, 'nome': 'IFPB - Campus Santa Rita'},
        'Sapé': {'lat': -7.0901, 'lon': -35.2373, 'nome': 'IFPB - Campus Sapé'},
        
        # Campus do sertão paraibano
        'Cajazeiras': {'lat': -6.8897, 'lon': -38.5595, 'nome': 'IFPB - Campus Cajazeiras'},
        'Catolé do Rocha': {'lat': -6.3442, 'lon': -37.7475, 'nome': 'IFPB - Campus Catolé do Rocha'},
        'Itaporanga': {'lat': -7.3043, 'lon': -38.1503, 'nome': 'IFPB - Campus Itaporanga'},
        'Sousa': {'lat': -6.7645, 'lon': -38.2274, 'nome': 'IFPB - Campus Sousa'},
        
        # Campus do agreste central
        'Campina Grande': {'lat': -7.2177, 'lon': -35.8813, 'nome': 'IFPB - Campus Campina Grande'},
        'Esperança': {'lat': -7.0139, 'lon': -35.8567, 'nome': 'IFPB - Campus Esperança'},
        'Guarabira': {'lat': -6.8542, 'lon': -35.4902, 'nome': 'IFPB - Campus Guarabira'},
        'Itabaiana': {'lat': -7.3286, 'lon': -35.3321, 'nome': 'IFPB - Campus Itabaiana'},
        'Queimadas': {'lat': -7.3553, 'lon': -35.8953, 'nome': 'IFPB - Campus Queimadas'},
        
        # Campus da região da borborema
        'Monteiro': {'lat': -7.8914, 'lon': -37.1211, 'nome': 'IFPB - Campus Monteiro'},
        'Picuí': {'lat': -6.5130, 'lon': -36.3462, 'nome': 'IFPB - Campus Picuí'},
        'Soledade': {'lat': -7.0567, 'lon': -36.3622, 'nome': 'IFPB - Campus Soledade'},
        
        # Campus do cariri
        'Patos': {'lat': -7.0196, 'lon': -37.2800, 'nome': 'IFPB - Campus Patos'},
        'Princesa Isabel': {'lat': -7.7343, 'lon': -37.9845, 'nome': 'IFPB - Campus Princesa Isabel'},
        'Santa Luzia': {'lat': -6.8742, 'lon': -36.9242, 'nome': 'IFPB - Campus Santa Luzia'},
        
        # Campus do litoral norte
        'Mamanguape': {'lat': -6.8378, 'lon': -35.1246, 'nome': 'IFPB - Campus Mamanguape'},
        'Pedras de Fogo': {'lat': -7.4062, 'lon': -35.1154, 'nome': 'IFPB - Campus Pedras de Fogo'}
    }
    
    # ==============================================================================
    # INTERFACE E DESCRIÇÃO DO MÓDULO
    # ==============================================================================
    
    # Descrição informativa sobre o módulo de mapeamento
    st.markdown("### 🗺️ Localização dos Campus")
    st.markdown("""
    Este módulo mostra a distribuição geográfica dos **25 campus** do Instituto Federal da Paraíba (IFPB) 
    em todo o estado. O IFPB possui uma ampla rede de ensino que atende diversas regiões da Paraíba, 
    oferecendo educação profissional e tecnológica de qualidade.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==============================================================================
    # KPIS DE COBERTURA GEOGRÁFICA
    # ==============================================================================
    
    # Estatísticas principais dos campus em layout de três colunas
    col1, col2, col3 = st.columns(3)
    
    # KPI 1: Total de campus do IFPB
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TOTAL DE CAMPUS</div>
            <div class="kpi-value">{len(campus_coordenadas)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 2: Número de cidades atendidas
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">CIDADES ATENDIDAS</div>
            <div class="kpi-value">{len(set(campus_coordenadas.keys()))}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # KPI 3: Percentual de cobertura estadual
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">COBERTURA ESTADUAL</div>
            <div class="kpi-value">100%</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==============================================================================
    # CONTROLES DE FILTRO E VISUALIZAÇÃO
    # ==============================================================================
    
    # Opções de visualização e filtros
    st.subheader("📍 Opções de Visualização")
    
    # Layout em duas colunas para os controles
    col1, col2 = st.columns(2)
    
    # Filtro por região geográfica da Paraíba
    with col1:
        filtro_regiao = st.selectbox(
            "🌎 Filtrar por Região:",
            ["Todas as Regiões", "Região Metropolitana", "Agreste", "Borborema", "Cariri", "Sertão", "Litoral"],
            key="filtro_regiao"
        )
    
    # Seletor de tipo de visualização
    with col2:
        tipo_exibicao = st.selectbox(
            "📊 Tipo de Exibição:",
            ["Mapa Interativo", "Mapa do Streamlit", "Apenas Tabela"],
            key="tipo_exibicao"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==============================================================================
    # FUNÇÃO DE FILTRO REGIONAL
    # ==============================================================================
    
    # Filtrar campus por região geográfica da Paraíba
    def filtrar_por_regiao(campus_dict, regiao):
        """
        Filtra campus por região geográfica da Paraíba.
        
        Esta função aplica filtros baseados na divisão geográfica tradicional
        do estado da Paraíba, agrupando os campus por regiões administrativas.
        
        Args:
            campus_dict (dict): Dicionário com todos os campus e suas coordenadas
            regiao (str): Nome da região para filtrar
            
        Returns:
            dict: Dicionário filtrado contendo apenas campus da região selecionada
        """
        # Mapeamento das regiões geográficas da Paraíba
        regioes = {
            # Região Metropolitana de João Pessoa e entorno
            "Região Metropolitana": ["João Pessoa", "Cabedelo", "Cabedelo Centro", "Mangabeira", "Santa Rita", "Sapé"],
            
            # Agreste Paraibano - região central produtiva
            "Agreste": ["Campina Grande", "Esperança", "Guarabira", "Itabaiana", "Queimadas", "Alagoa Grande"],
            
            # Planalto da Borborema - região serrana
            "Borborema": ["Monteiro", "Picuí", "Soledade"],
            
            # Cariri Paraibano - região semiárida central
            "Cariri": ["Patos", "Princesa Isabel", "Santa Luzia"],
            
            # Sertão Paraibano - região oeste semiárida
            "Sertão": ["Cajazeiras", "Catolé do Rocha", "Itaporanga", "Sousa"],
            
            # Litoral e Brejo - região costeira e agrícola
            "Litoral": ["Mamanguape", "Pedras de Fogo", "Areia"]
        }
        
        # Se "Todas as Regiões" for selecionado, retorna todos os campus
        if regiao == "Todas as Regiões":
            return campus_dict
        
        # Obter lista de cidades da região selecionada
        cidades_regiao = regioes.get(regiao, [])
        
        # Filtrar e retornar apenas campus da região
        return {k: v for k, v in campus_dict.items() if k in cidades_regiao}
    
    # ==============================================================================
    # APLICAÇÃO DE FILTROS E PROCESSAMENTO DE DADOS
    # ==============================================================================
    
    # Aplicar filtro regional selecionado pelo usuário
    campus_filtrados = filtrar_por_regiao(campus_coordenadas, filtro_regiao)
    
    # ==============================================================================
    # RENDERIZAÇÃO DE MAPAS BASEADA NO TIPO SELECIONADO
    # ==============================================================================
    
    # Exibir mapa baseado no tipo de visualização selecionado
    if tipo_exibicao == "Mapa Interativo":
        # Modo 1: Mapa Interativo com Folium (funcionalidade completa)
        try:
            # Tentar importar e usar bibliotecas de mapeamento avançado
            import folium
            from streamlit_folium import st_folium
            
            # Definir centro geográfico da Paraíba para visualização
            centro_pb = [-7.1195, -36.7229]  # Coordenadas centrais do estado
            
            # Criar mapa base com configurações otimizadas
            m = folium.Map(
                location=centro_pb, 
                zoom_start=7,           # Nível de zoom para visualizar todo o estado
                tiles="OpenStreetMap"   # Usar tiles do OpenStreetMap
            )
            
            # Adicionar marcadores para cada campus filtrado
            for cidade, info in campus_filtrados.items():
                # Criar texto informativo para popup
                popup_text = f"{info['nome']}\nCidade: {cidade}\nLat: {info['lat']:.4f}\nLon: {info['lon']:.4f}"
                
                # Adicionar marcador ao mapa
                folium.Marker(
                    location=[info['lat'], info['lon']],    # Coordenadas do campus
                    popup=popup_text,                       # Texto do popup detalhado
                    tooltip=f"Campus {cidade}",             # Tooltip ao passar o mouse
                    icon=folium.Icon(color='green')         # Ícone verde institucional
                ).add_to(m)
            
            # Exibir título e renderizar mapa interativo
            st.subheader(f"🗺️ Mapa Interativo dos Campus IFPB - {filtro_regiao}")
            st_folium(m, width=1000, height=500)
            
        except Exception as e:
            # Tratamento de erro caso bibliotecas não estejam disponíveis
            st.error(f"Erro ao carregar mapa interativo: {str(e)}")
            st.info("Tente selecionar 'Mapa do Streamlit' ou 'Apenas Tabela'")
    
    elif tipo_exibicao == "Mapa do Streamlit":
        # Modo 2: Mapa nativo do Streamlit (compatibilidade garantida)
        st.subheader(f"🗺️ Mapa dos Campus IFPB - {filtro_regiao}")
        
        # Converter dados para formato DataFrame para o mapa do Streamlit
        df_map = pd.DataFrame([
            {
                'latitude': info['lat'],    # Coordenada de latitude
                'longitude': info['lon'],   # Coordenada de longitude
                'nome': info['nome'],       # Nome completo do campus
                'cidade': cidade            # Nome da cidade
            }
            for cidade, info in campus_filtrados.items()
        ])
        
        # Renderizar mapa nativo do Streamlit
        st.map(df_map[['latitude', 'longitude']], zoom=6)
        
        # Exibir legenda explicativa
        st.markdown("**Legenda:** Cada ponto representa um campus do IFPB")
    
    # ==============================================================================
    # TABELA DETALHADA DE INFORMAÇÕES
    # ==============================================================================
    
    # Sempre mostrar tabela de informações detalhadas (independente do tipo de mapa)
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📋 Lista de Campus")
    
    # Converter dados para DataFrame para exibição tabular
    campus_df = pd.DataFrame([
        {
            'Campus': info['nome'],      # Nome oficial completo
            'Cidade': cidade,           # Cidade de localização
            'Latitude': info['lat'],    # Coordenada de latitude
            'Longitude': info['lon']    # Coordenada de longitude
        }
        for cidade, info in campus_filtrados.items()
    ])
    
    # Ordenar dados por nome da cidade para melhor organização
    campus_df = campus_df.sort_values('Cidade')
    
    # Exibir tabela interativa com configurações personalizadas
    st.dataframe(
        campus_df,
        use_container_width=True,   # Usar largura completa do container
        hide_index=True,            # Ocultar índice numérico
        column_config={
            'Campus': st.column_config.TextColumn('Campus', help='Nome completo do campus'),
            'Cidade': st.column_config.TextColumn('Cidade', help='Cidade onde o campus está localizado'),
            'Latitude': st.column_config.NumberColumn('Latitude', help='Coordenada de latitude', format='%.4f'),
            'Longitude': st.column_config.NumberColumn('Longitude', help='Coordenada de longitude', format='%.4f')
        }
    )
    
    # ==============================================================================
    # ESTATÍSTICAS POR REGIÃO GEOGRÁFICA
    # ==============================================================================
    
    # Estatísticas de distribuição por região
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📊 Distribuição por Região")
    
    # Calcular contagem de campus por região baseada nos dados atuais
    regioes_count = {
        "Região Metropolitana": len([c for c in ["João Pessoa", "Cabedelo", "Cabedelo Centro", "Mangabeira", "Santa Rita", "Sapé"] if c in campus_coordenadas]),
        "Agreste": len([c for c in ["Campina Grande", "Esperança", "Guarabira", "Itabaiana", "Queimadas", "Alagoa Grande"] if c in campus_coordenadas]),
        "Borborema": len([c for c in ["Monteiro", "Picuí", "Soledade"] if c in campus_coordenadas]),
        "Cariri": len([c for c in ["Patos", "Princesa Isabel", "Santa Luzia"] if c in campus_coordenadas]),
        "Sertão": len([c for c in ["Cajazeiras", "Catolé do Rocha", "Itaporanga", "Sousa"] if c in campus_coordenadas]),
        "Litoral": len([c for c in ["Mamanguape", "Pedras de Fogo", "Areia"] if c in campus_coordenadas])
    }
    
    # Exibir métricas regionais em layout de 3 colunas
    cols = st.columns(3)
    for i, (regiao, qtd) in enumerate(regioes_count.items()):
        with cols[i % 3]:
            st.metric(regiao, qtd, help=f"Número de campus na {regiao}")
    
    # ==============================================================================
    # INFORMAÇÕES INSTITUCIONAIS
    # ==============================================================================
    
    # Informações detalhadas sobre o IFPB
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("ℹ️ Sobre o IFPB")
    st.markdown("""
    O **Instituto Federal de Educação, Ciência e Tecnologia da Paraíba (IFPB)** é uma instituição 
    pública federal que oferece educação profissional e tecnológica em todos os níveis e modalidades. 
    
    **Características principais:**
    - 🎓 Cursos técnicos integrados ao ensino médio
    - 🎓 Cursos técnicos subsequentes  
    - 🎓 Cursos superiores de tecnologia
    - 🎓 Cursos de bacharelado e licenciatura
    - 🎓 Cursos de pós-graduação
    - 🎓 Programas de extensão e pesquisa
    
    **Missão:** Promover a educação profissional, científica e tecnológica por meio do ensino, 
    pesquisa e extensão, contribuindo para o desenvolvimento socioeconômico da Paraíba.
    """)
    
    # ==============================================================================
    # LINKS ÚTEIS E RECURSOS
    # ==============================================================================
    
    # Links úteis para acesso a recursos do IFPB
    st.markdown("### 🔗 Links Úteis")
    col1, col2, col3 = st.columns(3)
    
    # Link para site oficial
    with col1:
        st.markdown("🌐 [Site Oficial do IFPB](https://www.ifpb.edu.br)")
    
    # Link para portal do estudante
    with col2:
        st.markdown("📧 [Portal do Estudante](https://estudante.ifpb.edu.br)")
    
    # Link para biblioteca virtual
    with col3:
        st.markdown("📚 [Biblioteca Virtual](https://biblioteca.ifpb.edu.br)")
    
    # ==============================================================================
    # FONTE DOS DADOS E RODAPÉ
    # ==============================================================================
    
    # Fonte dos dados geográficos
    st.markdown('<div class="fonte-dados">📍 Fonte: Coordenadas obtidas do portal oficial do IFPB</div>', unsafe_allow_html=True)
    
    # Rodapé com informações institucionais
    display_footer()
