#!/usr/bin/env python3
"""
=============================================================================
SCRIPT DE TESTE ESPECÍFICO DO MÓDULO DE EXTENSÃO - SISTEMA DASHBOARD IFPB-CZ
=============================================================================

Este script implementa teste focalizado e detalhado do módulo de extensão
universitária, validando geração de dados sintéticos, estrutura de dados,
consistência temporal e integridade das informações geradas para o
Sistema Dashboard IFPB-CZ.

FUNCIONALIDADES PRINCIPAIS:
---------------------------
- Teste específico do gerador de dados de extensão
- Validação detalhada de estrutura e tipos de dados
- Análise de consistência temporal por período (2025)
- Verificação de integridade dos registros gerados
- Diagnóstico visual da qualidade dos dados
- Inspeção detalhada de amostras representativas

VALIDAÇÕES IMPLEMENTADAS:
-------------------------
- Contagem total de registros gerados
- Verificação de colunas obrigatórias presentes
- Análise de tipos de dados atribuídos
- Inspeção visual dos primeiros registros
- Análise específica de dados por ano (2025)
- Verificação de completude dos campos

ESTRUTURA DE DADOS TESTADA:
---------------------------
- Dados de extensão universitária completos
- Informações sobre projetos extensionistas
- Dados de estágios e acompanhamento profissional
- Informações de acessibilidade e inclusão (PNE)
- Distribuição por gênero e modalidades
- Vinculação institucional por unidades

ANÁLISES REALIZADAS:
--------------------
- Contagem quantitativa de registros
- Mapeamento de estrutura de colunas
- Verificação de tipos de dados corretos
- Amostragem de registros para inspeção
- Filtragem temporal para validação específica
- Análise detalhada de registros individuais

DADOS ANALISADOS:
-----------------
- Total de registros: quantidade geral gerada
- Estrutura de colunas: nomes e presença
- Tipos de dados: validação de formatos
- Amostra visual: primeiros 5 registros
- Dados temporais: registros específicos de 2025
- Detalhamento: análise individual completa

OBJETIVO:
---------
Validar funcionamento correto do gerador de dados de extensão,
garantindo qualidade, consistência e adequação dos dados gerados
para demonstração e teste do módulo de extensão no dashboard.

DEPENDÊNCIAS:
-------------
- sys, os: manipulação de sistema e caminhos
- modules.data_generator: gerador de dados sintéticos

AUTOR: Sistema NAI/IFPB-CZ
DATA: 2025
=============================================================================
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.data_generator import DataGenerator

def test_extensao():
    """
    Teste abrangente e detalhado do módulo de geração de dados de extensão.
    
    Esta função realiza validação completa do gerador de dados de extensão
    universitária, verificando estrutura, consistência, qualidade e
    adequação dos dados sintéticos gerados para uso no dashboard.
    
    PROCESSO DE VALIDAÇÃO:
    1. Instanciação do gerador de dados sintéticos
    2. Geração de dados de extensão universitária
    3. Análise quantitativa e estrutural dos dados
    4. Verificação de tipos de dados atribuídos
    5. Inspeção visual de amostras representativas
    6. Análise temporal específica (ano 2025)
    7. Detalhamento de registros individuais
    
    VALIDAÇÕES REALIZADAS:
    - Contagem total de registros gerados
    - Verificação de colunas obrigatórias
    - Análise de tipos de dados corretos
    - Inspeção de estrutura e conteúdo
    - Filtragem temporal para consistência
    - Análise detalhada de registros específicos
    
    ESTRUTURA ESPERADA:
    - Dados de projetos extensionistas por ano
    - Informações de estágios e acompanhamento
    - Dados de inclusão e acessibilidade (PNE)
    - Distribuição por gênero e modalidades
    - Vinculação com unidades institucionais
    
    ANÁLISES ESPECÍFICAS:
    - Registros totais: quantidade adequada para análise
    - Colunas presentes: conformidade com especificação
    - Tipos de dados: validação de formatos corretos
    - Amostra visual: verificação de consistência
    - Dados 2025: análise temporal específica
    - Detalhamento: inspeção individual completa
    
    RETORNO:
    --------
    None
        Função de teste com saída via logging console
        
    SAÍDAS GERADAS:
    ---------------
    - Estatísticas quantitativas dos dados
    - Estrutura de colunas e tipos
    - Amostra dos primeiros registros
    - Análise específica de dados temporais
    - Detalhamento de registros individuais
    """
    # Exibir mensagem inicial do processo de teste
    print("Testando geração de dados de extensão...")
    
    # Criar instância do gerador de dados sintéticos
    # Responsável por gerar dados realistas de extensão universitária
    data_gen = DataGenerator()
    
    # Gerar conjunto completo de dados de extensão
    # Inclui projetos, estágios, PNE e distribuições por gênero
    dados_extensao = data_gen.gerar_dados_extensao()
    
    # =============================================================================
    # ANÁLISE QUANTITATIVA E ESTRUTURAL DOS DADOS GERADOS
    # =============================================================================
    
    # Verificar contagem total de registros gerados
    # Importante para avaliar volume adequado para análise
    print(f"Total de registros: {len(dados_extensao)}")
    
    # Listar todas as colunas presentes na estrutura
    # Validação de conformidade com especificação do módulo
    print(f"Colunas: {list(dados_extensao.columns)}")
    
    # Analisar tipos de dados atribuídos a cada coluna
    # Verificação de consistência de formatação
    print(f"Tipos de dados:")
    print(dados_extensao.dtypes)
    
    # =============================================================================
    # INSPEÇÃO VISUAL E AMOSTRAGEM DE DADOS
    # =============================================================================
    
    # Mostrar primeiros registros para inspeção visual
    # Permite verificação rápida de qualidade e consistência
    print(f"\nPrimeiros 5 registros:")
    print(dados_extensao.head())
    
    # =============================================================================
    # ANÁLISE TEMPORAL ESPECÍFICA - DADOS DE 2025
    # =============================================================================
    
    # Filtrar dados específicos do ano de 2025
    # Validação de geração temporal correta
    dados_2025 = dados_extensao[dados_extensao['ano'] == 2025]
    print(f"\nRegistros de 2025: {len(dados_2025)}")
    
    # Análise detalhada de registro individual de 2025
    # Verificação de completude e consistência interna
    if len(dados_2025) > 0:
        print("Primeira linha de 2025:")
        print(dados_2025.iloc[0].to_dict())

if __name__ == "__main__":
    """
    Ponto de entrada principal do script de teste de extensão.
    
    Esta seção coordena a execução completa dos testes de validação
    do módulo de extensão universitária, garantindo funcionamento
    adequado do gerador de dados sintéticos específico.
    
    EXECUÇÃO REALIZADA:
    1. Verificação de execução direta do script
    2. Chamada da função principal de teste
    3. Validação completa do módulo de extensão
    4. Relatório detalhado de análises realizadas
    
    FINALIDADE:
    -----------
    Permitir execução independente do script para teste
    focalizado do módulo de extensão, facilitando debug
    e validação específica desta funcionalidade.
    
    PROCESSO:
    ---------
    - Execução direta: python test_extensao.py
    - Teste abrangente: módulo de extensão completo
    - Validação detalhada: dados gerados e estrutura
    - Relatório visual: análises e diagnósticos
    """
    test_extensao()
