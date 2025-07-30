#!/usr/bin/env python3
"""
=============================================================================
SCRIPT PARA CRIAÇÃO DE PACOTE DE PRODUÇÃO - SISTEMA DASHBOARD IFPB-CZ
=============================================================================

Este script implementa criação automatizada e otimizada de pacote completo
para deploy em servidor de produção do Sistema Dashboard IFPB-CZ, incluindo
apenas arquivos necessários para funcionamento em ambiente produtivo,
removendo arquivos de desenvolvimento, cache, logs e componentes
desnecessários para otimização do pacote de deploy.

FUNCIONALIDADES PRINCIPAIS:
---------------------------
- Criação automatizada de pacote ZIP completo para produção
- Seleção inteligente de arquivos e pastas obrigatórias
- Inclusão condicional de componentes opcionais existentes
- Exclusão automática de arquivos de desenvolvimento e cache
- Análise detalhada de estatísticas do projeto
- Compressão otimizada para redução de tamanho
- Relatório completo de criação e instruções de deploy

ESTRATÉGIA DE OTIMIZAÇÃO:
-------------------------
- Arquivos obrigatórios: componentes críticos para funcionamento
- Pastas essenciais: estrutura funcional completa
- Componentes opcionais: inclusão apenas se existentes
- Exclusão seletiva: desenvolvimento, cache e temporários
- Compressão máxima: ZIP_DEFLATED para menor tamanho
- Filtros avançados: extensões e padrões específicos

CATEGORIZAÇÃO DE ARQUIVOS:
--------------------------
OBRIGATÓRIOS:
- app.py: aplicação principal Streamlit
- requirements.txt: dependências críticas
- config.py: configurações do sistema
- README.md: documentação principal
- LICENSE: licença do projeto
- GUIA_ATUALIZACAO_DADOS.md: guia de atualização

OPCIONAIS:
- configurar_seguranca.py: script de configuração
- testar_seguranca.py: script de teste
- MODULO_MAPA.md: documentação do mapa

CATEGORIZAÇÃO DE PASTAS:
------------------------
OBRIGATÓRIAS:
- modules/: módulos funcionais do sistema
- .streamlit/: configurações específicas do framework
- logo-ifpb/: recursos visuais institucionais
- dados/: dados Excel (se existir)
- docs/: documentação técnica

OPCIONAIS:
- fluxo/: diagramas de fluxo

EXCLUSÕES IMPLEMENTADAS:
------------------------
ARQUIVOS DE DESENVOLVIMENTO:
- Scripts de criação e teste
- Arquivos de controle de versão
- Logs e temporários
- Cache e builds

PASTAS DE DESENVOLVIMENTO:
- .git/: controle de versão
- .venv/: ambiente virtual
- __pycache__/: cache Python
- build/, dist/: arquivos de build

EXTENSÕES EXCLUÍDAS:
- .pyc, .pyo: bytecode Python
- .log, .tmp: temporários
- .bak, .swp: backups e swap

ANÁLISES ESTATÍSTICAS:
----------------------
- Contagem total de arquivos no projeto
- Cálculo de tamanho total original
- Arquivos selecionados para produção
- Tamanho otimizado do pacote final
- Percentual de redução alcançado

VALIDAÇÕES IMPLEMENTADAS:
-------------------------
- Verificação de execução no diretório correto
- Existência de arquivos obrigatórios vs opcionais
- Filtros de exclusão aplicados recursivamente
- Contabilização precisa de arquivos e tamanhos
- Tratamento de exceções durante criação

RELATÓRIOS GERADOS:
-------------------
- Análise estatística completa do projeto
- Status de inclusão de cada componente
- Contagem de arquivos por categoria
- Tamanho final e percentual de otimização
- Instruções detalhadas para deploy em produção

NOMENCLATURA DE PACOTES:
------------------------
Formato: dashboard-ifpb-cz-producao-YYYYMMDD-HHMMSS.zip
Exemplo: dashboard-ifpb-cz-producao-20240730-142530.zip

OBJETIVO:
---------
Automatizar completamente a criação de pacotes otimizados
para deploy em produção, garantindo inclusão apenas de
componentes necessários e fornecendo instruções claras
para instalação e configuração em servidores.

DEPENDÊNCIAS:
-------------
- os, sys: manipulação de sistema e arquivos
- zipfile: criação e compressão de arquivos ZIP
- shutil: operações de arquivo de alto nível
- datetime: geração de timestamps para versionamento

AUTOR: Sistema Dashboard IFPB-CZ - NAI
VERSÃO: 2.0 - Dashboard Institucional Completo
DATA: Julho 2025
=============================================================================
"""

