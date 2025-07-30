#!/usr/bin/env python3
"""
=============================================================================
SCRIPT DE TESTE DE CONFIGURAÇÕES DE SEGURANÇA - SISTEMA DASHBOARD IFPB-CZ
=============================================================================

Este script implementa validação abrangente e detalhada das configurações
de segurança do Sistema Dashboard IFPB-CZ, verificando integridade,
funcionamento adequado e conformidade com políticas de segurança
institucionais para proteção de dados e prevenção de modificações
acidentais em ambiente de produção.

FUNCIONALIDADES PRINCIPAIS:
---------------------------
- Teste completo de configurações de segurança do sistema
- Validação de importação e carregamento de parâmetros
- Verificação de funcionalidade do gerador de dados
- Teste de proteções contra salvamento não autorizado
- Análise de modo de operação (produção vs desenvolvimento)
- Verificação de integridade dos arquivos de dados existentes

CONFIGURAÇÕES TESTADAS:
-----------------------
- PERMITIR_CRIACAO_PLANILHAS: controle de geração de arquivos
- SOBRESCREVER_ARQUIVOS_EXISTENTES: proteção contra perda
- MODO_SOMENTE_LEITURA: bloqueio de modificações acidentais
- MOSTRAR_LOGS: controle de verbosidade do sistema

TESTES DE SEGURANÇA IMPLEMENTADOS:
----------------------------------
- Carregamento seguro de configurações de segurança
- Instanciação protegida do gerador de dados
- Teste de salvamento com bloqueios ativos
- Verificação de carregamento de dados existentes
- Análise de conformidade com perfil de segurança
- Validação de presença de arquivos críticos

VERIFICAÇÕES DE INTEGRIDADE:
----------------------------
- Existência da pasta de dados principal
- Presença de todos os arquivos Excel obrigatórios
- Contagem de arquivos críticos encontrados
- Relatório de status de disponibilidade
- Diagnóstico de arquivos ausentes
- Orientação sobre uso de dados sintéticos

MODOS DE OPERAÇÃO VALIDADOS:
----------------------------
- PRODUÇÃO: máxima segurança e proteção de dados
- DESENVOLVIMENTO: flexibilidade para modificações
- Identificação automática do modo configurado
- Recomendações de segurança específicas

ARQUIVOS VERIFICADOS:
---------------------
- dados_ensino.xlsx: dados do módulo educacional
- dados_assistencia.xlsx: informações de assistência estudantil  
- dados_pesquisa.xlsx: dados de pesquisa acadêmica
- dados_extensao.xlsx: informações de extensão universitária
- dados_orcamento.xlsx: dados orçamentários institucionais
- dados_servidores.xlsx: informações de recursos humanos
- dados_ouvidoria.xlsx: dados do serviço de ouvidoria
- dados_auditoria.xlsx: informações de auditoria interna
- dados_mundo_trabalho.xlsx: dados de mercado de trabalho

RELATÓRIOS GERADOS:
-------------------
- Status das configurações de segurança carregadas
- Resultado dos testes de funcionalidade
- Análise do modo de operação configurado
- Mapeamento de arquivos de dados disponíveis
- Diagnóstico de integridade do sistema
- Recomendações de configuração apropriada

OBJETIVO:
---------
Garantir que o sistema esteja adequadamente configurado para
operação segura, validando proteções contra modificações
acidentais e verificando disponibilidade de dados necessários
para funcionamento correto do dashboard institucional.

DEPENDÊNCIAS:
-------------
- os, sys: manipulação de sistema e caminhos
- pandas: manipulação de dados para testes
- datetime: formatação de timestamps
- config: configurações de segurança do sistema
- modules.data_generator: gerador de dados para testes

AUTOR: Sistema NAI/IFPB-CZ
DATA: 2025
=============================================================================
"""

import os
import sys
import pandas as pd
from datetime import datetime

# Adicionar o módulo ao path para importação das configurações
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

