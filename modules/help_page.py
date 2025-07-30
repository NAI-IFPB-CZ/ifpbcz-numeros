import streamlit as st
from .utils import display_header_with_logo, display_footer

def show_help():
    """Página de ajuda completa para usuários do sistema"""
    
    display_header_with_logo("Sistema de Ajuda - Dashboard IFPB-CZ")
    
    # Menu de navegação da ajuda
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Guia do Usuário", 
        "📊 Formato dos Dados Excel", 
        "❓ Perguntas Frequentes",
        "📞 Contato e Suporte"
    ])
    
    with tab1:
        show_user_guide()
    
    with tab2:
        show_excel_format_guide()
    
    with tab3:
        show_faq()
    
    with tab4:
        show_contact_support()
    
    display_footer()

def show_user_guide():
    """Guia completo para usuários do sistema"""
    
    st.markdown("""
    # 📋 Guia do Usuário - Dashboard IFPB-CZ
    
    ## 🎯 Visão Geral do Sistema
    
    O **Dashboard IFPB-CZ** é uma ferramenta interativa que oferece uma visão consolidada 
    dos principais indicadores institucionais do Instituto Federal da Paraíba - Campus Cajazeiras.
    
    ### 🎯 Objetivo
    Fornecer aos gestores, comunidade acadêmica e público externo uma plataforma intuitiva 
    para acompanhamento de:
    - Indicadores de ensino e aprendizagem
    - Dados de assistência estudantil
    - Produção científica e projetos de pesquisa
    - Ações de extensão universitária
    - Gestão orçamentária e financeira
    - Recursos humanos (servidores)
    - Atendimento da ouvidoria
    - Auditorias e conformidade
    - Inserção no mundo do trabalho
    
    ### 👥 Usuários-Alvo
    - **Gestores**: Diretores, coordenadores e chefias
    - **Comunidade Acadêmica**: Professores, técnicos e estudantes
    - **Público Externo**: Comunidade local e órgãos de controle
    
    ---
    
    ## 🚀 Primeiros Passos
    
    ### Como Acessar
    1. **URL Local**: http://localhost:8501 (quando executado localmente)
    2. **URL da Rede**: Consulte o administrador do sistema
    
    ### Interface Principal
    
    #### 📱 Barra Lateral (Sidebar)
    - **Localização**: Lado esquerdo da tela
    - **Função**: Navegação entre os módulos do sistema
    - **Controle**: Pode ser recolhida/expandida usando o botão ☰
    
    #### 🖥️ Área Principal
    - **Localização**: Centro da tela
    - **Função**: Exibição dos dashboards e gráficos
    - **Interação**: Filtros e controles específicos de cada módulo
    
    ---
    
    ## 📊 Guia dos Módulos
    
    ### 🎓 Ensino
    **O que mostra**: Dados sobre matrículas, ingressantes, concluintes e indicadores acadêmicos
    
    **Filtros disponíveis**:
    - Ano letivo
    - Curso específico
    - Modalidade (Integrado, Subsequente, Concomitante)
    - Turno (Matutino, Vespertino, Noturno)
    
    **Gráficos principais**:
    - Evolução de matrículas por ano
    - Taxa de aprovação/reprovação
    - Distribuição por modalidade
    - Comparativo de desempenho por curso
    
    ### 🤝 Assistência Estudantil
    **O que mostra**: Programas de auxílio, bolsas e benefícios concedidos aos estudantes
    
    **Filtros disponíveis**:
    - Período (ano/mês)
    - Tipo de programa
    - Nível do curso (Técnico/Superior)
    
    **Gráficos principais**:
    - Evolução do número de beneficiários
    - Distribuição de recursos por programa
    - Perfil dos beneficiários (idade, gênero)
    - Valor total investido
    
    ### 🔬 Pesquisa
    **O que mostra**: Projetos de pesquisa, bolsistas, publicações e produção científica
    
    **Filtros disponíveis**:
    - Período
    - Área do conhecimento
    - Tipo de projeto (PIBIC, PIVIC, PIBITI)
    
    **Gráficos principais**:
    - Projetos ativos vs. concluídos
    - Número de bolsistas e voluntários
    - Publicações por área
    - Investimento em pesquisa
    
    ### 🌟 Extensão
    **O que mostra**: Projetos e eventos de extensão, participação da comunidade
    
    **Filtros disponíveis**:
    - Período
    - Área temática
    - Tipo de ação (Curso, Evento, Projeto)
    
    **Gráficos principais**:
    - Ações por área temática
    - Participação interna vs. externa
    - Carga horária total
    - Status das ações
    
    ### 💰 Orçamento
    **O que mostra**: Execução orçamentária, empenhamento, liquidação e pagamento
    
    **Filtros disponíveis**:
    - Exercício fiscal
    - Categoria orçamentária
    - Fonte de recurso
    
    **Gráficos principais**:
    - Execução orçamentária por categoria
    - Comparativo orçado vs. executado
    - Distribuição por fonte de recurso
    - Evolução mensal dos gastos
    
    ### 👥 Servidores
    **O que mostra**: Quadro de pessoal, distribuição por categoria, titulação e regime
    
    **Filtros disponíveis**:
    - Período
    - Categoria (Docente/Técnico-Administrativo)
    - Situação funcional
    
    **Gráficos principais**:
    - Distribuição por categoria
    - Perfil de titulação
    - Pirâmide etária
    - Regime de trabalho
    
    ### 📢 Ouvidoria
    **O que mostra**: Manifestações recebidas, tipos, canais e índices de satisfação
    
    **Filtros disponíveis**:
    - Período
    - Tipo de manifestação
    - Canal de atendimento
    
    **Gráficos principais**:
    - Evolução das manifestações
    - Distribuição por tipo
    - Tempo médio de resposta
    - Índice de satisfação
    
    ### 🔍 Auditoria
    **O que mostra**: Auditorias realizadas, recomendações e conformidade
    
    **Filtros disponíveis**:
    - Período
    - Tipo de auditoria
    - Origem (Interna/Externa)
    
    **Gráficos principais**:
    - Auditorias por tipo
    - Recomendações atendidas
    - Níveis de risco
    - Tempo de atendimento
    
    ### 💼 Mundo do Trabalho
    **O que mostra**: Situação profissional dos egressos, empregabilidade
    
    **Filtros disponíveis**:
    - Curso de origem
    - Tempo desde a conclusão
    - Setor de atividade
    
    **Gráficos principais**:
    - Taxa de empregabilidade
    - Distribuição salarial
    - Inserção por área de formação
    - Continuidade nos estudos
    
    ---
    
    ## 🎮 Como Usar os Filtros
    
    ### Seleção de Período
    - Use os controles de ano/mês para focar em períodos específicos
    - Alguns módulos permitem comparação entre períodos
    
    ### Filtros Específicos
    - Cada módulo possui filtros próprios no painel lateral
    - Os gráficos são atualizados automaticamente ao alterar filtros
    - Use "Todos" para visualizar dados agregados
    
    ### Interação com Gráficos
    - **Zoom**: Clique e arraste para ampliar uma área
    - **Pan**: Use shift + clique e arraste para mover
    - **Hover**: Passe o mouse sobre elementos para ver detalhes
    - **Legenda**: Clique para mostrar/ocultar séries
    
    ---
    
    ## 📈 Interpretando os Gráficos
    
    ### Gráficos de Barras
    - **Altura**: Representa o valor da métrica
    - **Cores**: Diferenciam categorias ou períodos
    - **Hover**: Mostra valores exatos
    
    ### Gráficos de Linha
    - **Tendência**: Mostra evolução temporal
    - **Pontos**: Valores específicos de cada período
    - **Múltiplas linhas**: Permitem comparação entre categorias
    
    ### Gráficos de Pizza
    - **Fatias**: Proporção de cada categoria
    - **Percentuais**: Mostrados automaticamente
    - **Cores**: Identificam diferentes categorias
    
    ### Mapas e Visualizações Especiais
    - **Coordenadas**: Mostram localização geográfica
    - **Marcadores**: Identificam pontos de interesse
    - **Zoom**: Permite navegação no mapa
    """)

