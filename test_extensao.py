#!/usr/bin/env python3
"""Script para testar a geração de dados de extensão"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.data_generator import DataGenerator

def test_extensao():
    """Testa a geração de dados de extensão"""
    print("Testando geração de dados de extensão...")
    
    # Criar instância do gerador
    data_gen = DataGenerator()
    
    # Gerar dados de extensão
    dados_extensao = data_gen.gerar_dados_extensao()
    
    # Verificar estrutura dos dados
    print(f"Total de registros: {len(dados_extensao)}")
    print(f"Colunas: {list(dados_extensao.columns)}")
    print(f"Tipos de dados:")
    print(dados_extensao.dtypes)
    
    # Mostrar alguns registros
    print(f"\nPrimeiros 5 registros:")
    print(dados_extensao.head())
    
    # Verificar dados de 2025
    dados_2025 = dados_extensao[dados_extensao['ano'] == 2025]
    print(f"\nRegistros de 2025: {len(dados_2025)}")
    
    if len(dados_2025) > 0:
        print("Primeira linha de 2025:")
        print(dados_2025.iloc[0].to_dict())

if __name__ == "__main__":
    test_extensao()