def testar_configuracoes_seguranca():
    """
    Teste abrangente e detalhado das configurações de segurança do sistema.
    
    Esta função realiza validação completa de todas as configurações de
    segurança implementadas no Sistema Dashboard IFPB-CZ, verificando
    carregamento correto, funcionalidade adequada e conformidade com
    políticas de proteção de dados institucionais.
    
    PROCESSO DE VALIDAÇÃO:
    1. Carregamento seguro das configurações de segurança
    2. Verificação de importação correta dos parâmetros
    3. Teste de funcionalidade do gerador de dados
    4. Validação de proteções contra salvamento não autorizado
    5. Análise de modo de operação configurado
    6. Relatório de conformidade com perfil de segurança
    
    CONFIGURAÇÕES ANALISADAS:
    - PERMITIR_CRIACAO_PLANILHAS: controle de geração de arquivos
    - SOBRESCREVER_ARQUIVOS_EXISTENTES: proteção contra perda
    - MODO_SOMENTE_LEITURA: bloqueio de modificações acidentais  
    - MOSTRAR_LOGS: controle de verbosidade do sistema
    
    TESTES REALIZADOS:
    - Importação segura do módulo de configurações
    - Instanciação protegida do gerador de dados
    - Criação de dados de teste para validação
    - Teste de salvamento com proteções ativas
    - Verificação de carregamento de dados existentes
    - Análise de conformidade com modo de operação
    
    ANÁLISES DE SEGURANÇA:
    - Bloqueio correto de operações não autorizadas
    - Funcionamento adequado das proteções implementadas
    - Identificação de modo de operação (produção/desenvolvimento)
    - Validação de políticas de segurança ativas
    - Recomendações de configuração apropriada
    
    RETORNO:
    --------
    bool
        True se todas as configurações estão funcionando corretamente,
        False se foram encontrados problemas críticos
        
    SAÍDAS GERADAS:
    ---------------
    - Status do carregamento das configurações
    - Valores atuais de cada parâmetro de segurança
    - Resultado dos testes de funcionalidade
    - Análise do modo de operação configurado
    - Recomendações de segurança específicas
    """
    # Exibir cabeçalho do teste de configurações de segurança
    print("🔒 TESTE DE CONFIGURAÇÕES DE SEGURANÇA")
    print("=" * 50)
    
    # =============================================================================
    # CARREGAMENTO E VALIDAÇÃO DAS CONFIGURAÇÕES DE SEGURANÇA
    # =============================================================================
    
    # Importar configurações críticas de segurança do sistema
    # Validação de disponibilidade e carregamento correto
    try:
        from config import (
            PERMITIR_CRIACAO_PLANILHAS,      # Controle de geração de arquivos
            SOBRESCREVER_ARQUIVOS_EXISTENTES, # Proteção contra perda de dados
            MODO_SOMENTE_LEITURA,             # Bloqueio de modificações
            MOSTRAR_LOGS                      # Controle de verbosidade
        )
        
        # Confirmar carregamento bem-sucedido das configurações
        print("✅ Configurações carregadas com sucesso:")
        print(f"   - PERMITIR_CRIACAO_PLANILHAS = {PERMITIR_CRIACAO_PLANILHAS}")
        print(f"   - SOBRESCREVER_ARQUIVOS_EXISTENTES = {SOBRESCREVER_ARQUIVOS_EXISTENTES}")
        print(f"   - MODO_SOMENTE_LEITURA = {MODO_SOMENTE_LEITURA}")
        print(f"   - MOSTRAR_LOGS = {MOSTRAR_LOGS}")
        
    except ImportError as e:
        # Falha crítica no carregamento das configurações
        print(f"❌ Erro ao carregar configurações: {e}")
        return False
    
    # Separador para seção de testes funcionais
    print("\n📊 TESTE DE FUNCIONALIDADE:")
    print("-" * 30)
    
    # =============================================================================
    # TESTE DE FUNCIONALIDADE DO GERADOR DE DADOS COM PROTEÇÕES ATIVAS
    # =============================================================================
    
    # Testar funcionamento do DataGenerator com configurações de segurança
    try:
        # Importar módulo do gerador de dados sintéticos
        from modules.data_generator import DataGenerator
        
        # Criar instância do gerador para testes de segurança
        data_gen = DataGenerator()
        
        # Criar conjunto de dados de teste para validação
        # Estrutura mínima para testar proteções de salvamento
        dados_teste = pd.DataFrame({
            'ano': [2024, 2025],           # Anos para teste temporal
            'campo_teste': ['teste1', 'teste2'], # Campos de exemplo
            'valor': [100, 200]             # Valores numéricos de teste
        })
        
        # =============================================================================
        # TESTE DE PROTEÇÃO CONTRA SALVAMENTO NÃO AUTORIZADO
        # =============================================================================
        
        # Testar salvamento com proteções de segurança ativas
        print("🧪 Testando salvamento de dados de teste...")
        resultado = data_gen._salvar_dados_excel(dados_teste, "teste_seguranca")
        
        # Analisar resultado do teste de salvamento
        if resultado is None:
            # Salvamento bloqueado corretamente pelas configurações
            print("✅ Salvamento bloqueado corretamente pelas configurações de segurança")
        else:
            # Salvamento realizado - configurações podem estar em modo desenvolvimento
            print(f"⚠️  Arquivo salvo em: {resultado}")
            print("   (Configurações de segurança podem estar desabilitadas)")
        
        # =============================================================================
        # TESTE DE CARREGAMENTO DE DADOS EXISTENTES
        # =============================================================================
        
        # Testar carregamento de dados sem modificação
        print("\n🧪 Testando carregamento de dados existentes...")
        dados_carregados = data_gen._carregar_dados_excel("teste_seguranca")
        
        # Analisar resultado do carregamento
        if dados_carregados is not None:
            # Dados carregados com sucesso
            print(f"✅ Dados carregados com sucesso: {len(dados_carregados)} registros")
        else:
            # Nenhum dado encontrado (situação normal se arquivo não existe)
            print("ℹ️  Nenhum dado carregado (arquivo pode não existir)")
        
    except Exception as e:
        # Erro durante execução dos testes
        print(f"❌ Erro durante o teste: {e}")
        return False
    
    # Separador para seção de resumo
    print("\n🎯 RESUMO DOS TESTES:")
    print("-" * 20)
    
    # =============================================================================
    # ANÁLISE DE CONFORMIDADE COM PERFIL DE SEGURANÇA
    # =============================================================================
    
    # Verificar configuração recomendada para ambiente de produção
    if MODO_SOMENTE_LEITURA and not PERMITIR_CRIACAO_PLANILHAS and not SOBRESCREVER_ARQUIVOS_EXISTENTES:
        # Sistema configurado para máxima segurança
        print("✅ Sistema configurado para PRODUÇÃO (modo seguro)")
        print("   - Dados protegidos contra alterações acidentais")
        print("   - Criação de planilhas bloqueada")
        print("   - Sobrescrita de arquivos bloqueada")
    else:
        # Sistema configurado para desenvolvimento ou modo menos restritivo
        print("⚠️  Sistema configurado para DESENVOLVIMENTO")
        print("   - Edição de dados permitida")
        print("   - Use apenas em ambiente de desenvolvimento")
    
    return True

