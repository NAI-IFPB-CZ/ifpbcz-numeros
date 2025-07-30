#!/usr/bin/env python3
"""
==============================================================================
SCRIPT PARA CRIAÇÃO DE PACOTE DE PRODUÇÃO
==============================================================================

Script para criar um arquivo ZIP contendo apenas os arquivos necessários
para deploy em servidor de produção do Sistema Dashboard IFPB-CZ.

Remove arquivos de desenvolvimento, cache, logs e outros desnecessários
para otimizar o pacote de deploy.

Autor: Sistema NAI/IFPB-CZ
Versão: 2.0 - Dashboard Institucional Completo
Data: Julho 2025
==============================================================================
"""

import os
import zipfile
import shutil
from datetime import datetime
import sys

# ==============================================================================
# CONFIGURAÇÕES DO PACOTE
# ==============================================================================

# Nome do arquivo ZIP de produção
NOME_PACOTE = f"dashboard-ifpb-cz-producao-{datetime.now().strftime('%Y%m%d-%H%M%S')}.zip"

# Arquivos e pastas OBRIGATÓRIOS para produção
ARQUIVOS_OBRIGATORIOS = [
    'app.py',                    # Aplicação principal
    'requirements.txt',          # Dependências
    'config.py',                 # Configurações do sistema
    'README.md',                 # Documentação principal
    'LICENSE',                   # Licença
    'GUIA_ATUALIZACAO_DADOS.md', # Guia de atualização
]

PASTAS_OBRIGATORIAS = [
    'modules',                   # Módulos do sistema
    '.streamlit',                # Configurações Streamlit
    'logo-ifpb',                 # Logotipos institucionais
    'dados',                     # Dados Excel (se existir)
    'docs',                      # Documentação técnica
]

# Arquivos e pastas OPCIONAIS (incluir se existirem)
ARQUIVOS_OPCIONAIS = [
    'configurar_seguranca.py',   # Script de configuração
    'testar_seguranca.py',       # Script de teste
    'MODULO_MAPA.md',            # Documentação do mapa
]

PASTAS_OPCIONAIS = [
    'fluxo',                     # Diagramas de fluxo
]

# Arquivos e pastas para EXCLUIR (desenvolvimento/cache)
EXCLUIR_ARQUIVOS = [
    'criar_pacote_producao.py',  # Este próprio script
    'criar_planilhas_exemplo.py',
    'criar_planilhas_exemplo_real.py',
    'test_dados_reais.py',
    'test_extensao.py',
    'README_old.md',
    'paginas-pesquisa.md',
    '.gitignore',
    '*.log',
    '*.tmp',
    'Thumbs.db',
    '.DS_Store',
]

EXCLUIR_PASTAS = [
    '.git',                      # Controle de versão
    '.venv',                     # Ambiente virtual
    '.vscode',                   # Configurações IDE
    '__pycache__',               # Cache Python
    '*.egg-info',                # Informações de pacote
    '.pytest_cache',             # Cache de testes
    'build',                     # Arquivos de build
    'dist',                      # Distribuição
]

EXCLUIR_EXTENSOES = [
    '.pyc',                      # Bytecode Python
    '.pyo',                      # Bytecode otimizado
    '.pyd',                      # Extensões Windows
    '.log',                      # Arquivos de log
    '.tmp',                      # Arquivos temporários
    '.bak',                      # Backups
    '.swp',                      # Arquivos swap
]

# ==============================================================================
# FUNÇÕES AUXILIARES
# ==============================================================================

def deve_excluir_arquivo(caminho_arquivo):
    """
    Verifica se um arquivo deve ser excluído do pacote.
    
    Args:
        caminho_arquivo (str): Caminho do arquivo
        
    Returns:
        bool: True se deve excluir, False caso contrário
    """
    nome_arquivo = os.path.basename(caminho_arquivo)
    
    # Verificar arquivos específicos para excluir
    for padrao in EXCLUIR_ARQUIVOS:
        if padrao.endswith('*'):
            if nome_arquivo.startswith(padrao[:-1]):
                return True
        elif nome_arquivo == padrao:
            return True
    
    # Verificar extensões para excluir
    _, extensao = os.path.splitext(nome_arquivo)
    if extensao in EXCLUIR_EXTENSOES:
        return True
    
    return False

