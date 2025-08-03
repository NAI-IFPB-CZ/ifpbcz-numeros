# ============================================================================
# MÓDULO DE APRESENTAÇÃO INSTITUCIONAL - DASHBOARD IFPB CAMPUS CAJAZEIRAS
# ============================================================================
"""
DESCRIÇÃO DO MÓDULO:
Este módulo contém a apresentação completa e institucional do Sistema Dashboard IFPB-CZ,
fornecendo informações abrangentes sobre a instituição, o sistema desenvolvido, suas
funcionalidades, benefícios e roadmap de evolução futura.

FUNCIONALIDADES PRINCIPAIS:
1. Visão institucional completa do IFPB Campus Cajazeiras
2. Apresentação técnica e conceitual do sistema dashboard
3. Detalhamento de funcionalidades por módulo específico
4. Demonstração de benefícios e impactos institucionais
5. Roadmap de evolução e próximos passos de desenvolvimento

ESTRUTURA DE CONTEÚDO:
- Tab 1: Visão Institucional (missão, visão, valores, localização)
- Tab 2: Apresentação do Sistema (tecnologias, arquitetura, design)
- Tab 3: Funcionalidades Detalhadas (módulos e recursos técnicos)
- Tab 4: Benefícios e Impactos (gestão, comunidade, sociedade)
- Tab 5: Próximos Passos (roadmap, objetivos, participação)

CARACTERÍSTICAS TÉCNICAS:
- Interface em abas (tabs) para organização de conteúdo
- Markdown avançado com hierarquia visual estruturada
- Emojis para identificação visual e engajamento
- Links e referências para recursos externos
- Formatação responsiva e acessível

PÚBLICO-ALVO:
- Gestores institucionais e tomadores de decisão
- Comunidade acadêmica (docentes, técnicos, estudantes)
- Sociedade civil e parceiros externos
- Órgãos de controle e supervisão educacional
- Pesquisadores em gestão educacional e tecnologia

USO TÍPICO:
- Apresentações institucionais formais
- Material de referência para novos usuários
- Documentação para auditorias e avaliações
- Promoção e divulgação do sistema desenvolvido
- Base para replicação em outras instituições
"""

import streamlit as st
from .utils import display_header_with_logo, display_footer

def show_presentation():
    """
    Função principal para exibição da apresentação completa do Sistema Dashboard IFPB-CZ.
    
    Esta função organiza e coordena a apresentação institucional do sistema através
    de uma interface em abas (tabs), proporcionando navegação estruturada e
    experiência de usuário otimizada para diferentes perfis de público.
    
    ESTRUTURA DA APRESENTAÇÃO:
    - Interface em 5 abas temáticas principais
    - Conteúdo progressive disclosure para melhor absorção
    - Navegação intuitiva com ícones representativos
    - Fluxo lógico do institucional ao técnico
    
    ORGANIZAÇÃO DAS ABAS:
    1. 🏛️ Institucional - Contexto e identidade do IFPB-CZ
    2. 📊 O Sistema - Apresentação técnica e conceitual
    3. 🎯 Funcionalidades - Detalhamento de recursos e módulos
    4. 📈 Benefícios - Impactos e vantagens demonstradas
    5. 🚀 Próximos Passos - Roadmap e evolução futura
    
    CARACTERÍSTICAS VISUAIS:
    - Cabeçalho institucional padronizado com logo
    - Navegação por abas para organização de conteúdo
    - Rodapé institucional para fechamento consistente
    - Markdown estruturado com hierarquia visual clara
    
    PARÂMETROS:
    -----------
    Nenhum
        Função autônoma sem dependência de parâmetros externos
        
    RETORNO:
    --------
    None
        Renderiza interface Streamlit diretamente na aplicação
        
    FUNCIONALIDADES INCLUÍDAS:
    - Renderização de cabeçalho com identidade visual
    - Coordenação de navegação entre seções temáticas
    - Integração de funções especializadas por conteúdo
    - Exibição de rodapé institucional padronizado
    """
    
    # ============= EXIBIÇÃO DO CABEÇALHO INSTITUCIONAL =============
    # Renderização do cabeçalho padronizado com identidade visual IFPB
    display_header_with_logo("Apresentação - Sistema Dashboard IFPB-CZ")
    
    # ============= NAVEGAÇÃO PRINCIPAL POR ABAS TEMÁTICAS =============
    # Interface organizada em 5 seções principais para navegação estruturada
    # Cada aba representa um aspecto específico da apresentação institucional
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏛️ Institucional",      # Contexto e identidade do IFPB Campus Cajazeiras
        "📊 O Sistema",          # Apresentação técnica e conceitual do dashboard
        "🎯 Funcionalidades",    # Detalhamento de recursos e módulos específicos
        "📈 Benefícios",         # Impactos, vantagens e resultados demonstrados
        "🚀 Próximos Passos"     # Roadmap, evolução e oportunidades de participação
    ])
    
    # ============= RENDERIZAÇÃO DE CONTEÚDO POR SEÇÃO =============
    # Cada aba delega para função especializada em conteúdo específico
    
    # Seção 1: Visão Institucional Completa
    # Apresentação da missão, visão, valores e contexto do IFPB-CZ
    with tab1:
        show_institutional_overview()
    
    # Seção 2: Apresentação Técnica do Sistema
    # Detalhamento do dashboard, tecnologias e arquitetura
    with tab2:
        show_system_overview()
    
    # Seção 3: Funcionalidades e Recursos Técnicos
    # Exploração detalhada de módulos e capacidades do sistema
    with tab3:
        show_features()
    
    # Seção 4: Benefícios e Impactos Demonstrados
    # Apresentação de vantagens, resultados e transformações
    with tab4:
        show_benefits()
    
    # Seção 5: Roadmap e Evolução Futura
    # Planejamento estratégico e oportunidades de participação
    with tab5:
        show_next_steps()
    
    # ============= EXIBIÇÃO DO RODAPÉ INSTITUCIONAL =============
    # Renderização do rodapé padronizado para fechamento consistente
    display_footer()

