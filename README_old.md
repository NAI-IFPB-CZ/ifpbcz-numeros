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
python -m venv venv
```

3. **Ative o ambiente virtual:**

```bash
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
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
└── figuras-modelo/       # Figuras de exemplo
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

1. Substitua os arquivos Excel na pasta `dados/`
2. Mantenha o formato das colunas conforme especificado
3. Reinicie o sistema para carregar os novos dados

### Validação

- Verifique o formato antes de substituir arquivos
- Consulte a página de Ajuda para especificações
- Teste em ambiente de desenvolvimento

## 🚀 Execução Avançada

### Desenvolvimento

```bash
# Porta personalizada
streamlit run app.py --server.port 8502

# Acesso externo
streamlit run app.py --server.address 0.0.0.0
```

### Produção

Para ambiente de produção considere:

- Usar servidor web como Nginx
- Configurar SSL/HTTPS
- Implementar autenticação
- Configurar backup automático

## ⚠️ Observações Importantes

1. **Backup regular** dos dados Excel
2. **Validação** do formato antes de substituir arquivos
3. **Teste** em ambiente de desenvolvimento
4. **Monitoramento** dos logs para detectar problemas
5. **Atualização periódica** das dependências

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
*Versão 2.0 - Suporte a dados Excel*
