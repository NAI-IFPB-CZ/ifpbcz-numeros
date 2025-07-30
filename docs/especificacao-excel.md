# Especificação Técnica - Formato dos Arquivos Excel

## 📋 Visão Geral

Este documento detalha as especificações técnicas para os arquivos Excel (.xlsx) utilizados pelo Dashboard IFPB-CZ. Cada módulo do sistema requer um arquivo específico com estrutura padronizada.

## 📁 Estrutura de Arquivos Obrigatória

### Localização
Todos os arquivos devem estar na pasta: `dados/`

### Nomenclatura dos Arquivos
- `dados_ensino.xlsx` - Módulo de Ensino
- `dados_assistencia.xlsx` - Módulo de Assistência Estudantil  
- `dados_pesquisa.xlsx` - Módulo de Pesquisa
- `dados_extensao.xlsx` - Módulo de Extensão
- `dados_orcamento.xlsx` - Módulo de Orçamento
- `dados_servidores.xlsx` - Módulo de Servidores
- `dados_ouvidoria.xlsx` - Módulo de Ouvidoria
- `dados_auditoria.xlsx` - Módulo de Auditoria
- `dados_mundo_trabalho.xlsx` - Módulo do Mundo do Trabalho

## 📊 Estrutura das Planilhas

### Planilhas Obrigatórias em Cada Arquivo
1. **Planilha de Dados**: Nome específico conforme detalhado abaixo
2. **Planilha de Metadados**: Criada automaticamente pelo sistema

### Regras Gerais
- **Primeira linha**: Sempre contém os cabeçalhos das colunas
- **Dados**: A partir da segunda linha
- **Células vazias**: Não são permitidas - usar 0 para números ou "N/A" para texto
- **Encoding**: UTF-8
- **Separador decimal**: Ponto (.)

---

## 📚 Especificações por Módulo

### 🎓 Módulo de Ensino

**Arquivo**: `dados_ensino.xlsx`  
**Planilha**: `Dados_Ensino`

| Coluna | Tipo | Obrigatório | Descrição | Valores Aceitos | Exemplo |
|--------|------|-------------|-----------|-----------------|---------|
| `ano` | Inteiro | ✅ | Ano do registro | 2020-2030 | 2024 |
| `curso` | Texto | ✅ | Nome do curso | Texto livre | "Técnico em Informática" |
| `matriculados` | Inteiro | ✅ | Alunos matriculados | ≥ 0 | 85 |
| `formados` | Inteiro | ✅ | Alunos formados | ≥ 0 | 42 |
| `desistentes` | Inteiro | ✅ | Número de desistentes | ≥ 0 | 8 |
| `transferidos` | Inteiro | ✅ | Número de transferidos | ≥ 0 | 3 |
| `modalidade` | Texto | ✅ | Modalidade do curso | "Integrado", "Subsequente", "Concomitante" | "Integrado" |
| `turno` | Texto | ✅ | Turno de funcionamento | "Matutino", "Vespertino", "Noturno" | "Matutino" |
| `semestre` | Inteiro | ✅ | Semestre | 1 ou 2 | 1 |
| `campus` | Texto | ✅ | Campus | Texto livre | "Cajazeiras" |
| `aprovacao_percentual` | Decimal | ❌ | Percentual de aprovação | 0.0 - 100.0 | 85.5 |
| `reprovacao_percentual` | Decimal | ❌ | Percentual de reprovação | 0.0 - 100.0 | 14.5 |
| `nota_media` | Decimal | ❌ | Nota média da turma | 0.0 - 10.0 | 7.8 |

---

### 🤝 Módulo de Assistência Estudantil

**Arquivo**: `dados_assistencia.xlsx`  
**Planilha**: `Dados_Assistencia`

| Coluna | Tipo | Obrigatório | Descrição | Valores Aceitos | Exemplo |
|--------|------|-------------|-----------|-----------------|---------|
| `ano` | Inteiro | ✅ | Ano do registro | 2020-2030 | 2024 |
| `mes` | Inteiro | ✅ | Mês | 1-12 | 6 |
| `unidade` | Texto | ✅ | Unidade/Campus | Texto livre | "Campus Cajazeiras" |
| `programa` | Texto | ✅ | Programa de assistência | Texto livre | "Auxílio Alimentação" |
| `nivel_curso` | Texto | ✅ | Nível do curso | "Técnico", "Superior" | "Técnico" |
| `parcelas` | Inteiro | ✅ | Parcelas pagas | ≥ 0 | 45 |
| `alunos_beneficiados` | Inteiro | ✅ | Alunos beneficiados | ≥ 0 | 42 |
| `valor_total` | Decimal | ✅ | Valor total em reais | ≥ 0.00 | 18500.00 |
| `faixa_idade` | Texto | ❌ | Faixa etária | "16-20", "21-25", "26-30", "31+" | "16-20" |
| `genero` | Texto | ❌ | Gênero | "Masculino", "Feminino" | "Masculino" |