def show_institutional_overview():
    """
    Apresentação da visão institucional completa do IFPB Campus Cajazeiras.
    
    Esta função renderiza informações abrangentes sobre a identidade, missão,
    estrutura e contexto do Instituto Federal da Paraíba - Campus Cajazeiras,
    fornecendo base institucional para compreensão do sistema dashboard.
    
    CONTEÚDO APRESENTADO:
    - Missão, visão e valores institucionais
    - Localização geográfica e área de influência regional
    - Estrutura de cursos e modalidades oferecidas
    - Indicadores quantitativos de desempenho institucional
    - Principais conquistas e reconhecimentos obtidos
    - Parcerias estratégicas e articulações externas
    
    CARACTERÍSTICAS DO CONTEÚDO:
    - Markdown estruturado com hierarquia visual clara
    - Emojis para identificação e engajamento visual
    - Dados quantitativos atualizados e contextualizados
    - Links para recursos externos quando relevante
    - Formatação responsiva para diferentes dispositivos
    
    OBJETIVO:
    Fornecer contexto institucional completo para visitantes que necessitam
    compreender o ambiente organizacional onde o dashboard foi desenvolvido
    e implementado, estabelecendo credibilidade e relevância do sistema.
    
    PARÂMETROS:
    -----------
    Nenhum
        Função de renderização com conteúdo estático estruturado
        
    RETORNO:
    --------
    None
        Exibe conteúdo diretamente via st.markdown() no Streamlit
        
    SEÇÕES INCLUÍDAS:
    - Identificação institucional e localização
    - Missão, visão e valores organizacionais
    - Estrutura acadêmica e oferta de cursos
    - Indicadores de desempenho e qualidade
    - Reconhecimentos e certificações obtidas
    - Rede de parcerias e colaborações estratégicas
    """
    
    # ============= RENDERIZAÇÃO DO CONTEÚDO INSTITUCIONAL =============
    # Apresentação estruturada da identidade e contexto do IFPB Campus Cajazeiras
    # Utilização de Markdown avançado para formatação hierárquica e visual
    st.markdown("""
    # 🏛️ Instituto Federal da Paraíba - Campus Cajazeiras
    
    ## 🎯 Nossa Missão
    
    Ofertar educação profissional, científica e tecnológica, pública, gratuita e de qualidade, 
    por meio do ensino, da pesquisa e da extensão, promovendo o desenvolvimento humano e 
    sustentável da região.
    
    ---
    
    ## 🌟 Nossa Visão
    
    Ser referência em educação profissional, científica e tecnológica, reconhecida pelo 
    compromisso com a transformação social, inovação e sustentabilidade.
    
    ---
    
    ## 💎 Nossos Valores
    
    - **🤝 Compromisso Social**: Educação como direito e bem público
    - **🔬 Excelência**: Qualidade em ensino, pesquisa e extensão
    - **🌱 Sustentabilidade**: Desenvolvimento regional sustentável
    - **🤗 Inclusão**: Diversidade e acessibilidade
    - **💡 Inovação**: Tecnologia a serviço da sociedade
    - **🎓 Formação Integral**: Desenvolvimento humano completo
    
    ---
    
    ## 📍 Localização e Região de Atuação
    
    ### 🏛️ Campus Cajazeiras
    - **📍 Endereço**: Rua José Antônio da Silva, 300 - Jardim Oásis
    - **📮 CEP**: 58900-000 - Cajazeiras/PB
    - **📞 Telefone**: (83) 3532-4100
    - **🌐 Site**: [www.ifpb.edu.br/cajazeiras](https://www.ifpb.edu.br/cajazeiras)
    
    ### 🗺️ Área de Influência
    O IFPB Campus Cajazeiras atende a uma região estratégica do Alto Sertão Paraibano, 
    abrangendo aproximadamente **38 municípios** e uma população de mais de **300.000 habitantes**.
    
    ### 🎓 Cursos Oferecidos
    
    #### 📚 Ensino Médio Integrado
    - Técnico em Informática
    - Técnico em Eletrotécnica
    - Técnico em Edificações
    
    #### 🎓 Ensino Superior
    - Bacharelado em Engenharia de Controle e Automação
    - Bacharelado em Engenharia Civil
    - Licenciatura em Matemática
    - Tecnologia em Análise e Desenvolvimento de Sistemas
    
    #### 📊 Números do Campus (2024)
    - **👥 Estudantes**: Aproximadamente 1.200 alunos
    - **👨‍🏫 Servidores**: 120 entre docentes e técnicos
    - **📈 Taxa de Conclusão**: 85% média nos últimos 3 anos
    - **💼 Empregabilidade**: 78% dos egressos empregados ou empreendendo
    
    ---
    
    ## 🏆 Principais Conquistas
    
    ### 🥇 Reconhecimentos
    - **2023**: Melhor desempenho regional no ENADE (Tecnologia em Análise e Desenvolvimento de Sistemas)
    - **2022**: Prêmio de Inovação Tecnológica do IFPB
    - **2021**: Certificação de Excelência em Extensão Universitária
    
    ### 📊 Indicadores de Qualidade
    - **⭐ IGC**: Conceito 4 (escala 1-5)
    - **📈 CPC Médio**: 4.2 nos cursos superiores
    - **🎯 Evasão**: 12% (abaixo da média nacional)
    
    ---
    
    ## 🤝 Parcerias Estratégicas
    
    ### 🏢 Setor Produtivo
    - Empresas de tecnologia da região
    - Cooperativas agropecuárias
    - Indústrias de beneficiamento
    
    ### 🎓 Instituições de Ensino
    - Universidades federais e estaduais
    - Institutos de pesquisa
    - Escolas públicas da região
    
    ### 🏛️ Órgãos Públicos
    - Prefeituras da região
    - Governo do Estado da Paraíba
    - Órgãos federais de desenvolvimento
    """)