def show_excel_format_guide():
    """Guia detalhado sobre formato dos arquivos Excel"""
    
def show_excel_format_guide():
    """Guia detalhado sobre formato dos arquivos Excel"""
    
    st.markdown("""
    # 📊 Formato dos Dados Excel
    
    ## 📋 Visão Geral
    
    Esta página explica como os dados devem ser formatados nos arquivos Excel (.xlsx) para 
    cada módulo do sistema. Todos os arquivos devem ser salvos na pasta `dados/` 
    na raiz do projeto.
    
    ### 📁 Estrutura de Arquivos
    
    Cada módulo possui seu próprio arquivo Excel com nome específico:
    
    - `dados_ensino.xlsx` - Dados do módulo de Ensino
    - `dados_assistencia.xlsx` - Dados de Assistência Estudantil  
    - `dados_pesquisa.xlsx` - Dados de Pesquisa
    - `dados_extensao.xlsx` - Dados de Extensão
    - `dados_orcamento.xlsx` - Dados de Orçamento
    - `dados_servidores.xlsx` - Dados de Servidores
    - `dados_ouvidoria.xlsx` - Dados de Ouvidoria
    - `dados_auditoria.xlsx` - Dados de Auditoria
    - `dados_mundo_trabalho.xlsx` - Dados do Mundo do Trabalho
    
    ### 📊 Estrutura das Planilhas
    
    Cada arquivo Excel deve conter duas planilhas:
    - **Dados** (ou nome específico): Contém os dados principais
    - **Metadados**: Informações sobre os dados (criada automaticamente)
    
    ---
    """)
    
    # Ensino
    st.markdown("""
    ## 🎓 Módulo de Ensino
    
    **Arquivo:** `dados_ensino.xlsx`  
    **Planilha:** `Dados_Ensino`
    
    ### Colunas Obrigatórias:
    
    | Coluna | Tipo | Descrição | Exemplo |
    |--------|------|-----------|---------|
    | `ano` | Inteiro | Ano do registro | 2024 |
    | `curso` | Texto | Nome do curso | "Técnico em Informática" |
    | `matriculados` | Inteiro | Número de alunos matriculados | 85 |
    | `formados` | Inteiro | Número de alunos formados | 42 |
    | `desistentes` | Inteiro | Número de desistentes | 8 |
    | `transferidos` | Inteiro | Número de transferidos | 3 |
    | `modalidade` | Texto | Modalidade do curso | "Integrado", "Subsequente", "Concomitante" |
    | `turno` | Texto | Turno de funcionamento | "Matutino", "Vespertino", "Noturno" |
    | `semestre` | Inteiro | Semestre (1 ou 2) | 1 |
    | `campus` | Texto | Campus onde é ofertado | "Cajazeiras" |
    | `aprovacao_percentual` | Decimal | Percentual de aprovação | 85.5 |
    | `reprovacao_percentual` | Decimal | Percentual de reprovação | 14.5 |
    | `nota_media` | Decimal | Nota média da turma | 7.8 |
    
    ---
    """)
    
    # Assistência Estudantil
    st.markdown("""
    ## 🤝 Módulo de Assistência Estudantil
    
    **Arquivo:** `dados_assistencia.xlsx`  
    **Planilha:** `Dados_Assistencia`
    
    ### Colunas Obrigatórias:
    
    | Coluna | Tipo | Descrição | Exemplo |
    |--------|------|-----------|---------|
    | `ano` | Inteiro | Ano do registro | 2024 |
    | `mes` | Inteiro | Mês (1-12) | 6 |
    | `unidade` | Texto | Unidade/Campus | "Campus Cajazeiras" |
    | `programa` | Texto | Programa de assistência | "Auxílio Alimentação" |
    | `nivel_curso` | Texto | Nível do curso | "Técnico", "Superior" |
    | `parcelas` | Inteiro | Número de parcelas pagas | 45 |
    | `alunos_beneficiados` | Inteiro | Número de alunos beneficiados | 42 |
    | `valor_total` | Decimal | Valor total em reais | 18500.00 |
    | `faixa_idade` | Texto | Faixa etária | "16-20", "21-25", "26-30", "31+" |
    | `genero` | Texto | Gênero | "Masculino", "Feminino" |
    
    ---
    """)
    
    # Pesquisa
    st.markdown("""
    ## 🔬 Módulo de Pesquisa
    
    **Arquivo:** `dados_pesquisa.xlsx`  
    **Planilha:** `Dados_Pesquisa`
    
    ### Colunas Obrigatórias:
    
    | Coluna | Tipo | Descrição | Exemplo |
    |--------|------|-----------|---------|
    | `ano` | Inteiro | Ano do registro | 2024 |
    | `unidade` | Texto | Unidade/Campus | "Campus Cajazeiras" |
    | `area_conhecimento` | Texto | Área do conhecimento | "Ciências Exatas" |
    | `tipo_projeto` | Texto | Tipo de projeto | "PIBIC", "PIVIC", "PIBITI" |
    | `projetos_ativos` | Inteiro | Projetos em andamento | 15 |
    | `projetos_concluidos` | Inteiro | Projetos finalizados | 8 |
    | `bolsistas` | Inteiro | Número de bolsistas | 12 |
    | `voluntarios` | Inteiro | Número de voluntários | 5 |
    | `publicacoes` | Inteiro | Número de publicações | 3 |
    | `orientadores` | Inteiro | Número de orientadores | 6 |
    | `valor_investido` | Decimal | Valor investido em reais | 45000.00 |
    
    ---
    """)
    
    # Extensão
    st.markdown("""
    ## 🌟 Módulo de Extensão
    
    **Arquivo:** `dados_extensao.xlsx`  
    **Planilha:** `Dados_Extensao`
    
    ### Colunas Obrigatórias:
    
    | Coluna | Tipo | Descrição | Exemplo |
    |--------|------|-----------|---------|
    | `ano` | Inteiro | Ano do registro | 2024 |
    | `unidade` | Texto | Unidade/Campus | "Campus Cajazeiras" |
    | `area_tematica` | Texto | Área temática | "Educação", "Saúde", "Tecnologia" |
    | `tipo_acao` | Texto | Tipo de ação | "Curso", "Evento", "Projeto" |
    | `titulo` | Texto | Título da ação | "Curso de Informática Básica" |
    | `participantes_internos` | Inteiro | Participantes do IFPB | 25 |
    | `participantes_externos` | Inteiro | Participantes da comunidade | 80 |
    | `carga_horaria` | Inteiro | Carga horária total | 40 |
    | `coordenador` | Texto | Nome do coordenador | "Prof. João Silva" |
    | `status` | Texto | Status da ação | "Concluído", "Em andamento", "Planejado" |
    
    ---
    """)
    
    # Orçamento
    st.markdown("""
    ## 💰 Módulo de Orçamento
    
    **Arquivo:** `dados_orcamento.xlsx`  
    **Planilha:** `Dados_Orcamento`
    
    ### Colunas Obrigatórias:
    
    | Coluna | Tipo | Descrição | Exemplo |
    |--------|------|-----------|---------|
    | `ano` | Inteiro | Ano do registro | 2024 |
    | `mes` | Inteiro | Mês (1-12) | 6 |
    | `unidade` | Texto | Unidade/Campus | "Campus Cajazeiras" |
    | `categoria` | Texto | Categoria orçamentária | "Custeio", "Investimentos", "Pessoal" |
    | `subcategoria` | Texto | Subcategoria | "Material de Consumo", "Equipamentos" |
    | `valor_orcado` | Decimal | Valor orçado | 150000.00 |
    | `valor_empenhado` | Decimal | Valor empenhado | 120000.00 |
    | `valor_liquidado` | Decimal | Valor liquidado | 100000.00 |
    | `valor_pago` | Decimal | Valor pago | 95000.00 |
    | `fonte_recurso` | Texto | Fonte do recurso | "Tesouro", "Próprios", "Convênios" |
    
    ---
    """)
    
    # Servidores
    st.markdown("""
    ## 👥 Módulo de Servidores
    
    **Arquivo:** `dados_servidores.xlsx`  
    **Planilha:** `Dados_Servidores`
    
    ### Colunas Obrigatórias:
    
    | Coluna | Tipo | Descrição | Exemplo |
    |--------|------|-----------|---------|
    | `ano` | Inteiro | Ano do registro | 2024 |
    | `mes` | Inteiro | Mês (1-12) | 6 |
    | `unidade` | Texto | Unidade/Campus | "Campus Cajazeiras" |
    | `categoria` | Texto | Categoria do servidor | "Docente", "Técnico-Administrativo" |
    | `regime_trabalho` | Texto | Regime de trabalho | "Dedicação Exclusiva", "40h", "20h" |
    | `situacao` | Texto | Situação funcional | "Ativo", "Licença", "Afastado" |
    | `titulacao` | Texto | Titulação | "Graduação", "Especialização", "Mestrado", "Doutorado" |
    | `faixa_etaria` | Texto | Faixa etária | "20-30", "31-40", "41-50", "51-60", "60+" |
    | `genero` | Texto | Gênero | "Masculino", "Feminino" |
    | `quantidade` | Inteiro | Quantidade de servidores | 1 |
    
    ---
    """)
    
    # Ouvidoria
    st.markdown("""
    ## 📢 Módulo de Ouvidoria
    
    **Arquivo:** `dados_ouvidoria.xlsx`  
    **Planilha:** `Dados_Ouvidoria`
    
    ### Colunas Obrigatórias:
    
    | Coluna | Tipo | Descrição | Exemplo |
    |--------|------|-----------|---------|
    | `ano` | Inteiro | Ano do registro | 2024 |
    | `mes` | Inteiro | Mês (1-12) | 6 |
    | `unidade` | Texto | Unidade/Campus | "Campus Cajazeiras" |
    | `tipo_manifestacao` | Texto | Tipo de manifestação | "Reclamação", "Sugestão", "Elogio" |
    | `assunto` | Texto | Assunto da manifestação | "Ensino", "Infraestrutura", "Serviços" |
    | `canal` | Texto | Canal de atendimento | "Sistema", "Presencial", "Telefone" |
    | `status` | Texto | Status da manifestação | "Aberta", "Em análise", "Concluída" |
    | `tipo_usuario` | Texto | Tipo do usuário | "Estudante", "Servidor", "Comunidade" |
    | `prazo_resposta` | Inteiro | Prazo para resposta (dias) | 10 |
    | `satisfacao` | Inteiro | Nível de satisfação (1-5) | 4 |
    
    ---
    """)
    
    # Auditoria
    st.markdown("""
    ## 🔍 Módulo de Auditoria
    
    **Arquivo:** `dados_auditoria.xlsx`  
    **Planilha:** `Dados_Auditoria`
    
    ### Colunas Obrigatórias:
    
    | Coluna | Tipo | Descrição | Exemplo |
    |--------|------|-----------|---------|
    | `ano` | Inteiro | Ano do registro | 2024 |
    | `mes` | Inteiro | Mês (1-12) | 6 |
    | `unidade` | Texto | Unidade/Campus | "Campus Cajazeiras" |
    | `tipo_auditoria` | Texto | Tipo de auditoria | "Financeira", "Gestão", "Conformidade" |
    | `origem` | Texto | Origem da auditoria | "Interna", "Externa", "CGU" |
    | `status` | Texto | Status da auditoria | "Iniciada", "Em andamento", "Concluída" |
    | `recomendacoes` | Inteiro | Número de recomendações | 5 |
    | `recomendacoes_atendidas` | Inteiro | Recomendações atendidas | 3 |
    | `prazo_atendimento` | Inteiro | Prazo para atendimento (dias) | 90 |
    | `risco_nivel` | Texto | Nível de risco | "Baixo", "Médio", "Alto" |
    
    ---
    """)
    
    # Mundo do Trabalho
    st.markdown("""
    ## 💼 Módulo do Mundo do Trabalho
    
    **Arquivo:** `dados_mundo_trabalho.xlsx`  
    **Planilha:** `Dados_Mundo_Trabalho`
    
    ### Colunas Obrigatórias:
    
    | Coluna | Tipo | Descrição | Exemplo |
    |--------|------|-----------|---------|
    | `ano` | Inteiro | Ano do registro | 2024 |
    | `unidade` | Texto | Unidade/Campus | "Campus Cajazeiras" |
    | `curso` | Texto | Curso de origem | "Técnico em Informática" |
    | `situacao_profissional` | Texto | Situação atual | "Empregado", "Desempregado", "Estudando" |
    | `setor_atividade` | Texto | Setor de atividade | "Tecnologia", "Educação", "Saúde" |
    | `salario_faixa` | Texto | Faixa salarial | "1-2 SM", "2-3 SM", "3-5 SM", "5+ SM" |
    | `tipo_vinculo` | Texto | Tipo de vínculo | "CLT", "Estágio", "Autônomo", "Concursado" |
    | `tempo_conclusao` | Inteiro | Anos desde a conclusão | 2 |
    | `continua_estudando` | Texto | Continua estudando | "Sim", "Não" |
    | `trabalha_area_formacao` | Texto | Trabalha na área | "Sim", "Não", "Parcialmente" |
    
    ---
    """)
    
    st.markdown("""
    ## ⚠️ Observações Importantes
    
    1. **Nomes das colunas**: Devem ser exatamente como especificado (case-sensitive)
    2. **Tipos de dados**: Respeitar os tipos especificados (Inteiro, Decimal, Texto)
    3. **Valores nulos**: Evitar células vazias, usar 0 para números ou "N/A" para texto
    4. **Encoding**: Salvar os arquivos com codificação UTF-8
    5. **Formato de data**: Usar formato YYYY-MM-DD para datas
    6. **Decimais**: Usar ponto (.) como separador decimal
    7. **Planilha ativa**: A planilha com os dados deve ser a primeira ou ter o nome especificado
    
    ## 📝 Exemplo de Uso
    
    1. Criar um arquivo Excel com o nome correto (ex: `dados_ensino.xlsx`)
    2. Nomear a planilha conforme especificado (ex: `Dados_Ensino`)
    3. Criar cabeçalhos na primeira linha com os nomes das colunas
    4. Preencher os dados nas linhas seguintes
    5. Salvar o arquivo na pasta `dados/`
    6. Executar o sistema - os dados serão carregados automaticamente
    
    ## 🔄 Atualização de Dados
    
    Para atualizar os dados, basta substituir o arquivo Excel na pasta `dados/` e reiniciar o sistema.
    O sistema detectará automaticamente as alterações e exibirá a data de atualização.
    """)

