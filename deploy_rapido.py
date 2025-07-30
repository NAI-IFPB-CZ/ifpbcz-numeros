#!/usr/bin/env python3
"""
=============================================================================
SCRIPT SIMPLIFICADO PARA DEPLOY RÁPIDO - SISTEMA DASHBOARD IFPB-CZ
=============================================================================

Este script implementa criação automatizada de pacote mínimo e otimizado
para deploy rápido do Sistema Dashboard IFPB-CZ, incluindo apenas arquivos
essenciais para funcionamento básico em ambiente de produção, reduzindo
tempo de upload e complexidade de instalação em servidores.

FUNCIONALIDADES PRINCIPAIS:
---------------------------
- Criação automatizada de pacote ZIP compactado
- Seleção inteligente de arquivos essenciais mínimos
- Exclusão automática de cache e arquivos desnecessários
- Compressão otimizada para redução de tamanho
- Timestamp automático para versionamento de deploys
- Validação de integridade antes da compactação

ESTRATÉGIA DE DEPLOY RÁPIDO:
----------------------------
- Arquivos mínimos: apenas componentes críticos
- Pastas essenciais: estrutura funcional básica
- Exclusão de cache: __pycache__ e .pyc removidos
- Compressão máxima: ZIP_DEFLATED para menor tamanho
- Nomenclatura versionada: timestamp para identificação

ARQUIVOS ESSENCIAIS INCLUÍDOS:
------------------------------
- app.py: aplicação principal Streamlit
- requirements.txt: dependências críticas
- config.py: configurações do sistema
- README.md: documentação de instalação

PASTAS ESSENCIAIS INCLUÍDAS:
----------------------------
- modules/: todos os módulos funcionais do dashboard
- .streamlit/: configurações específicas do framework
- logo-ifpb/: recursos visuais institucionais

OTIMIZAÇÕES IMPLEMENTADAS:
--------------------------
- Exclusão de __pycache__: remoção de cache Python
- Filtro de .pyc: eliminação de bytecode compilado
- Compressão DEFLATED: máxima redução de tamanho
- Estrutura mínima: apenas arquivos funcionais críticos

VALIDAÇÕES DE SEGURANÇA:
------------------------
- Verificação de existência antes da inclusão
- Tratamento de exceções durante compactação
- Relatório de arquivos incluídos com sucesso
- Cálculo de tamanho final do pacote

PROCESSO DE CRIAÇÃO:
--------------------
1. Geração de nome único com timestamp
2. Verificação individual de arquivos essenciais
3. Inclusão seletiva de pastas com filtros
4. Exclusão automática de cache e temporários
5. Compactação otimizada com ZIP_DEFLATED
6. Relatório de resultado e tamanho final

NOMENCLATURA DE ARQUIVOS:
-------------------------
Formato: dashboard-deploy-rapido-YYYYMMDD-HHMM.zip
Exemplo: dashboard-deploy-rapido-20240730-1425.zip

VANTAGENS DO DEPLOY RÁPIDO:
---------------------------
- Upload mais rápido: arquivo menor
- Instalação simplificada: menos arquivos
- Menor complexidade: estrutura mínima
- Funcionalidade completa: todos os recursos principais
- Versionamento automático: identificação por timestamp

OBJETIVO:
---------
Facilitar deploys rápidos e eficientes do Sistema Dashboard
IFPB-CZ em ambientes de produção, reduzindo tempo de upload
e mantendo funcionalidade completa com estrutura mínima
essencial para operação adequada.

USO:
----
python deploy_rapido.py

SAÍDA:
------
Arquivo ZIP compactado pronto para upload no servidor

DEPENDÊNCIAS:
-------------
- os: manipulação de sistema de arquivos
- zipfile: criação e compressão de arquivos ZIP
- datetime: geração de timestamps para versionamento

AUTOR: Sistema Dashboard IFPB-CZ - NAI
DATA: 2024
=============================================================================
"""

import os
import zipfile
from datetime import datetime