import os
import zipfile
import shutil
from datetime import datetime
import sys

# =============================================================================
# CONFIGURAÇÕES ABRANGENTES DO PACOTE DE PRODUÇÃO
# =============================================================================

# Nome do arquivo ZIP de produção com timestamp único
NOME_PACOTE = f"dashboard-ifpb-cz-producao-{datetime.now().strftime('%Y%m%d-%H%M%S')}.zip"

# =============================================================================
# DEFINIÇÃO DE ARQUIVOS E PASTAS OBRIGATÓRIAS PARA PRODUÇÃO
# =============================================================================

# Arquivos críticos obrigatórios para funcionamento em produção
ARQUIVOS_OBRIGATORIOS = [
    'app.py',                    # Aplicação principal Streamlit
    'requirements.txt',          # Dependências críticas Python
    'config.py',                 # Configurações centrais do sistema
    'README.md',                 # Documentação principal de instalação
    'LICENSE',                   # Licença do projeto
    'GUIA_ATUALIZACAO_DADOS.md', # Guia para atualização de dados
]

# Pastas essenciais obrigatórias para estrutura funcional completa
PASTAS_OBRIGATORIAS = [
    'modules',                   # Módulos funcionais do dashboard
    '.streamlit',                # Configurações específicas do Streamlit
    'logo-ifpb',                 # Recursos visuais institucionais
    'dados',                     # Dados Excel (incluir se existir)
    'docs',                      # Documentação técnica detalhada
]

# =============================================================================
# DEFINIÇÃO DE COMPONENTES OPCIONAIS (INCLUIR APENAS SE EXISTENTES)
# =============================================================================

# Arquivos opcionais úteis mas não críticos para funcionamento
ARQUIVOS_OPCIONAIS = [
    'configurar_seguranca.py',   # Script de configuração de segurança
    'testar_seguranca.py',       # Script de validação de segurança
    'MODULO_MAPA.md',            # Documentação específica do módulo mapa
]

# Pastas opcionais com conteúdo complementar
PASTAS_OPCIONAIS = [
    'fluxo',                     # Diagramas de fluxo do sistema
]

# =============================================================================
# DEFINIÇÃO DE EXCLUSÕES (ARQUIVOS DE DESENVOLVIMENTO E CACHE)
# =============================================================================

# Arquivos específicos para excluir (desenvolvimento e temporários)
EXCLUIR_ARQUIVOS = [
    'criar_pacote_producao.py',  # Este próprio script de criação
    'criar_planilhas_exemplo.py',     # Scripts de criação de exemplos
    'criar_planilhas_exemplo_real.py', # Scripts de dados de exemplo
    'test_dados_reais.py',       # Scripts de teste de dados
    'test_extensao.py',          # Scripts de teste específicos
    'README_old.md',             # Documentação obsoleta
    'paginas-pesquisa.md',       # Documentação de desenvolvimento
    '.gitignore',                # Configurações de controle de versão
    '*.log',                     # Arquivos de log (padrão)
    '*.tmp',                     # Arquivos temporários (padrão)
    'Thumbs.db',                 # Cache de thumbnails Windows
    '.DS_Store',                 # Arquivos de sistema macOS
]

