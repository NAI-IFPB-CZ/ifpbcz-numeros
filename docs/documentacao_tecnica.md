# 🔧 Documentação Técnica - Sistema Dashboard IFPB-CZ

## 📖 Índice

1. [Arquitetura Técnica](#-arquitetura-técnica)
2. [Configuração e Instalação](#-configuração-e-instalação)
3. [Estrutura de Dados](#-estrutura-de-dados)
4. [APIs e Integrações](#-apis-e-integrações)
5. [Sistema de Segurança](#-sistema-de-segurança)
6. [Monitoramento e Logs](#-monitoramento-e-logs)
7. [Troubleshooting](#-troubleshooting)

---

## 🏗️ Arquitetura Técnica

### 🎯 Padrão Arquitetural
- **Padrão**: Modular Monolítico
- **Framework**: Streamlit (Python)
- **Estrutura**: MVC Adaptado para Dashboards

### 🔗 Componentes Principais

#### 1. **Camada de Apresentação**
```python
# app.py - Controlador Principal
- Interface Streamlit
- Roteamento de módulos
- Gerenciamento de sessão
- CSS customizado
```

#### 2. **Camada de Negócio**
```python
# modules/ - Lógica de Negócio
- Processamento de dados
- Geração de visualizações
- Validações de negócio
- Transformações de dados
```

#### 3. **Camada de Dados**
```python
# data_generator.py - Acesso a Dados
- Carregamento de planilhas Excel
- Geração de dados sintéticos
- Cache de dados
- Validação de estrutura
```

---

## ⚙️ Configuração e Instalação

### 📋 Pré-requisitos
- Python 3.12 ou superior
- pip (gerenciador de pacotes Python)
- Ambiente virtual (recomendado)

### 🚀 Instalação

```bash
# 1. Clonar o repositório
git clone <repository-url>
cd ifpbcz-numeros

# 2. Criar ambiente virtual
python -m venv .venv

# 3. Ativar ambiente virtual
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Executar aplicação
streamlit run app.py
```

### 📦 Dependências Principais

```txt
streamlit>=1.28.0          # Framework web
plotly>=5.15.0            # Gráficos interativos
folium>=0.14.0            # Mapas interativos
streamlit-folium>=0.13.0  # Integração Folium-Streamlit
pandas>=2.0.0             # Manipulação de dados
numpy>=1.24.0             # Computação numérica
openpyxl>=3.1.0           # Leitura de Excel
wordcloud>=1.9.0          # Nuvens de palavras
matplotlib>=3.7.0         # Gráficos estáticos
```

---

## 📊 Estrutura de Dados

### 📄 Formato das Planilhas Excel

#### Estrutura Padrão
```
dados/
├── dados_ensino.xlsx
├── dados_pesquisa.xlsx
├── dados_extensao.xlsx
├── dados_assistencia.xlsx
├── dados_orcamento.xlsx
├── dados_servidores.xlsx
├── dados_ouvidoria.xlsx
├── dados_auditoria.xlsx
└── dados_mundo_trabalho.xlsx
```

#### Colunas Obrigatórias por Módulo

**🎓 Ensino (dados_ensino.xlsx)**
```python
colunas_obrigatorias = [
    'curso', 'modalidade', 'periodo', 
    'matriculados', 'concluintes', 'evadidos',
    'aprovados', 'reprovados', 'data'
]
```

**🔬 Pesquisa (dados_pesquisa.xlsx)**
```python
colunas_obrigatorias = [
    'projeto', 'area_conhecimento', 'tipo',
    'pesquisadores', 'bolsistas', 'orcamento',
    'status', 'data_inicio', 'data_fim'
]
```

**🌟 Extensão (dados_extensao.xlsx)**
```python
colunas_obrigatorias = [
    'projeto', 'area_tematica', 'publico_alvo',
    'participantes', 'beneficiarios', 'orcamento',
    'coordenador', 'data_inicio', 'data_fim'
]
```

### 🔄 DataGenerator

#### Métodos Principais
```python
class DataGenerator:
    def __init__(self):
        # Configurações de segurança
        # Cache de dados
        # Validações iniciais
    
    def carregar_dados_excel(self, arquivo: str) -> pd.DataFrame:
        # Carrega dados de planilha Excel
        # Aplica validações
        # Retorna DataFrame limpo
    
    def gerar_dados_sinteticos(self, modulo: str, qtd_registros: int) -> pd.DataFrame:
        # Gera dados realistas para teste
        # Mantém consistência temporal
        # Aplica distribuições estatísticas
    
    def validar_estrutura(self, df: pd.DataFrame, colunas_esperadas: list) -> bool:
        # Valida estrutura do DataFrame
        # Verifica tipos de dados
        # Identifica inconsistências
```

---

## 🔌 APIs e Integrações

### 🌐 Integrações Externas (Futuras)

#### Sistema Acadêmico SUAP
```python
# Exemplo de integração futura
class SUAPIntegration:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
    
    def get_matriculas(self, periodo: str) -> dict:
        # Buscar dados de matrícula
        pass
    
    def get_notas(self, curso: str, periodo: str) -> dict:
        # Buscar dados de notas
        pass
```

#### API CNPQ Lattes
```python
# Exemplo de integração pesquisa
class LattesIntegration:
    def get_producao_cientifica(self, cpf_pesquisador: str) -> dict:
        # Buscar produção científica
        pass
    
    def get_projetos_pesquisa(self, instituicao: str) -> dict:
        # Buscar projetos de pesquisa
        pass
```

### 🗺️ Integração de Mapas

#### Folium + Streamlit
```python
# modules/mapa.py
def create_interactive_map(campus_data: dict) -> folium.Map:
    # Criar mapa base
    m = folium.Map(location=centro_pb, zoom_start=7)
    
    # Adicionar marcadores
    for campus, info in campus_data.items():
        folium.Marker(
            location=[info['lat'], info['lon']],
            popup=create_popup_html(info),
            tooltip=f"Campus {campus}",
            icon=folium.Icon(color='green', icon='info-sign')
        ).add_to(m)
    
    return m
```

---

## 🔐 Sistema de Segurança

### ⚙️ Arquivo de Configuração (config.py)

```python
# Configurações de segurança do sistema
CONFIGURACOES_SEGURANCA = {
    'PERMITIR_CRIACAO_PLANILHAS': False,
    'SOBRESCREVER_ARQUIVOS_EXISTENTES': False,
    'MODO_SOMENTE_LEITURA': True,
    'BACKUP_AUTOMATICO': True,
    'LOG_OPERACOES': True
}

# Configurações de backup
CONFIGURACOES_BACKUP = {
    'PASTA_BACKUP': 'backups/',
    'MANTER_VERSOES': 5,
    'COMPRESSAO': True,
    'FORMATO_DATA': '%Y%m%d_%H%M%S'
}
```

### 🔒 Níveis de Acesso

#### Modo Somente Leitura (Padrão)
```python
if CONFIGURACOES_SEGURANCA['MODO_SOMENTE_LEITURA']:
    # Bloquear operações de escrita
    # Permitir apenas visualização
    # Logs de acesso
```

#### Modo Edição (Administrador)
```python
if not CONFIGURACOES_SEGURANCA['MODO_SOMENTE_LEITURA']:
    # Permitir modificações
    # Backup automático antes de alterações
    # Logs detalhados de modificações
```

### 🛡️ Scripts de Gestão

#### configurar_seguranca.py
```python
def alterar_modo_seguranca(modo: str):
    """
    Altera entre modo seguro e modo edição
    
    Args:
        modo: 'seguro' ou 'edicao'
    """
    if modo == 'seguro':
        configuracoes['MODO_SOMENTE_LEITURA'] = True
        configuracoes['PERMITIR_CRIACAO_PLANILHAS'] = False
    elif modo == 'edicao':
        configuracoes['MODO_SOMENTE_LEITURA'] = False
        # Solicitar confirmação para operações críticas
```

#### testar_seguranca.py
```python
def testar_configuracoes_seguranca():
    """
    Testa todas as configurações de segurança
    Valida permissões de arquivo
    Verifica integridade dos dados
    """
    testes = [
        testar_modo_leitura(),
        testar_backup_automatico(),
        testar_validacao_dados(),
        testar_logs_operacao()
    ]
    return all(testes)
```

---

## 📊 Monitoramento e Logs

### 📝 Sistema de Logs

#### Configuração de Logging
```python
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/sistema.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('IFPB_Dashboard')
```

#### Tipos de Logs
```python
# Log de acesso
logger.info(f"Usuário acessou módulo: {modulo_nome}")

# Log de erro
logger.error(f"Erro ao carregar dados: {erro_detalhes}")

# Log de operação
logger.warning(f"Tentativa de operação não autorizada: {operacao}")

# Log de performance
logger.debug(f"Tempo de carregamento: {tempo_execucao}s")
```

### 📈 Métricas de Performance

#### Monitoramento de Uso
```python
def monitorar_performance():
    """
    Monitora métricas de performance do sistema
    """
    metricas = {
        'tempo_carregamento_pagina': time.time() - inicio,
        'memoria_utilizada': psutil.virtual_memory().percent,
        'modulo_mais_acessado': get_modulo_popular(),
        'usuarios_ativos': count_active_sessions()
    }
    
    salvar_metricas(metricas)
```

---

## 🐛 Troubleshooting

### ❗ Problemas Comuns

#### 1. Erro de Importação de Módulos
```bash
# Erro
ModuleNotFoundError: No module named 'folium'

# Solução
pip install folium streamlit-folium
```

#### 2. Planilha Excel Não Encontrada
```python
# Erro
FileNotFoundError: dados/dados_ensino.xlsx

# Solução
# Verificar se arquivo existe na pasta dados/
# Verificar permissões de leitura
# Usar dados sintéticos como fallback
```

#### 3. Mapa Não Carrega
```python
# Diagnóstico
def diagnosticar_mapa():
    try:
        import folium
        import streamlit_folium
        print("✅ Dependências OK")
        
        # Testar criação de mapa simples
        m = folium.Map()
        print("✅ Folium OK")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
```

#### 4. Performance Lenta
```python
# Otimizações
@st.cache_data
def carregar_dados_cache(arquivo):
    """Cache de dados para melhor performance"""
    return pd.read_excel(arquivo)

# Reduzir dados exibidos
dados_limitados = dados.head(1000)  # Mostrar apenas 1000 registros

# Lazy loading de gráficos
if st.button("Carregar Gráfico Detalhado"):
    mostrar_grafico_complexo()
```

### 🔧 Scripts de Diagnóstico

#### diagnostico_sistema.py
```python
def diagnostico_completo():
    """
    Executa diagnóstico completo do sistema
    """
    print("🔍 Iniciando diagnóstico...")
    
    # Verificar Python e dependências
    verificar_ambiente()
    
    # Verificar arquivos de dados
    verificar_dados()
    
    # Verificar permissões
    verificar_permissoes()
    
    # Verificar conectividade
    verificar_conectividade()
    
    # Testar módulos
    testar_modulos()
    
    print("✅ Diagnóstico concluído!")
```

### 📞 Suporte Técnico

#### Informações para Suporte
```python
def gerar_info_suporte():
    """
    Gera informações técnicas para suporte
    """
    info = {
        'versao_python': sys.version,
        'versao_streamlit': st.__version__,
        'sistema_operacional': platform.system(),
        'data_instalacao': get_install_date(),
        'configuracoes_ativas': get_active_configs(),
        'logs_recentes': get_recent_logs(),
        'erros_conhecidos': get_known_errors()
    }
    
    return info
```

---

## 🚀 Deploy e Produção

### 🌐 Opções de Deploy

#### 1. Streamlit Cloud
```bash
# Arquivo .streamlit/config.toml
[server]
port = 8501
headless = true

[theme]
primaryColor = "#1a8c73"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
```

#### 2. Docker
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

#### 3. Servidor Local
```bash
# Configurar serviço systemd
sudo systemctl enable ifpb-dashboard
sudo systemctl start ifpb-dashboard
```

### 🔒 Configurações de Produção

```python
# Configurações específicas para produção
PRODUCAO = {
    'DEBUG': False,
    'CACHE_TTL': 3600,  # 1 hora
    'MAX_UPLOAD_SIZE': 50,  # MB
    'BACKUP_FREQUENCY': 'daily',
    'LOG_LEVEL': 'INFO'
}
```

---

*📅 Última atualização: 17 de julho de 2025*  
*🏛️ IFPB - Campus Cajazeiras*  
*👨‍💻 Documentação técnica do sistema de dashboards*
