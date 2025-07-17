# 📚 Documentação do Sistema Dashboard IFPB-CZ

Esta pasta contém a documentação completa do Sistema de Visualização de Dados Institucionais do IFPB Campus Cajazeiras.

## 📄 Arquivos de Documentação

### 📋 [Diagrama de Fluxo do Sistema](diagrama_fluxo_sistema.md)
Documento principal com:
- 🗂️ Visão geral da arquitetura
- 🔄 Fluxos de navegação e dados
- 🗺️ Diagramas Mermaid interativos
- 📁 Estrutura de arquivos e módulos
- 🎯 Funcionalidades por módulo

### �️ [Diagrama Visual do Fluxo](diagrama_visual_fluxo.md)
Representação visual em ASCII art com:
- 🚀 Fluxo principal do sistema
- 💾 Fluxo de dados detalhado
- 🔐 Fluxo de segurança
- 🗺️ Fluxo específico do módulo mapa
- 📱 Responsividade mobile/desktop

### �🔧 [Documentação Técnica](documentacao_tecnica.md)
Guia técnico detalhado com:
- 🏗️ Arquitetura de software
- ⚙️ Instruções de instalação
- 📊 Estrutura de dados
- 🔐 Sistema de segurança
- 🐛 Troubleshooting
- 🚀 Deploy e produção

## 🎯 Para Desenvolvedores

### 📖 Leitura Recomendada
1. **Iniciantes**: Comece com o [Diagrama Visual](diagrama_visual_fluxo.md) para entender o fluxo geral
2. **Desenvolvedores**: Consulte o [Diagrama de Fluxo](diagrama_fluxo_sistema.md) e a [Documentação Técnica](documentacao_tecnica.md)
3. **Administradores**: Foque nas seções de segurança e deploy da documentação técnica

### 🔧 Configuração Rápida
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar sistema
streamlit run app.py

# 3. Acessar no navegador
http://localhost:8501
```

## 🌟 Funcionalidades Principais

### 📊 Módulos Disponíveis
- 🎓 **Ensino**: Dados acadêmicos e performance
- 🔬 **Pesquisa**: Projetos e produção científica
- 🌟 **Extensão**: Projetos comunitários
- 🤝 **Assistência Estudantil**: Programas de apoio
- 💰 **Orçamento**: Execução financeira
- 👥 **Servidores**: Recursos humanos
- 📢 **Ouvidoria**: Manifestações e atendimento
- 🔍 **Auditoria**: Conformidade e melhorias
- 💼 **Mundo do Trabalho**: Empregabilidade
- 🗺️ **Mapa dos Campus**: Localização geográfica

### 🔐 Sistema de Segurança
- ✅ Modo somente leitura (padrão)
- ✅ Backup automático de dados
- ✅ Logs de operações
- ✅ Validação de integridade

## 🚀 Tecnologias

### 🐍 Backend
- **Python 3.12+**: Linguagem principal
- **Streamlit**: Framework de dashboards
- **Pandas**: Manipulação de dados
- **Plotly**: Gráficos interativos

### 🗺️ Visualização
- **Folium**: Mapas interativos
- **WordCloud**: Nuvens de palavras
- **Matplotlib**: Gráficos estáticos

### 📊 Dados
- **Excel/XLSX**: Fonte de dados principal
- **OpenPyXL**: Leitura de planilhas
- **DataGenerator**: Dados sintéticos para teste

## 📞 Suporte

### 🏛️ Instituição
- **IFPB - Campus Cajazeiras**
- **Núcleo de Avaliação Institucional (NAI)**

### 📧 Contato
- Para dúvidas técnicas, consulte a [documentação técnica](documentacao_tecnica.md)
- Para problemas de instalação, veja a seção troubleshooting
- Para sugestões de melhorias, abra uma issue no repositório

---

*📅 Última atualização: 17 de julho de 2025*  
*🏛️ IFPB - Campus Cajazeiras*  
*📊 Sistema de Dashboards Institucionais*
