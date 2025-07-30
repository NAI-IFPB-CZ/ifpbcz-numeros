#!/usr/bin/env python3
"""
==============================================================================
VERIFICADOR DE INTEGRIDADE PARA PRODUÇÃO
==============================================================================

Script para verificar se o projeto está pronto para deploy em produção.
Valida a presença de arquivos obrigatórios, configurações e dependências.

Uso: python verificar_deploy.py

Autor: Sistema NAI/IFPB-CZ
==============================================================================
"""

import os
import sys
import importlib.util

def verificar_arquivo_existe(arquivo, obrigatorio=True):
    """Verifica se um arquivo existe."""
    existe = os.path.exists(arquivo)
    status = "✅" if existe else ("❌" if obrigatorio else "⚠️")
    tipo = "OBRIGATÓRIO" if obrigatorio else "OPCIONAL"
    print(f"   {status} {arquivo} ({tipo})")
    return existe

def verificar_pasta_existe(pasta, obrigatorio=True):
    """Verifica se uma pasta existe e tem conteúdo."""
    existe = os.path.exists(pasta) and os.path.isdir(pasta)
    if existe:
        arquivos = len([f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))])
        status = "✅"
        info = f"({arquivos} arquivos)"
    else:
        status = "❌" if obrigatorio else "⚠️"
        info = "(não encontrada)"
    
    tipo = "OBRIGATÓRIA" if obrigatorio else "OPCIONAL"
    print(f"   {status} {pasta}/ {info} ({tipo})")
    return existe

def verificar_configuracoes():
    """Verifica as configurações do sistema."""
    print("\n🔧 VERIFICANDO CONFIGURAÇÕES:")
    print("-" * 50)
    
    erros = 0
    
    # Verificar config.py
    if os.path.exists('config.py'):
        try:
            spec = importlib.util.spec_from_file_location("config", "config.py")
            config = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(config)
            
            # Verificar configurações de segurança
            if hasattr(config, 'MODO_SOMENTE_LEITURA'):
                if config.MODO_SOMENTE_LEITURA:
                    print("   ✅ Modo somente leitura ativado (recomendado para produção)")
                else:
                    print("   ⚠️  Modo somente leitura desativado (considere ativar para produção)")
            
            if hasattr(config, 'USE_REAL_DATA'):
                if config.USE_REAL_DATA:
                    print("   ✅ Configurado para usar dados reais")
                else:
                    print("   ⚠️  Configurado para usar dados sintéticos")
            
        except Exception as e:
            print(f"   ❌ Erro ao carregar config.py: {e}")
            erros += 1
    else:
        print("   ❌ config.py não encontrado")
        erros += 1
    
    # Verificar .streamlit/config.toml
    if os.path.exists('.streamlit/config.toml'):
        print("   ✅ Configurações Streamlit encontradas")
    else:
        print("   ⚠️  Configurações Streamlit não encontradas")
    
    return erros == 0

def verificar_dependencias():
    """Verifica se as dependências estão especificadas."""
    print("\n📦 VERIFICANDO DEPENDÊNCIAS:")
    print("-" * 50)
    
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            linhas = f.readlines()
        
        deps_encontradas = []
        for linha in linhas:
            linha = linha.strip()
            if linha and not linha.startswith('#'):
                deps_encontradas.append(linha.split('>=')[0].split('==')[0])
        
        deps_essenciais = ['streamlit', 'pandas', 'numpy', 'plotly', 'openpyxl', 'folium']
        
        print(f"   ✅ {len(deps_encontradas)} dependências especificadas")
        
        for dep in deps_essenciais:
            if dep in deps_encontradas:
                print(f"   ✅ {dep}")
            else:
                print(f"   ❌ {dep} (FALTANDO)")
        
        return all(dep in deps_encontradas for dep in deps_essenciais)
    else:
        print("   ❌ requirements.txt não encontrado")
        return False