# Pastas específicas para excluir (desenvolvimento e cache)
EXCLUIR_PASTAS = [
    '.git',                      # Controle de versão Git
    '.venv',                     # Ambiente virtual Python
    '.vscode',                   # Configurações do VS Code
    '__pycache__',               # Cache de bytecode Python
    '*.egg-info',                # Informações de pacote Python
    '.pytest_cache',             # Cache do framework de testes
    'build',                     # Arquivos de build/compilação
    'dist',                      # Distribuição de pacotes
]

# Extensões de arquivos para excluir automaticamente
EXCLUIR_EXTENSOES = [
    '.pyc',                      # Bytecode Python compilado
    '.pyo',                      # Bytecode Python otimizado
    '.pyd',                      # Extensões Windows Python
    '.log',                      # Arquivos de log diversos
    '.tmp',                      # Arquivos temporários
    '.bak',                      # Arquivos de backup
    '.swp',                      # Arquivos swap de editores
]

# =============================================================================
# FUNÇÕES AUXILIARES ESPECIALIZADAS PARA PROCESSAMENTO
# =============================================================================

def deve_excluir_arquivo(caminho_arquivo):
    """
    Verificação inteligente se um arquivo deve ser excluído do pacote.
    
    Esta função implementa lógica avançada para determinar se um arquivo
    específico deve ser excluído do pacote de produção, baseando-se em
    padrões de nome, extensões e listas de exclusão predefinidas.
    
    PROCESSO DE VERIFICAÇÃO:
    1. Extração do nome base do arquivo
    2. Verificação contra lista de arquivos específicos
    3. Suporte para padrões com wildcards (*)
    4. Verificação de extensões indesejadas
    5. Decisão final de inclusão/exclusão
    
    PADRÕES SUPORTADOS:
    - Nomes exatos: correspondência completa
    - Wildcards: padrões terminados com *
    - Extensões: filtros por tipo de arquivo
    
    CATEGORIAS DE EXCLUSÃO:
    - Arquivos de desenvolvimento específicos
    - Scripts de teste e configuração
    - Documentação obsoleta
    - Cache e temporários do sistema
    
    PARÂMETROS:
    -----------
    caminho_arquivo : str
        Caminho completo ou relativo do arquivo a verificar
        
    RETORNO:
    --------
    bool
        True se arquivo deve ser excluído, False se deve ser incluído
        
    LÓGICA IMPLEMENTADA:
    --------------------
    - Verificação de padrões específicos na lista EXCLUIR_ARQUIVOS
    - Suporte para wildcards com prefixos
    - Verificação de extensões na lista EXCLUIR_EXTENSOES
    - Priorização de exclusão para segurança
    """
    # Extrair nome base do arquivo para análise
    nome_arquivo = os.path.basename(caminho_arquivo)
    
    # =============================================================================
    # VERIFICAÇÃO CONTRA LISTA DE ARQUIVOS ESPECÍFICOS PARA EXCLUSÃO
    # =============================================================================
    
    # Iterar por todos os padrões de exclusão definidos
    for padrao in EXCLUIR_ARQUIVOS:
        if padrao.endswith('*'):
            # Padrão com wildcard - verificar prefixo
            if nome_arquivo.startswith(padrao[:-1]):
                return True
        elif nome_arquivo == padrao:
            # Correspondência exata de nome
            return True
    
    # =============================================================================
    # VERIFICAÇÃO DE EXTENSÕES INDESEJADAS
    # =============================================================================
    
    # Extrair extensão do arquivo para verificação
    _, extensao = os.path.splitext(nome_arquivo)
    if extensao in EXCLUIR_EXTENSOES:
        return True
    
    # Arquivo aprovado para inclusão no pacote
    return False

