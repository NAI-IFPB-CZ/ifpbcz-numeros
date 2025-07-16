# 📊 Guia para Usar Dados Reais no Dashboard IFPB-CZ

## 🔄 Alternância entre Dados Sintéticos e Reais

O sistema suporta dois modos de operação:
- **Dados Sintéticos**: Gerados automaticamente para demonstração
- **Dados Reais**: Carregados de planilhas Excel com dados institucionais

## 📋 Pré-requisitos

1. **Python 3.8+**
2. **Bibliotecas necessárias**:
   ```bash
   pip install pandas openpyxl streamlit plotly
   ```

## 🚀 Passo a Passo para Usar Dados Reais

### 1. Criar Estrutura de Planilhas de Exemplo
```bash
python criar_planilhas_exemplo.py
```

### 2. Estrutura de Arquivos Necessária
```
dados/
├── dados_assistencia.xlsx
├── dados_auditoria.xlsx
├── dados_ensino.xlsx
├── dados_extensao.xlsx
├── dados_mundo_trabalho.xlsx
├── dados_orcamento.xlsx
├── dados_ouvidoria.xlsx
├── dados_pesquisa.xlsx
└── dados_servidores.xlsx
```

### 3. Estrutura das Planilhas

#### 📚 dados_extensao.xlsx
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ano | int | Ano de referência (ex: 2025) |
| unidade | str | Nome da unidade IFPB |
| curso | str | Nome do curso |
| modalidade | str | Presencial, EAD, Híbrida |
| genero | str | Masculino, Feminino, Outro |
| estagios_concluidos | int | Número de estágios concluídos |
| pne_ingressantes | int | Ingressantes com necessidades especiais |
| tipo_necessidade | str | Tipo de necessidade especial |

#### 🎓 dados_ensino.xlsx
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ano | int | Ano de referência |
| campus | str | Nome do campus |
| curso | str | Nome do curso |
| modalidade | str | Modalidade do curso |
| matriculados | int | Número de matriculados |
| formados | int | Número de formados |
| desistentes | int | Número de desistentes |
| transferidos | int | Número de transferidos |

#### 📖 dados_pesquisa.xlsx
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ano | int | Ano de referência |
| tipo_publicacao | str | Artigos, Capítulos, Trabalhos |
| quantidade | int | Quantidade de publicações |
| area_conhecimento | str | Área do conhecimento |
| servidor | str | Nome do servidor (opcional) |

#### 💰 dados_assistencia.xlsx
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ano | int | Ano de referência |
| campus | str | Nome do campus |
| auxilio_tipo | str | Tipo de auxílio |
| beneficiarios | int | Número de beneficiários |
| valor_total | float | Valor total investido |

#### 🔍 dados_auditoria.xlsx
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ano | int | Ano de referência |
| tipo_auditoria | str | Tipo de auditoria |
| numero_auditorias | int | Número de auditorias |
| recomendacoes | int | Número de recomendações |

#### 💼 dados_mundo_trabalho.xlsx
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ano | int | Ano de referência |
| campus | str | Nome do campus |
| curso | str | Nome do curso |
| empregabilidade | float | Taxa de empregabilidade (%) |
| salario_medio | float | Salário médio dos egressos |

#### 💵 dados_orcamento.xlsx
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ano | int | Ano de referência |
| categoria | str | Categoria orçamentária |
| valor_orcado | float | Valor orçado |
| valor_executado | float | Valor executado |

#### 📞 dados_ouvidoria.xlsx
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ano | int | Ano de referência |
| tipo_manifestacao | str | Tipo de manifestação |
| quantidade | int | Quantidade de manifestações |
| status | str | Status da manifestação |

#### 👥 dados_servidores.xlsx
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| ano | int | Ano de referência |
| campus | str | Nome do campus |
| categoria | str | Categoria do servidor |
| quantidade | int | Quantidade de servidores |
| genero | str | Gênero do servidor |

### 4. Configurar o Sistema

Edite o arquivo `config.py`:

```python
# Para usar dados reais
USE_REAL_DATA = True

# Para usar dados sintéticos
USE_REAL_DATA = False
```

### 5. Testar o Sistema

```bash
# Testar carregamento de dados
python test_dados_reais.py

# Executar o dashboard
streamlit run app.py
```

## 🛠️ Configurações Avançadas

### config.py
```python
USE_REAL_DATA = True          # Usar dados reais
VALIDAR_DADOS = True          # Validar estrutura
MOSTRAR_LOGS = True           # Mostrar logs de carregamento
CACHE_DADOS = True            # Cache para performance
USAR_DADOS_BACKUP = True      # Usar sintéticos como backup
```

## 🔧 Solução de Problemas

### ❌ Arquivo não encontrado
```
FileNotFoundError: Arquivo 'dados_extensao.xlsx' não encontrado
```
**Solução**: Execute `python criar_planilhas_exemplo.py`

### ❌ Colunas faltantes
```
ValueError: Colunas faltantes em Extensão: ['ano', 'unidade']
```
**Solução**: Verifique se sua planilha possui todas as colunas obrigatórias

### ❌ Erro de tipo de dados
```
TypeError: Cannot convert string to int
```
**Solução**: Verifique se os dados estão no formato correto (números em colunas numéricas)

## 📝 Dicas Importantes

1. **Backup**: Sempre mantenha backup dos dados originais
2. **Validação**: Use `VALIDAR_DADOS = True` para detectar problemas
3. **Logs**: Ative `MOSTRAR_LOGS = True` para debugar problemas
4. **Performance**: Use `CACHE_DADOS = True` para melhor performance
5. **Segurança**: Não commite arquivos com dados sensíveis

## 🚨 Avisos de Segurança

- ⚠️ **Dados Sensíveis**: Não inclua dados pessoais ou confidenciais
- ⚠️ **Backup**: Sempre faça backup antes de modificar planilhas
- ⚠️ **Validação**: Valide dados antes de colocar em produção

## 📞 Suporte

Se encontrar problemas:
1. Execute `python test_dados_reais.py` para diagnosticar
2. Verifique os logs no terminal
3. Confirme a estrutura das planilhas
4. Verifique as configurações em `config.py`
