#!/usr/bin/env python3
"""
Script para alternar configurações de segurança do sistema

Este script ajuda a alternar entre modo seguro (produção) e modo de edição (desenvolvimento).
"""

import os
import sys

def alterar_configuracoes_seguranca(modo):
    """
    Altera as configurações de segurança no arquivo config.py
    
    Args:
        modo (str): 'seguro' para produção ou 'edicao' para desenvolvimento
    """
    
    config_file = 'config.py'
    
    if not os.path.exists(config_file):
        print(f"❌ Arquivo {config_file} não encontrado!")
        return False
    
    # Ler o arquivo atual
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if modo == 'seguro':
        # Configurações para produção (modo seguro)
        content = content.replace(
            'PERMITIR_CRIACAO_PLANILHAS = True',
            'PERMITIR_CRIACAO_PLANILHAS = False'
        )
        content = content.replace(
            'SOBRESCREVER_ARQUIVOS_EXISTENTES = True',
            'SOBRESCREVER_ARQUIVOS_EXISTENTES = False'
        )
        content = content.replace(
            'MODO_SOMENTE_LEITURA = False',
            'MODO_SOMENTE_LEITURA = True'
        )
        
        print("✅ Configurações alteradas para MODO SEGURO (Produção)")
        print("   - PERMITIR_CRIACAO_PLANILHAS = False")
        print("   - SOBRESCREVER_ARQUIVOS_EXISTENTES = False")
        print("   - MODO_SOMENTE_LEITURA = True")
        
    elif modo == 'edicao':
        # Configurações para desenvolvimento (modo edição)
        content = content.replace(
            'PERMITIR_CRIACAO_PLANILHAS = False',
            'PERMITIR_CRIACAO_PLANILHAS = True'
        )
        content = content.replace(
            'SOBRESCREVER_ARQUIVOS_EXISTENTES = False',
            'SOBRESCREVER_ARQUIVOS_EXISTENTES = True'
        )
        content = content.replace(
            'MODO_SOMENTE_LEITURA = True',
            'MODO_SOMENTE_LEITURA = False'
        )
        
        print("✅ Configurações alteradas para MODO EDIÇÃO (Desenvolvimento)")
        print("   - PERMITIR_CRIACAO_PLANILHAS = True")
        print("   - SOBRESCREVER_ARQUIVOS_EXISTENTES = True")
        print("   - MODO_SOMENTE_LEITURA = False")
        
    else:
        print("❌ Modo inválido! Use 'seguro' ou 'edicao'")
        return False
    
    # Escrever o arquivo modificado
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n📝 Arquivo {config_file} atualizado com sucesso!")
    print("🔄 Reinicie o sistema Streamlit para aplicar as mudanças.")
    
    return True

def mostrar_configuracoes_atuais():
    """Mostra as configurações atuais"""
    try:
        from config import (
            PERMITIR_CRIACAO_PLANILHAS,
            SOBRESCREVER_ARQUIVOS_EXISTENTES,
            MODO_SOMENTE_LEITURA
        )
        
        print("📊 CONFIGURAÇÕES ATUAIS:")
        print(f"   - PERMITIR_CRIACAO_PLANILHAS = {PERMITIR_CRIACAO_PLANILHAS}")
        print(f"   - SOBRESCREVER_ARQUIVOS_EXISTENTES = {SOBRESCREVER_ARQUIVOS_EXISTENTES}")
        print(f"   - MODO_SOMENTE_LEITURA = {MODO_SOMENTE_LEITURA}")
        
        if MODO_SOMENTE_LEITURA:
            print("   🔒 Sistema em MODO SEGURO (Produção)")
        else:
            print("   🔓 Sistema em MODO EDIÇÃO (Desenvolvimento)")
            
    except ImportError:
        print("❌ Erro ao carregar configurações do config.py")

def main():
    """Função principal"""
    print("🔧 Gerenciador de Configurações de Segurança")
    print("=" * 50)
    
    if len(sys.argv) < 2:
        print("💡 Uso:")
        print("   python configurar_seguranca.py <modo>")
        print("   python configurar_seguranca.py status")
        print("")
        print("📋 Modos disponíveis:")
        print("   seguro  - Ativa proteções para produção")
        print("   edicao  - Permite edição para desenvolvimento")
        print("   status  - Mostra configurações atuais")
        print("")
        mostrar_configuracoes_atuais()
        return
    
    modo = sys.argv[1].lower()
    
    if modo == 'status':
        mostrar_configuracoes_atuais()
    elif modo in ['seguro', 'edicao']:
        alterar_configuracoes_seguranca(modo)
    else:
        print("❌ Modo inválido! Use 'seguro', 'edicao' ou 'status'")

if __name__ == "__main__":
    main()
