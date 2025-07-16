#!/usr/bin/env python3
"""
Script para testar a alternância entre dados sintéticos e reais
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config
from modules.data_generator import DataGenerator
from modules.data_generator_real import DataGeneratorReal

def test_dados_sinteticos():
    """Testa a geração de dados sintéticos"""
    print("="*50)
    print("🔧 TESTANDO DADOS SINTÉTICOS")
    print("="*50)
    
    try:
        data_gen = DataGenerator()
        dados_extensao = data_gen.gerar_dados_extensao()
        
        print(f"✅ Dados sintéticos de extensão: {len(dados_extensao)} registros")
        print(f"📊 Colunas: {list(dados_extensao.columns)}")
        print(f"📅 Anos: {dados_extensao['ano'].min()} a {dados_extensao['ano'].max()}")
        
    except Exception as e:
        print(f"❌ Erro ao gerar dados sintéticos: {str(e)}")

def test_dados_reais():
    """Testa o carregamento de dados reais"""
    print("="*50)
    print("📊 TESTANDO DADOS REAIS")
    print("="*50)
    
    try:
        data_gen = DataGeneratorReal()
        dados_extensao = data_gen.gerar_dados_extensao()
        
        print(f"✅ Dados reais de extensão: {len(dados_extensao)} registros")
        print(f"📊 Colunas: {list(dados_extensao.columns)}")
        print(f"📅 Anos: {dados_extensao['ano'].min()} a {dados_extensao['ano'].max()}")
        
    except Exception as e:
        print(f"❌ Erro ao carregar dados reais: {str(e)}")
        print("💡 Dica: Execute 'python criar_planilhas_exemplo.py' para criar dados de exemplo")

def main():
    print("🚀 SISTEMA DE TESTE - DADOS SINTÉTICOS vs REAIS")
    print("="*60)
    
    print(f"📋 Configuração atual: USE_REAL_DATA = {config.USE_REAL_DATA}")
    print(f"📋 Validar dados: {config.VALIDAR_DADOS}")
    print(f"📋 Mostrar logs: {config.MOSTRAR_LOGS}")
    print(f"📋 Usar backup: {config.USAR_DADOS_BACKUP}")
    
    # Testar dados sintéticos
    test_dados_sinteticos()
    
    # Testar dados reais
    test_dados_reais()
    
    print("\n" + "="*60)
    print("📖 INSTRUÇÕES PARA USAR DADOS REAIS:")
    print("="*60)
    print("1. Execute: python criar_planilhas_exemplo.py")
    print("2. Substitua os arquivos na pasta 'dados/' pelos seus dados reais")
    print("3. Altere USE_REAL_DATA = True no arquivo config.py")
    print("4. Reinicie o sistema Streamlit")
    print("5. Verifique se os dados foram carregados corretamente")
    
    print("\n📝 ESTRUTURA NECESSÁRIA DOS ARQUIVOS:")
    print("- dados/dados_extensao.xlsx")
    print("- dados/dados_ensino.xlsx")
    print("- dados/dados_pesquisa.xlsx")
    print("- dados/dados_assistencia.xlsx")
    print("- dados/dados_auditoria.xlsx")
    print("- dados/dados_mundo_trabalho.xlsx")
    print("- dados/dados_orcamento.xlsx")
    print("- dados/dados_ouvidoria.xlsx")
    print("- dados/dados_servidores.xlsx")

if __name__ == "__main__":
    main()
