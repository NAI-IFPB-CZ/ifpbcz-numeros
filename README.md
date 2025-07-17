# Sistema de Dashboards Institucionais IFPB - Campus Cajazeiras

## 📋 Visão Geral

Sistema completo de dashboards para visualização de dados institucionais do IFPB Campus Cajazeiras, desenvolvido com Streamlit e Python. O sistema inclui 9 módulos principais e suporte a dados em formato Excel.

## 📊 Módulos Disponíveis

1. **🎓 Ensino** - Dados acadêmicos, cursos, matrículas e desempenho
2. **🤝 Assistência Estudantil** - Programas de auxílio e benefícios
3. **🔬 Pesquisa** - Projetos, publicações e produção científica
4. **🌟 Extensão** - Ações de extensão e projetos comunitários
5. **💰 Orçamento** - Execução orçamentária e financeira
6. **👥 Servidores** - Dados de recursos humanos
7. **📢 Ouvidoria** - Manifestações e atendimentos
8. **🔍 Auditoria** - Auditorias e recomendações
9. **💼 Mundo do Trabalho** - Inserção profissional de egressos

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório:**

```bash
git clone <repositório>
cd ifpbcz-numeros
```

2. **Crie um ambiente virtual (recomendado):**

```bash
python -m venv .venv
```

3. **Ative o ambiente virtual:**

```bash
# Windows:
.venv\Scripts\activate

# Linux/Mac:
source .venv/bin/activate
```

4. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

### Execução

1. **Inicie o servidor Streamlit:**

```bash
streamlit run app.py
```

2. **Acesse a aplicação:**

Abra seu navegador e acesse `http://localhost:8501`

## ✨ Características Principais

### Interface Limpa

- **Elementos removidos:** Menu hamburger, botões de deploy, watermark "Made with Streamlit"
- **Logo institucional:** Presente no cabeçalho e sidebar
- **Navegação intuitiva:** Menu lateral organizado por módulos

### Identidade Visual