def deve_excluir_pasta(caminho_pasta):
    """
    Verificação inteligente se uma pasta deve ser excluída do pacote.
    
    Esta função implementa lógica especializada para determinar se uma
    pasta específica deve ser excluída do pacote de produção, baseando-se
    em padrões de nome e listas de exclusão predefinidas para pastas
    de desenvolvimento, cache e temporários.
    
    PROCESSO DE VERIFICAÇÃO:
    1. Extração do nome base da pasta
    2. Verificação contra lista de pastas específicas
    3. Suporte para padrões com wildcards (*)
    4. Decisão final de inclusão/exclusão
    
    CATEGORIAS DE EXCLUSÃO:
    - Controle de versão (.git)
    - Ambientes virtuais (.venv)
    - Cache de IDEs e editores
    - Cache de bytecode Python
    - Arquivos de build e distribuição
    
    PADRÕES SUPORTADOS:
    - Nomes exatos: correspondência completa
    - Wildcards: padrões terminados com *
    
    PARÂMETROS:
    -----------
    caminho_pasta : str
        Caminho completo ou relativo da pasta a verificar
        
    RETORNO:
    --------
    bool
        True se pasta deve ser excluída, False se deve ser incluída
        
    LÓGICA IMPLEMENTADA:
    --------------------
    - Verificação de padrões específicos na lista EXCLUIR_PASTAS
    - Suporte para wildcards com prefixos
    - Priorização de exclusão para segurança
    """
    # Extrair nome base da pasta para análise
    nome_pasta = os.path.basename(caminho_pasta)
    
    # =============================================================================
    # VERIFICAÇÃO CONTRA LISTA DE PASTAS ESPECÍFICAS PARA EXCLUSÃO
    # =============================================================================
    
    # Iterar por todos os padrões de exclusão de pastas
    for padrao in EXCLUIR_PASTAS:
        if padrao.endswith('*'):
            # Padrão com wildcard - verificar prefixo
            if nome_pasta.startswith(padrao[:-1]):
                return True
        elif nome_pasta == padrao:
            # Correspondência exata de nome
            return True
    
    # Pasta aprovada para inclusão no pacote
    return False

def contar_arquivos_pasta(caminho_pasta):
    """
    Contagem inteligente de arquivos em pasta com filtros de exclusão.
    
    Esta função realiza contagem recursiva de arquivos em uma pasta,
    aplicando automaticamente filtros de exclusão para pastas e arquivos
    que não devem ser incluídos no pacote de produção, fornecendo
    estatística precisa de arquivos válidos.
    
    PROCESSO DE CONTAGEM:
    1. Verificação de existência da pasta
    2. Percorrimento recursivo da estrutura
    3. Aplicação de filtros de exclusão para subpastas
    4. Contagem de arquivos válidos apenas
    5. Retorno de estatística precisa
    
    FILTROS APLICADOS:
    - Exclusão de subpastas indesejadas
    - Filtro de arquivos por padrões e extensões
    - Validação de cada item individual
    
    PARÂMETROS:
    -----------
    caminho_pasta : str
        Caminho da pasta para contagem recursiva
        
    RETORNO:
    --------
    int
        Número total de arquivos válidos encontrados
        
    FUNCIONALIDADES:
    ----------------
    - Contagem recursiva completa
    - Aplicação de filtros de exclusão
    - Tratamento de pastas inexistentes
    - Validação individual de arquivos
    """
    # Inicializar contador de arquivos válidos
    contador = 0
    
    # Verificar existência da pasta antes do processamento
    if os.path.exists(caminho_pasta):
        # Percorrer estrutura recursivamente
        for root, dirs, files in os.walk(caminho_pasta):
            # Aplicar filtro de exclusão para subpastas
            dirs[:] = [d for d in dirs if not deve_excluir_pasta(os.path.join(root, d))]
            
            # Contar apenas arquivos que não devem ser excluídos
            for arquivo in files:
                caminho_arquivo = os.path.join(root, arquivo)
                if not deve_excluir_arquivo(caminho_arquivo):
                    contador += 1
                    
    return contador