---

### 🔬 Módulo de Pesquisa

**Arquivo**: `dados_pesquisa.xlsx`  
**Planilha**: `Dados_Pesquisa`

| Coluna | Tipo | Obrigatório | Descrição | Valores Aceitos | Exemplo |
|--------|------|-------------|-----------|-----------------|---------|
| `ano` | Inteiro | ✅ | Ano do registro | 2020-2030 | 2024 |
| `unidade` | Texto | ✅ | Unidade/Campus | Texto livre | "Campus Cajazeiras" |
| `area_conhecimento` | Texto | ✅ | Área do conhecimento | Texto livre | "Ciências Exatas" |
| `tipo_projeto` | Texto | ✅ | Tipo de projeto | "PIBIC", "PIVIC", "PIBITI", "Outro" | "PIBIC" |
| `projetos_ativos` | Inteiro | ✅ | Projetos em andamento | ≥ 0 | 15 |
| `projetos_concluidos` | Inteiro | ✅ | Projetos finalizados | ≥ 0 | 8 |
| `bolsistas` | Inteiro | ✅ | Número de bolsistas | ≥ 0 | 12 |
| `voluntarios` | Inteiro | ✅ | Número de voluntários | ≥ 0 | 5 |
| `publicacoes` | Inteiro | ❌ | Número de publicações | ≥ 0 | 3 |
| `orientadores` | Inteiro | ❌ | Número de orientadores | ≥ 0 | 6 |
| `valor_investido` | Decimal | ❌ | Valor investido | ≥ 0.00 | 45000.00 |

---

### 🌟 Módulo de Extensão

**Arquivo**: `dados_extensao.xlsx`  
**Planilha**: `Dados_Extensao`

| Coluna | Tipo | Obrigatório | Descrição | Valores Aceitos | Exemplo |
|--------|------|-------------|-----------|-----------------|---------|
| `ano` | Inteiro | ✅ | Ano do registro | 2020-2030 | 2024 |
| `unidade` | Texto | ✅ | Unidade/Campus | Texto livre | "Campus Cajazeiras" |
| `area_tematica` | Texto | ✅ | Área temática | "Educação", "Saúde", "Tecnologia", "Cultura", "Meio Ambiente", "Trabalho", "Justiça", "Direitos Humanos" | "Educação" |
| `tipo_acao` | Texto | ✅ | Tipo de ação | "Curso", "Evento", "Projeto", "Prestação de Serviços" | "Curso" |
| `titulo` | Texto | ✅ | Título da ação | Texto livre | "Curso de Informática Básica" |
| `participantes_internos` | Inteiro | ✅ | Participantes do IFPB | ≥ 0 | 25 |
| `participantes_externos` | Inteiro | ✅ | Participantes da comunidade | ≥ 0 | 80 |
| `carga_horaria` | Inteiro | ✅ | Carga horária total | ≥ 0 | 40 |
| `coordenador` | Texto | ❌ | Nome do coordenador | Texto livre | "Prof. João Silva" |
| `status` | Texto | ✅ | Status da ação | "Concluído", "Em andamento", "Planejado", "Cancelado" | "Concluído" |

---

### 💰 Módulo de Orçamento

**Arquivo**: `dados_orcamento.xlsx`  
**Planilha**: `Dados_Orcamento`

| Coluna | Tipo | Obrigatório | Descrição | Valores Aceitos | Exemplo |
|--------|------|-------------|-----------|-----------------|---------|
| `ano` | Inteiro | ✅ | Ano do registro | 2020-2030 | 2024 |
| `mes` | Inteiro | ✅ | Mês | 1-12 | 6 |
| `unidade` | Texto | ✅ | Unidade/Campus | Texto livre | "Campus Cajazeiras" |
| `categoria` | Texto | ✅ | Categoria orçamentária | "Custeio", "Investimentos", "Pessoal" | "Custeio" |
| `subcategoria` | Texto | ✅ | Subcategoria | Texto livre | "Material de Consumo" |
| `valor_orcado` | Decimal | ✅ | Valor orçado | ≥ 0.00 | 150000.00 |
| `valor_empenhado` | Decimal | ✅ | Valor empenhado | ≥ 0.00 | 120000.00 |
| `valor_liquidado` | Decimal | ✅ | Valor liquidado | ≥ 0.00 | 100000.00 |
| `valor_pago` | Decimal | ✅ | Valor pago | ≥ 0.00 | 95000.00 |
| `fonte_recurso` | Texto | ✅ | Fonte do recurso | "Tesouro", "Próprios", "Convênios", "Emendas" | "Tesouro" |