- **Cores institucionais:** Verde (#1a8c73) e branco seguindo padrão IFPB
- **Logo IFPB:** Integrado ao cabeçalho de cada página
- **Design responsivo:** Funciona em desktop e mobile

## 📁 Estrutura do Projeto

```
ifpbcz-numeros/
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências
├── README.md             # Documentação
├── .streamlit/
│   └── config.toml       # Configurações do Streamlit
├── modules/
│   ├── data_generator.py  # Gerador e leitor de dados
│   ├── utils.py          # Funções utilitárias
│   ├── help_page.py      # Página de ajuda
│   ├── ensino.py         # Módulo de Ensino
│   ├── assistencia_estudantil.py  # Módulo de Assistência
│   ├── pesquisa.py       # Módulo de Pesquisa
│   ├── extensao.py       # Módulo de Extensão
│   ├── orcamento.py      # Módulo de Orçamento
│   ├── servidores.py     # Módulo de Servidores
│   ├── ouvidoria.py      # Módulo de Ouvidoria
│   ├── auditoria.py      # Módulo de Auditoria
│   └── mundo_trabalho.py # Módulo Mundo do Trabalho
├── dados/                # Arquivos Excel com dados
│   ├── dados_ensino.xlsx
│   ├── dados_assistencia.xlsx
│   ├── dados_pesquisa.xlsx
│   ├── dados_extensao.xlsx
│   ├── dados_orcamento.xlsx
│   ├── dados_servidores.xlsx
│   ├── dados_ouvidoria.xlsx
│   ├── dados_auditoria.xlsx
│   └── dados_mundo_trabalho.xlsx
├── logo-ifpb/            # Logotipos institucionais
├── figuras-modelo/       # Figuras de exemplo
├── config.py             # Configurações do sistema
├── configurar_seguranca.py  # Script para alterar configurações
├── testar_seguranca.py   # Script para testar configurações
└── GUIA_ATUALIZACAO_DADOS.md  # Guia de atualização de dados
```

## 📊 Configuração de Dados

### Fonte de Dados

O sistema lê dados de arquivos Excel (`.xlsx`) localizados na pasta `dados/`. Cada módulo possui um arquivo correspondente:

- `dados_ensino.xlsx` - Dados do módulo de Ensino
- `dados_assistencia.xlsx` - Dados de Assistência Estudantil
- `dados_pesquisa.xlsx` - Dados de Pesquisa
- `dados_extensao.xlsx` - Dados de Extensão
- `dados_orcamento.xlsx` - Dados de Orçamento
- `dados_servidores.xlsx` - Dados de Servidores
- `dados_ouvidoria.xlsx` - Dados de Ouvidoria
- `dados_auditoria.xlsx` - Dados de Auditoria
- `dados_mundo_trabalho.xlsx` - Dados do Mundo do Trabalho

### Especificações dos Dados

Para informações detalhadas sobre o formato de cada arquivo Excel, acesse a **página de Ajuda** no sistema (botão "❓ Ajuda" no menu lateral).

Cada arquivo Excel contém:

- **Planilha principal:** Dados formatados conforme especificação
- **Planilha "Metadados":** Informações sobre atualização (criada automaticamente)

## 🔧 Personalização

### Logotipos

Coloque os logotipos da instituição na pasta `logo-ifpb/`:

- `IFPB-cz.png` - Logo principal do IFPB Cajazeiras

### Cores Institucionais

As cores são definidas no arquivo `app.py`:

- Verde principal: `#1a8c73`
- Verde escuro: `#0d5a4e`
- Verde claro: `#2db896`

### Configurações Streamlit

Edite `.streamlit/config.toml` para personalizar:

- Tema da aplicação
- Configurações de servidor
- Opções de interface

## 📈 Funcionalidades

### Dashboards Interativos

- **Gráficos dinâmicos** com Plotly
- **Filtros interativos** por ano, curso, programa
- **KPIs e métricas** em tempo real
- **Tabelas responsivas** com dados detalhados

### Visualizações Avançadas

- **Gráficos de linha, barras e pizza**
- **Mapas de calor**
- **Nuvens de palavras**
- **Métricas destacadas**

### Recursos Especiais

- **Detecção automática** de arquivos Excel
- **Timestamp de atualização** em cada módulo
- **Fallback para dados fictícios** quando arquivos não existem
- **Validação de dados** com tratamento de erros
- **Proteção contra criação acidental** de planilhas
- **Modo somente leitura** para prevenir alterações

## 🔒 Configurações de Segurança

### Proteção de Dados

O sistema inclui configurações de segurança no arquivo `config.py`:

```python
# Configurações de segurança
PERMITIR_CRIACAO_PLANILHAS = False  # Impede criação automática de planilhas
SOBRESCREVER_ARQUIVOS_EXISTENTES = False  # Impede sobrescrita acidental
MODO_SOMENTE_LEITURA = True  # Modo somente leitura para proteção
```

### Configuração Recomendada para Produção

```python
USE_REAL_DATA = True  # Usar dados reais da instituição
PERMITIR_CRIACAO_PLANILHAS = False  # Bloquear criação automática
SOBRESCREVER_ARQUIVOS_EXISTENTES = False  # Proteger arquivos existentes
MODO_SOMENTE_LEITURA = True  # Modo somente leitura
VALIDAR_DADOS = True  # Validar dados ao carregar
```

### Habilitando Edição de Dados

Para permitir a criação/edição de planilhas (apenas para desenvolvimento):

```python
PERMITIR_CRIACAO_PLANILHAS = True
SOBRESCREVER_ARQUIVOS_EXISTENTES = True
MODO_SOMENTE_LEITURA = False
```

## 📚 Documentação

### Página de Ajuda

O sistema inclui uma página de ajuda completa (botão "❓ Ajuda") com:

- Especificações detalhadas dos formatos Excel
- Exemplos de estruturas de dados
- Orientações para atualização
- Solução de problemas comuns

### Módulos Detalhados

Cada módulo oferece:

- **Visão geral** com KPIs principais
- **Gráficos interativos** com múltiplas visualizações
- **Filtros dinâmicos** para análise personalizada
- **Tabelas de dados** com informações detalhadas

## 🔄 Atualização de Dados

### Processo de Atualização

1. **Verifique as configurações de segurança** no arquivo `config.py`
2. **Faça backup** dos arquivos existentes
3. **Substitua os arquivos Excel** na pasta `dados/`
4. **Mantenha o formato das colunas** conforme especificado
5. **Reinicie o sistema** para carregar os novos dados

### Configurações de Segurança

Por padrão, o sistema está configurado para **modo somente leitura** para prevenir alterações acidentais:

- ✅ **Modo seguro**: Impede criação automática de planilhas
- ✅ **Proteção de dados**: Não sobrescreve arquivos existentes  
- ✅ **Somente leitura**: Previne alterações acidentais

### Habilitando Edição (Desenvolvedor)

Para permitir criação/edição de planilhas, altere no `config.py`:

```python
PERMITIR_CRIACAO_PLANILHAS = True
SOBRESCREVER_ARQUIVOS_EXISTENTES = True
MODO_SOMENTE_LEITURA = False
```

### Validação

- Verifique o formato antes de substituir arquivos
- Consulte a página de Ajuda para especificações
- Teste em ambiente de desenvolvimento
- Monitore os logs para verificar se há avisos de segurança

## 🚀 Execução Avançada

### Desenvolvimento

```bash
# Porta personalizada
streamlit run app.py --server.port 8502

# Acesso externo
streamlit run app.py --server.address 0.0.0.0
```

## 🛠️ Scripts de Gerenciamento

### Configuração de Segurança

**Alterar configurações de segurança:**

```bash
# Verificar configurações atuais
python configurar_seguranca.py status

# Ativar modo seguro (produção)
python configurar_seguranca.py seguro

# Ativar modo edição (desenvolvimento)
python configurar_seguranca.py edicao
```

### Teste de Configurações

**Testar configurações de segurança:**

```bash
# Executar teste completo
python testar_seguranca.py
```

Este script verifica:

- ✅ Carregamento das configurações
- ✅ Funcionamento das proteções
- ✅ Presença dos arquivos de dados
- ✅ Logs de segurança

### Produção

Para ambiente de produção considere:

- Usar servidor web como Nginx
- Configurar SSL/HTTPS
- Implementar autenticação
- Configurar backup automático

## ⚠️ Observações Importantes

### Segurança dos Dados

1. **Configurações de segurança** ativadas por padrão no `config.py`
2. **Modo somente leitura** previne alterações acidentais
3. **Backup regular** dos dados Excel antes de qualquer atualização
4. **Validação** do formato antes de substituir arquivos
5. **Teste** em ambiente de desenvolvimento

### Operação do Sistema

1. **Monitoramento** dos logs para detectar problemas
2. **Atualização periódica** das dependências
3. **Verificação** das configurações de segurança após atualizações
4. **Documentação** de mudanças nas configurações

### Mensagens de Segurança

O sistema exibe avisos quando:

- ⚠️ Tentativa de criação de planilhas com `PERMITIR_CRIACAO_PLANILHAS = False`
- ⚠️ Tentativa de sobrescrita com `SOBRESCREVER_ARQUIVOS_EXISTENTES = False`
- ⚠️ Operações bloqueadas no `MODO_SOMENTE_LEITURA = True`

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Processo:

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Faça um push para a branch
5. Abra um Pull Request

---

**Sistema desenvolvido para o IFPB Campus Cajazeiras**  
*Versão 3.0 - Suporte a dados Excel*
