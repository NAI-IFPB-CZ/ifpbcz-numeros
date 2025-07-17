#!/usr/bin/env python3
"""
Script para alternar configurações de segurança do sistema

Este script ajuda a alternar entre modo seguro (produção) e modo de edição (desenvolvimento).
Permite configurar rapidamente as variáveis de segurança no arquivo config.py

FUNCIONAMENTO:
- Modo Seguro (Produção): Impede criação/edição de planilhas, protege dados existentes
- Modo Edição (Desenvolvimento): Permite criação/edição de planilhas para testes

SEGURANÇA:
- PERMITIR_CRIACAO_PLANILHAS: Controla se novas planilhas podem ser criadas
- SOBRESCREVER_ARQUIVOS_EXISTENTES: Controla se arquivos existentes podem ser sobrescritos
- MODO_SOMENTE_LEITURA: Força o sistema a operar apenas em leitura

EXEMPLOS DE USO:
    python configurar_seguranca.py seguro   # Ativa modo seguro
    python configurar_seguranca.py edicao   # Ativa modo edição
    python configurar_seguranca.py status   # Mostra configurações atuais

AUTOR: Sistema Dashboard IFPB-CZ
DATA: 2025
"""

# Importações necessárias
import os      # Para verificar existência de arquivos
import sys     # Para capturar argumentos da linha de comando

def alterar_configuracoes_seguranca(modo):
    """
    Altera as configurações de segurança no arquivo config.py
    
    Args:
        modo (str): 'seguro' para produção ou 'edicao' para desenvolvimento
    
    Returns:
        bool: True se alteração foi bem-sucedida, False caso contrário
    """
    
    # Nome do arquivo de configuração
    config_file = 'config.py'
    
    # Verificar se o arquivo de configuração existe
    if not os.path.exists(config_file):
        print(f"❌ Arquivo {config_file} não encontrado!")
        return False
    
    # Ler o conteúdo atual do arquivo config.py
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Configurar para modo seguro (produção)
    if modo == 'seguro':
        # Configurações para produção (modo seguro)
        # Desabilita criação de novas planilhas
        content = content.replace(
            'PERMITIR_CRIACAO_PLANILHAS = True',
            'PERMITIR_CRIACAO_PLANILHAS = False'
        )
        # Desabilita sobrescrita de arquivos existentes
        content = content.replace(
            'SOBRESCREVER_ARQUIVOS_EXISTENTES = True',
            'SOBRESCREVER_ARQUIVOS_EXISTENTES = False'
        )
        # Ativa modo somente leitura
        content = content.replace(
            'MODO_SOMENTE_LEITURA = False',
            'MODO_SOMENTE_LEITURA = True'
        )
        
        # Informar ao usuário as mudanças aplicadas
        print("✅ Configurações alteradas para MODO SEGURO (Produção)")
        print("   - PERMITIR_CRIACAO_PLANILHAS = False")
        print("   - SOBRESCREVER_ARQUIVOS_EXISTENTES = False")
        print("   - MODO_SOMENTE_LEITURA = True")
        
    # Configurar para modo de edição (desenvolvimento)
    elif modo == 'edicao':
        # Configurações para desenvolvimento (modo edição)
        # Permite criação de novas planilhas
        content = content.replace(
            'PERMITIR_CRIACAO_PLANILHAS = False',
            'PERMITIR_CRIACAO_PLANILHAS = True'
        )
        # Permite sobrescrita de arquivos existentes
        content = content.replace(
            'SOBRESCREVER_ARQUIVOS_EXISTENTES = False',
            'SOBRESCREVER_ARQUIVOS_EXISTENTES = True'
        )
        # Desativa modo somente leitura
        content = content.replace(
            'MODO_SOMENTE_LEITURA = True',
            'MODO_SOMENTE_LEITURA = False'
        )
        
        # Informar ao usuário as mudanças aplicadas
        print("✅ Configurações alteradas para MODO EDIÇÃO (Desenvolvimento)")
        print("   - PERMITIR_CRIACAO_PLANILHAS = True")
        print("   - SOBRESCREVER_ARQUIVOS_EXISTENTES = True")
        print("   - MODO_SOMENTE_LEITURA = False")
        
    else:
        # Modo inválido fornecido
        print("❌ Modo inválido! Use 'seguro' ou 'edicao'")
        return False
    
    # Salvar as alterações no arquivo config.py
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Confirmação de sucesso
    print(f"\n📝 Arquivo {config_file} atualizado com sucesso!")
    print("🔄 Reinicie o sistema Streamlit para aplicar as mudanças.")
    
    return True

def mostrar_configuracoes_atuais():
    """
    Mostra as configurações atuais do sistema
    
    Lê as configurações do arquivo config.py e exibe no console
    Indica se o sistema está em modo seguro ou edição
    """
    try:
        # Importar as configurações atuais do arquivo config.py
        from config import (
            PERMITIR_CRIACAO_PLANILHAS,
            SOBRESCREVER_ARQUIVOS_EXISTENTES,
            MODO_SOMENTE_LEITURA
        )
        
        # Exibir o estado atual das configurações
        print("📊 CONFIGURAÇÕES ATUAIS:")
        print(f"   - PERMITIR_CRIACAO_PLANILHAS = {PERMITIR_CRIACAO_PLANILHAS}")
        print(f"   - SOBRESCREVER_ARQUIVOS_EXISTENTES = {SOBRESCREVER_ARQUIVOS_EXISTENTES}")
        print(f"   - MODO_SOMENTE_LEITURA = {MODO_SOMENTE_LEITURA}")
        
        # Determinar e exibir o modo atual do sistema
        if MODO_SOMENTE_LEITURA:
            print("   🔒 Sistema em MODO SEGURO (Produção)")
        else:
            print("   🔓 Sistema em MODO EDIÇÃO (Desenvolvimento)")
            
    except ImportError:
        # Erro ao importar configurações - arquivo config.py pode não existir
        print("❌ Erro ao carregar configurações do config.py")

def main():
    """
    Função principal do script
    
    Processa argumentos da linha de comando e executa a ação correspondente:
    - seguro: Ativa modo seguro (produção)
    - edicao: Ativa modo edição (desenvolvimento)  
    - status: Mostra configurações atuais
    """
    # Cabeçalho do programa
    print("🔧 Gerenciador de Configurações de Segurança")
    print("=" * 50)
    
    # Verificar se foi fornecido algum argumento
    if len(sys.argv) < 2:
        # Exibir instruções de uso se nenhum argumento for fornecido
        print("💡 Uso:")
        print("   python configurar_seguranca.py <modo>")
        print("   python configurar_seguranca.py status")
        print("")
        print("📋 Modos disponíveis:")
        print("   seguro  - Ativa proteções para produção")
        print("   edicao  - Permite edição para desenvolvimento")
        print("   status  - Mostra configurações atuais")
        print("")
        # Mostrar configurações atuais como informação adicional
        mostrar_configuracoes_atuais()
        return
    
    # Capturar o modo solicitado (convertido para minúsculas)
    modo = sys.argv[1].lower()
    
    # Processar o comando baseado no modo solicitado
    if modo == 'status':
        # Exibir apenas o status atual
        mostrar_configuracoes_atuais()
    elif modo in ['seguro', 'edicao']:
        # Alterar configurações para o modo solicitado
        alterar_configuracoes_seguranca(modo)
    else:
        # Modo inválido fornecido
        print("❌ Modo inválido! Use 'seguro', 'edicao' ou 'status'")


# Ponto de entrada do script
# Este bloco só é executado quando o script é chamado diretamente
if __name__ == "__main__":
    main()