---

### 👥 Módulo de Servidores

**Arquivo**: `dados_servidores.xlsx`  
**Planilha**: `Dados_Servidores`

| Coluna | Tipo | Obrigatório | Descrição | Valores Aceitos | Exemplo |
|--------|------|-------------|-----------|-----------------|---------|
| `ano` | Inteiro | ✅ | Ano do registro | 2020-2030 | 2024 |
| `mes` | Inteiro | ✅ | Mês | 1-12 | 6 |
| `unidade` | Texto | ✅ | Unidade/Campus | Texto livre | "Campus Cajazeiras" |
| `categoria` | Texto | ✅ | Categoria do servidor | "Docente", "Técnico-Administrativo" | "Docente" |
| `regime_trabalho` | Texto | ✅ | Regime de trabalho | "Dedicação Exclusiva", "40h", "20h" | "Dedicação Exclusiva" |
| `situacao` | Texto | ✅ | Situação funcional | "Ativo", "Licença", "Afastado", "Aposentado" | "Ativo" |
| `titulacao` | Texto | ✅ | Titulação | "Ensino Médio", "Graduação", "Especialização", "Mestrado", "Doutorado" | "Mestrado" |
| `faixa_etaria` | Texto | ✅ | Faixa etária | "20-30", "31-40", "41-50", "51-60", "60+" | "31-40" |
| `genero` | Texto | ✅ | Gênero | "Masculino", "Feminino" | "Masculino" |
| `quantidade` | Inteiro | ✅ | Quantidade de servidores | ≥ 1 | 1 |

---

### 📢 Módulo de Ouvidoria

**Arquivo**: `dados_ouvidoria.xlsx`  
**Planilha**: `Dados_Ouvidoria`

| Coluna | Tipo | Obrigatório | Descrição | Valores Aceitos | Exemplo |
|--------|------|-------------|-----------|-----------------|---------|
| `ano` | Inteiro | ✅ | Ano do registro | 2020-2030 | 2024 |
| `mes` | Inteiro | ✅ | Mês | 1-12 | 6 |
| `unidade` | Texto | ✅ | Unidade/Campus | Texto livre | "Campus Cajazeiras" |
| `tipo_manifestacao` | Texto | ✅ | Tipo de manifestação | "Reclamação", "Sugestão", "Elogio", "Denúncia", "Informação" | "Reclamação" |
| `assunto` | Texto | ✅ | Assunto da manifestação | "Ensino", "Infraestrutura", "Serviços", "Atendimento", "Outro" | "Ensino" |
| `canal` | Texto | ✅ | Canal de atendimento | "Sistema", "Presencial", "Telefone", "E-mail", "Carta" | "Sistema" |
| `status` | Texto | ✅ | Status da manifestação | "Aberta", "Em análise", "Concluída", "Arquivada" | "Concluída" |
| `tipo_usuario` | Texto | ✅ | Tipo do usuário | "Estudante", "Servidor", "Comunidade", "Outro" | "Estudante" |
| `prazo_resposta` | Inteiro | ❌ | Prazo para resposta (dias) | ≥ 0 | 10 |
| `satisfacao` | Inteiro | ❌ | Nível de satisfação | 1-5 | 4 |

---

### 🔍 Módulo de Auditoria

**Arquivo**: `dados_auditoria.xlsx`  
**Planilha**: `Dados_Auditoria`

| Coluna | Tipo | Obrigatório | Descrição | Valores Aceitos | Exemplo |
|--------|------|-------------|-----------|-----------------|---------|
| `ano` | Inteiro | ✅ | Ano do registro | 2020-2030 | 2024 |
| `mes` | Inteiro | ✅ | Mês | 1-12 | 6 |
| `unidade` | Texto | ✅ | Unidade/Campus | Texto livre | "Campus Cajazeiras" |
| `tipo_auditoria` | Texto | ✅ | Tipo de auditoria | "Financeira", "Gestão", "Conformidade", "Operacional" | "Financeira" |
| `origem` | Texto | ✅ | Origem da auditoria | "Interna", "Externa", "CGU", "TCU" | "Interna" |
| `status` | Texto | ✅ | Status da auditoria | "Iniciada", "Em andamento", "Concluída", "Cancelada" | "Concluída" |
| `recomendacoes` | Inteiro | ✅ | Número de recomendações | ≥ 0 | 5 |
| `recomendacoes_atendidas` | Inteiro | ✅ | Recomendações atendidas | ≥ 0 | 3 |
| `prazo_atendimento` | Inteiro | ❌ | Prazo para atendimento (dias) | ≥ 0 | 90 |
| `risco_nivel` | Texto | ✅ | Nível de risco | "Baixo", "Médio", "Alto", "Crítico" | "Médio" |

