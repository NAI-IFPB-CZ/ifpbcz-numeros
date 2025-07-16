#!/usr/bin/env python3
"""
Teste das configurações de segurança do sistema

Este script testa se as configurações de segurança estão funcionando corretamente.
"""

import os
import sys
import pandas as pd
from datetime import datetime

# Adicionar o módulo ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

def testar_configuracoes_seguranca():
    """Testa as configurações de segurança"""
    
    print("🔒 TESTE DE CONFIGURAÇÕES DE SEGURANÇA")
    print("=" * 50)
    
    # Importar configurações
    try:
        from config import (
            PERMITIR_CRIACAO_PLANILHAS,
            SOBRESCREVER_ARQUIVOS_EXISTENTES,
            MODO_SOMENTE_LEITURA,
            MOSTRAR_LOGS
        )
        
        print("✅ Configurações carregadas com sucesso:")
        print(f"   - PERMITIR_CRIACAO_PLANILHAS = {PERMITIR_CRIACAO_PLANILHAS}")
        print(f"   - SOBRESCREVER_ARQUIVOS_EXISTENTES = {SOBRESCREVER_ARQUIVOS_EXISTENTES}")
        print(f"   - MODO_SOMENTE_LEITURA = {MODO_SOMENTE_LEITURA}")
        print(f"   - MOSTRAR_LOGS = {MOSTRAR_LOGS}")
        
    except ImportError as e:
        print(f"❌ Erro ao carregar configurações: {e}")
        return False
    
    print("\n📊 TESTE DE FUNCIONALIDADE:")
    print("-" * 30)
    
    # Testar DataGenerator
    try:
        from modules.data_generator import DataGenerator
        
        # Criar instância do gerador
        data_gen = DataGenerator()
        
        # Criar dados de teste
        dados_teste = pd.DataFrame({
            'ano': [2024, 2025],
            'campo_teste': ['teste1', 'teste2'],
            'valor': [100, 200]
        })
        
        # Testar salvamento
        print("🧪 Testando salvamento de dados de teste...")
        resultado = data_gen._salvar_dados_excel(dados_teste, "teste_seguranca")
        
        if resultado is None:
            print("✅ Salvamento bloqueado corretamente pelas configurações de segurança")
        else:
            print(f"⚠️  Arquivo salvo em: {resultado}")
            print("   (Configurações de segurança podem estar desabilitadas)")
        
        # Testar carregamento
        print("\n🧪 Testando carregamento de dados existentes...")
        dados_carregados = data_gen._carregar_dados_excel("teste_seguranca")
        
        if dados_carregados is not None:
            print(f"✅ Dados carregados com sucesso: {len(dados_carregados)} registros")
        else:
            print("ℹ️  Nenhum dado carregado (arquivo pode não existir)")
        
    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")
        return False
    
    print("\n🎯 RESUMO DOS TESTES:")
    print("-" * 20)
    
    # Verificar configuração recomendada para produção
    if MODO_SOMENTE_LEITURA and not PERMITIR_CRIACAO_PLANILHAS and not SOBRESCREVER_ARQUIVOS_EXISTENTES:
        print("✅ Sistema configurado para PRODUÇÃO (modo seguro)")
        print("   - Dados protegidos contra alterações acidentais")
        print("   - Criação de planilhas bloqueada")
        print("   - Sobrescrita de arquivos bloqueada")
    else:
        print("⚠️  Sistema configurado para DESENVOLVIMENTO")
        print("   - Edição de dados permitida")
        print("   - Use apenas em ambiente de desenvolvimento")
    
    return True

def verificar_arquivos_dados():
    """Verifica se os arquivos de dados existem"""
    
    print("\n📁 VERIFICAÇÃO DE ARQUIVOS DE DADOS:")
    print("-" * 35)
    
    pasta_dados = "dados"
    arquivos_esperados = [
        "dados_ensino.xlsx",
        "dados_assistencia.xlsx",
        "dados_pesquisa.xlsx",
        "dados_extensao.xlsx",
        "dados_orcamento.xlsx",
        "dados_servidores.xlsx",
        "dados_ouvidoria.xlsx",
        "dados_auditoria.xlsx",
        "dados_mundo_trabalho.xlsx"
    ]
    
    if not os.path.exists(pasta_dados):
        print(f"❌ Pasta '{pasta_dados}' não encontrada")
        return False
    
    arquivos_encontrados = 0
    for arquivo in arquivos_esperados:
        caminho = os.path.join(pasta_dados, arquivo)
        if os.path.exists(caminho):
            print(f"✅ {arquivo}")
            arquivos_encontrados += 1
        else:
            print(f"❌ {arquivo} - não encontrado")
    
    print(f"\n📊 Resultado: {arquivos_encontrados}/{len(arquivos_esperados)} arquivos encontrados")
    
    if arquivos_encontrados == len(arquivos_esperados):
        print("✅ Todos os arquivos de dados estão presentes")
    else:
        print("⚠️  Alguns arquivos de dados estão ausentes")
        print("   O sistema usará dados sintéticos para módulos sem arquivos")
    
    return True

def main():
    """Função principal"""
    print(f"🔧 Teste de Segurança - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("")
    
    # Executar testes
    if testar_configuracoes_seguranca():
        verificar_arquivos_dados()
        
        print("\n🎉 TESTE CONCLUÍDO!")
        print("=" * 20)
        print("✅ Configurações de segurança testadas com sucesso")
        print("📝 Verifique os logs acima para detalhes específicos")
        
    else:
        print("\n❌ TESTE FALHOU!")
        print("=" * 15)
        print("❌ Problemas encontrados nas configurações de segurança")
        print("📝 Verifique os erros acima para mais detalhes")

if __name__ == "__main__":
    main()