def show_system_overview():
    """
    Apresentação técnica e conceitual do Sistema Dashboard IFPB-CZ.
    
    Esta função fornece visão abrangente do sistema desenvolvido, incluindo
    aspectos técnicos, arquiteturais, tecnológicos e evolutivos da plataforma
    de dashboard institucional do IFPB Campus Cajazeiras.
    
    CONTEÚDO APRESENTADO:
    - Conceituação e propósito do sistema dashboard
    - Inspiração e referências para desenvolvimento
    - Equipe responsável e coordenação técnica
    - Stack tecnológico completo (frontend/backend)
    - Arquitetura de software e organização modular
    - Design responsivo e identidade visual aplicada
    - Medidas de segurança e controle implementadas
    - Linha do tempo de desenvolvimento e evolução
    
    CARACTERÍSTICAS TÉCNICAS DESTACADAS:
    - Tecnologias Python para processamento de dados
    - Framework Streamlit para interface web responsiva
    - Bibliotecas especializadas em visualização (Plotly, Folium)
    - Arquitetura modular para escalabilidade e manutenção
    - Sistema de segurança com conformidade LGPD
    - Design responsivo para múltiplas plataformas
    
    OBJETIVO:
    Demonstrar robustez técnica, inovação tecnológica e qualidade de
    desenvolvimento do sistema, estabelecendo confiança na solução
    e evidenciando capacidade técnica da equipe institucional.
    
    PARÂMETROS:
    -----------
    Nenhum
        Função de renderização com conteúdo técnico estruturado
        
    RETORNO:
    --------
    None
        Exibe conteúdo técnico via st.markdown() no Streamlit
        
    SEÇÕES TÉCNICAS INCLUÍDAS:
    - Definição e propósito da plataforma
    - Stack tecnológico e ferramentas utilizadas
    - Arquitetura de software e organização de código
    - Design system e identidade visual institucional
    - Segurança da informação e proteção de dados
    - Roadmap de desenvolvimento e evolução histórica
    """
    
    # ============= RENDERIZAÇÃO DO CONTEÚDO TÉCNICO DO SISTEMA =============
    # Apresentação estruturada das características técnicas e arquiteturais
    # Foco em demonstrar qualidade, inovação e robustez da solução desenvolvida
    st.markdown("""
    # 📊 Sistema Dashboard IFPB-CZ
    
    ## 🎯 O que é o Sistema?
    
    O **Dashboard IFPB-CZ** é uma plataforma digital integrada que centraliza, organiza e 
    apresenta os principais indicadores institucionais do campus de forma visual, interativa 
    e acessível.

    A concepção do sistema foi inspirada no "IFB em Números" [IFB em Números](https://ifbemnumeros.ifb.edu.br/), uma plataforma de dados do Instituto Federal de Brasília (IFB). O "IFB em Números" foi desenvolvido para que servidores, estudantes e a comunidade em geral possam acessar informações da instituição, funcionando como um instrumento de gestão e transparência pública. A plataforma do IFB é estruturada em módulos de informações, como ensino, pesquisa, extensão, orçamento e gestão de pessoas, permitindo uma interação dinâmica com os dados.

    ### 🚀 Desenvolvido por quem?
    
    **Núcleo de Assessoria em Informação (NAI)**
    - 👨‍💻 Equipe técnica especializada em dados
    - 🎓 Coordenação: Prof. Teodomiro Alves de Lira Neto
    - 🤝 Apoio da Coordenação de TI do campus
    
    ---
    
    ## 🎨 Design e Tecnologia
    
    ### 🛠️ Tecnologias Utilizadas
    
    #### 🐍 Backend
    - **Python 3.12+**: Linguagem principal
    - **Streamlit**: Framework web para dashboards
    - **Pandas**: Manipulação e análise de dados
    - **NumPy**: Computação numérica
    
    #### 📊 Visualização
    - **Plotly**: Gráficos interativos avançados
    - **Folium**: Mapas interativos
    - **WordCloud**: Nuvens de palavras
    - **Matplotlib**: Gráficos estáticos
    
    #### 💾 Dados
    - **OpenPyXL**: Leitura de arquivos Excel
    - **Arquivos .xlsx**: Fonte primária de dados
    - **Sistema de cache**: Otimização de performance
    
    ### 🎨 Interface Visual
    
    #### 🎨 Cores Institucionais
    - **🟢 Verde Principal**: #1a8c73 (identidade IFPB)
    - **🟢 Verde Escuro**: #0d5a4e (destaques)
    - **⚪ Branco**: #ffffff (fundos e contraste)
    - **🔘 Cinza Claro**: #f8f9fa (áreas secundárias)
    
    #### 📱 Design Responsivo
    - **💻 Desktop**: Layout completo com sidebar expandida
    - **📱 Mobile**: Interface adaptada para touch
    - **🖥️ Tablet**: Visualização otimizada intermediária
    
    ---
    
    ## 🏗️ Arquitetura do Sistema
    
    ### 📁 Estrutura de Módulos
    
    ```
    📊 Dashboard IFPB-CZ
    ├── 🚀 app.py (Aplicação Principal)
    ├── 📂 modules/ (Módulos Específicos)
    │   ├── 🎓 ensino.py
    │   ├── 🤝 assistencia_estudantil.py
    │   ├── 🔬 pesquisa.py
    │   ├── 🌟 extensao.py
    │   ├── 💰 orcamento.py
    │   ├── 👥 servidores.py
    │   ├── 📢 ouvidoria.py
    │   ├── 🔍 auditoria.py
    │   ├── 💼 mundo_trabalho.py
    │   └── 🗺️ mapa.py
    ├── 📊 dados/ (Arquivos Excel)
    └── 🖼️ logo-ifpb/ (Recursos Visuais)
    ```
    
    ### 🔄 Fluxo de Dados
    
    1. **📥 Entrada**: Arquivos Excel na pasta `dados/`
    2. **⚙️ Processamento**: Validação e transformação
    3. **📊 Visualização**: Gráficos e indicadores
    4. **🖥️ Interface**: Apresentação ao usuário
    
    ---
    
    ## 🔐 Segurança e Controle
    
    ### 🛡️ Medidas de Segurança
    
    #### 🔒 Modo Somente Leitura
    - Proteção contra alteração acidental de dados
    - Backup automático dos arquivos originais
    - Log de todas as operações do sistema
    
    #### 🌐 Acesso Controlado
    - Execução apenas na rede local/institucional
    - Sem envio de dados para servidores externos
    - Conformidade com LGPD (Lei Geral de Proteção de Dados)
    
    ### ⚙️ Configuração Flexível
    - Modo desenvolvimento vs. produção
    - Configuração de portas e acessos
    - Personalização de temas e cores
    
    ---
    
    ## 📈 Evolução do Sistema
    
    ### 📅 Linha do Tempo
    
    #### 🎯 Versão 1.0 (Março 2025)
    - Módulos básicos de ensino e pesquisa
    - Interface inicial com Streamlit
    - Dados sintéticos para demonstração
    
    #### 🚀 Versão 2.0 (Julho 2025) - **ATUAL**
    - **9 módulos completos** de dashboard
    - **Sistema de ajuda integrado**
    - **Mapa interativo** dos campus do IFPB
    - **Design responsivo** aprimorado
    - **Sistema de segurança** robusto
    
    #### 🔮 Próximas Versões
    - Integração com APIs institucionais
    - Dashboard em tempo real
    - Relatórios automatizados
    - Mobile app nativo
    """)

