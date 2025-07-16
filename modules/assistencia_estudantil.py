import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .utils import display_header_with_logo, display_footer

def assistencia_estudantil_module(data_gen):
    """Módulo de Assistência Estudantil"""
    
    # Cabeçalho com logo
    display_header_with_logo("Assistência Estudantil")
    
    # Gerar dados
    dados_assistencia = data_gen.gerar_dados_assistencia()
    
    # Filtrar dados para 2025
    dados_2025 = dados_assistencia[dados_assistencia['ano'] == 2025]
    
    # Calcular KPIs
    total_beneficios = dados_2025['parcelas'].sum()
    total_alunos_beneficiados = dados_2025['alunos_beneficiados'].sum()
    
    # Faixa de idade com mais beneficiados
    faixa_mais_beneficiada = dados_2025.groupby('faixa_idade')['alunos_beneficiados'].sum().idxmax()
    
    # Cartões de KPI
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">NÚMERO DE BENEFÍCIOS CONCEDIDOS</div>
            <div class="kpi-value">{total_beneficios:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">ALUNOS BENEFICIADOS PELA ASSISTÊNCIA ESTUDANTIL</div>
            <div class="kpi-value">{total_alunos_beneficiados:,}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-title">FAIXA DE IDADE COM MAIS ALUNOS BENEFICIADOS</div>
            <div class="kpi-value">{faixa_mais_beneficiada}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Gráfico 1: Quantidade de Parcelas por Programa
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Quantidade de Parcelas por Programa da Assistência Estudantil")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ano_selecionado = st.selectbox(
            "Ano:",
            sorted(dados_assistencia['ano'].unique(), reverse=True),
            key="ano_assist_1"
        )
    
    with col2:
        unidade_selecionada = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_assistencia['unidade'].unique()),
            key="unidade_assist_1"
        )
    
    # Filtrar dados
    dados_filtrados = dados_assistencia[dados_assistencia['ano'] == ano_selecionado]
    
    if unidade_selecionada != "Todas":
        dados_filtrados = dados_filtrados[dados_filtrados['unidade'] == unidade_selecionada]
    
    # Agrupar por programa
    dados_grafico = dados_filtrados.groupby('programa')['parcelas'].sum().reset_index()
    
    # Criar gráfico de dispersão/barras
    fig = px.scatter(
        dados_grafico,
        x='programa',
        y='parcelas',
        size='parcelas',
        color='parcelas',
        title=f"Quantidade de Parcelas por Programa - {ano_selecionado}",
        color_continuous_scale=['#e8f5f2', '#1a8c73', '#0d5a4e'],
        size_max=25
    )
    
    fig.update_layout(
        xaxis_title="Programa",
        yaxis_title="Quantidade de Parcelas",
        xaxis_tickangle=-45,
        height=550,
        showlegend=False
    )
    
    # Adicionar barra de cores customizada
    fig.update_coloraxes(
        colorbar_title="Intensidade<br>(Parcelas)",
        colorbar_thickness=15,
        colorbar_len=0.7
    )
    
    # Melhorar a aparência dos círculos
    fig.update_traces(
        marker=dict(
            line=dict(width=1, color='rgba(0,0,0,0.4)'),
            sizemin=8
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico 2: Parcelas por Programa e Nível de Curso
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Parcelas por Programa e Nível de Curso")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ano_selecionado_2 = st.selectbox(
            "Ano:",
            sorted(dados_assistencia['ano'].unique(), reverse=True),
            key="ano_assist_2"
        )
    
    with col2:
        unidade_selecionada_2 = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_assistencia['unidade'].unique()),
            key="unidade_assist_2"
        )
    
    with col3:
        nivel_selecionado = st.selectbox(
            "Nível de Curso:",
            ["Todos"] + list(dados_assistencia['nivel_curso'].unique()),
            key="nivel_assist_2"
        )
    
    # Filtrar dados
    dados_filtrados_2 = dados_assistencia[dados_assistencia['ano'] == ano_selecionado_2]
    
    if unidade_selecionada_2 != "Todas":
        dados_filtrados_2 = dados_filtrados_2[dados_filtrados_2['unidade'] == unidade_selecionada_2]
    
    if nivel_selecionado != "Todos":
        dados_filtrados_2 = dados_filtrados_2[dados_filtrados_2['nivel_curso'] == nivel_selecionado]
    
    # Agrupar dados
    dados_grafico_2 = dados_filtrados_2.groupby(['programa', 'nivel_curso'])['parcelas'].sum().reset_index()
    
    # Criar gráfico
    fig2 = px.scatter(
        dados_grafico_2,
        x='programa',
        y='parcelas',
        color='parcelas',
        size='parcelas',
        symbol='nivel_curso',
        title=f"Parcelas por Programa e Nível de Curso - {ano_selecionado_2}",
        color_continuous_scale=['#e8f5f2', '#1a8c73', '#0d5a4e'],
        size_max=20,
        labels={'parcelas': 'Quantidade de Parcelas', 'programa': 'Programa', 'nivel_curso': 'Nível de Curso'}
    )
    
    fig2.update_layout(
        xaxis_title="Programa",
        yaxis_title="Quantidade de Parcelas",
        xaxis_tickangle=-45,
        height=550,
        legend=dict(
            title="Nível de Curso",
            orientation="v",
            yanchor="top",
            y=0.98,
            xanchor="left",
            x=1.01,
            font=dict(size=11),
            itemsizing="constant",
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="rgba(0,0,0,0.1)",
            borderwidth=1
        ),
        margin=dict(r=140)
    )
    
    # Adicionar barra de cores customizada
    fig2.update_coloraxes(
        colorbar_title="Intensidade<br>(Parcelas)",
        colorbar_thickness=12,
        colorbar_len=0.4,
        colorbar_x=1.01,
        colorbar_y=0.2
    )
    
    # Melhorar a aparência dos símbolos
    fig2.update_traces(
        marker=dict(
            line=dict(width=1, color='rgba(0,0,0,0.4)'),
            sizemin=6
        )
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gráfico adicional: Distribuição por Gênero
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📊 Distribuição de Benefícios por Gênero")
    
    dados_genero = dados_2025.groupby('genero')['alunos_beneficiados'].sum().reset_index()
    
    fig3 = px.pie(
        dados_genero,
        values='alunos_beneficiados',
        names='genero',
        title="Distribuição de Alunos Beneficiados por Gênero - 2025",
        color_discrete_sequence=['#1a8c73', '#0d5a4e']
    )
    
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Novo Gráfico: Evolução Temporal da Assistência Estudantil
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 Evolução Temporal da Assistência Estudantil")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        anos_disponiveis = sorted(dados_assistencia['ano'].unique())
        anos_selecionados = st.multiselect(
            "Selecione os anos:",
            anos_disponiveis,
            default=anos_disponiveis[-3:],  # Últimos 3 anos como padrão
            key="anos_evolucao_assist"
        )
    
    with col2:
        unidade_evolucao = st.selectbox(
            "Unidade:",
            ["Todas"] + list(dados_assistencia['unidade'].unique()),
            key="unidade_evolucao_assist"
        )
    
    with col3:
        metrica_evolucao = st.selectbox(
            "Métrica:",
            ["Quantidade de Parcelas", "Alunos Beneficiados", "Valor Total"],
            key="metrica_evolucao_assist"
        )
    
    if anos_selecionados:
        # Filtrar dados pelos anos selecionados
        dados_evolucao = dados_assistencia[dados_assistencia['ano'].isin(anos_selecionados)]
        
        if unidade_evolucao != "Todas":
            dados_evolucao = dados_evolucao[dados_evolucao['unidade'] == unidade_evolucao]
        
        # Definir coluna para agrupamento baseada na métrica selecionada
        if metrica_evolucao == "Quantidade de Parcelas":
            coluna_metrica = 'parcelas'
        elif metrica_evolucao == "Alunos Beneficiados":
            coluna_metrica = 'alunos_beneficiados'
        else:  # Valor Total
            coluna_metrica = 'valor_total'
        
        # Agrupar por ano e programa
        dados_linha = dados_evolucao.groupby(['ano', 'programa'])[coluna_metrica].sum().reset_index()
        
        # Criar gráfico de linha
        fig_linha = px.line(
            dados_linha,
            x='ano',
            y=coluna_metrica,
            color='programa',
            title=f"Evolução de {metrica_evolucao} por Programa ao Longo dos Anos",
            markers=True,
            color_discrete_sequence=['#1a8c73', '#0d5a4e', '#2db896', '#4dcca8', '#6dd9bb']
        )
        
        fig_linha.update_layout(
            xaxis_title="Ano",
            yaxis_title=metrica_evolucao,
            height=500,
            xaxis=dict(tickmode='linear', dtick=1),
            hovermode='x unified'
        )
        
        fig_linha.update_traces(
            line=dict(width=3),
            marker=dict(size=8)
        )
        
        st.plotly_chart(fig_linha, use_container_width=True)
        
        # Tabela resumo da evolução
        st.markdown("### 📋 Resumo da Evolução")
        
        # Criar tabela pivot para resumo
        tabela_resumo = dados_linha.pivot(index='programa', columns='ano', values=coluna_metrica)
        tabela_resumo = tabela_resumo.fillna(0)
        
        # Adicionar coluna de crescimento percentual
        if len(anos_selecionados) > 1:
            anos_ordenados = sorted(anos_selecionados)
            primeiro_ano = anos_ordenados[0]
            ultimo_ano = anos_ordenados[-1]
            
            if primeiro_ano in tabela_resumo.columns and ultimo_ano in tabela_resumo.columns:
                tabela_resumo['Crescimento %'] = ((tabela_resumo[ultimo_ano] - tabela_resumo[primeiro_ano]) / 
                                                 tabela_resumo[primeiro_ano] * 100).round(1)
                tabela_resumo['Crescimento %'] = tabela_resumo['Crescimento %'].fillna(0)
        
        # Formatar números na tabela
        if metrica_evolucao == "Valor Total":
            tabela_formatada = tabela_resumo.copy()
            for col in tabela_formatada.columns:
                if col != 'Crescimento %':
                    tabela_formatada[col] = tabela_formatada[col].apply(lambda x: f"R$ {x:,.2f}" if x != 0 else "R$ 0,00")
                elif col == 'Crescimento %':
                    tabela_formatada[col] = tabela_formatada[col].apply(lambda x: f"{x:+.1f}%" if x != 0 else "0.0%")
        else:
            tabela_formatada = tabela_resumo.copy()
            for col in tabela_formatada.columns:
                if col != 'Crescimento %':
                    tabela_formatada[col] = tabela_formatada[col].apply(lambda x: f"{x:,.0f}" if x != 0 else "0")
                elif col == 'Crescimento %':
                    tabela_formatada[col] = tabela_formatada[col].apply(lambda x: f"{x:+.1f}%" if x != 0 else "0.0%")
        
        st.dataframe(tabela_formatada, use_container_width=True)
        
    else:
        st.warning("⚠️ Selecione pelo menos um ano para visualizar a evolução.")
    
    st.markdown('<div class="fonte-dados">Fonte de Dados: IFPB-CZ</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Rodapé
    display_footer()
    # Fim do módulo de Assistência Estudantil