# vamos deixar só como backup, pois o mapa.py já está atualizado
# e funcionando corretamente 17/07/2025
# não é necessário manter este arquivo, depois lembrar de remover.

import streamlit as st
import pandas as pd
from .utils import display_header_with_logo, display_footer

def mapa_module(data_gen):
    """
    Módulo de Mapa dos Campus do IFPB na Paraíba
    
    Este módulo exibe informações de localização dos campus do IFPB
    com opção de mapa interativo quando possível.
    """
    
    # Cabeçalho com logo
    display_header_with_logo("Mapa dos Campus IFPB")
    
    # Coordenadas dos campus do IFPB na Paraíba
    campus_coordenadas = {
        'Areia': {'lat': -6.9607, 'lon': -35.7007, 'nome': 'IFPB - Campus Areia'},
        'Cabedelo': {'lat': -6.9814, 'lon': -34.8339, 'nome': 'IFPB - Campus Cabedelo'},
        'Cabedelo Centro': {'lat': -6.9814, 'lon': -34.8339, 'nome': 'IFPB - Campus Cabedelo Centro'},
        'Cajazeiras': {'lat': -6.8897, 'lon': -38.5595, 'nome': 'IFPB - Campus Cajazeiras'},
        'Campina Grande': {'lat': -7.2177, 'lon': -35.8813, 'nome': 'IFPB - Campus Campina Grande'},
        'Catolé do Rocha': {'lat': -6.3442, 'lon': -37.7475, 'nome': 'IFPB - Campus Catolé do Rocha'},
        'Esperança': {'lat': -7.0139, 'lon': -35.8567, 'nome': 'IFPB - Campus Esperança'},
        'Guarabira': {'lat': -6.8542, 'lon': -35.4902, 'nome': 'IFPB - Campus Guarabira'},
        'Itabaiana': {'lat': -7.3286, 'lon': -35.3321, 'nome': 'IFPB - Campus Itabaiana'},
        'Itaporanga': {'lat': -7.3043, 'lon': -38.1503, 'nome': 'IFPB - Campus Itaporanga'},
        'João Pessoa': {'lat': -7.1195, 'lon': -34.8450, 'nome': 'IFPB - Campus João Pessoa'},
        'Mangabeira': {'lat': -7.1195, 'lon': -34.8450, 'nome': 'IFPB - Campus Mangabeira'},
        'Monteiro': {'lat': -7.8914, 'lon': -37.1211, 'nome': 'IFPB - Campus Monteiro'},
        'Patos': {'lat': -7.0196, 'lon': -37.2800, 'nome': 'IFPB - Campus Patos'},
        'Pedras de Fogo': {'lat': -7.4062, 'lon': -35.1154, 'nome': 'IFPB - Campus Pedras de Fogo'},
        'Picuí': {'lat': -6.5130, 'lon': -36.3462, 'nome': 'IFPB - Campus Picuí'},
        'Princesa Isabel': {'lat': -7.7343, 'lon': -37.9845, 'nome': 'IFPB - Campus Princesa Isabel'},
        'Santa Luzia': {'lat': -6.8742, 'lon': -36.9242, 'nome': 'IFPB - Campus Santa Luzia'},
        'Santa Rita': {'lat': -7.1137, 'lon': -34.9781, 'nome': 'IFPB - Campus Santa Rita'},
        'Soledade': {'lat': -7.0567, 'lon': -36.3622, 'nome': 'IFPB - Campus Soledade'},
        'Sousa': {'lat': -6.7645, 'lon': -38.2274, 'nome': 'IFPB - Campus Sousa'},
        'Mamanguape': {'lat': -6.8378, 'lon': -35.1246, 'nome': 'IFPB - Campus Mamanguape'},
        'Sapé': {'lat': -7.0901, 'lon': -35.2373, 'nome': 'IFPB - Campus Sapé'},
        'Queimadas': {'lat': -7.3553, 'lon': -35.8953, 'nome': 'IFPB - Campus Queimadas'},
        'Alagoa Grande': {'lat': -7.0539, 'lon': -35.2906, 'nome': 'IFPB - Campus Alagoa Grande'}
    }
    
    # Descrição do módulo
    st.markdown("### 🗺️ Localização dos Campus")
    st.markdown("""
    Este módulo mostra a distribuição geográfica dos **25 campus** do Instituto Federal da Paraíba (IFPB) 
    em todo o estado. O IFPB possui uma ampla rede de ensino que atende diversas regiões da Paraíba, 
    oferecendo educação profissional e tecnológica de qualidade.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Estatísticas dos campus
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">TOTAL DE CAMPUS</div>
            <div class="kpi-value">{len(campus_coordenadas)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">CIDADES ATENDIDAS</div>
            <div class="kpi-value">{len(set(campus_coordenadas.keys()))}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">COBERTURA ESTADUAL</div>
            <div class="kpi-value">100%</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Opções de visualização
    st.subheader("📍 Opções de Visualização")
    
    col1, col2 = st.columns(2)
    
    with col1:
        filtro_regiao = st.selectbox(
            "🌎 Filtrar por Região:",
            ["Todas as Regiões", "Região Metropolitana", "Agreste", "Borborema", "Cariri", "Sertão", "Litoral"],
            key="filtro_regiao"
        )
    
    with col2:
        tipo_exibicao = st.selectbox(
            "📊 Tipo de Exibição:",
            ["Mapa Interativo", "Mapa do Streamlit", "Apenas Tabela"],
            key="tipo_exibicao"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Filtrar campus por região
    def filtrar_por_regiao(campus_dict, regiao):
        """Filtra campus por região geográfica da Paraíba"""
        regioes = {
            "Região Metropolitana": ["João Pessoa", "Cabedelo", "Cabedelo Centro", "Mangabeira", "Santa Rita", "Sapé"],
            "Agreste": ["Campina Grande", "Esperança", "Guarabira", "Itabaiana", "Queimadas", "Alagoa Grande"],
            "Borborema": ["Monteiro", "Picuí", "Soledade"],
            "Cariri": ["Patos", "Princesa Isabel", "Santa Luzia"],
            "Sertão": ["Cajazeiras", "Catolé do Rocha", "Itaporanga", "Sousa"],
            "Litoral": ["Mamanguape", "Pedras de Fogo", "Areia"]
        }
        
        if regiao == "Todas as Regiões":
            return campus_dict
        
        cidades_regiao = regioes.get(regiao, [])
        return {k: v for k, v in campus_dict.items() if k in cidades_regiao}
    
    # Aplicar filtro
    campus_filtrados = filtrar_por_regiao(campus_coordenadas, filtro_regiao)
    
    # Exibir mapa baseado no tipo selecionado
    if tipo_exibicao == "Mapa Interativo":
        try:
            # Tentar carregar folium
            import folium
            from streamlit_folium import st_folium
            
            # Criar mapa
            centro_pb = [-7.1195, -36.7229]
            m = folium.Map(location=centro_pb, zoom_start=7, tiles="OpenStreetMap")
            
            # Adicionar marcadores
            for cidade, info in campus_filtrados.items():
                popup_text = f"{info['nome']}\nCidade: {cidade}\nLat: {info['lat']:.4f}\nLon: {info['lon']:.4f}"
                folium.Marker(
                    location=[info['lat'], info['lon']],
                    popup=popup_text,
                    tooltip=f"Campus {cidade}",
                    icon=folium.Icon(color='green')
                ).add_to(m)
            
            st.subheader(f"🗺️ Mapa Interativo dos Campus IFPB - {filtro_regiao}")
            st_folium(m, width=1000, height=500)
            
        except Exception as e:
            st.error(f"Erro ao carregar mapa interativo: {str(e)}")
            st.info("Tente selecionar 'Mapa do Streamlit' ou 'Apenas Tabela'")
    
    elif tipo_exibicao == "Mapa do Streamlit":
        # Usar mapa nativo do Streamlit
        st.subheader(f"🗺️ Mapa dos Campus IFPB - {filtro_regiao}")
        
        # Converter para DataFrame
        df_map = pd.DataFrame([
            {
                'latitude': info['lat'],
                'longitude': info['lon'],
                'nome': info['nome'],
                'cidade': cidade
            }
            for cidade, info in campus_filtrados.items()
        ])
        
        # Exibir mapa do Streamlit
        st.map(df_map[['latitude', 'longitude']], zoom=6)
        
        # Mostrar legenda
        st.markdown("**Legenda:** Cada ponto representa um campus do IFPB")
    
    # Sempre mostrar tabela de informações
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📋 Lista de Campus")
    
    # Converter para DataFrame para exibição
    campus_df = pd.DataFrame([
        {
            'Campus': info['nome'],
            'Cidade': cidade,
            'Latitude': info['lat'],
            'Longitude': info['lon']
        }
        for cidade, info in campus_filtrados.items()
    ])
    
    # Ordenar por nome da cidade
    campus_df = campus_df.sort_values('Cidade')
    
    # Exibir tabela
    st.dataframe(
        campus_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            'Campus': st.column_config.TextColumn('Campus', help='Nome completo do campus'),
            'Cidade': st.column_config.TextColumn('Cidade', help='Cidade onde o campus está localizado'),
            'Latitude': st.column_config.NumberColumn('Latitude', help='Coordenada de latitude', format='%.4f'),
            'Longitude': st.column_config.NumberColumn('Longitude', help='Coordenada de longitude', format='%.4f')
        }
    )
    
    # Estatísticas por região
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📊 Distribuição por Região")
    
    # Contar campus por região
    regioes_count = {
        "Região Metropolitana": len([c for c in ["João Pessoa", "Cabedelo", "Cabedelo Centro", "Mangabeira", "Santa Rita", "Sapé"] if c in campus_coordenadas]),
        "Agreste": len([c for c in ["Campina Grande", "Esperança", "Guarabira", "Itabaiana", "Queimadas", "Alagoa Grande"] if c in campus_coordenadas]),
        "Borborema": len([c for c in ["Monteiro", "Picuí", "Soledade"] if c in campus_coordenadas]),
        "Cariri": len([c for c in ["Patos", "Princesa Isabel", "Santa Luzia"] if c in campus_coordenadas]),
        "Sertão": len([c for c in ["Cajazeiras", "Catolé do Rocha", "Itaporanga", "Sousa"] if c in campus_coordenadas]),
        "Litoral": len([c for c in ["Mamanguape", "Pedras de Fogo", "Areia"] if c in campus_coordenadas])
    }
    
    # Exibir como métricas
    cols = st.columns(3)
    for i, (regiao, qtd) in enumerate(regioes_count.items()):
        with cols[i % 3]:
            st.metric(regiao, qtd, help=f"Número de campus na {regiao}")
    
    # Informações sobre o IFPB
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
    
    # Links úteis
    st.markdown("### 🔗 Links Úteis")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("🌐 [Site Oficial do IFPB](https://www.ifpb.edu.br)")
    
    with col2:
        st.markdown("📧 [Portal do Estudante](https://estudante.ifpb.edu.br)")
    
    with col3:
        st.markdown("📚 [Biblioteca Virtual](https://biblioteca.ifpb.edu.br)")
    
    # Fonte dos dados
    st.markdown('<div class="fonte-dados">📍 Fonte: Coordenadas obtidas do portal oficial do IFPB</div>', unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