def show_faq():
    """Seção de Perguntas Frequentes"""
    
    st.markdown("""
    # ❓ Perguntas Frequentes (FAQ)
    
    ## 🔄 Sobre Atualização de Dados
    
    **P: Os dados são atualizados em tempo real?**
    R: Não. Os dados são carregados dos arquivos Excel na pasta `dados/` quando o sistema é iniciado. 
    Para atualizar, substitua os arquivos e reinicie o sistema.
    
    **P: Com que frequência os dados devem ser atualizados?**
    R: Recomenda-se atualização mensal para a maioria dos módulos, exceto orçamento que pode 
    ser atualizado semanalmente.
    
    **P: Como sei quando os dados foram atualizados pela última vez?**
    R: Cada módulo exibe a data da última atualização no rodapé da página.
    
    ---
    
    ## 📊 Sobre Exportação de Dados
    
    **P: Posso exportar os gráficos?**
    R: Sim! Use o botão de menu (três pontos) no canto superior direito de cada gráfico 
    para salvar como imagem (PNG) ou dados (CSV).
    
    **P: Posso imprimir os dashboards?**
    R: Sim. Use Ctrl+P no navegador. O sistema está otimizado para impressão.
    
    **P: Os dados podem ser exportados para Excel?**
    R: Os dados já estão em formato Excel na pasta `dados/`. Para dados filtrados, 
    use a opção de download CSV disponível em alguns gráficos.
    
    ---
    
    ## 🔧 Sobre Problemas Técnicos
    
    **P: O sistema está lento. O que fazer?**
    R: 1) Verifique sua conexão com a internet
       2) Feche outras abas do navegador
       3) Limpe o cache do navegador (Ctrl+Shift+Del)
       4) Entre em contato com o suporte
    
    **P: Os gráficos não estão carregando. O que fazer?**
    R: 1) Atualize a página (F5)
       2) Verifique se há erros nos dados Excel
       3) Verifique se todos os arquivos estão na pasta `dados/`
       4) Entre em contato com o suporte
    
    **P: Não consigo ver alguns módulos. Por quê?**
    R: Verifique se os arquivos Excel correspondentes estão na pasta `dados/` 
    e se possuem o formato correto conforme especificado na aba "Formato dos Dados Excel".
    
    ---
    
    ## 📱 Sobre Dispositivos e Navegadores
    
    **P: O sistema funciona em celulares e tablets?**
    R: Sim! O sistema é responsivo e se adapta a diferentes tamanhos de tela.
    
    **P: Qual navegador devo usar?**
    R: Recomendamos Chrome, Firefox, Safari ou Edge nas versões mais recentes.
    
    **P: Posso usar no Internet Explorer?**
    R: Não recomendamos. Use navegadores modernos para melhor experiência.
    
    ---
    
    ## 🔐 Sobre Segurança e Acesso
    
    **P: Os dados são seguros?**
    R: Sim. O sistema roda localmente e não envia dados para servidores externos.
    
    **P: Quem pode acessar o sistema?**
    R: Apenas usuários com acesso à rede local onde o sistema está instalado.
    
    **P: Preciso fazer login?**
    R: Não. O sistema é de acesso livre dentro da rede autorizada.
    
    ---
    
    ## 📈 Sobre Indicadores e Métricas
    
    **P: O que significa 'Saldo de Admissões'?**
    R: É a diferença entre novos ingressantes e egressos (formados + evadidos) em um período.
    
    **P: Como é calculada a taxa de aprovação?**
    R: (Número de aprovados / Total de matriculados) × 100
    
    **P: O que são 'dados sintéticos'?**
    R: São dados gerados automaticamente para demonstração quando os arquivos reais 
    não estão disponíveis. Eles seguem padrões realistas mas não representam dados reais.
    
    ---
    
    ## 💡 Dicas de Uso
    
    **P: Como posso comparar dados de diferentes anos?**
    R: Use os filtros de período em cada módulo. Alguns gráficos permitem visualização 
    de múltiplos anos simultaneamente.
    
    **P: Posso personalizar as cores dos gráficos?**
    R: As cores seguem o padrão institucional do IFPB. Para personalizações, 
    entre em contato com o suporte técnico.
    
    **P: Como interpretar os gráficos de tendência?**
    R: Linhas ascendentes indicam crescimento, descendentes indicam redução. 
    Passe o mouse sobre os pontos para ver valores exatos.
    """)

