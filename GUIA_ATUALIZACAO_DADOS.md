# 📊 Guia Completo: Atualização de Dados Reais no Dashboard IFPB-CZ

## 🎯 Objetivo

Este guia ensina como atualizar o sistema Dashboard IFPB-CZ com dados reais das planilhas Excel, substituindo completamente os dados sintéticos gerados automaticamente, seguindo as melhores práticas de segurança.

## 📋 Pré-requisitos

- ✅ Sistema Dashboard IFPB-CZ instalado e funcionando
- ✅ Microsoft Excel ou LibreOffice Calc
- ✅ Dados institucionais organizados por módulos
- ✅ Acesso à pasta do projeto
- ✅ Conhecimento básico das configurações de segurança

## 🔒 Configurações de Segurança

### ⚠️ **IMPORTANTE: Configurações Padrão**

O sistema está configurado por padrão com proteções de segurança ativadas:

```python
# Configurações de segurança (config.py)
PERMITIR_CRIACAO_PLANILHAS = False      # Impede criação automática
SOBRESCREVER_ARQUIVOS_EXISTENTES = False # Protege arquivos existentes
MODO_SOMENTE_LEITURA = True             # Modo somente leitura
```

### 🛡️ **Verificar Configurações Atuais**

Antes de começar, verifique as configurações:

```bash
# Verificar configurações atuais
python configurar_seguranca.py status

# Testar configurações de segurança
python testar_seguranca.py
```

## 🗂️ Estrutura de Dados Necessária

### 📁 Diretório de Dados

```text
ifpbcz-numeros/
├── dados/
│   ├── dados_assistencia.xlsx
│   ├── dados_auditoria.xlsx
│   ├── dados_ensino.xlsx
│   ├── dados_extensao.xlsx
│   ├── dados_mundo_trabalho.xlsx
│   ├── dados_orcamento.xlsx
│   ├── dados_ouvidoria.xlsx
│   ├── dados_pesquisa.xlsx
│   └── dados_servidores.xlsx
└── modules/
    └── data_generator.py
```

## 🔧 Passo a Passo Detalhado

### 1️⃣ Configuração Inicial de Segurança

#### 🔒 **Verificar Configurações Atuais**

```bash
# Verificar configurações atuais
python configurar_seguranca.py status

# Resultado esperado (modo seguro):
# PERMITIR_CRIACAO_PLANILHAS = False
# SOBRESCREVER_ARQUIVOS_EXISTENTES = False
# MODO_SOMENTE_LEITURA = True
```

#### 🛡️ **Configuração Recomendada para Atualização**

Para atualizar dados com segurança, altere no arquivo `config.py`:

```python
# Configuração recomendada para atualização de dados
USE_REAL_DATA = True                    # Usar dados reais
PERMITIR_CRIACAO_PLANILHAS = False      # Manter proteção
SOBRESCREVER_ARQUIVOS_EXISTENTES = False # Manter proteção
MODO_SOMENTE_LEITURA = True             # Modo somente leitura
VALIDAR_DADOS = True                    # Validar dados
```

### 2️⃣ Preparação dos Arquivos Excel

#### 📚 **dados_ensino.xlsx**

**Descrição**: Dados de matriculados, formados, desistentes e transferidos por campus/curso

**Colunas obrigatórias**:

| Coluna | Tipo | Exemplo | Descrição |
|--------|------|---------|-----------|
| `ano` | Número | 2024 | Ano de referência |
| `campus` | Texto | "IFPB - Campus Campina Grande" | Nome completo do campus |
| `curso` | Texto | "Técnico em Informática" | Nome do curso |
| `modalidade` | Texto | "Presencial" | Modalidade do curso |
| `matriculados` | Número | 150 | Número de alunos matriculados |
| `formados` | Número | 120 | Número de alunos formados |
| `desistentes` | Número | 25 | Número de desistentes |
| `transferidos` | Número | 5 | Número de transferidos |

**Exemplo de dados**:

```text
ano | campus                    | curso                  | modalidade | matriculados | formados | desistentes | transferidos
2024| IFPB - Campus CG         | Técnico em Informática | Presencial | 150          | 120      | 25          | 5
2024| IFPB - Campus Cajazeiras | Técnico em Eletrônica  | Presencial | 80           | 65       | 12          | 3
```

---

#### 📚 **dados_extensao.xlsx**
**Descrição**: Dados de estágios concluídos e ingressantes com necessidades especiais

**Colunas obrigatórias**:
| Coluna | Tipo | Exemplo | Descrição |
|--------|------|---------|-----------|
| `ano` | Número | 2024 | Ano de referência |
| `unidade` | Texto | "IFPB - Campus Campina Grande" | Nome da unidade |
| `curso` | Texto | "Técnico em Informática" | Nome do curso |
| `modalidade` | Texto | "Presencial" | Modalidade do curso |
| `genero` | Texto | "Masculino" | Gênero dos estudantes |
| `estagios_concluidos` | Número | 45 | Número de estágios concluídos |
| `pne_ingressantes` | Número | 3 | Ingressantes com necessidades especiais |
| `tipo_necessidade` | Texto | "Física" | Tipo de necessidade especial |

---

#### 📚 **dados_pesquisa.xlsx**
**Descrição**: Dados de publicações acadêmicas e pesquisas

**Colunas obrigatórias**:
| Coluna | Tipo | Exemplo | Descrição |
|--------|------|---------|-----------|
| `ano` | Número | 2024 | Ano de referência |
| `tipo_publicacao` | Texto | "Artigos" | Tipo de publicação |
| `quantidade` | Número | 25 | Quantidade de publicações |
| `area_conhecimento` | Texto | "Ciências Exatas" | Área do conhecimento |

**Tipos de publicação aceitos**:

- `"Artigos"`
- `"Capítulos de Livros"`
- `"Trabalhos em Eventos"`

---

#### 📚 **dados_assistencia.xlsx**
**Descrição**: Dados de assistência estudantil e auxílios

**Colunas obrigatórias**:
| Coluna | Tipo | Exemplo | Descrição |
|--------|------|---------|-----------|
| `ano` | Número | 2024 | Ano de referência |
| `campus` | Texto | "IFPB - Campus Campina Grande" | Nome do campus |
| `auxilio_tipo` | Texto | "Auxílio Alimentação" | Tipo de auxílio |
| `beneficiarios` | Número | 450 | Número de beneficiários |
| `valor_total` | Número | 180000.00 | Valor total investido |

---

#### 📚 **dados_auditoria.xlsx**
**Descrição**: Dados de auditorias internas e externas

**Colunas obrigatórias**:
| Coluna | Tipo | Exemplo | Descrição |
|--------|------|---------|-----------|
| `ano` | Número | 2024 | Ano de referência |
| `tipo_auditoria` | Texto | "Auditoria Interna" | Tipo de auditoria |
| `numero_auditorias` | Número | 12 | Número de auditorias realizadas |
| `recomendacoes` | Número | 45 | Número de recomendações |

---

#### 📚 **dados_mundo_trabalho.xlsx**
**Descrição**: Dados de empregabilidade e salários dos egressos

**Colunas obrigatórias**:
| Coluna | Tipo | Exemplo | Descrição |
|--------|------|---------|-----------|
| `ano` | Número | 2024 | Ano de referência |
| `campus` | Texto | "IFPB - Campus Campina Grande" | Nome do campus |
| `curso` | Texto | "Técnico em Informática" | Nome do curso |
| `empregabilidade` | Número | 85.5 | Taxa de empregabilidade (%) |
| `salario_medio` | Número | 2850.00 | Salário médio dos egressos |

---

#### 📚 **dados_orcamento.xlsx**
**Descrição**: Dados orçamentários e execução financeira