---

### 💼 Módulo do Mundo do Trabalho

**Arquivo**: `dados_mundo_trabalho.xlsx`  
**Planilha**: `Dados_Mundo_Trabalho`

| Coluna | Tipo | Obrigatório | Descrição | Valores Aceitos | Exemplo |
|--------|------|-------------|-----------|-----------------|---------|
| `ano` | Inteiro | ✅ | Ano do registro | 2020-2030 | 2024 |
| `unidade` | Texto | ✅ | Unidade/Campus | Texto livre | "Campus Cajazeiras" |
| `curso` | Texto | ✅ | Curso de origem | Texto livre | "Técnico em Informática" |
| `situacao_profissional` | Texto | ✅ | Situação atual | "Empregado", "Desempregado", "Estudando", "Empreendedor" | "Empregado" |
| `setor_atividade` | Texto | ❌ | Setor de atividade | "Tecnologia", "Educação", "Saúde", "Indústria", "Comércio", "Serviços", "Público" | "Tecnologia" |
| `salario_faixa` | Texto | ❌ | Faixa salarial | "Até 1 SM", "1-2 SM", "2-3 SM", "3-5 SM", "5+ SM" | "2-3 SM" |
| `tipo_vinculo` | Texto | ❌ | Tipo de vínculo | "CLT", "Estágio", "Autônomo", "Concursado", "Temporário" | "CLT" |
| `tempo_conclusao` | Inteiro | ✅ | Anos desde a conclusão | ≥ 0 | 2 |
| `continua_estudando` | Texto | ✅ | Continua estudando | "Sim", "Não" | "Sim" |
| `trabalha_area_formacao` | Texto | ✅ | Trabalha na área | "Sim", "Não", "Parcialmente" | "Sim" |

---

## ⚠️ Regras de Validação

### Regras Gerais
1. **Nomes das colunas**: Exatamente como especificado (case-sensitive)
2. **Ordem das colunas**: Não importa, mas recomenda-se seguir a tabela
3. **Linhas vazias**: Não são permitidas no meio dos dados
4. **Cabeçalhos**: Sempre na primeira linha
5. **Formato de arquivo**: Excel (.xlsx) - não usar .xls

### Validações por Tipo
- **Inteiro**: Números inteiros sem decimais (ex: 10, 0, 250)
- **Decimal**: Números com até 2 casas decimais (ex: 10.50, 0.00, 1234.99)
- **Texto**: Qualquer caractere, máximo 255 caracteres por célula
- **Data**: Formato YYYY-MM-DD (ex: 2024-06-15)

### Valores Especiais
- **Células vazias**: Usar 0 para números, "N/A" para texto
- **Valores nulos**: Não são aceitos
- **Números negativos**: Apenas onde explicitamente permitido

---

## 📝 Exemplo Prático

### Arquivo: dados_ensino.xlsx - Planilha: Dados_Ensino

```
| ano | curso                    | matriculados | formados | desistentes | transferidos | modalidade   | turno    | semestre | campus     | aprovacao_percentual | reprovacao_percentual | nota_media |
|-----|--------------------------|--------------|----------|-------------|--------------|--------------|----------|----------|------------|---------------------|----------------------|------------|
| 2024| Técnico em Informática   | 85           | 42       | 8           | 3            | Integrado    | Matutino | 1        | Cajazeiras | 85.5                | 14.5                 | 7.8        |
| 2024| Técnico em Eletrotécnica | 73           | 38       | 5           | 2            | Integrado    | Vespertino| 1        | Cajazeiras | 89.2                | 10.8                 | 8.1        |
| 2024| Superior em Sistemas     | 45           | 22       | 3           | 1            | Superior     | Noturno  | 2        | Cajazeiras | 92.3                | 7.7                  | 8.5        |
```

---

## 🔄 Processo de Atualização

### Passos para Atualizar Dados
1. **Backup**: Faça cópia do arquivo atual
2. **Edição**: Modifique os dados seguindo as especificações
3. **Validação**: Verifique formatos e valores obrigatórios
4. **Substituição**: Coloque o novo arquivo na pasta `dados/`
5. **Teste**: Reinicie o sistema e verifique se carregou corretamente

### Verificação de Erros
O sistema exibirá mensagens de erro se:
- Arquivo não encontrado
- Colunas obrigatórias ausentes
- Tipos de dados incorretos
- Valores fora dos intervalos permitidos

---

## 📞 Suporte Técnico

Para dúvidas sobre a formatação dos dados:
- **E-mail**: nai.cajazeiras@ifpb.edu.br
- **Telefone**: (83) 3532-4100 (Ramal: 4120)

*Documento técnico elaborado pelo NAI/IFPB-CZ*  
*Versão: 2.0 | Última atualização: Julho 2025*
