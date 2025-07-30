import streamlit as st
from .utils import display_header_with_logo, display_footer

def show_help():
    """Página de ajuda com especificações dos formatos de dados Excel"""
    
    display_header_with_logo("Ajuda - Formato dos Dados Excel")
    
    st.markdown("""
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
    
    display_footer()