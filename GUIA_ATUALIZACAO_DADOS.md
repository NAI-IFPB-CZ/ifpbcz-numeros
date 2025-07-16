# 📊 Guia Completo: Atualização de Dados Reais no Dashboard IFPB-CZ

## 🎯 Objetivo

Este guia ensina como atualizar o sistema Dashboard IFPB-CZ com dados reais das planilhas Excel, substituindo completamente os dados sintéticos gerados automaticamente.

## 📋 Pré-requisitos

- ✅ Sistema Dashboard IFPB-CZ instalado e funcionando
- ✅ Microsoft Excel ou LibreOffice Calc
- ✅ Dados institucionais organizados por módulos
- ✅ Acesso à pasta do projeto

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

### 1️⃣ Preparação dos Arquivos Excel

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

### 2️⃣ Modificação do Data Generator

#### 📝 Localize o arquivo `modules/data_generator.py`

#### 🔧 Substitua os métodos de geração por carregamento de Excel

**Exemplo para o módulo de ensino**:

```python
def gerar_dados_ensino(self):
    """Carrega dados reais de ensino do arquivo Excel"""
    try:
        # Caminho para o arquivo Excel
        arquivo_path = os.path.join(self.dados_directory, "dados_ensino.xlsx")
        
        # Verificar se o arquivo existe
        if not os.path.exists(arquivo_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {arquivo_path}")
        
        # Carregar dados do Excel
        df = pd.read_excel(arquivo_path)
        
        # Validar colunas obrigatórias
        colunas_obrigatorias = ['ano', 'campus', 'curso', 'modalidade', 
                               'matriculados', 'formados', 'desistentes', 'transferidos']
        
        for coluna in colunas_obrigatorias:
            if coluna not in df.columns:
                raise ValueError(f"Coluna obrigatória '{coluna}' não encontrada no arquivo Excel")
        
        # Converter tipos de dados
        df['ano'] = df['ano'].astype(int)
        df['matriculados'] = df['matriculados'].fillna(0).astype(int)
        df['formados'] = df['formados'].fillna(0).astype(int)
        df['desistentes'] = df['desistentes'].fillna(0).astype(int)
        df['transferidos'] = df['transferidos'].fillna(0).astype(int)
        
        # Salvar dados no Excel (se necessário)
        self._salvar_dados_excel(df, "dados_ensino.xlsx")
        
        return df
        
    except Exception as e:
        print(f"Erro ao carregar dados de ensino: {str(e)}")
        raise
```

### 3️⃣ Aplicação das Modificações

#### 📋 **Para cada módulo, repita os seguintes passos:**

1. **Abra o arquivo** `modules/data_generator.py`
2. **Localize o método** correspondente (ex: `gerar_dados_ensino()`)
3. **Substitua todo o código** do método pela lógica de carregamento Excel
4. **Teste o carregamento** de dados

#### 🔄 **Exemplo de substituição completa**

```python
# ANTES (dados sintéticos)
def gerar_dados_ensino(self):
    # Código que gera dados aleatórios...
    dados = []
    for ano in range(2015, 2026):
        # Geração sintética complexa...
    
# DEPOIS (dados reais)
def gerar_dados_ensino(self):
    """Carrega dados reais de ensino do arquivo Excel"""
    arquivo_path = os.path.join(self.dados_directory, "dados_ensino.xlsx")
    df = pd.read_excel(arquivo_path)
    
    # Validações e conversões...
    
    return df
```

### 4️⃣ Validação e Teste

#### ✅ **Checklist de Validação**

1. **Estrutura dos arquivos Excel**:
   - [ ] Todas as colunas obrigatórias presentes
   - [ ] Tipos de dados corretos (números, texto, datas)
   - [ ] Sem valores vazios em colunas críticas

2. **Consistência dos dados**:
   - [ ] Anos coerentes (não futuro demais)
   - [ ] Valores numéricos não negativos
   - [ ] Nomes de campus padronizados

3. **Funcionamento do sistema**:
   - [ ] Dashboard carrega sem erros
   - [ ] Gráficos exibem dados corretos
   - [ ] Filtros funcionam adequadamente

#### 🧪 **Comando de teste**

```bash
# Executar o sistema
streamlit run app.py

# Verificar no navegador
# http://localhost:8501
```

### 5️⃣ Atualização Periódica

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

#### 🔄 **Processo de Atualização**

1. **Backup dos dados atuais**:

   ```bash
   # Crie uma cópia da pasta dados
   cp -r dados dados_backup_$(date +%Y%m%d)
   ```

2. **Atualização dos arquivos Excel**:
   - Substitua os arquivos na pasta `dados/`
   - Mantenha os nomes dos arquivos

3. **Teste do sistema**:
   - Execute o dashboard
   - Verifique cada módulo
   - Confirme funcionamento dos gráficos

4. **Validação dos dados**:
   - Compare com período anterior
   - Verifique consistência dos números
   - Teste filtros e interações

## 🚨 Solução de Problemas

### ❌ **Erro: Arquivo não encontrado**

```text
FileNotFoundError: dados_ensino.xlsx
```

**Solução**: Verifique se o arquivo está na pasta `dados/` com o nome exato.

### ❌ **Erro: Coluna não encontrada**

```text
ValueError: Coluna 'matriculados' não encontrada
```

**Solução**: Verifique se todas as colunas obrigatórias estão presentes no Excel.

### ❌ **Erro: Tipo de dados incorreto**

```text
TypeError: Cannot convert string to int
```

**Solução**: Verifique se colunas numéricas contêm apenas números.

### ❌ **Dashboard não carrega**

```text
Streamlit error
```

**Solução**:

1. Verifique o terminal para mensagens de erro
2. Confirme que todos os arquivos Excel estão presentes
3. Reinicie o servidor Streamlit

## 📞 Suporte e Manutenção

### 🔧 **Manutenção Preventiva**

- Backup semanal dos dados
- Validação mensal da estrutura
- Teste trimestral do sistema completo

### 📋 **Logs de Auditoria**

- Documente cada atualização
- Registre problemas encontrados
- Mantenha histórico de mudanças

### 📖 **Documentação**

- Mantenha este guia atualizado
- Documente customizações específicas
- Registre procedimentos especiais

---

## 🎯 Resumo Executivo

Este guia fornece um processo completo para substituir os dados sintéticos por dados reais no Dashboard IFPB-CZ. A implementação correta garante que o sistema reflita com precisão a situação atual da instituição, fornecendo informações confiáveis para tomada de decisões estratégicas.

**Tempo estimado de implementação**: 2-4 horas
**Frequência de atualização recomendada**: Mensal
**Responsável**: Equipe NAI/Gestão de Dados