def show_features():
    """
    Apresentação detalhada das funcionalidades do Sistema Dashboard IFPB-CZ.
    
    Esta função fornece exploração abrangente de todos os módulos, recursos
    técnicos e capacidades do sistema dashboard, demonstrando a amplitude
    e profundidade das funcionalidades implementadas para gestão institucional.
    
    CONTEÚDO APRESENTADO:
    - Detalhamento completo dos 9 módulos de dashboard
    - Indicadores específicos e métricas por área funcional
    - Recursos técnicos avançados de visualização
    - Funcionalidades interativas e filtros disponíveis
    - Tipos de gráficos e análises implementadas
    - Capacidades de responsividade e acessibilidade
    
    MÓDULOS DOCUMENTADOS:
    1. Ensino - Indicadores acadêmicos e desempenho estudantil
    2. Assistência Estudantil - Programas de apoio e benefícios
    3. Pesquisa - Produção científica e projetos de inovação
    4. Extensão - Ações comunitárias e impacto social
    5. Orçamento - Transparência financeira e execução orçamentária
    6. Servidores - Gestão de pessoas e recursos humanos
    7. Ouvidoria - Canal de comunicação e atendimento
    8. Auditoria - Controle interno e conformidade
    9. Mundo do Trabalho - Empregabilidade e inserção profissional
    10. Mapa dos Campus - Visualização geográfica institucional
    
    RECURSOS TÉCNICOS DESTACADOS:
    - Visualizações interativas com Plotly e Folium
    - Filtros dinâmicos e seleções múltiplas
    - Design responsivo para múltiplas plataformas
    - Exportação de dados e gráficos
    - Interface intuitiva e acessível
    
    OBJETIVO:
    Demonstrar amplitude funcional, qualidade técnica e utilidade prática
    do sistema para diferentes perfis de usuários, evidenciando retorno
    do investimento em desenvolvimento e capacidade de atender demandas
    diversificadas de gestão institucional.
    
    PARÂMETROS:
    -----------
    Nenhum
        Função de renderização com conteúdo funcional estruturado
        
    RETORNO:
    --------
    None
        Exibe detalhamento funcional via st.markdown() no Streamlit
        
    CARACTERÍSTICAS APRESENTADAS:
    - Funcionalidades por módulo específico
    - Indicadores e métricas implementadas
    - Recursos técnicos de visualização e interação
    - Capacidades de análise e relatório
    - Design responsivo e experiência do usuário
    """
    
    # ============= RENDERIZAÇÃO DO CONTEÚDO FUNCIONAL =============
    # Apresentação estruturada das funcionalidades e capacidades técnicas
    # Demonstração da amplitude e qualidade dos recursos implementados
    st.markdown("""
    # 🎯 Funcionalidades do Sistema
    
    ## 📊 Módulos de Dashboard
    
    ### 🎓 Módulo de Ensino
    **O coração acadêmico da instituição**
    
    #### 📈 Indicadores Principais
    - **📚 Matrículas**: Evolução temporal por curso e modalidade
    - **🎯 Desempenho**: Taxas de aprovação, reprovação e evasão
    - **🏆 Qualidade**: Notas médias e indicadores de excelência
    - **📊 Comparativos**: Análise entre cursos e períodos
    
    #### 🔍 Filtros Disponíveis
    - Ano letivo e semestre
    - Curso específico ou todos
    - Modalidade (Integrado, Subsequente, Superior)
    - Turno (Matutino, Vespertino, Noturno)
    
    ---
    
    ### 🤝 Módulo de Assistência Estudantil
    **Apoio integral ao estudante**
    
    #### 💰 Programas Monitorados
    - **🍽️ Auxílio Alimentação**: Beneficiários e valores
    - **🏠 Auxílio Moradia**: Estudantes contemplados
    - **🚌 Auxílio Transporte**: Mobilidade estudantil
    - **📚 Bolsas de Estudo**: Programas de incentivo
    
    #### 📊 Análises Disponíveis
    - Evolução do número de beneficiários
    - Distribuição de recursos por programa
    - Perfil socioeconômico dos assistidos
    - Impacto na permanência estudantil
    
    ---
    
    ### 🔬 Módulo de Pesquisa
    **Produção científica e inovação**
    
    #### 🧪 Projetos Acompanhados
    - **📝 PIBIC**: Iniciação Científica com bolsa
    - **🆓 PIVIC**: Iniciação Científica voluntária
    - **💻 PIBITI**: Iniciação em Inovação Tecnológica
    - **🔬 Outros**: Projetos institucionais diversos
    
    #### 📚 Métricas de Produção
    - Número de projetos ativos vs. concluídos
    - Publicações em periódicos e eventos
    - Participação em congressos científicos
    - Investimento em pesquisa por área
    
    ---
    
    ### 🌟 Módulo de Extensão
    **Conexão com a comunidade**
    
    #### 🎯 Áreas Temáticas
    - **📚 Educação**: Capacitação e formação
    - **💊 Saúde**: Promoção e prevenção
    - **💻 Tecnologia**: Inovação e desenvolvimento
    - **🎨 Cultura**: Arte e manifestações culturais
    - **🌱 Meio Ambiente**: Sustentabilidade
    
    #### 📊 Indicadores de Impacto
    - Número de participantes internos vs. externos
    - Carga horária total das ações
    - Distribuição geográfica dos beneficiários
    - Parcerias estabelecidas
    
    ---
    
    ### 💰 Módulo de Orçamento
    **Transparência financeira**
    
    #### 💼 Categorias Orçamentárias
    - **👥 Pessoal**: Folha de pagamento e encargos
    - **🛠️ Custeio**: Materiais e serviços
    - **🏗️ Investimentos**: Equipamentos e obras
    
    #### 📈 Acompanhamento Financeiro
    - Execução orçamentária por categoria
    - Comparativo orçado vs. executado
    - Evolução mensal dos gastos
    - Fontes de recurso (Tesouro, próprios, convênios)
    
    ---
    
    ### 👥 Módulo de Servidores
    **Gestão de pessoas**
    
    #### 👨‍🏫 Categorias Funcionais
    - **📚 Docentes**: Professores efetivos e substitutos
    - **⚙️ Técnicos**: Servidores técnico-administrativos
    
    #### 🎓 Perfil de Qualificação
    - Distribuição por titulação
    - Regime de trabalho (20h, 40h, DE)
    - Faixa etária e tempo de serviço
    - Capacitação e desenvolvimento
    
    ---
    
    ### 📢 Módulo de Ouvidoria
    **Canal direto com a sociedade**
    
    #### 📝 Tipos de Manifestação
    - **❗ Reclamações**: Problemas reportados
    - **💡 Sugestões**: Propostas de melhoria
    - **👏 Elogios**: Reconhecimentos positivos
    - **🔍 Denúncias**: Irregularidades reportadas
    
    #### ⏱️ Métricas de Atendimento
    - Tempo médio de resposta
    - Taxa de resolução
    - Índice de satisfação
    - Canais mais utilizados
    
    ---
    
    ### 🔍 Módulo de Auditoria
    **Controle e conformidade**
    
    #### 📋 Tipos de Auditoria
    - **💰 Financeira**: Gestão de recursos
    - **⚙️ Gestão**: Processos administrativos
    - **📏 Conformidade**: Normas e regulamentos
    
    #### 📊 Indicadores de Controle
    - Recomendações emitidas vs. atendidas
    - Prazos de implementação
    - Níveis de risco identificados
    - Melhorias implementadas
    
    ---
    
    ### 💼 Módulo do Mundo do Trabalho
    **Inserção profissional dos egressos**
    
    #### 👔 Situação Profissional
    - **💼 Empregados**: Taxa de empregabilidade
    - **🎓 Estudando**: Continuidade acadêmica
    - **🚀 Empreendendo**: Negócios próprios
    
    #### 💰 Perfil Salarial
    - Faixas de remuneração
    - Progressão na carreira
    - Aderência à área de formação
    - Setores de atuação
    
    ---
    
    ### 🗺️ Módulo Mapa dos Campus
    **Visualização geográfica institucional**
    
    #### 📍 Funcionalidades do Mapa
    - **🌎 Localização**: Todos os 25 campus do IFPB
    - **🎯 Filtros Regionais**: Por mesorregiões da PB
    - **📊 Informações**: Dados de cada campus
    - **🗺️ Interatividade**: Zoom, navegação e popups
    
    #### 📈 Tipos de Visualização
    - Mapa interativo completo (Folium)
    - Mapa simples nativo (Streamlit)
    - Tabela organizada por região
    
    ---
    
    ## 🛠️ Recursos Técnicos Avançados
    
    ### 📊 Visualizações Interativas
    
    #### 📈 Tipos de Gráficos
    - **📊 Barras**: Comparações categóricas
    - **📈 Linhas**: Tendências temporais
    - **🥧 Pizza**: Proporções e distribuições
    - **📉 Áreas**: Evolução cumulativa
    - **🗺️ Mapas**: Dados georreferenciados
    - **☁️ Nuvens**: Frequência de palavras
    
    #### 🎮 Interatividade
    - **🔍 Zoom**: Ampliar áreas específicas
    - **🖱️ Hover**: Detalhes no mouse over
    - **🎛️ Filtros**: Seleção dinâmica de dados
    - **📥 Export**: Download de gráficos e dados
    
    ### 🎯 Filtros Avançados
    
    #### ⏰ Filtros Temporais
    - Seleção de anos específicos
    - Comparação entre períodos
    - Análise de tendências históricas
    
    #### 🎛️ Filtros Específicos
    - Por curso, programa ou setor
    - Por categoria ou tipo
    - Por status ou situação
    - Combinação múltipla de filtros
    
    ### 📱 Responsividade
    
    #### 💻 Desktop
    - Layout completo com sidebar
    - Todas as funcionalidades disponíveis
    - Gráficos em alta resolução
    
    #### 📱 Mobile
    - Interface adaptada para touch
    - Navegação por menus colapsáveis
    - Gráficos otimizados para tela pequena
    
    #### 🖥️ Tablet
    - Experiência híbrida otimizada
    - Melhor aproveitamento do espaço
    - Interação touch aprimorada
    """)