def verificar_arquivos_dados():
    """
    Verificação abrangente da integridade dos arquivos de dados do sistema.
    
    Esta função realiza validação completa da disponibilidade e integridade
    dos arquivos Excel contendo dados reais do Sistema Dashboard IFPB-CZ,
    garantindo que todos os módulos tenham acesso aos dados necessários
    para funcionamento adequado.
    
    PROCESSO DE VERIFICAÇÃO:
    1. Validação da existência da pasta principal de dados
    2. Verificação individual de cada arquivo Excel obrigatório
    3. Contagem de arquivos encontrados vs esperados
    4. Relatório detalhado de status de disponibilidade
    5. Diagnóstico de arquivos ausentes
    6. Orientações sobre uso de dados sintéticos alternativos
    
    ARQUIVOS VERIFICADOS:
    - dados_ensino.xlsx: informações educacionais do campus
    - dados_assistencia.xlsx: dados de assistência estudantil
    - dados_pesquisa.xlsx: informações de pesquisa acadêmica
    - dados_extensao.xlsx: dados de extensão universitária
    - dados_orcamento.xlsx: informações orçamentárias
    - dados_servidores.xlsx: dados de recursos humanos
    - dados_ouvidoria.xlsx: informações de ouvidoria
    - dados_auditoria.xlsx: dados de auditoria interna
    - dados_mundo_trabalho.xlsx: informações de mercado de trabalho
    
    ANÁLISES REALIZADAS:
    - Existência da estrutura de pastas necessária
    - Disponibilidade individual de cada arquivo crítico
    - Contagem total de arquivos encontrados
    - Identificação de arquivos ausentes específicos
    - Relatório de integridade geral do sistema
    
    RETORNO:
    --------
    bool
        True se a verificação foi executada com sucesso,
        False se houve falha crítica na estrutura de pastas
        
    SAÍDAS GERADAS:
    ---------------
    - Status individual de cada arquivo de dados
    - Contagem total de arquivos encontrados
    - Diagnóstico de integridade do sistema
    - Orientações sobre dados sintéticos alternativos
    """
    # Exibir cabeçalho da verificação de arquivos
    print("\n📁 VERIFICAÇÃO DE ARQUIVOS DE DADOS:")
    print("-" * 35)
    
    # Definir estrutura de dados esperada no sistema
    pasta_dados = "dados"  # Pasta principal contendo arquivos Excel
    
    # Lista completa de arquivos Excel obrigatórios para funcionamento
    arquivos_esperados = [
        "dados_ensino.xlsx",           # Dados educacionais do campus
        "dados_assistencia.xlsx",      # Informações de assistência estudantil
        "dados_pesquisa.xlsx",         # Dados de pesquisa acadêmica
        "dados_extensao.xlsx",         # Informações de extensão universitária
        "dados_orcamento.xlsx",        # Dados orçamentários institucionais
        "dados_servidores.xlsx",       # Informações de recursos humanos
        "dados_ouvidoria.xlsx",        # Dados do serviço de ouvidoria
        "dados_auditoria.xlsx",        # Informações de auditoria interna
        "dados_mundo_trabalho.xlsx"    # Dados de mercado de trabalho
    ]
    
    # =============================================================================
    # VALIDAÇÃO DE ESTRUTURA DE PASTAS NECESSÁRIA
    # =============================================================================
    
    # Verificar existência da pasta principal de dados
    if not os.path.exists(pasta_dados):
        print(f"❌ Pasta '{pasta_dados}' não encontrada")
        return False
    
    # =============================================================================
    # VERIFICAÇÃO INDIVIDUAL DE CADA ARQUIVO CRÍTICO
    # =============================================================================
    
    # Contador para estatísticas de disponibilidade
    arquivos_encontrados = 0
    
    # Iterar por todos os arquivos esperados para verificação
    for arquivo in arquivos_esperados:
        # Construir caminho completo para cada arquivo
        caminho = os.path.join(pasta_dados, arquivo)
        
        # Verificar disponibilidade individual do arquivo
        if os.path.exists(caminho):
            # Arquivo encontrado e disponível
            print(f"✅ {arquivo}")
            arquivos_encontrados += 1
        else:
            # Arquivo ausente - sistema usará dados sintéticos
            print(f"❌ {arquivo} - não encontrado")
    
    # =============================================================================
    # RELATÓRIO DE INTEGRIDADE E DIAGNÓSTICO FINAL
    # =============================================================================
    
    # Exibir estatísticas de disponibilidade dos dados
    print(f"\n📊 Resultado: {arquivos_encontrados}/{len(arquivos_esperados)} arquivos encontrados")
    
    # Analisar integridade geral do sistema de dados
    if arquivos_encontrados == len(arquivos_esperados):
        # Sistema com dados completos e íntegros
        print("✅ Todos os arquivos de dados estão presentes")
    else:
        # Sistema com dados parciais - orientação sobre funcionamento
        print("⚠️  Alguns arquivos de dados estão ausentes")
        print("   O sistema usará dados sintéticos para módulos sem arquivos")
    
    return True