def deve_excluir_pasta(caminho_pasta):
    """
    Verifica se uma pasta deve ser excluída do pacote.
    
    Args:
        caminho_pasta (str): Caminho da pasta
        
    Returns:
        bool: True se deve excluir, False caso contrário
    """
    nome_pasta = os.path.basename(caminho_pasta)
    
    # Verificar pastas específicas para excluir
    for padrao in EXCLUIR_PASTAS:
        if padrao.endswith('*'):
            if nome_pasta.startswith(padrao[:-1]):
                return True
        elif nome_pasta == padrao:
            return True
    
    return False

def contar_arquivos_pasta(caminho_pasta):
    """
    Conta o número de arquivos em uma pasta recursivamente.
    
    Args:
        caminho_pasta (str): Caminho da pasta
        
    Returns:
        int: Número de arquivos
    """
    contador = 0
    if os.path.exists(caminho_pasta):
        for root, dirs, files in os.walk(caminho_pasta):
            # Filtrar pastas que devem ser excluídas
            dirs[:] = [d for d in dirs if not deve_excluir_pasta(os.path.join(root, d))]
            
            # Contar arquivos que não devem ser excluídos
            for arquivo in files:
                caminho_arquivo = os.path.join(root, arquivo)
                if not deve_excluir_arquivo(caminho_arquivo):
                    contador += 1
    return contador

def obter_tamanho_pasta(caminho_pasta):
    """
    Calcula o tamanho total de uma pasta em bytes.
    
    Args:
        caminho_pasta (str): Caminho da pasta
        
    Returns:
        int: Tamanho em bytes
    """
    tamanho_total = 0
    if os.path.exists(caminho_pasta):
        for root, dirs, files in os.walk(caminho_pasta):
            # Filtrar pastas que devem ser excluídas
            dirs[:] = [d for d in dirs if not deve_excluir_pasta(os.path.join(root, d))]
            
            # Somar tamanho dos arquivos
            for arquivo in files:
                caminho_arquivo = os.path.join(root, arquivo)
                if not deve_excluir_arquivo(caminho_arquivo):
                    try:
                        tamanho_total += os.path.getsize(caminho_arquivo)
                    except (OSError, IOError):
                        pass
    return tamanho_total

def formatar_tamanho(tamanho_bytes):
    """
    Formata o tamanho em bytes para formato legível.
    
    Args:
        tamanho_bytes (int): Tamanho em bytes
        
    Returns:
        str: Tamanho formatado
    """
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if tamanho_bytes < 1024.0:
            return f"{tamanho_bytes:.1f} {unidade}"
        tamanho_bytes /= 1024.0
    return f"{tamanho_bytes:.1f} TB"

# ==============================================================================
# FUNÇÃO PRINCIPAL
# ==============================================================================