def verificar_modulos():
    """Verifica se todos os módulos estão presentes."""
    print("\n🧩 VERIFICANDO MÓDULOS:")
    print("-" * 50)
    
    modulos_essenciais = [
        'modules/__init__.py',
        'modules/utils.py',
        'modules/data_generator.py',
        'modules/help_page.py',
        'modules/presentation.py',
        'modules/ensino.py',
        'modules/assistencia_estudantil.py',
        'modules/pesquisa.py',
        'modules/extensao.py',
        'modules/orcamento.py',
        'modules/servidores.py',
        'modules/ouvidoria.py',
        'modules/auditoria.py',
        'modules/mundo_trabalho.py',
        'modules/mapa.py'
    ]
    
    todos_presentes = True
    for modulo in modulos_essenciais:
        existe = verificar_arquivo_existe(modulo, obrigatorio=True)
        if not existe:
            todos_presentes = False
    
    return todos_presentes

def main():
    """Função principal de verificação."""
    print("=" * 70)
    print("🔍 VERIFICADOR DE INTEGRIDADE PARA PRODUÇÃO")
    print("   Sistema Dashboard IFPB-CZ")
    print("=" * 70)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists('app.py'):
        print("❌ ERRO: Execute este script na raiz do projeto!")
        print("   O arquivo 'app.py' não foi encontrado.")
        sys.exit(1)
    
    erros = 0
    avisos = 0
    
    # 1. Verificar arquivos principais
    print("\n📄 VERIFICANDO ARQUIVOS PRINCIPAIS:")
    print("-" * 50)
    
    arquivos_principais = [
        ('app.py', True),
        ('requirements.txt', True),
        ('config.py', True),
        ('README.md', True),
        ('LICENSE', False),
        ('GUIA_ATUALIZACAO_DADOS.md', False)
    ]
    
    for arquivo, obrigatorio in arquivos_principais:
        if not verificar_arquivo_existe(arquivo, obrigatorio):
            if obrigatorio:
                erros += 1
            else:
                avisos += 1
    
    # 2. Verificar pastas principais
    print("\n📁 VERIFICANDO PASTAS PRINCIPAIS:")
    print("-" * 50)
    
    pastas_principais = [
        ('modules', True),
        ('.streamlit', True),
        ('logo-ifpb', True),
        ('dados', False),
        ('docs', False),
        ('fluxo', False)
    ]
    
    for pasta, obrigatorio in pastas_principais:
        if not verificar_pasta_existe(pasta, obrigatorio):
            if obrigatorio:
                erros += 1
            else:
                avisos += 1
    
    # 3. Verificar módulos
    if not verificar_modulos():
        erros += 1
    
    # 4. Verificar configurações
    if not verificar_configuracoes():
        erros += 1
    
    # 5. Verificar dependências
    if not verificar_dependencias():
        erros += 1
    
    # 6. Relatório final
    print("\n" + "=" * 70)
    print("📊 RELATÓRIO FINAL:")
    print("-" * 50)
    
    if erros == 0:
        print("🎉 PROJETO PRONTO PARA PRODUÇÃO!")
        print("   ✅ Todos os arquivos obrigatórios estão presentes")
        print("   ✅ Configurações verificadas")
        print("   ✅ Dependências completas")
        
        if avisos > 0:
            print(f"   ⚠️  {avisos} arquivo(s) opcional(is) ausente(s)")
        
        print("\n🚀 PRÓXIMOS PASSOS:")
        print("   1. Execute: python criar_pacote_producao.py")
        print("   2. Faça upload do ZIP para o servidor")
        print("   3. Extraia e configure conforme README.md")
        
        return True
        
    else:
        print(f"❌ PROJETO NÃO ESTÁ PRONTO PARA PRODUÇÃO!")
        print(f"   🔴 {erros} erro(s) crítico(s) encontrado(s)")
        
        if avisos > 0:
            print(f"   ⚠️  {avisos} aviso(s)")
        
        print("\n🔧 CORREÇÕES NECESSÁRIAS:")
        print("   • Corrija os erros marcados com ❌")
        print("   • Verifique a documentação do projeto")
        print("   • Execute novamente este script após as correções")
        
        return False

if __name__ == "__main__":
    sucesso = main()
    print()
    sys.exit(0 if sucesso else 1)