def criar_deploy_rapido():
    """
    Criação automatizada de pacote mínimo para deploy rápido do sistema.
    
    Esta função implementa processo completo de criação de pacote ZIP
    otimizado para deploy rápido do Sistema Dashboard IFPB-CZ, incluindo
    apenas arquivos e pastas essenciais para funcionamento básico,
    com compressão máxima e exclusão de arquivos desnecessários.
    
    PROCESSO DE CRIAÇÃO:
    1. Geração de nome único com timestamp atual
    2. Definição de listas de arquivos e pastas essenciais
    3. Criação de arquivo ZIP com compressão otimizada
    4. Inclusão seletiva de arquivos com validação
    5. Processamento de pastas com filtros de exclusão
    6. Cálculo de tamanho final e relatório de resultado
    
    ARQUIVOS INCLUÍDOS:
    - app.py: aplicação principal do Streamlit
    - requirements.txt: dependências críticas do Python
    - config.py: configurações do sistema
    - README.md: documentação de instalação
    
    PASTAS INCLUÍDAS:
    - modules/: todos os módulos funcionais completos
    - .streamlit/: configurações específicas do framework
    - logo-ifpb/: recursos visuais institucionais
    
    OTIMIZAÇÕES APLICADAS:
    - Compressão ZIP_DEFLATED: máxima redução de tamanho
    - Exclusão de __pycache__: remoção de cache Python
    - Filtro de .pyc: eliminação de bytecode compilado
    - Validação de existência: apenas arquivos válidos
    
    FILTROS DE EXCLUSÃO:
    - Diretórios __pycache__: cache Python desnecessário
    - Arquivos .pyc: bytecode compilado temporário
    - Estruturas de cache: otimização de tamanho
    
    NOMENCLATURA GERADA:
    Formato: dashboard-deploy-rapido-YYYYMMDD-HHMM.zip
    Timestamp: identificação única por data/hora
    
    RETORNO:
    --------
    None
        Função de criação com saída via logging console
        Arquivo ZIP criado no diretório atual
        
    SAÍDAS GERADAS:
    ---------------
    - Nome do arquivo ZIP sendo criado
    - Status de inclusão de cada arquivo/pasta
    - Tamanho final do pacote em MB
    - Confirmação de prontidão para upload
    - Tratamento de erros durante criação
    """
    # Gerar nome único do arquivo ZIP com timestamp atual
    nome_zip = f"dashboard-deploy-rapido-{datetime.now().strftime('%Y%m%d-%H%M')}.zip"
    
    # =============================================================================
    # DEFINIÇÃO DE ARQUIVOS ESSENCIAIS MÍNIMOS PARA FUNCIONAMENTO
    # =============================================================================
    
    # Lista de arquivos críticos obrigatórios para operação básica
    arquivos_essenciais = [
        'app.py',           # Aplicação principal Streamlit
        'requirements.txt', # Dependências críticas Python
        'config.py',        # Configurações do sistema
        'README.md'         # Documentação de instalação
    ]
    
    # =============================================================================
    # DEFINIÇÃO DE PASTAS ESSENCIAIS MÍNIMAS PARA ESTRUTURA FUNCIONAL
    # =============================================================================
    
    # Lista de pastas críticas para funcionamento completo
    pastas_essenciais = [
        'modules',      # Módulos funcionais do dashboard
        '.streamlit',   # Configurações específicas do framework
        'logo-ifpb'     # Recursos visuais institucionais
    ]
    
    # Exibir início do processo de criação
    print(f"🚀 Criando deploy rápido: {nome_zip}")
    
    # =============================================================================
    # PROCESSO DE CRIAÇÃO DO PACOTE ZIP OTIMIZADO
    # =============================================================================
    
    try:
        # Criar arquivo ZIP com compressão máxima
        with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            
            # =============================================================================
            # INCLUSÃO DE ARQUIVOS ESSENCIAIS COM VALIDAÇÃO
            # =============================================================================
            
            # Adicionar arquivos essenciais individualmente
            for arquivo in arquivos_essenciais:
                if os.path.exists(arquivo):
                    # Incluir arquivo validado no pacote
                    zipf.write(arquivo)
                    print(f"✅ {arquivo}")
            
            # =============================================================================
            # INCLUSÃO DE PASTAS COM FILTROS DE OTIMIZAÇÃO
            # =============================================================================
            
            # Adicionar pastas essenciais com filtros de exclusão
            for pasta in pastas_essenciais:
                if os.path.exists(pasta):
                    # Percorrer estrutura de pastas recursivamente
                    for root, dirs, files in os.walk(pasta):
                        # Aplicar filtro de exclusão para cache Python
                        dirs[:] = [d for d in dirs if d != '__pycache__']
                        
                        # Processar arquivos individuais com filtros
                        for arquivo in files:
                            # Excluir bytecode compilado Python
                            if not arquivo.endswith('.pyc'):
                                caminho = os.path.join(root, arquivo)
                                zipf.write(caminho)
                    print(f"✅ {pasta}/")
        
        # =============================================================================
        # RELATÓRIO FINAL DE CRIAÇÃO E ESTATÍSTICAS
        # =============================================================================
        
        # Calcular tamanho final do pacote em MB
        tamanho = os.path.getsize(nome_zip) / 1024 / 1024
        print(f"✅ Deploy criado: {nome_zip} ({tamanho:.1f} MB)")
        print("🚀 Pronto para upload no servidor!")
        
    except Exception as e:
        # Tratamento de erros durante criação do pacote
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    """
    Ponto de entrada principal do script de deploy rápido.
    
    Esta seção coordena a execução completa do processo de criação
    de pacote mínimo para deploy rápido do Sistema Dashboard IFPB-CZ,
    garantindo inclusão apenas de arquivos essenciais com otimizações
    de tamanho e tempo de upload.
    
    EXECUÇÃO REALIZADA:
    1. Verificação de execução direta do script
    2. Chamada da função principal de criação de pacote
    3. Processo completo de compactação otimizada
    4. Geração de arquivo ZIP pronto para deploy
    
    FINALIDADE:
    -----------
    Permitir execução independente do script para criação
    rápida de pacote de deploy, facilitando uploads eficientes
    e instalações simplificadas em servidores de produção.
    
    PROCESSO:
    ---------
    - Execução direta: python deploy_rapido.py
    - Criação automática: pacote ZIP otimizado
    - Compressão máxima: redução de tamanho
    - Upload eficiente: arquivo mínimo funcional
    """
    criar_deploy_rapido()