def criar_pacote_producao():
    """
    Cria o pacote ZIP para produção com apenas os arquivos necessários.
    """
    print("=" * 70)
    print("🚀 CRIADOR DE PACOTE DE PRODUÇÃO - Dashboard IFPB-CZ")
    print("=" * 70)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists('app.py'):
        print("❌ ERRO: Execute este script na raiz do projeto!")
        print("   O arquivo 'app.py' não foi encontrado no diretório atual.")
        return False
    
    print(f"📦 Criando pacote: {NOME_PACOTE}")
    print()
    
    # Estatísticas iniciais
    print("📊 ANÁLISE DO PROJETO:")
    print("-" * 50)
    
    total_arquivos = 0
    total_tamanho = 0
    arquivos_incluidos = 0
    tamanho_incluido = 0
    
    # Contabilizar arquivos do diretório atual
    for item in os.listdir('.'):
        if os.path.isfile(item):
            total_arquivos += 1
            total_tamanho += os.path.getsize(item)
            if not deve_excluir_arquivo(item):
                arquivos_incluidos += 1
                tamanho_incluido += os.path.getsize(item)
        elif os.path.isdir(item) and not deve_excluir_pasta(item):
            arquivos_pasta = contar_arquivos_pasta(item)
            tamanho_pasta = obter_tamanho_pasta(item)
            total_arquivos += arquivos_pasta
            total_tamanho += tamanho_pasta
            arquivos_incluidos += arquivos_pasta
            tamanho_incluido += tamanho_pasta
    
    print(f"📁 Total de arquivos no projeto: {total_arquivos}")
    print(f"📊 Tamanho total: {formatar_tamanho(total_tamanho)}")
    print(f"✅ Arquivos para produção: {arquivos_incluidos}")
    print(f"📦 Tamanho do pacote: {formatar_tamanho(tamanho_incluido)}")
    print(f"🗜️  Redução: {((total_tamanho - tamanho_incluido) / total_tamanho * 100):.1f}%")
    print()
    
    # Criar o arquivo ZIP
    print("📦 CRIANDO PACOTE:")
    print("-" * 50)
    
    try:
        with zipfile.ZipFile(NOME_PACOTE, 'w', zipfile.ZIP_DEFLATED) as zipf:
            
            # Adicionar arquivos obrigatórios
            print("📋 Adicionando arquivos obrigatórios...")
            for arquivo in ARQUIVOS_OBRIGATORIOS:
                if os.path.exists(arquivo):
                    zipf.write(arquivo)
                    print(f"   ✅ {arquivo}")
                else:
                    print(f"   ⚠️  {arquivo} (não encontrado)")
            
            # Adicionar arquivos opcionais
            print("\n📋 Adicionando arquivos opcionais...")
            for arquivo in ARQUIVOS_OPCIONAIS:
                if os.path.exists(arquivo):
                    zipf.write(arquivo)
                    print(f"   ✅ {arquivo}")
                else:
                    print(f"   ⏭️  {arquivo} (não encontrado)")
            
            # Adicionar pastas obrigatórias
            print("\n📁 Adicionando pastas obrigatórias...")
            for pasta in PASTAS_OBRIGATORIAS:
                if os.path.exists(pasta):
                    arquivos_adicionados = 0
                    for root, dirs, files in os.walk(pasta):
                        # Filtrar subpastas que devem ser excluídas
                        dirs[:] = [d for d in dirs if not deve_excluir_pasta(os.path.join(root, d))]
                        
                        for arquivo in files:
                            caminho_arquivo = os.path.join(root, arquivo)
                            if not deve_excluir_arquivo(caminho_arquivo):
                                zipf.write(caminho_arquivo)
                                arquivos_adicionados += 1
                    
                    print(f"   ✅ {pasta}/ ({arquivos_adicionados} arquivos)")
                else:
                    print(f"   ⚠️  {pasta}/ (não encontrado)")
            
            # Adicionar pastas opcionais
            print("\n📁 Adicionando pastas opcionais...")
            for pasta in PASTAS_OPCIONAIS:
                if os.path.exists(pasta):
                    arquivos_adicionados = 0
                    for root, dirs, files in os.walk(pasta):
                        # Filtrar subpastas que devem ser excluídas
                        dirs[:] = [d for d in dirs if not deve_excluir_pasta(os.path.join(root, d))]
                        
                        for arquivo in files:
                            caminho_arquivo = os.path.join(root, arquivo)
                            if not deve_excluir_arquivo(caminho_arquivo):
                                zipf.write(caminho_arquivo)
                                arquivos_adicionados += 1
                    
                    print(f"   ✅ {pasta}/ ({arquivos_adicionados} arquivos)")
                else:
                    print(f"   ⏭️  {pasta}/ (não encontrado)")
        
        # Verificar o arquivo criado
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
        print(f"❌ ERRO ao criar o pacote: {e}")
        return False

# ==============================================================================
# EXECUTAR SCRIPT
# ==============================================================================

if __name__ == "__main__":
    print()
    sucesso = criar_pacote_producao()
    
    if sucesso:
        print("✅ Processo concluído com sucesso!")
        sys.exit(0)
    else:
        print("❌ Processo falhou!")
        sys.exit(1)
