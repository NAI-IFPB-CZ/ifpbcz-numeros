#!/usr/bin/env python3
"""
==============================================================================
SCRIPT SIMPLIFICADO PARA DEPLOY RÁPIDO
==============================================================================

Versão simplificada do criador de pacote para deploys rápidos.
Inclui apenas os arquivos essenciais para funcionamento básico.

Uso: python deploy_rapido.py

Autor: Sistema NAI/IFPB-CZ
==============================================================================
"""

import os
import zipfile
from datetime import datetime

def criar_deploy_rapido():
    """Cria um pacote mínimo para deploy rápido."""
    
    nome_zip = f"dashboard-deploy-rapido-{datetime.now().strftime('%Y%m%d-%H%M')}.zip"
    
    # Arquivos essenciais mínimos
    arquivos_essenciais = [
        'app.py',
        'requirements.txt',
        'config.py',
        'README.md'
    ]
    
    # Pastas essenciais mínimas
    pastas_essenciais = [
        'modules',
        '.streamlit',
        'logo-ifpb'
    ]
    
    print(f"🚀 Criando deploy rápido: {nome_zip}")
    
    try:
        with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            
            # Adicionar arquivos
            for arquivo in arquivos_essenciais:
                if os.path.exists(arquivo):
                    zipf.write(arquivo)
                    print(f"✅ {arquivo}")
            
            # Adicionar pastas
            for pasta in pastas_essenciais:
                if os.path.exists(pasta):
                    for root, dirs, files in os.walk(pasta):
                        # Excluir cache
                        dirs[:] = [d for d in dirs if d != '__pycache__']
                        
                        for arquivo in files:
                            if not arquivo.endswith('.pyc'):
                                caminho = os.path.join(root, arquivo)
                                zipf.write(caminho)
                    print(f"✅ {pasta}/")
        
        tamanho = os.path.getsize(nome_zip) / 1024 / 1024
        print(f"✅ Deploy criado: {nome_zip} ({tamanho:.1f} MB)")
        print("🚀 Pronto para upload no servidor!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    criar_deploy_rapido()