def obter_tamanho_pasta(caminho_pasta):
    """
    Cálculo inteligente do tamanho total de pasta com filtros de exclusão.
    
    Esta função realiza cálculo recursivo do tamanho total de uma pasta,
    aplicando automaticamente filtros de exclusão para pastas e arquivos
    que não devem ser incluídos no pacote de produção, fornecendo
    estatística precisa do tamanho efetivo.
    
    PROCESSO DE CÁLCULO:
    1. Verificação de existência da pasta
    2. Percorrimento recursivo da estrutura
    3. Aplicação de filtros de exclusão para subpastas
    4. Soma de tamanhos de arquivos válidos apenas
    5. Tratamento de exceções de acesso
    
    FILTROS APLICADOS:
    - Exclusão de subpastas indesejadas
    - Filtro de arquivos por padrões e extensões
    - Validação de cada item individual
    
    TRATAMENTO DE ERROS:
    - Captura de exceções OSError e IOError
    - Continuidade do processamento mesmo com erros
    - Estatística precisa mesmo com falhas parciais
    
    PARÂMETROS:
    -----------
    caminho_pasta : str
        Caminho da pasta para cálculo de tamanho
        
    RETORNO:
    --------
    int
        Tamanho total em bytes dos arquivos válidos
        
    FUNCIONALIDADES:
    ----------------
    - Cálculo recursivo completo
    - Aplicação de filtros de exclusão
    - Tratamento robusto de erros
    - Precisão na contabilização
    """
    # Inicializar acumulador de tamanho total
    tamanho_total = 0
    
    # Verificar existência da pasta antes do processamento
    if os.path.exists(caminho_pasta):
        # Percorrer estrutura recursivamente
        for root, dirs, files in os.walk(caminho_pasta):
            # Aplicar filtro de exclusão para subpastas
            dirs[:] = [d for d in dirs if not deve_excluir_pasta(os.path.join(root, d))]
            
            # Somar tamanho apenas de arquivos válidos
            for arquivo in files:
                caminho_arquivo = os.path.join(root, arquivo)
                if not deve_excluir_arquivo(caminho_arquivo):
                    try:
                        # Tentar obter tamanho do arquivo
                        tamanho_total += os.path.getsize(caminho_arquivo)
                    except (OSError, IOError):
                        # Continuar processamento mesmo com erros de acesso
                        pass
                        
    return tamanho_total

def formatar_tamanho(tamanho_bytes):
    """
    Formatação inteligente de tamanho em bytes para formato legível.
    
    Esta função converte valores de tamanho em bytes para formato
    legível por humanos, utilizando unidades apropriadas (B, KB, MB, GB, TB)
    com precisão decimal adequada para apresentação em relatórios.
    
    PROCESSO DE FORMATAÇÃO:
    1. Conversão progressiva por unidades
    2. Verificação de limiar para cada unidade
    3. Aplicação de precisão decimal apropriada
    4. Retorno de string formatada legível
    
    UNIDADES SUPORTADAS:
    - B: bytes (valores menores que 1024)
    - KB: kilobytes (1024 bytes)
    - MB: megabytes (1024 KB)
    - GB: gigabytes (1024 MB)
    - TB: terabytes (1024 GB)
    
    PRECISÃO:
    - 1 casa decimal para valores maiores que 1
    - Formatação automática baseada na magnitude
    
    PARÂMETROS:
    -----------
    tamanho_bytes : int
        Tamanho em bytes para formatação
        
    RETORNO:
    --------
    str
        Tamanho formatado com unidade apropriada
        
    EXEMPLOS:
    ---------
    - 512 -> "512.0 B"
    - 1536 -> "1.5 KB"
    - 2097152 -> "2.0 MB"
    """
    # Iterar por unidades em ordem crescente
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if tamanho_bytes < 1024.0:
            # Unidade apropriada encontrada
            return f"{tamanho_bytes:.1f} {unidade}"
        # Converter para próxima unidade
        tamanho_bytes /= 1024.0
    
    # Para valores extremamente grandes (terabytes)
    return f"{tamanho_bytes:.1f} TB"

# =============================================================================
# FUNÇÃO PRINCIPAL DE CRIAÇÃO DO PACOTE DE PRODUÇÃO
# =============================================================================