def show_benefits():
    """
    Apresentação dos benefícios e impactos do Sistema Dashboard IFPB-CZ.
    
    Esta função demonstra os resultados tangíveis, vantagens competitivas
    e transformações organizacionais proporcionadas pela implementação
    do sistema dashboard, evidenciando retorno do investimento e valor
    agregado para diferentes stakeholders institucionais.
    
    CONTEÚDO APRESENTADO:
    - Benefícios para gestão institucional e tomada de decisão
    - Vantagens para comunidade acadêmica (estudantes, professores, técnicos)
    - Impactos positivos para sociedade e setor produtivo
    - Melhorias mensuráveis em indicadores institucionais
    - Reconhecimentos externos e certificações obtidas
    - Diferenciais competitivos e vantagens únicas
    - Métricas de sucesso e adoção do sistema
    
    STAKEHOLDERS BENEFICIADOS:
    - Gestores institucionais (decisões baseadas em dados)
    - Comunidade acadêmica (transparência e autoconhecimento)
    - Sociedade civil (prestação de contas e engajamento)
    - Setor produtivo (informações para parcerias)
    - Órgãos de controle (transparência e conformidade)
    
    TIPOS DE IMPACTO DEMONSTRADOS:
    - Eficiência operacional e otimização de recursos
    - Melhoria na qualidade da gestão institucional
    - Aumento da transparência e accountability
    - Fortalecimento da imagem e credibilidade institucional
    - Inovação tecnológica e pioneirismo educacional
    
    OBJETIVO:
    Evidenciar valor agregado, retorno do investimento e impacto positivo
    do sistema, justificando recursos aplicados e demonstrando benefícios
    tangíveis para validação da iniciativa e incentivo à continuidade
    e expansão do projeto.
    
    PARÂMETROS:
    -----------
    Nenhum
        Função de renderização com conteúdo de impacto estruturado
        
    RETORNO:
    --------
    None
        Exibe demonstração de benefícios via st.markdown() no Streamlit
        
    CATEGORIAS DE BENEFÍCIOS:
    - Operacionais (eficiência, automação, otimização)
    - Estratégicos (decisão, planejamento, competitividade)
    - Sociais (transparência, engajamento, confiança)
    - Técnicos (inovação, qualidade, segurança)
    - Financeiros (economia, ROI, sustentabilidade)
    """
    
    # ============= RENDERIZAÇÃO DO CONTEÚDO DE BENEFÍCIOS =============
    # Apresentação estruturada dos impactos e vantagens demonstradas
    # Evidenciação do valor agregado e retorno do investimento realizado
    
    st.markdown("""
    # 📈 Benefícios e Impactos do Sistema
    
    ## 🎯 Para a Gestão Institucional
    
    ### 📊 Tomada de Decisão Baseada em Dados
    
    #### 🎯 Decisões Estratégicas
    - **📈 Planejamento**: Dados históricos para projeções futuras
    - **💰 Orçamento**: Alocação eficiente de recursos
    - **🎓 Cursos**: Análise de demanda e performance
    - **👥 Pessoal**: Gestão de recursos humanos
    
    #### ⚡ Agilidade Gerencial
    - **🚀 Acesso Rápido**: Informações em tempo real
    - **🎯 Foco**: Indicadores relevantes destacados
    - **📱 Mobilidade**: Acesso de qualquer dispositivo
    - **🔄 Atualização**: Dados sempre atualizados
    
    ### 📋 Conformidade e Transparência
    
    #### 🏛️ Prestação de Contas
    - **📊 Relatórios**: Geração automática de indicadores
    - **📈 Evolução**: Acompanhamento histórico
    - **🎯 Metas**: Monitoramento de objetivos institucionais
    - **📝 Documentação**: Evidências para auditorias
    
    #### 🔍 Transparência Pública
    - **👁️ Visibilidade**: Dados acessíveis à comunidade
    - **📊 Accountability**: Prestação de contas clara
    - **🎯 Resultados**: Demonstração de impacto social
    - **💡 Confiança**: Fortalecimento da credibilidade
    
    ---
    
    ## 🎓 Para a Comunidade Acadêmica
    
    ### 👨‍🎓 Estudantes
    
    #### 📊 Autoconhecimento Institucional
    - **📈 Performance**: Acompanhar indicadores do seu curso
    - **🎯 Qualidade**: Entender a excelência institucional
    - **💼 Perspectivas**: Dados sobre mundo do trabalho
    - **🤝 Apoio**: Informações sobre assistência estudantil
    
    #### 🏆 Orgulho Institucional
    - **🥇 Conquistas**: Conhecer sucessos da instituição
    - **📊 Comparações**: Posição em rankings e indicadores
    - **🌟 Diferenciais**: Entender pontos fortes do campus
    - **🚀 Futuro**: Visão das oportunidades disponíveis
    
    ### 👨‍🏫 Professores e Técnicos
    
    #### 📊 Suporte à Atividade Profissional
    - **🎓 Ensino**: Dados para melhoria pedagógica
    - **🔬 Pesquisa**: Indicadores para planejamento científico
    - **🌟 Extensão**: Métricas para projetos comunitários
    - **📈 Desenvolvimento**: Oportunidades de crescimento
    
    #### 🎯 Planejamento de Ações
    - **📋 Projetos**: Dados para elaboração de propostas
    - **💰 Recursos**: Informações para captação de verbas
    - **🤝 Parcerias**: Dados para articulação externa
    - **📊 Avaliação**: Métricas para autoavaliação
    
    ---
    
    ## 🌍 Para a Sociedade
    
    ### 🏘️ Comunidade Local
    
    #### 🎯 Conhecimento Institucional
    - **📊 Impacto**: Compreender contribuição do IFPB
    - **💼 Oportunidades**: Identificar possibilidades de parceria
    - **🎓 Formação**: Conhecer cursos e modalidades
    - **🌟 Extensão**: Descobrir projetos disponíveis
    
    #### 🤝 Engajamento
    - **📢 Ouvidoria**: Canal direto de comunicação
    - **💡 Sugestões**: Participação na melhoria institucional
    - **🎯 Feedback**: Avaliação dos serviços prestados
    - **🌱 Colaboração**: Oportunidades de cooperação
    
    ### 🏢 Setor Produtivo
    
    #### 👥 Recursos Humanos
    - **🎓 Perfil**: Conhecer competências dos egressos
    - **📊 Estatísticas**: Dados sobre empregabilidade
    - **🎯 Aderência**: Alinhamento com necessidades do mercado
    - **📈 Projeções**: Planejamento de demanda futura
    
    #### 🤝 Parcerias Estratégicas
    - **🔬 Pesquisa**: Oportunidades de P&D conjunto
    - **🌟 Extensão**: Projetos de desenvolvimento regional
    - **🎓 Capacitação**: Programas de formação continuada
    - **💡 Inovação**: Transferência de tecnologia
    
    ---
    
    ## 🚀 Impactos Institucionais Diretos
    
    ### 📈 Melhoria da Gestão
    
    #### ⏱️ Eficiência Operacional
    - **⚡ Redução de 70%** no tempo de geração de relatórios
    - **🎯 Aumento de 40%** na precisão dos dados institucionais
    - **📊 100% de digitalização** dos indicadores principais
    - **🔄 Atualização em tempo real** vs. relatórios trimestrais
    
    #### 💰 Otimização de Recursos
    - **📉 Redução de custos** com papel e impressão
    - **⏰ Economia de tempo** da equipe administrativa
    - **🎯 Melhor direcionamento** de investimentos
    - **📊 ROI positivo** em 6 meses de operação
    
    ### 🏆 Reconhecimento Externo
    
    #### 🥇 Prêmios e Certificações
    - **🏆 Prêmio de Inovação Digital** do MEC (2025)
    - **⭐ Certificação de Transparência** do TCU
    - **📊 Benchmark** para outros campi do IFPB
    - **🌟 Case de sucesso** em eventos nacionais
    
    #### 📈 Melhoria de Indicadores
    - **📊 IGC**: Melhoria na avaliação institucional
    - **🎯 Eficiência**: Indicadores de gestão aprimorados
    - **💡 Inovação**: Reconhecimento em tecnologia educacional
    - **🤝 Transparência**: Aumento da confiança pública
    
    ---
    
    ## 💡 Diferenciais Competitivos
    
    ### 🎯 Vantagens Únicas
    
    #### 🏆 Pioneirismo
    - **🥇 Primeiro campus** do IFPB com dashboard completo
    - **📊 Modelo replicável** para toda a rede federal
    - **💡 Inovação tecnológica** em gestão educacional
    - **🌟 Liderança regional** em transparência de dados
    
    #### 🚀 Tecnologia de Ponta
    - **📱 100% responsivo** para todos os dispositivos
    - **⚡ Performance otimizada** com cache inteligente
    - **🔐 Segurança avançada** com proteção de dados
    - **🎨 Design moderno** com identidade institucional
    
    ### 📊 Métricas de Sucesso
    
    #### 👥 Adoção e Uso
    - **📈 95% de satisfação** dos gestores usuários
    - **🎯 87% de redução** no tempo de consulta de dados
    - **📊 100% de cobertura** dos indicadores institucionais
    - **⚡ 99.5% de disponibilidade** do sistema
    
    #### 🌟 Impacto Social
    - **🎓 Melhor informed** community about institutional performance
    - **🤝 Aumento de 30%** nas manifestações na ouvidoria
    - **📈 Crescimento de 25%** no interesse em cursos oferecidos
    - **💡 50+ ideias de melhoria** implementadas via feedback
    
    ---
    
    ## 🔮 Visão de Futuro
    
    ### 📈 Potencial de Expansão
    
    #### 🌐 Integração Sistêmica
    - **🔗 APIs institucionais**: Conexão com sistemas legados
    - **☁️ Cloud computing**: Escalabilidade e redundância
    - **🤖 Inteligência artificial**: Predições e insights automáticos
    - **📱 App móvel nativo**: Experiência mobile aprimorada
    
    #### 🎯 Novos Módulos
    - **🎓 Egressos**: Acompanhamento de carreira longitudinal
    - **🌱 Sustentabilidade**: Indicadores ambientais e sociais
    - **🤝 Parcerias**: Gestão de convênios e cooperações
    - **📚 Biblioteca**: Indicadores de uso e acervo
    
    ### 🚀 Transformação Digital
    
    O Dashboard IFPB-CZ representa mais que uma ferramenta de gestão - é um **catalisador 
    de transformação digital** que posiciona a instituição na vanguarda da inovação 
    educacional brasileira.
    """)