**Colunas obrigatórias**:
| Coluna | Tipo | Exemplo | Descrição |
|--------|------|---------|-----------|
| `ano` | Número | 2024 | Ano de referência |
| `categoria` | Texto | "Custeio" | Categoria orçamentária |
| `valor_orcado` | Número | 5500000.00 | Valor orçado |
| `valor_executado` | Número | 5350000.00 | Valor executado |

---

#### 📚 **dados_ouvidoria.xlsx**
**Descrição**: Dados de manifestações da ouvidoria

**Colunas obrigatórias**:
| Coluna | Tipo | Exemplo | Descrição |
|--------|------|---------|-----------|
| `ano` | Número | 2024 | Ano de referência |
| `tipo_manifestacao` | Texto | "Reclamação" | Tipo de manifestação |
| `quantidade` | Número | 85 | Quantidade de manifestações |
| `status` | Texto | "Resolvido" | Status da manifestação |

---

#### 📚 **dados_servidores.xlsx**
**Descrição**: Dados de servidores por campus e categoria

**Colunas obrigatórias**:
| Coluna | Tipo | Exemplo | Descrição |
|--------|------|---------|-----------|
| `ano` | Número | 2024 | Ano de referência |
| `campus` | Texto | "IFPB - Campus Campina Grande" | Nome do campus |
| `categoria` | Texto | "Docente" | Categoria do servidor |
| `quantidade` | Número | 125 | Quantidade de servidores |
| `genero` | Texto | "Masculino" | Gênero do servidor |

---

### 3️⃣ Método Recomendado: Substituição Direta de Arquivos

#### � **Processo Seguro (Método Recomendado)**

**⚠️ Este é o método mais seguro e recomendado para atualização de dados:**

1. **Backup dos dados atuais**:
   ```bash
   # Fazer backup da pasta dados
   cp -r dados dados_backup_$(date +%Y%m%d)
   ```

2. **Preparar os novos arquivos Excel**:
   - Siga as especificações de colunas detalhadas abaixo
   - Valide os dados antes da substituição
   - Mantenha os nomes exatos dos arquivos

3. **Substituir os arquivos**:
   ```bash
   # Substituir arquivos na pasta dados/
   # Manter nomes exatos: dados_ensino.xlsx, dados_pesquisa.xlsx, etc.
   ```

4. **Verificar a atualização**:
   ```bash
   # Testar o sistema
   python testar_seguranca.py
   streamlit run app.py
   ```

#### � **Método Alternativo (Apenas para Desenvolvimento)**

Se você precisar modificar o código do sistema (não recomendado para produção):

1. **Alterar configurações de segurança temporariamente**:
   ```bash
   python configurar_seguranca.py edicao
   ```

2. **Fazer modificações necessárias**

3. **Restaurar configurações de segurança**:
   ```bash
   python configurar_seguranca.py seguro
   ```

### 4️⃣ Especificações Detalhadas dos Arquivos Excel

### 5️⃣ Validação e Teste

#### 🔍 **Validação com Ferramentas de Segurança**

**1. Testar configurações de segurança:**

```bash
# Executar teste completo de segurança
python testar_seguranca.py
```

**2. Verificar carregamento de dados:**

```bash
# Executar o sistema
streamlit run app.py

# Verificar no navegador
# http://localhost:8501
```

#### ✅ **Checklist de Validação**

1. **Configurações de segurança**:
   - [ ] Configurações de segurança ativadas (`python configurar_seguranca.py status`)
   - [ ] Teste de segurança passou (`python testar_seguranca.py`)
   - [ ] Modo somente leitura ativado

2. **Estrutura dos arquivos Excel**:
   - [ ] Todas as colunas obrigatórias presentes
   - [ ] Tipos de dados corretos (números, texto, datas)
   - [ ] Sem valores vazios em colunas críticas

3. **Consistência dos dados**:
   - [ ] Anos coerentes (não futuro demais)
   - [ ] Valores numéricos não negativos
   - [ ] Nomes de campus padronizados