def criar_pacote_producao():
    """
    Função principal para criação do pacote ZIP otimizado para produção.
    
    Esta função coordena todo o processo de criação do pacote de produção
    do Sistema Dashboard IFPB-CZ, incluindo análise do projeto, seleção
    inteligente de arquivos, aplicação de filtros de exclusão, criação
    do arquivo ZIP otimizado e geração de relatório completo com
    instruções para deploy.
    
    PROCESSO COMPLETO EXECUTADO:
    1. Validação de execução no diretório correto
    2. Análise estatística completa do projeto
    3. Criação do arquivo ZIP com compressão otimizada
    4. Inclusão seletiva de arquivos obrigatórios
    5. Inclusão condicional de componentes opcionais
    6. Processamento de pastas com filtros aplicados
    7. Geração de relatório final e instruções
    
    ANÁLISES ESTATÍSTICAS REALIZADAS:
    - Contagem total de arquivos no projeto
    - Cálculo de tamanho total original
    - Arquivos selecionados para produção
    - Tamanho otimizado do pacote final
    - Percentual de redução alcançado
    
    INCLUSÃO DE COMPONENTES:
    - Arquivos obrigatórios: sempre incluídos se existentes
    - Arquivos opcionais: incluídos apenas se existentes
    - Pastas obrigatórias: processadas com filtros
    - Pastas opcionais: incluídas condicionalmente
    
    OTIMIZAÇÕES APLICADAS:
    - Compressão ZIP_DEFLATED para menor tamanho
    - Filtros recursivos para exclusão automática
    - Contabilização precisa de arquivos incluídos
    - Validação de existência antes da inclusão
    
    RELATÓRIOS GERADOS:
    - Análise estatística do projeto
    - Status de inclusão por categoria
    - Instruções detalhadas para deploy
    - Informações de configuração necessárias
    
    VALIDAÇÕES DE SEGURANÇA:
    - Verificação de diretório de execução
    - Tratamento de exceções durante criação
    - Validação de arquivos obrigatórios
    - Relatório de status para cada componente
    
    RETORNO:
    --------
    bool
        True se pacote foi criado com sucesso,
        False se houve falha crítica no processo
        
    SAÍDAS GERADAS:
    ---------------
    - Cabeçalho identificador do processo
    - Análise estatística detalhada do projeto
    - Status de inclusão de cada componente
    - Arquivo ZIP otimizado para produção
    - Instruções completas para deploy
    - Documentação de referência disponível
    """
    # Exibir cabeçalho principal do processo
    print("=" * 70)
    print("🚀 CRIADOR DE PACOTE DE PRODUÇÃO - Dashboard IFPB-CZ")
    print("=" * 70)
    
    # =============================================================================
    # VALIDAÇÃO DE EXECUÇÃO NO DIRETÓRIO CORRETO DO PROJETO
    # =============================================================================
    
    # Verificar se estamos no diretório raiz do projeto
    if not os.path.exists('app.py'):
        print("❌ ERRO: Execute este script na raiz do projeto!")
        print("   O arquivo 'app.py' não foi encontrado no diretório atual.")
        return False
    
    # Informar nome do pacote que será criado
    print(f"📦 Criando pacote: {NOME_PACOTE}")
    print()
    
    # =============================================================================
    # ANÁLISE ESTATÍSTICA COMPLETA DO PROJETO
    # =============================================================================
    
    print("📊 ANÁLISE DO PROJETO:")
    print("-" * 50)
    
    # Inicializar contadores para estatísticas
    total_arquivos = 0      # Total de arquivos no projeto
    total_tamanho = 0       # Tamanho total original
    arquivos_incluidos = 0  # Arquivos selecionados para produção
    tamanho_incluido = 0    # Tamanho otimizado do pacote
    
    # Contabilizar arquivos do diretório raiz atual
    for item in os.listdir('.'):
        if os.path.isfile(item):
            # Processar arquivo individual
            total_arquivos += 1
            total_tamanho += os.path.getsize(item)
            if not deve_excluir_arquivo(item):
                arquivos_incluidos += 1
                tamanho_incluido += os.path.getsize(item)
        elif os.path.isdir(item) and not deve_excluir_pasta(item):
            # Processar pasta recursivamente
            arquivos_pasta = contar_arquivos_pasta(item)
            tamanho_pasta = obter_tamanho_pasta(item)
            total_arquivos += arquivos_pasta
            total_tamanho += tamanho_pasta
            arquivos_incluidos += arquivos_pasta
            tamanho_incluido += tamanho_pasta
    
    # Exibir estatísticas detalhadas
    print(f"📁 Total de arquivos no projeto: {total_arquivos}")
    print(f"📊 Tamanho total: {formatar_tamanho(total_tamanho)}")
    print(f"✅ Arquivos para produção: {arquivos_incluidos}")
    print(f"📦 Tamanho do pacote: {formatar_tamanho(tamanho_incluido)}")
    print(f"🗜️  Redução: {((total_tamanho - tamanho_incluido) / total_tamanho * 100):.1f}%")
    print()
    
    # =============================================================================
    # CRIAÇÃO DO ARQUIVO ZIP COM COMPRESSÃO OTIMIZADA
    # =============================================================================
    
    print("📦 CRIANDO PACOTE:")
    print("-" * 50)
    
    try:
        # Criar arquivo ZIP com compressão máxima
        with zipfile.ZipFile(NOME_PACOTE, 'w', zipfile.ZIP_DEFLATED) as zipf:
            
            # =============================================================================
            # INCLUSÃO DE ARQUIVOS OBRIGATÓRIOS
            # =============================================================================
            
            print("📋 Adicionando arquivos obrigatórios...")
            for arquivo in ARQUIVOS_OBRIGATORIOS:
                if os.path.exists(arquivo):
                    # Arquivo obrigatório encontrado e incluído
                    zipf.write(arquivo)
                    print(f"   ✅ {arquivo}")
                else:
                    # Arquivo obrigatório ausente - alerta
                    print(f"   ⚠️  {arquivo} (não encontrado)")
            
            # =============================================================================
            # INCLUSÃO DE ARQUIVOS OPCIONAIS (APENAS SE EXISTENTES)
            # =============================================================================
            
            print("\n📋 Adicionando arquivos opcionais...")
            for arquivo in ARQUIVOS_OPCIONAIS:
                if os.path.exists(arquivo):
                    # Arquivo opcional encontrado e incluído
                    zipf.write(arquivo)
                    print(f"   ✅ {arquivo}")
                else:
                    # Arquivo opcional ausente - informativo
                    print(f"   ⏭️  {arquivo} (não encontrado)")
            
            # =============================================================================
            # INCLUSÃO DE PASTAS OBRIGATÓRIAS COM FILTROS
            # =============================================================================
            
            print("\n📁 Adicionando pastas obrigatórias...")
            for pasta in PASTAS_OBRIGATORIAS:
                if os.path.exists(pasta):
                    # Processar pasta recursivamente com filtros
                    arquivos_adicionados = 0
                    for root, dirs, files in os.walk(pasta):
                        # Aplicar filtro de exclusão para subpastas
                        dirs[:] = [d for d in dirs if not deve_excluir_pasta(os.path.join(root, d))]
                        
                        # Processar arquivos individuais
                        for arquivo in files:
                            caminho_arquivo = os.path.join(root, arquivo)
                            if not deve_excluir_arquivo(caminho_arquivo):
                                zipf.write(caminho_arquivo)
                                arquivos_adicionados += 1
                    
                    print(f"   ✅ {pasta}/ ({arquivos_adicionados} arquivos)")
                else:
                    # Pasta obrigatória ausente - alerta
                    print(f"   ⚠️  {pasta}/ (não encontrado)")
            
            # =============================================================================
            # INCLUSÃO DE PASTAS OPCIONAIS (APENAS SE EXISTENTES)
            # =============================================================================
            
            print("\n📁 Adicionando pastas opcionais...")
            for pasta in PASTAS_OPCIONAIS:
                if os.path.exists(pasta):
                    # Processar pasta opcional recursivamente
                    arquivos_adicionados = 0
                    for root, dirs, files in os.walk(pasta):
                        # Aplicar filtro de exclusão para subpastas
                        dirs[:] = [d for d in dirs if not deve_excluir_pasta(os.path.join(root, d))]
                        
                        # Processar arquivos individuais
                        for arquivo in files:
                            caminho_arquivo = os.path.join(root, arquivo)
                            if not deve_excluir_arquivo(caminho_arquivo):
                                zipf.write(caminho_arquivo)
                                arquivos_adicionados += 1
                    
                    print(f"   ✅ {pasta}/ ({arquivos_adicionados} arquivos)")
                else:
                    # Pasta opcional ausente - informativo
                    print(f"   ⏭️  {pasta}/ (não encontrado)")
        
        # =============================================================================
        # VERIFICAÇÃO FINAL E RELATÓRIO DE SUCESSO
        # =============================================================================
        
        # Calcular tamanho final do arquivo ZIP criado
        tamanho_zip = os.path.getsize(NOME_PACOTE)
        
        print()
        print("🎉 PACOTE CRIADO COM SUCESSO!")
        print("=" * 70)
        print(f"📦 Arquivo: {NOME_PACOTE}")
        print(f"📊 Tamanho: {formatar_tamanho(tamanho_zip)}")
        print(f"📅 Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print()
        print("🚀 INSTRUÇÕES PARA DEPLOY:")
        print("-" * 50)
        print("1. Faça upload do arquivo ZIP para o servidor")
        print("2. Extraia o conteúdo em uma pasta (ex: /var/www/dashboard)")
        print("3. Instale as dependências: pip install -r requirements.txt")
        print("4. Configure o arquivo config.py para produção")
        print("5. Execute: streamlit run app.py --server.port 8501")
        print()
        print("📚 DOCUMENTAÇÃO:")
        print("-" * 50)
        print("• README.md - Instruções completas de instalação")
        print("• docs/ - Documentação técnica detalhada")
        print("• Sistema de ajuda integrado (botão ❓ na interface)")
        print()
        
        return True
        
    except Exception as e:
        # Tratamento de erro durante criação do pacote
        print(f"❌ ERRO ao criar o pacote: {e}")
        return False

# =============================================================================
# COORDENAÇÃO DE EXECUÇÃO DO SCRIPT
# =============================================================================

if __name__ == "__main__":
    """
    Ponto de entrada principal do script de criação de pacote de produção.
    
    Esta seção coordena a execução completa do processo de criação de
    pacote otimizado para produção do Sistema Dashboard IFPB-CZ,
    gerando código de saída apropriado para integração com sistemas
    de automação e CI/CD.
    
    EXECUÇÃO REALIZADA:
    1. Verificação de execução direta do script
    2. Chamada da função principal de criação
    3. Processo completo de análise e compactação
    4. Determinação de código de saída baseado em resultado
    
    CÓDIGOS DE SAÍDA:
    - 0: pacote criado com sucesso
    - 1: falha durante criação do pacote
    
    FINALIDADE:
    -----------
    Permitir execução independente do script para criação
    automatizada de pacotes de produção, com integração
    apropriada em pipelines de deploy e CI/CD.
    
    PROCESSO:
    ---------
    - Execução direta: python criar_pacote_producao.py
    - Criação otimizada: pacote ZIP completo
    - Relatório detalhado: estatísticas e instruções
    - Código de saída: compatível com automação
    """
    print()
    
    # Executar criação do pacote e capturar resultado
    sucesso = criar_pacote_producao()
    
    if sucesso:
        print("✅ Processo concluído com sucesso!")
        sys.exit(0)
    else:
        print("❌ Processo falhou!")
        sys.exit(1)