def show_contact_support():
    """Seção de contato e suporte"""
    
    st.markdown("""
    # 📞 Contato e Suporte
    
    ## 🏢 Informações Institucionais
    
    **Instituto Federal da Paraíba - Campus Cajazeiras**
    - **Endereço**: Rua José Antônio da Silva, 300 - Jardim Oásis
    - **CEP**: 58900-000 - Cajazeiras/PB
    - **Telefone**: (83) 3532-4100
    - **Site**: [www.ifpb.edu.br/cajazeiras](https://www.ifpb.edu.br/cajazeiras)
    
    ---
    
    ## 👨‍💻 Suporte Técnico do Sistema
    
    ### Núcleo de Assessoria em Informação (NAI)
    - **E-mail**: nai.cajazeiras@ifpb.edu.br
    - **Telefone**: (83) 3532-4100 (Ramal: 4120)
    - **Horário**: Segunda a Sexta, 08h às 17h
    
    ### Coordenação de Tecnologia da Informação (CTI)
    - **E-mail**: cti.cajazeiras@ifpb.edu.br
    - **Telefone**: (83) 3532-4100 (Ramal: 4115)
    - **Horário**: Segunda a Sexta, 07h às 16h
    
    ---
    
    ## 🆘 Para Emergências
    
    ### Problemas Críticos do Sistema
    - **WhatsApp Suporte**: (83) 9 9999-9999 # vai ser atualizado em breve
    - **E-mail Urgente**: nai.cajazeiras@ifpb.edu.br
    - **Disponibilidade**: 24h para problemas críticos
    
    ---
    
    ## 📝 Como Relatar Problemas
    
    ### Informações Necessárias
    Ao entrar em contato, forneça:
    
    1. **Descrição do Problema**
       - O que estava tentando fazer?
       - O que aconteceu de errado?
       - Mensagens de erro (se houver)
    
    2. **Informações Técnicas**
       - Navegador usado (Chrome, Firefox, etc.)
       - Sistema operacional (Windows, Mac, Linux)
       - Hora aproximada do problema
    
    3. **Capturas de Tela**
       - Se possível, anexe prints da tela mostrando o problema
    
    ### Template de E-mail para Suporte
    ```
    Assunto: [DASHBOARD] Problema em [Nome do Módulo]
    
    Olá,
    
    Estou enfrentando o seguinte problema no Dashboard IFPB-CZ:
    
    DESCRIÇÃO:
    [Descreva o que aconteceu]
    
    PASSOS PARA REPRODUZIR:
    1. [Primeiro passo]
    2. [Segundo passo]
    3. [Terceiro passo]
    
    RESULTADO ESPERADO:
    [O que deveria acontecer]
    
    RESULTADO ATUAL:
    [O que realmente aconteceu]
    
    INFORMAÇÕES TÉCNICAS:
    - Navegador: [Chrome/Firefox/etc.]
    - Sistema: [Windows/Mac/Linux]
    - Horário: [DD/MM/AAAA HH:MM]
    
    Obrigado(a),
    [Seu nome]
    [Seu setor/função]
    ```
    
    ---
    
    ## 🎓 Treinamento e Capacitação
    
    ### Workshops Disponíveis
    - **Uso Básico do Dashboard**: 2h - Toda segunda terça-feira do mês
    - **Interpretação de Dados**: 4h - Primeira sexta-feira do mês
    - **Gestão de Dados Excel**: 3h - Sob demanda
    
    ### Inscrições
    - **E-mail**: nai.cajazeiras@ifpb.edu.br
    - **Telefone**: (83) 3532-4100 (Ramal: 4125)
    
    ---
    
    ## 📚 Recursos Adicionais
    
    ### Documentação Técnica
    - **Manual do Administrador**: Disponível na pasta `docs/`
    - **Código Fonte**: [GitHub Repository](https://github.com/MichelZero/ifpbcz-numeros)
    - **Changelog**: Histórico de atualizações no README.md
    
    ### Tutoriais em Vídeo
    - **Canal YouTube**: [IFPB Cajazeiras - Tutoriais](https://youtube.com/@ifpbcajazeiras)
    - **Playlist Dashboard**: Tutoriais específicos do sistema
    
    ---
    
    ## 🔄 Atualizações e Manutenção
    
    ### Horários de Manutenção Programada
    - **Diária**: 02h às 03h (backup automático)
    - **Semanal**: Domingo, 01h às 04h (atualizações menores)
    - **Mensal**: Primeira segunda-feira, 18h às 22h (atualizações maiores)
    
    ### Notificações de Manutenção
    - **E-mail**: Enviado com 48h de antecedência
    - **Sistema**: Banner de aviso na página principal
    - **WhatsApp**: Grupos de usuários cadastrados
    
    ---
    
    ## ⭐ Feedback e Sugestões
    
    Sua opinião é importante! Entre em contato para:
    - Sugerir melhorias
    - Reportar bugs
    - Solicitar novas funcionalidades
    - Compartilhar casos de sucesso
    
    **E-mail Feedback**: feedback.dashboard@ifpb.edu.br
    
    ---
    
    ## 🏆 Créditos
    
    **Desenvolvimento**: Núcleo de Assessoria em Informação (NAI/IFPB-CZ)
    **Coordenação**: Prof. Teodomiro Alves de Lira Neto
    **Equipe Técnica**: NAI - IFPB Cajazeiras
    **Versão**: 2.0 - Dashboard Institucional Completo
    **Data**: Julho 2025
    """)
    
    # Informações de contato em destaque
    st.info("""
    🆘 **SUPORTE RÁPIDO**
    
    📧 **E-mail**: nai.cajazeiras@ifpb.edu.br
    📞 **Telefone**: (83) 3532-4100 (Ramal: 4120)
    💬 **WhatsApp**: (83) 9 9999-9999 (Emergências)
    🕒 **Horário**: Segunda a Sexta, 08h às 17h
    """)
    
    # display_footer() estava duplicado, removido para evitar redundância. 28/07/2025