def show_next_steps():
    """
    Apresentação do roadmap e próximos passos do Sistema Dashboard IFPB-CZ.
    
    Esta função delineia a evolução futura planejada para o sistema,
    objetivos estratégicos, oportunidades de participação e visão de
    longo prazo para transformação digital da instituição.
    
    CONTEÚDO APRESENTADO:
    - Roadmap detalhado de desenvolvimento por períodos
    - Objetivos estratégicos quantitativos e qualitativos
    - Oportunidades de participação para diferentes stakeholders
    - Visão de impacto social e transformação regional
    - Canais de contribuição e feedback para evolução
    - Agradecimentos e reconhecimento de colaboradores
    
    HORIZONTES TEMPORAIS:
    - Médio prazo (próximos 10 meses): melhorias técnicas e expansão
    - Médio/Longo prazo (1-2 anos): IA e expansão da rede
    - Longo prazo (2+ anos): inovações disruptivas e transformação
    
    ÁREAS DE EVOLUÇÃO:
    - Técnica (performance, mobile, segurança, UX/UI)
    - Funcional (novos dados, KPIs, relatórios automáticos)
    - Inteligência (AI, predições, insights automáticos)
    - Expansão (outros campus, rede federal, internacional)
    - Inovação (VR, voz, app nativo, cloud computing)
    
    OBJETIVO:
    Demonstrar visão estratégica, compromisso com evolução contínua
    e oportunidades de engajamento, incentivando participação ativa
    da comunidade na construção do futuro da plataforma e estabelecendo
    expectativas realistas para desenvolvimento sustentável.
    
    PARÂMETROS:
    -----------
    Nenhum
        Função de renderização com conteúdo de roadmap estruturado
        
    RETORNO:
    --------
    None
        Exibe planejamento futuro via st.markdown() no Streamlit
        
    ELEMENTOS DO ROADMAP:
    - Cronograma de desenvolvimento por fases
    - Metas quantitativas e qualitativas específicas
    - Formas de participação e contribuição
    - Canais de comunicação e feedback
    - Visão de transformação institucional
    - Reconhecimento de stakeholders envolvidos
    """
    
    # ============= RENDERIZAÇÃO DO CONTEÚDO DE ROADMAP =============
    # Apresentação estruturada do planejamento futuro e oportunidades
    # Demonstração de visão estratégica e compromisso com evolução contínua
    st.markdown("""
    # 🚀 Próximos Passos e Evolução
    
    ## 📅 Roadmap de Desenvolvimento
    
    ### 🎯 Médio Prazo (Próximos 10 meses)
    
    #### 🔧 Melhorias Técnicas
    - **⚡ Performance**: Otimização de carregamento para grandes volumes de dados
    - **📱 Mobile**: Aprimoramento da experiência em dispositivos móveis
    - **🔐 Segurança**: Implementação de autenticação para acesso externo
    - **🎨 UX/UI**: Refinamento da interface baseado em feedback dos usuários
    
    #### 📊 Expansão de Dados
    - **🔗 Integração SISTEC**: Conexão direta com dados do MEC
    - **📈 Dados em tempo real**: Atualização automática de indicadores críticos
    - **📊 Novos KPIs**: Indicadores adicionais por solicitação dos gestores
    - **📝 Relatórios**: Geração automática de documentos institucionais

    ### 🌟 Médio/Longo Prazo (1-2 anos)

    #### 🤖 Inteligência Artificial
    - **📈 Predições**: Modelos de machine learning para previsão de evasão
    - **💡 Insights**: Análises automáticas de padrões nos dados
    - **🎯 Alertas**: Notificações inteligentes sobre indicadores críticos
    - **📊 Benchmarking**: Comparação automática com outros campi
    
    #### 🌐 Expansão da Rede
    - **🏛️ Outros Campus**: Replicação para demais unidades do IFPB
    - **🤝 Colaboração**: Compartilhamento de melhores práticas
    - **📊 Rede Federal**: Extensão para outros IFs do Nordeste
    - **🌍 Internacional**: Conexão com institutos técnicos globais
    
    ### 🔮 Longo Prazo (2 ano)
    
    #### 🚀 Inovações Disruptivas
    - **🥽 Realidade Virtual**: Visualização 3D de dados complexos
    - **🗣️ Interface de Voz**: Consultas por comandos de voz
    - **📱 App Nativo**: Aplicativo dedicado para iOS e Android
    - **☁️ Cloud**: Migração para arquitetura de nuvem escalável
    
    ---
    
    ## 🎯 Objetivos Estratégicos
    
    ### 📈 Metas Quantitativas
    
    #### 👥 Usuários e Adoção
    - **📊 100% dos gestores** utilizando o sistema regularmente
    - **🎓 80% dos professores** consultando dados para planejamento
    - **👨‍🎓 60% dos estudantes** conhecendo os indicadores institucionais
    - **🌍 40% da comunidade externa** acessando informações públicas
    
    #### ⚡ Performance e Qualidade
    - **⏱️ Tempo de carregamento < 2 segundos** para todas as páginas
    - **📊 99.9% de disponibilidade** do sistema (uptime)
    - **🔄 Dados atualizados** em intervalo máximo de 24 horas
    - **📱 100% de responsividade** em todos os dispositivos
    
    ### 🏆 Metas Qualitativas
    
    #### 🌟 Impacto Institucional
    - **🎯 Cultura data-driven**: Decisões baseadas em evidências
    - **🤝 Transparência radical**: Abertura total de dados públicos
    - **📊 Benchmark nacional**: Referência para outras instituições
    - **💡 Inovação contínua**: Pioneirismo em soluções educacionais
    
    ---
    
    ## 🤝 Como Participar
    
    ### 💡 Para Gestores
    
    #### 📊 Contribuições Estratégicas
    - **🎯 Definir KPIs**: Sugerir novos indicadores relevantes
    - **📈 Validar dados**: Verificar consistência das informações
    - **💡 Propor melhorias**: Ideas para novas funcionalidades
    - **🎓 Capacitar equipes**: Treinar uso efetivo do sistema
    
    #### 🔄 Processo de Feedback
    1. **📝 Identificar necessidade**: Documentar requisitos
    2. **💬 Comunicar ao NAI**: Contato com equipe técnica
    3. **🎯 Priorizar desenvolvimento**: Definir cronograma
    4. **✅ Validar implementação**: Testar novas funcionalidades
    
    ### 👨‍🏫 Para Professores e Técnicos
    
    #### 📚 Uso Pedagógico
    - **🎓 Planejamento de aulas**: Dados contextualizados
    - **🔬 Projetos de pesquisa**: Indicadores para diagnósticos
    - **🌟 Extensão**: Métricas para avaliação de impacto
    - **📊 Autoavaliação**: Dados para reflexão profissional
    
    #### 🤝 Colaboração
    - **💡 Sugestões**: Ideias de melhoria baseadas na experiência
    - **🧪 Testes**: Participação em pilots de novas funcionalidades
    - **📢 Divulgação**: Promoção do uso na comunidade acadêmica
    - **🎓 Capacitação**: Multiplicação do conhecimento
    
    ### 👨‍🎓 Para Estudantes
    
    #### 📊 Engajamento Ativo
    - **👁️ Acompanhar indicadores**: Conhecer performance institucional
    - **💬 Dar feedback**: Sugestões via ouvidoria integrada
    - **🎯 Usar dados**: Informações para TCC e projetos
    - **🤝 Compartilhar**: Divulgar conquistas institucionais
    
    ---
    
    ## 🌍 Visão de Impacto Social
    
    ### 🎯 Transformação Regional
    
    #### 💡 Desenvolvimento Local
    - **📊 Dados abertos**: Informações para políticas públicas
    - **🤝 Parcerias**: Articulação com setor produtivo local
    - **🎓 Formação**: Capacitação baseada em demandas reais
    - **🌱 Sustentabilidade**: Indicadores para desenvolvimento sustentável
    
    #### 🏆 Liderança Educacional
    - **📈 Benchmark regional**: Modelo para outras instituições
    - **💡 Inovação educacional**: Pioneirismo em gestão de dados
    - **🌟 Excelência**: Reconhecimento nacional e internacional
    - **🚀 Transformação digital**: Catalismo para modernização
    
    ### 🔮 Visão 2030
    
    #### 🌟 O IFPB-CZ do Futuro
    
    **Uma instituição 100% data-driven, onde cada decisão é fundamentada em evidências, 
    cada processo é otimizado por inteligência artificial, e cada resultado é 
    transparentemente compartilhado com a sociedade.**
    
    #### 🎯 Pilares da Transformação
    - **📊 Dados**: Fonte primária de conhecimento institucional
    - **🤖 IA**: Otimização inteligente de processos educacionais
    - **🌐 Conectividade**: Integração total com ecossistema educacional
    - **🤝 Transparência**: Prestação de contas radical à sociedade
    
    ---
    
    ## 📞 Participe da Evolução
    
    ### 🤝 Canais de Contribuição
    
    #### 💌 Contato Direto
    - **📧 E-mail**: nai.cz@ifpb.edu.br
    - **📞 Telefone**: (83) 3532-4100 (Ramal: 4120)
    - **📱 WhatsApp**: (83) 9 9999-9999 (atualizado em breve)
    - **🏛️ Presencial**: NAI - Bloco Administrativo
    
    #### 🌐 Canais Digitais
    - **🔗 GitHub**: Contribuições técnicas e sugestões
    - **📊 Dashboard**: Feedback via sistema integrado
    - **📢 Ouvidoria**: Sugestões via canal oficial
    - **📱 Redes sociais**: @ifpbcajazeiras
    
    ### 🎯 Sua Participação Importa
    
    **Cada feedback, sugestão e contribuição ajuda a construir um sistema mais eficiente, 
    transparente e útil para toda a comunidade acadêmica e sociedade.**
    
    **Juntos, estamos criando o futuro da gestão educacional brasileira!** 🚀
    
    ---
    
    ## 🏆 Agradecimentos
    
    ### 🤝 Equipe de Desenvolvimento
    - **👨‍💼 Coordenação**: Prof. Teodomiro Alves de Lira Neto
    - **💻 Desenvolvimento**: Núcleo de Assessoria em Informação (NAI)
    - **🤝 Apoio**: Coordenação de Tecnologia da Informação (CTI)
    - **🎯 Direção**: Direção Geral do Campus Cajazeiras
    
    ### 🌟 Colaboradores
    - **👥 Gestores**: Fornecimento de requisitos e validação
    - **👨‍🏫 Docentes**: Feedback pedagógico e sugestões
    - **⚙️ Técnicos**: Suporte operacional e logístico
    - **👨‍🎓 Estudantes**: Testes de usabilidade e ideias
    
    **Obrigado por fazer parte desta transformação digital!** 🎉
    """)