def main():
    """
    Função principal de coordenação dos testes de segurança do sistema.
    
    Esta função coordena a execução completa de todos os testes de
    segurança e integridade do Sistema Dashboard IFPB-CZ, organizando
    a sequência de validações e gerando relatório consolidado dos
    resultados obtidos.
    
    PROCESSO DE EXECUÇÃO:
    1. Registro de timestamp de início dos testes
    2. Execução dos testes de configurações de segurança
    3. Verificação de integridade dos arquivos de dados
    4. Geração de relatório consolidado de resultados
    5. Apresentação de conclusões e recomendações
    
    TESTES COORDENADOS:
    - Configurações de segurança: validação completa
    - Arquivos de dados: verificação de integridade
    - Modo de operação: análise de conformidade
    - Proteções ativas: teste de funcionalidade
    
    SAÍDAS GERADAS:
    - Timestamp de execução dos testes
    - Resultado consolidado de todos os testes
    - Status de integridade do sistema
    - Recomendações de configuração
    - Orientações para resolução de problemas
    
    RETORNO:
    --------
    None
        Função de coordenação com saída via logging console
    """
    # Registrar timestamp de início dos testes de segurança
    print(f"🔧 Teste de Segurança - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("")
    
    # =============================================================================
    # EXECUÇÃO SEQUENCIAL DOS TESTES DE SEGURANÇA E INTEGRIDADE
    # =============================================================================
    
    # Executar testes de configurações de segurança primeiro
    if testar_configuracoes_seguranca():
        # Se testes de segurança foram bem-sucedidos, verificar arquivos
        verificar_arquivos_dados()
        
        # =============================================================================
        # RELATÓRIO FINAL DE SUCESSO DOS TESTES
        # =============================================================================
        
        print("\n🎉 TESTE CONCLUÍDO!")
        print("=" * 20)
        print("✅ Configurações de segurança testadas com sucesso")
        print("📝 Verifique os logs acima para detalhes específicos")
        
    else:
        # =============================================================================
        # RELATÓRIO DE FALHA NOS TESTES CRÍTICOS
        # =============================================================================
        
        print("\n❌ TESTE FALHOU!")
        print("=" * 15)
        print("❌ Problemas encontrados nas configurações de segurança")
        print("📝 Verifique os erros acima para mais detalhes")

if __name__ == "__main__":
    """
    Ponto de entrada principal do script de teste de segurança.
    
    Esta seção coordena a execução completa dos testes de validação
    das configurações de segurança do Sistema Dashboard IFPB-CZ,
    garantindo funcionamento adequado das proteções implementadas
    e integridade dos dados do sistema.
    
    EXECUÇÃO REALIZADA:
    1. Verificação de execução direta do script
    2. Chamada da função principal de coordenação
    3. Execução de todos os testes de segurança
    4. Geração de relatório consolidado de resultados
    
    FINALIDADE:
    -----------
    Permitir execução independente do script para validação
    completa das configurações de segurança, facilitando
    verificação de conformidade e diagnóstico de problemas.
    
    PROCESSO:
    ---------
    - Execução direta: python testar_seguranca.py
    - Validação completa: configurações e arquivos
    - Teste abrangente: proteções e integridade
    - Relatório detalhado: resultados e recomendações
    """
    main()
