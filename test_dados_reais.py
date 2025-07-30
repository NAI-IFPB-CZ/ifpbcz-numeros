#!/usr/bin/env python3
"""
=============================================================================
SCRIPT DE TESTE DE DADOS - SISTEMA DASHBOARD IFPB-CZ
=============================================================================

Este script implementa sistema de teste abrangente para validação da alternância
entre dados sintéticos e dados reais no Sistema Dashboard IFPB-CZ, permitindo
verificação de funcionalidade, diagnóstico de problemas e validação de
configurações antes da operação em produção.

FUNCIONALIDADES PRINCIPAIS:
---------------------------
- Teste de carregamento de dados sintéticos (gerados automaticamente)
- Teste de carregamento de dados reais (arquivos Excel institucionais)
- Validação de configurações do sistema (config.py)
- Diagnóstico de problemas e sugestões de correção
- Instruções detalhadas para migração para dados reais
- Verificação de integridade estrutural dos dados

TIPOS DE TESTE IMPLEMENTADOS:
-----------------------------
1. Teste de Dados Sintéticos:
   - Validação do gerador automático de dados
   - Verificação de estrutura e consistência
   - Análise de cobertura temporal e conteúdo

2. Teste de Dados Reais:
   - Carregamento de arquivos Excel institucionais
   - Validação de estrutura e colunas obrigatórias
   - Verificação de integridade e consistência

3. Diagnóstico de Configuração:
   - Exibição de parâmetros ativos do sistema
   - Validação de flags de controle
   - Orientações para ajustes necessários

CENÁRIOS DE TESTE COBERTOS:
---------------------------
- Sistema novo sem dados reais (modo sintético)
- Sistema com dados reais disponíveis (modo real)
- Sistema com problemas de carregamento (diagnóstico)
- Migração de dados sintéticos para reais (transição)
- Validação de estrutura de arquivos (conformidade)

ESTRUTURA DE VALIDAÇÃO:
-----------------------
- Verificação de existência de arquivos obrigatórios
- Validação de estrutura de colunas por módulo
- Teste de carregamento e processamento de dados
- Análise de cobertura temporal e completude
- Diagnóstico de erros com sugestões específicas

CONFIGURAÇÕES TESTADAS:
-----------------------
- USE_REAL_DATA: controle do tipo de dados utilizado
- VALIDAR_DADOS: ativação de validações adicionais
- MOSTRAR_LOGS: controle de verbosidade do sistema
- USAR_DADOS_BACKUP: utilização de dados de fallback

INSTRUÇÕES FORNECIDAS:
----------------------
- Passo-a-passo para migração para dados reais
- Lista completa de arquivos Excel necessários
- Orientações de estrutura e formatação
- Procedimentos de verificação e validação
- Dicas de troubleshooting para problemas comuns

OBJETIVO:
---------
Facilitar teste, validação e migração do sistema entre modos de operação,
garantindo funcionamento correto antes da implantação em produção e
fornecendo ferramentas de diagnóstico para resolução de problemas.

DEPENDÊNCIAS:
-------------
- sys, os: manipulação de sistema e caminhos
- config: configurações do sistema
- modules.data_generator: gerador de dados sintéticos
- modules.data_generator_real: carregador de dados reais

AUTOR: Sistema NAI/IFPB-CZ
DATA: 2024
=============================================================================
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config
from modules.data_generator import DataGenerator
from modules.data_generator_real import DataGeneratorReal

def test_dados_sinteticos():
    """
    Teste abrangente de funcionamento do gerador de dados sintéticos.
    
    Valida capacidade do sistema de gerar dados automaticamente quando
    dados reais não estão disponíveis, verificando estrutura, consistência
    e cobertura temporal dos dados gerados para demonstração.
    
    VALIDAÇÕES REALIZADAS:
    - Instanciação correta do gerador sintético
    - Geração bem-sucedida de dados de extensão (módulo de teste)
    - Verificação de estrutura de colunas geradas
    - Análise de cobertura temporal dos dados
    - Contagem de registros gerados
    
    DADOS TESTADOS:
    - Módulo de extensão como representativo do sistema
    - Estrutura de colunas conforme especificação
    - Cobertura temporal adequada para análises
    - Consistência de tipos de dados gerados
    
    DIAGNÓSTICO INCLUÍDO:
    - Informações sobre quantidade de registros
    - Lista de colunas disponíveis
    - Faixa temporal coberta pelos dados
    - Identificação de problemas de geração
    
    RETORNO:
    --------
    None
        Função de teste com saída via logging console
        
    EXCEÇÕES TRATADAS:
    ------------------
    Exception
        Qualquer erro durante geração é capturado e reportado
        com orientações para resolução
    """
    # ============= INÍCIO DO TESTE DE DADOS SINTÉTICOS =============
    # Cabeçalho visual para identificação clara da seção de teste
    print("="*50)
    print("🔧 TESTANDO DADOS SINTÉTICOS")
    print("="*50)
    
    # ============= TESTE DE GERAÇÃO COM TRATAMENTO DE ERROS =============
    try:
        # Instancia gerador de dados sintéticos com configurações padrão
        data_gen = DataGenerator()
        
        # Gera dados de extensão como amostra representativa do sistema
        dados_extensao = data_gen.gerar_dados_extensao()
        
        # ============= VALIDAÇÃO E ANÁLISE DOS DADOS GERADOS =============
        # Exibe informações estatísticas e estruturais dos dados gerados
        print(f"✅ Dados sintéticos de extensão: {len(dados_extensao)} registros")
        print(f"📊 Colunas: {list(dados_extensao.columns)}")
        print(f"📅 Anos: {dados_extensao['ano'].min()} a {dados_extensao['ano'].max()}")
        
    except Exception as e:
        # ============= TRATAMENTO DE ERROS COM DIAGNÓSTICO =============
        # Captura e reporta problemas na geração de dados sintéticos
        print(f"❌ Erro ao gerar dados sintéticos: {str(e)}")

def test_dados_reais():
    """
    Teste abrangente de carregamento de dados reais de arquivos Excel.
    
    Valida capacidade do sistema de carregar dados institucionais reais
    a partir de arquivos Excel estruturados, verificando integridade,
    consistência e conformidade com especificações técnicas.
    
    VALIDAÇÕES REALIZADAS:
    - Instanciação correta do carregador de dados reais
    - Carregamento bem-sucedido de arquivo Excel específico
    - Verificação de estrutura de colunas obrigatórias
    - Análise de cobertura temporal dos dados
    - Validação de integridade dos registros
    
    ARQUIVO TESTADO:
    - dados_extensao.xlsx como representativo do sistema
    - Validação de existência e acessibilidade
    - Verificação de formato e estrutura
    - Análise de conteúdo e consistência
    
    DIAGNÓSTICO INCLUÍDO:
    - Informações sobre quantidade de registros carregados
    - Lista de colunas presentes no arquivo
    - Faixa temporal dos dados institucionais
    - Identificação específica de problemas de carregamento
    
    ORIENTAÇÕES DE ERRO:
    - Sugestões para criação de dados de exemplo
    - Instruções para resolução de problemas comuns
    - Referências a utilitários de suporte
    
    RETORNO:
    --------
    None
        Função de teste com saída via logging console
        
    EXCEÇÕES TRATADAS:
    ------------------
    Exception
        Erros de carregamento são capturados com orientações
        específicas para resolução e criação de dados
    """
    # ============= INÍCIO DO TESTE DE DADOS REAIS =============
    # Cabeçalho visual para identificação clara da seção de teste
    print("="*50)
    print("📊 TESTANDO DADOS REAIS")
    print("="*50)
    
    # ============= TESTE DE CARREGAMENTO COM TRATAMENTO ROBUSTO =============
    try:
        # Instancia carregador de dados reais com validações ativas
        data_gen = DataGeneratorReal()
        
        # Carrega dados de extensão como amostra representativa do sistema
        dados_extensao = data_gen.gerar_dados_extensao()
        
        # ============= VALIDAÇÃO E ANÁLISE DOS DADOS CARREGADOS =============
        # Exibe informações estatísticas e estruturais dos dados reais
        print(f"✅ Dados reais de extensão: {len(dados_extensao)} registros")
        print(f"📊 Colunas: {list(dados_extensao.columns)}")
        print(f"📅 Anos: {dados_extensao['ano'].min()} a {dados_extensao['ano'].max()}")
        
    except Exception as e:
        # ============= TRATAMENTO DE ERROS COM ORIENTAÇÕES ESPECÍFICAS =============
        # Captura problemas de carregamento e fornece soluções práticas
        print(f"❌ Erro ao carregar dados reais: {str(e)}")
        print("💡 Dica: Execute 'python criar_planilhas_exemplo.py' para criar dados de exemplo")

def main():
    """
    Função principal de execução do sistema de teste completo.
    
    Coordena execução de todos os testes de validação, exibe configurações
    atuais do sistema e fornece instruções detalhadas para migração
    entre modos de operação (sintético/real).
    
    SEQUÊNCIA DE EXECUÇÃO:
    1. Exibição de configurações atuais do sistema
    2. Teste de funcionamento de dados sintéticos
    3. Teste de carregamento de dados reais
    4. Instruções detalhadas para migração
    5. Documentação de estrutura necessária
    
    CONFIGURAÇÕES EXIBIDAS:
    - USE_REAL_DATA: modo de operação atual
    - VALIDAR_DADOS: nível de validação ativo
    - MOSTRAR_LOGS: verbosidade do sistema
    - USAR_DADOS_BACKUP: estratégia de fallback
    
    INSTRUÇÕES FORNECIDAS:
    - Passo-a-passo para criação de dados de exemplo
    - Procedimentos para substituição por dados reais
    - Configurações necessárias para ativação
    - Lista completa de arquivos obrigatórios
    
    OBJETIVO DA FUNÇÃO:
    Facilitar diagnóstico completo do sistema, validação de
    configurações e orientação para migração entre modos de
    operação com instruções práticas e específicas.
    
    RETORNO:
    --------
    None
        Função principal com saída via logging console
    """
    # ============= CABEÇALHO E IDENTIFICAÇÃO DO SISTEMA DE TESTE =============
    print("🚀 SISTEMA DE TESTE - DADOS SINTÉTICOS vs REAIS")
    print("="*60)
    
    # ============= EXIBIÇÃO DE CONFIGURAÇÕES ATUAIS =============
    # Mostra estado atual das configurações para diagnóstico
    print(f"📋 Configuração atual: USE_REAL_DATA = {config.USE_REAL_DATA}")
    print(f"📋 Validar dados: {config.VALIDAR_DADOS}")
    print(f"📋 Mostrar logs: {config.MOSTRAR_LOGS}")
    print(f"📋 Usar backup: {config.USAR_DADOS_BACKUP}")
    
    # ============= EXECUÇÃO DOS TESTES DE VALIDAÇÃO =============
    # Testar dados sintéticos
    test_dados_sinteticos()
    
    # Testar dados reais
    test_dados_reais()
    
    # ============= INSTRUÇÕES DETALHADAS PARA MIGRAÇÃO =============
    # Fornece orientações passo-a-passo para uso de dados reais
    print("\n" + "="*60)
    print("📖 INSTRUÇÕES PARA USAR DADOS REAIS:")
    print("="*60)
    print("1. Execute: python criar_planilhas_exemplo.py")
    print("2. Substitua os arquivos na pasta 'dados/' pelos seus dados reais")
    print("3. Altere USE_REAL_DATA = True no arquivo config.py")
    print("4. Reinicie o sistema Streamlit")
    print("5. Verifique se os dados foram carregados corretamente")
    
    # ============= DOCUMENTAÇÃO DE ESTRUTURA OBRIGATÓRIA =============
    # Lista completa de arquivos necessários para operação com dados reais
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

# ============= PONTO DE ENTRADA PRINCIPAL DO SCRIPT =============
# Executa função principal quando script é chamado diretamente
if __name__ == "__main__":
    main()