4. **Funcionamento do sistema**:
   - [ ] Dashboard carrega sem erros
   - [ ] Gráficos exibem dados corretos
   - [ ] Filtros funcionam adequadamente
   - [ ] Sem mensagens de erro de segurança

#### 🚨 **Mensagens de Segurança**

Se você vir estas mensagens, é normal (configuração segura):

- ⚠️ `Modo somente leitura ativado`
- ⚠️ `Criação de planilhas desabilitada`
- ⚠️ `Sobrescrita está desabilitada`

### 6️⃣ Atualização Periódica

#### 📅 **Rotina de Atualização**

1. **Mensalmente**:
   - Atualize dados de ensino
   - Atualize dados de assistência
   - Atualize dados de ouvidoria

2. **Trimestralmente**:
   - Atualize dados de pesquisa
   - Atualize dados de extensão
   - Atualize dados de mundo do trabalho

3. **Semestralmente**:
   - Atualize dados de orçamento
   - Atualize dados de auditoria
   - Atualize dados de servidores

#### 🔄 **Processo de Atualização Segura**

1. **Verificar configurações de segurança**:

   ```bash
   # Verificar se está em modo seguro
   python configurar_seguranca.py status
   ```

2. **Backup dos dados atuais**:

   ```bash
   # Criar backup com timestamp
   cp -r dados dados_backup_$(date +%Y%m%d_%H%M%S)
   ```

3. **Atualização dos arquivos Excel**:
   - Substitua os arquivos na pasta `dados/`
   - Mantenha os nomes exatos dos arquivos
   - Não altere as configurações de segurança

4. **Teste do sistema**:

   ```bash
   # Testar configurações de segurança
   python testar_seguranca.py
   
   # Executar o dashboard
   streamlit run app.py
   ```

5. **Validação dos dados**:
   - Compare com período anterior
   - Verifique consistência dos números
   - Teste filtros e interações
   - Confirme que não há erros de segurança

#### 📋 **Log de Atualização**

Mantenha um registro de atualizações:

```text
Data: ___________
Arquivos atualizados: ___________
Período dos dados: ___________
Responsável: ___________
Observações: ___________
```

## 🚨 Solução de Problemas

### 🔒 **Problemas de Segurança**

#### ❌ **Erro: Modo somente leitura ativado**

```text
⚠️ AVISO: Modo somente leitura ativado
```

**Solução**: Isso é normal e indica que o sistema está protegido. Para verificar:

```bash
python configurar_seguranca.py status
```

#### ❌ **Erro: Criação de planilhas desabilitada**

```text
⚠️ AVISO: Criação de planilhas desabilitada
```

**Solução**: Configure `USE_REAL_DATA = True` no `config.py` e substitua os arquivos diretamente.

#### ❌ **Erro: Sobrescrita desabilitada**

```text
⚠️ AVISO: Sobrescrita está desabilitada
```

**Solução**: Isso protege seus dados. Substitua os arquivos manualmente na pasta `dados/`.

### 📁 **Problemas de Arquivos**

#### ❌ **Erro: Arquivo não encontrado**

```text
FileNotFoundError: dados_ensino.xlsx
```

**Solução**: Verifique se o arquivo está na pasta `dados/` com o nome exato.

#### ❌ **Erro: Coluna não encontrada**

```text
ValueError: Coluna 'matriculados' não encontrada
```

**Solução**: Verifique se todas as colunas obrigatórias estão presentes no Excel.

#### ❌ **Erro: Tipo de dados incorreto**

```text
TypeError: Cannot convert string to int
```

**Solução**: Verifique se colunas numéricas contêm apenas números.

### 🖥️ **Problemas do Sistema**

#### ❌ **Dashboard não carrega**

```text
Streamlit error
```

**Solução**:

1. Verifique o terminal para mensagens de erro
2. Execute `python testar_seguranca.py`
3. Confirme que todos os arquivos Excel estão presentes
4. Reinicie o servidor Streamlit

#### ❌ **Dados não aparecem**

**Solução**:

1. Verifique se `USE_REAL_DATA = True` no `config.py`
2. Confirme que os arquivos Excel estão na pasta `dados/`
3. Execute `python testar_seguranca.py` para diagnóstico

## 📞 Suporte e Manutenção

### 🔧 **Ferramentas de Manutenção**

#### **Scripts de Gerenciamento**

```bash
# Verificar configurações atuais
python configurar_seguranca.py status

# Alterar para modo seguro (recomendado)
python configurar_seguranca.py seguro

# Alterar para modo edição (apenas desenvolvimento)
python configurar_seguranca.py edicao

# Testar configurações de segurança
python testar_seguranca.py
```

#### **Verificações de Rotina**

```bash
# Verificação semanal
python testar_seguranca.py

# Verificação mensal (antes de atualizações)
python configurar_seguranca.py status
python testar_seguranca.py

# Backup trimestral
cp -r dados dados_backup_trimestral_$(date +%Y%m%d)
```

### 🔒 **Manutenção Preventiva**

- **Semanal**: Verificar configurações de segurança
- **Mensal**: Backup dos dados e teste completo
- **Trimestral**: Validação completa da estrutura
- **Semestral**: Revisão das configurações e documentação

### 📋 **Logs de Auditoria**

Mantenha um registro de:

- Cada atualização de dados (data, arquivos, responsável)
- Problemas encontrados e soluções aplicadas
- Mudanças nas configurações de segurança
- Histórico de backups realizados

### 📖 **Documentação**

- Mantenha este guia atualizado
- Documente customizações específicas da instituição
- Registre procedimentos especiais
- Mantenha lista de contatos técnicos

### 🆘 **Contatos de Suporte**

- **Suporte Técnico**: NAI (Núcleo de Apoio à Inovação)
- **Gestão de Dados**: Equipe de TI
- **Emergências**: Backup e restauração

### 📊 **Monitoramento**

#### **Indicadores de Saúde do Sistema**

- ✅ Configurações de segurança ativas
- ✅ Arquivos de dados atualizados
- ✅ Sistema sem erros
- ✅ Backups realizados regularmente

---

## 🎯 Resumo Executivo

Este guia fornece um processo completo e seguro para atualizar os dados do Dashboard IFPB-CZ com informações reais da instituição. A implementação correta, seguindo as práticas de segurança estabelecidas, garante que o sistema reflita com precisão a situação atual da instituição.

### 🔐 **Principais Mudanças de Segurança**

- **Modo somente leitura** por padrão
- **Proteção contra criação acidental** de planilhas
- **Prevenção de sobrescrita** não autorizada
- **Ferramentas de verificação** e teste

### 📋 **Método Recomendado**

1. **Verificar configurações**: `python configurar_seguranca.py status`
2. **Fazer backup**: `cp -r dados dados_backup_$(date +%Y%m%d)`
3. **Substituir arquivos** diretamente na pasta `dados/`
4. **Testar sistema**: `python testar_seguranca.py`
5. **Validar funcionamento**: `streamlit run app.py`

### ⏱️ **Informações Práticas**

- **Tempo estimado de implementação**: 1-2 horas
- **Frequência de atualização recomendada**: Mensal
- **Método principal**: Substituição direta de arquivos
- **Responsável**: Equipe NAI/Gestão de Dados

### ✅ **Benefícios da Nova Abordagem**

- ✅ **Segurança**: Proteção contra alterações acidentais
- ✅ **Simplicidade**: Processo mais direto e claro
- ✅ **Confiabilidade**: Validação automática das configurações
- ✅ **Rastreabilidade**: Logs e auditoria completos

### 🚀 **Próximos Passos**

1. Configurar `USE_REAL_DATA = True` no `config.py`
2. Preparar os arquivos Excel seguindo as especificações
3. Seguir o processo de atualização segura
4. Implementar rotina de manutenção preventiva

---

**Sistema desenvolvido para o IFPB Campus Cajazeiras**  
*Versão 3.0 - Configurações de Segurança Integradas*
