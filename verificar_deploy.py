#!/usr/bin/env python3
"""
=============================================================================
VERIFICADOR DE INTEGRIDADE PARA PRODUÇÃO - SISTEMA DASHBOARD IFPB-CZ
=============================================================================

Este script implementa verificação abrangente e detalhada da integridade
do Sistema Dashboard IFPB-CZ antes do deploy em ambiente de produção,
validando presença de arquivos obrigatórios, configurações de segurança,
dependências críticas e estrutura de módulos necessária para funcionamento
adequado em servidor de produção.

FUNCIONALIDADES PRINCIPAIS:
---------------------------
- Verificação completa de arquivos principais obrigatórios
- Validação de estrutura de pastas e conteúdo
- Análise de configurações de segurança para produção
- Verificação de dependências críticas no requirements.txt
- Validação de integridade dos módulos do sistema
- Relatório detalhado de prontidão para produção

VERIFICAÇÕES IMPLEMENTADAS:
---------------------------
- Arquivos principais: app.py, requirements.txt, config.py, README.md
- Pastas obrigatórias: modules/, .streamlit/, logo-ifpb/
- Módulos essenciais: todos os componentes do dashboard
- Configurações: modo somente leitura, uso de dados reais
- Dependências: streamlit, pandas, numpy, plotly, openpyxl, folium
- Estrutura: integridade geral do projeto

ANÁLISES DE PRODUÇÃO:
---------------------
- Modo somente leitura: proteção contra modificações acidentais
- Configurações de segurança: validação de políticas ativas
- Dados reais: verificação de configuração apropriada
- Dependências completas: todas as bibliotecas necessárias
- Estrutura íntegra: todos os módulos e arquivos presentes

RELATÓRIOS GERADOS:
-------------------
- Status individual de cada arquivo verificado
- Análise de configurações de segurança
- Mapeamento de dependências encontradas vs necessárias
- Relatório de integridade dos módulos
- Diagnóstico final de prontidão para produção
- Instruções para próximos passos do deploy

VALIDAÇÕES DE SEGURANÇA:
------------------------
- MODO_SOMENTE_LEITURA: proteção de dados em produção
- USE_REAL_DATA: configuração apropriada de fonte de dados
- Configurações Streamlit: otimizações para servidor
- Estrutura de pastas: organização adequada para deploy

ARQUIVOS OBRIGATÓRIOS VERIFICADOS:
----------------------------------
- app.py: aplicação principal Streamlit
- requirements.txt: especificação de dependências
- config.py: configurações do sistema
- README.md: documentação de instalação
- modules/: pasta com todos os módulos funcionais
- .streamlit/: configurações específicas do Streamlit
- logo-ifpb/: recursos visuais institucionais

MÓDULOS ESSENCIAIS VALIDADOS:
-----------------------------
- utils.py: utilitários compartilhados
- data_generator.py: gerador de dados sintéticos
- help_page.py: sistema de ajuda e suporte
- presentation.py: apresentação institucional
- ensino.py: módulo de dados educacionais
- assistencia_estudantil.py: assistência estudantil
- pesquisa.py: dados de pesquisa acadêmica
- extensao.py: extensão universitária
- orcamento.py: dados orçamentários
- servidores.py: recursos humanos
- ouvidoria.py: serviço de ouvidoria
- auditoria.py: auditoria interna
- mundo_trabalho.py: mercado de trabalho
- mapa.py: funcionalidades de mapeamento

DEPENDÊNCIAS CRÍTICAS:
----------------------
- streamlit: framework web principal
- pandas: manipulação de dados
- numpy: computação numérica
- plotly: visualizações interativas
- openpyxl: manipulação de arquivos Excel
- folium: mapas interativos

OBJETIVO:
---------
Garantir que o Sistema Dashboard IFPB-CZ esteja completamente
pronto para deploy em ambiente de produção, com todos os
componentes necessários, configurações adequadas e estrutura
íntegra para funcionamento confiável em servidor.

USO:
----
python verificar_deploy.py

RETORNO:
--------
- Código de saída 0: projeto pronto para produção
- Código de saída 1: correções necessárias antes do deploy

DEPENDÊNCIAS:
-------------
- os, sys: manipulação de sistema e caminhos
- importlib.util: carregamento dinâmico de módulos

AUTOR: Sistema NAI/IFPB-CZ
DATA: 2025
=============================================================================
"""

import os
import sys
import importlib.util

def verificar_arquivo_existe(arquivo, obrigatorio=True):
    """
    Verificação detalhada da existência de arquivos individuais do sistema.
    
    Esta função realiza validação específica da presença de arquivos
    críticos para o funcionamento do Sistema Dashboard IFPB-CZ,
    categorizando como obrigatórios ou opcionais e gerando feedback
    visual adequado para diagnóstico de integridade.
    
    PROCESSO DE VERIFICAÇÃO:
    1. Verificação de existência física do arquivo
    2. Determinação de status visual baseado em obrigatoriedade
    3. Exibição de feedback formatado com categorização
    4. Retorno de status booleano para agregação
    
    CATEGORIZAÇÃO:
    - OBRIGATÓRIO: arquivo crítico para funcionamento
    - OPCIONAL: arquivo recomendado mas não essencial
    
    FEEDBACK VISUAL:
    - ✅: arquivo presente e verificado
    - ❌: arquivo obrigatório ausente (erro crítico)
    - ⚠️: arquivo opcional ausente (aviso)
    
    PARÂMETROS:
    -----------
    arquivo : str
        Caminho relativo ou absoluto do arquivo a verificar
    obrigatorio : bool, optional
        Se True, marca como obrigatório (padrão: True)
        
    RETORNO:
    --------
    bool
        True se arquivo existe, False caso contrário
        
    SAÍDAS GERADAS:
    ---------------
    - Status visual do arquivo com ícone apropriado
    - Nome do arquivo verificado
    - Categorização (OBRIGATÓRIO/OPCIONAL)
    """
    # Verificar existência física do arquivo no sistema
    existe = os.path.exists(arquivo)
    
    # Determinar ícone de status baseado em existência e obrigatoriedade
    status = "✅" if existe else ("❌" if obrigatorio else "⚠️")
    
    # Determinar categoria de classificação do arquivo
    tipo = "OBRIGATÓRIO" if obrigatorio else "OPCIONAL"
    
    # Exibir feedback formatado com status visual
    print(f"   {status} {arquivo} ({tipo})")
    
    return existe

def verificar_pasta_existe(pasta, obrigatorio=True):
    """
    Verificação abrangente da existência e conteúdo de pastas do sistema.
    
    Esta função realiza validação completa da presença de pastas
    críticas para o Sistema Dashboard IFPB-CZ, incluindo análise
    de conteúdo interno e categorização de importância para
    funcionamento adequado em produção.
    
    PROCESSO DE VERIFICAÇÃO:
    1. Verificação de existência física da pasta
    2. Validação de que é efetivamente um diretório
    3. Contagem de arquivos presentes na pasta
    4. Determinação de status visual baseado em resultados
    5. Exibição de feedback detalhado com estatísticas
    
    ANÁLISES REALIZADAS:
    - Existência: pasta presente no sistema de arquivos
    - Tipo: confirmação de que é diretório válido
    - Conteúdo: contagem de arquivos internos
    - Categoria: classificação de importância
    
    FEEDBACK DETALHADO:
    - Nome da pasta com indicador de diretório (/)
    - Contagem de arquivos encontrados
    - Categorização (OBRIGATÓRIA/OPCIONAL)
    - Status visual apropriado
    
    PARÂMETROS:
    -----------
    pasta : str
        Nome ou caminho da pasta a verificar
    obrigatorio : bool, optional
        Se True, marca como obrigatória (padrão: True)
        
    RETORNO:
    --------
    bool
        True se pasta existe e é diretório válido, False caso contrário
        
    SAÍDAS GERADAS:
    ---------------
    - Status visual com ícone de resultado
    - Nome da pasta com indicador de diretório
    - Contagem de arquivos ou indicação de ausência
    - Categorização de importância
    """
    # Verificar existência física e tipo da pasta
    existe = os.path.exists(pasta) and os.path.isdir(pasta)
    
    if existe:
        # Contar arquivos presentes na pasta para análise de conteúdo
        arquivos = len([f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))])
        status = "✅"
        info = f"({arquivos} arquivos)"
    else:
        # Pasta não encontrada ou não é diretório válido
        status = "❌" if obrigatorio else "⚠️"
        info = "(não encontrada)"
    
    # Determinar categoria de classificação da pasta
    tipo = "OBRIGATÓRIA" if obrigatorio else "OPCIONAL"
    
    # Exibir feedback detalhado com estatísticas
    print(f"   {status} {pasta}/ {info} ({tipo})")
    
    return existe

def verificar_configuracoes():
    """
    Verificação abrangente das configurações críticas do sistema para produção.
    
    Esta função realiza validação completa de todas as configurações
    necessárias para deploy seguro do Sistema Dashboard IFPB-CZ em
    ambiente de produção, incluindo análise de configurações de
    segurança, fonte de dados e otimizações do Streamlit.
    
    PROCESSO DE VERIFICAÇÃO:
    1. Carregamento dinâmico do módulo config.py
    2. Validação de configurações de segurança críticas
    3. Análise de configuração de fonte de dados
    4. Verificação de configurações do Streamlit
    5. Relatório de conformidade para produção
    
    CONFIGURAÇÕES ANALISADAS:
    - MODO_SOMENTE_LEITURA: proteção contra modificações
    - USE_REAL_DATA: configuração de fonte de dados
    - config.toml: otimizações específicas do Streamlit
    
    VALIDAÇÕES DE SEGURANÇA:
    - Modo somente leitura: recomendado para produção
    - Dados reais vs sintéticos: configuração apropriada
    - Configurações Streamlit: otimizações de servidor
    
    ANÁLISES REALIZADAS:
    - Existência e carregamento correto do config.py
    - Presença de atributos de configuração essenciais
    - Valores adequados para ambiente de produção
    - Configurações complementares do Streamlit
    
    RETORNO:
    --------
    bool
        True se todas as configurações estão adequadas,
        False se há problemas críticos de configuração
        
    SAÍDAS GERADAS:
    ---------------
    - Status de carregamento do arquivo de configuração
    - Análise de cada configuração crítica
    - Recomendações para ambiente de produção
    - Identificação de problemas de configuração
    """
    # Exibir cabeçalho da seção de verificação de configurações
    print("\n🔧 VERIFICANDO CONFIGURAÇÕES:")
    print("-" * 50)
    
    # Contador de erros críticos encontrados
    erros = 0
    
    # =============================================================================
    # VERIFICAÇÃO E CARREGAMENTO DO ARQUIVO DE CONFIGURAÇÃO PRINCIPAL
    # =============================================================================
    
    # Verificar presença e carregar config.py dinamicamente
    if os.path.exists('config.py'):
        try:
            # Carregamento dinâmico seguro do módulo de configuração
            spec = importlib.util.spec_from_file_location("config", "config.py")
            config = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(config)
            
            # =============================================================================
            # VALIDAÇÃO DE CONFIGURAÇÕES DE SEGURANÇA PARA PRODUÇÃO
            # =============================================================================
            
            # Verificar configuração de modo somente leitura
            if hasattr(config, 'MODO_SOMENTE_LEITURA'):
                if config.MODO_SOMENTE_LEITURA:
                    # Configuração recomendada para ambiente de produção
                    print("   ✅ Modo somente leitura ativado (recomendado para produção)")
                else:
                    # Configuração de desenvolvimento - alerta para produção
                    print("   ⚠️  Modo somente leitura desativado (considere ativar para produção)")
            
            # Verificar configuração de fonte de dados
            if hasattr(config, 'USE_REAL_DATA'):
                if config.USE_REAL_DATA:
                    # Sistema configurado para usar dados reais
                    print("   ✅ Configurado para usar dados reais")
                else:
                    # Sistema usando dados sintéticos
                    print("   ⚠️  Configurado para usar dados sintéticos")
            
        except Exception as e:
            # Erro crítico no carregamento das configurações
            print(f"   ❌ Erro ao carregar config.py: {e}")
            erros += 1
    else:
        # Arquivo de configuração obrigatório não encontrado
        print("   ❌ config.py não encontrado")
        erros += 1
    
    # =============================================================================
    # VERIFICAÇÃO DE CONFIGURAÇÕES ESPECÍFICAS DO STREAMLIT
    # =============================================================================
    
    # Verificar presença de configurações otimizadas do Streamlit
    if os.path.exists('.streamlit/config.toml'):
        # Configurações específicas encontradas
        print("   ✅ Configurações Streamlit encontradas")
    else:
        # Configurações opcionais não encontradas
        print("   ⚠️  Configurações Streamlit não encontradas")
    
    return erros == 0

def verificar_dependencias():
    """
    Verificação completa das dependências críticas do sistema para produção.
    
    Esta função realiza validação abrangente de todas as dependências
    especificadas no requirements.txt, verificando presença de bibliotecas
    essenciais para funcionamento correto do Sistema Dashboard IFPB-CZ
    em ambiente de produção.
    
    PROCESSO DE VERIFICAÇÃO:
    1. Carregamento e análise do arquivo requirements.txt
    2. Parsing de dependências especificadas
    3. Comparação com lista de dependências essenciais
    4. Validação de presença de cada biblioteca crítica
    5. Relatório de dependências encontradas vs necessárias
    
    DEPENDÊNCIAS ESSENCIAIS VERIFICADAS:
    - streamlit: framework web principal da aplicação
    - pandas: manipulação e análise de dados
    - numpy: computação numérica e arrays
    - plotly: visualizações interativas e gráficos
    - openpyxl: leitura e escrita de arquivos Excel
    - folium: mapas interativos e geolocalização
    
    ANÁLISES REALIZADAS:
    - Contagem total de dependências especificadas
    - Verificação individual de cada dependência essencial
    - Identificação de dependências ausentes críticas
    - Validação de completude para funcionamento
    
    PARSING DE VERSÕES:
    - Suporte para especificações >= e ==
    - Extração de nomes de pacotes limpos
    - Ignorar comentários e linhas vazias
    - Tratamento de formatos diversos de especificação
    
    RETORNO:
    --------
    bool
        True se todas as dependências essenciais estão presentes,
        False se há dependências críticas ausentes
        
    SAÍDAS GERADAS:
    ---------------
    - Contagem total de dependências especificadas
    - Status individual de cada dependência essencial
    - Identificação de dependências ausentes
    - Análise de completude do requirements.txt
    """
    # Exibir cabeçalho da seção de verificação de dependências
    print("\n📦 VERIFICANDO DEPENDÊNCIAS:")
    print("-" * 50)
    
    # =============================================================================
    # CARREGAMENTO E ANÁLISE DO ARQUIVO REQUIREMENTS.TXT
    # =============================================================================
    
    if os.path.exists('requirements.txt'):
        # Carregar e processar conteúdo do requirements.txt
        with open('requirements.txt', 'r') as f:
            linhas = f.readlines()
        
        # Parsing de dependências especificadas
        deps_encontradas = []
        for linha in linhas:
            linha = linha.strip()
            # Filtrar comentários e linhas vazias
            if linha and not linha.startswith('#'):
                # Extrair nome do pacote removendo especificadores de versão
                deps_encontradas.append(linha.split('>=')[0].split('==')[0])
        
        # =============================================================================
        # DEFINIÇÃO E VERIFICAÇÃO DE DEPENDÊNCIAS ESSENCIAIS
        # =============================================================================
        
        # Lista de dependências críticas para funcionamento
        deps_essenciais = ['streamlit', 'pandas', 'numpy', 'plotly', 'openpyxl', 'folium']
        
        # Relatório de contagem total
        print(f"   ✅ {len(deps_encontradas)} dependências especificadas")
        
        # Verificação individual de cada dependência essencial
        for dep in deps_essenciais:
            if dep in deps_encontradas:
                # Dependência essencial encontrada
                print(f"   ✅ {dep}")
            else:
                # Dependência crítica ausente
                print(f"   ❌ {dep} (FALTANDO)")
        
        # Retornar status baseado na presença de todas as dependências essenciais
        return all(dep in deps_encontradas for dep in deps_essenciais)
    else:
        # Arquivo de dependências obrigatório não encontrado
        print("   ❌ requirements.txt não encontrado")
        return False

def verificar_modulos():
    """
    Verificação abrangente da integridade de todos os módulos do sistema.
    
    Esta função realiza validação completa da presença de todos os
    módulos Python essenciais para funcionamento do Sistema Dashboard
    IFPB-CZ, garantindo que a estrutura modular esteja íntegra para
    deploy em ambiente de produção.
    
    PROCESSO DE VERIFICAÇÃO:
    1. Definição de lista completa de módulos essenciais
    2. Verificação individual da presença de cada módulo
    3. Categorização como arquivos obrigatórios críticos
    4. Contabilização de módulos ausentes
    5. Relatório de integridade da estrutura modular
    
    MÓDULOS ESSENCIAIS VERIFICADOS:
    - __init__.py: inicialização do pacote modules
    - utils.py: utilitários compartilhados do sistema
    - data_generator.py: gerador de dados sintéticos
    - help_page.py: sistema de ajuda e documentação
    - presentation.py: apresentação institucional
    - ensino.py: módulo de dados educacionais
    - assistencia_estudantil.py: assistência estudantil
    - pesquisa.py: dados de pesquisa acadêmica
    - extensao.py: extensão universitária
    - orcamento.py: dados orçamentários
    - servidores.py: recursos humanos
    - ouvidoria.py: serviço de ouvidoria
    - auditoria.py: auditoria interna
    - mundo_trabalho.py: mercado de trabalho
    - mapa.py: funcionalidades de mapeamento
    
    CATEGORIZAÇÃO:
    - Todos os módulos são marcados como OBRIGATÓRIOS
    - Ausência de qualquer módulo impede funcionamento
    - Estrutura modular crítica para sistema completo
    
    ANÁLISES REALIZADAS:
    - Presença física de cada arquivo de módulo
    - Validação da estrutura completa esperada
    - Identificação de módulos ausentes críticos
    - Relatório de integridade modular geral
    
    RETORNO:
    --------
    bool
        True se todos os módulos essenciais estão presentes,
        False se há módulos críticos ausentes
        
    SAÍDAS GERADAS:
    ---------------
    - Status individual de cada módulo essencial
    - Identificação de módulos ausentes
    - Categorização como obrigatórios
    - Análise de completude da estrutura modular
    """
    # Exibir cabeçalho da seção de verificação de módulos
    print("\n🧩 VERIFICANDO MÓDULOS:")
    print("-" * 50)
    
    # =============================================================================
    # DEFINIÇÃO COMPLETA DE MÓDULOS ESSENCIAIS DO SISTEMA
    # =============================================================================
    
    # Lista abrangente de todos os módulos críticos para funcionamento
    modulos_essenciais = [
        'modules/__init__.py',              # Inicialização do pacote modules
        'modules/utils.py',                 # Utilitários compartilhados
        'modules/data_generator.py',        # Gerador de dados sintéticos
        'modules/help_page.py',             # Sistema de ajuda e documentação
        'modules/presentation.py',          # Apresentação institucional
        'modules/ensino.py',                # Módulo de dados educacionais
        'modules/assistencia_estudantil.py', # Assistência estudantil
        'modules/pesquisa.py',              # Dados de pesquisa acadêmica
        'modules/extensao.py',              # Extensão universitária
        'modules/orcamento.py',             # Dados orçamentários
        'modules/servidores.py',            # Recursos humanos
        'modules/ouvidoria.py',             # Serviço de ouvidoria
        'modules/auditoria.py',             # Auditoria interna
        'modules/mundo_trabalho.py',        # Mercado de trabalho
        'modules/mapa.py'                   # Funcionalidades de mapeamento
    ]
    
    # =============================================================================
    # VERIFICAÇÃO INDIVIDUAL DE CADA MÓDULO ESSENCIAL
    # =============================================================================
    
    # Flag para rastrear integridade completa da estrutura modular
    todos_presentes = True
    
    # Iterar por todos os módulos essenciais para verificação
    for modulo in modulos_essenciais:
        # Verificar presença do módulo (todos marcados como obrigatórios)
        existe = verificar_arquivo_existe(modulo, obrigatorio=True)
        if not existe:
            # Registrar falha na integridade modular
            todos_presentes = False
    
    return todos_presentes

def main():
    """
    Função principal de coordenação da verificação de integridade para produção.
    
    Esta função coordena a execução completa de todas as verificações
    necessárias para validar se o Sistema Dashboard IFPB-CZ está
    adequadamente preparado para deploy em ambiente de produção,
    organizando sequência de validações e gerando relatório
    consolidado de prontidão.
    
    PROCESSO DE VERIFICAÇÃO COMPLETA:
    1. Validação de execução no diretório correto do projeto
    2. Verificação de arquivos principais obrigatórios
    3. Validação de estrutura de pastas necessárias
    4. Análise de integridade dos módulos do sistema
    5. Verificação de configurações de segurança
    6. Validação de dependências críticas
    7. Geração de relatório final consolidado
    
    VERIFICAÇÕES COORDENADAS:
    - Arquivos principais: app.py, requirements.txt, config.py, etc.
    - Pastas obrigatórias: modules/, .streamlit/, logo-ifpb/
    - Módulos essenciais: todos os componentes funcionais
    - Configurações: segurança e fonte de dados
    - Dependências: bibliotecas críticas completas
    
    ANÁLISES DE PRONTIDÃO:
    - Contabilização de erros críticos encontrados
    - Contabilização de avisos não críticos
    - Determinação de status final de prontidão
    - Geração de instruções para próximos passos
    
    RELATÓRIOS GERADOS:
    - Status detalhado de cada categoria verificada
    - Contagem de problemas críticos vs avisos
    - Diagnóstico final de prontidão para produção
    - Instruções específicas para correções ou deploy
    
    RETORNO:
    --------
    bool
        True se projeto está pronto para produção,
        False se há problemas críticos que impedem deploy
        
    SAÍDAS GERADAS:
    ---------------
    - Cabeçalho identificador do verificador
    - Status detalhado de todas as verificações
    - Relatório final consolidado de prontidão
    - Instruções para próximos passos apropriados
    """
    # Exibir cabeçalho principal do verificador de integridade
    print("=" * 70)
    print("🔍 VERIFICADOR DE INTEGRIDADE PARA PRODUÇÃO")
    print("   Sistema Dashboard IFPB-CZ")
    print("=" * 70)
    
    # =============================================================================
    # VALIDAÇÃO DE EXECUÇÃO NO DIRETÓRIO CORRETO DO PROJETO
    # =============================================================================
    
    # Verificar se estamos no diretório raiz correto do projeto
    if not os.path.exists('app.py'):
        print("❌ ERRO: Execute este script na raiz do projeto!")
        print("   O arquivo 'app.py' não foi encontrado.")
        sys.exit(1)
    
    # Contadores para estatísticas de problemas encontrados
    erros = 0    # Problemas críticos que impedem deploy
    avisos = 0   # Problemas não críticos recomendados
    
    # =============================================================================
    # 1. VERIFICAÇÃO DE ARQUIVOS PRINCIPAIS OBRIGATÓRIOS
    # =============================================================================
    
    print("\n📄 VERIFICANDO ARQUIVOS PRINCIPAIS:")
    print("-" * 50)
    
    # Lista de arquivos principais com classificação de obrigatoriedade
    arquivos_principais = [
        ('app.py', True),                    # Aplicação principal Streamlit
        ('requirements.txt', True),          # Especificação de dependências
        ('config.py', True),                 # Configurações do sistema
        ('README.md', True),                 # Documentação de instalação
        ('LICENSE', False),                  # Licença do projeto (opcional)
        ('GUIA_ATUALIZACAO_DADOS.md', False) # Guia de atualização (opcional)
    ]
    
    # Verificar cada arquivo principal individualmente
    for arquivo, obrigatorio in arquivos_principais:
        if not verificar_arquivo_existe(arquivo, obrigatorio):
            if obrigatorio:
                erros += 1
            else:
                avisos += 1
    
    # =============================================================================
    # 2. VERIFICAÇÃO DE PASTAS PRINCIPAIS NECESSÁRIAS
    # =============================================================================
    
    print("\n📁 VERIFICANDO PASTAS PRINCIPAIS:")
    print("-" * 50)
    
    # Lista de pastas principais com classificação de obrigatoriedade
    pastas_principais = [
        ('modules', True),      # Módulos funcionais do sistema
        ('.streamlit', True),   # Configurações específicas Streamlit
        ('logo-ifpb', True),    # Recursos visuais institucionais
        ('dados', False),       # Dados reais (opcional, usa sintéticos)
        ('docs', False),        # Documentação adicional (opcional)
        ('fluxo', False)        # Diagramas de fluxo (opcional)
    ]
    
    # Verificar cada pasta principal individualmente
    for pasta, obrigatorio in pastas_principais:
        if not verificar_pasta_existe(pasta, obrigatorio):
            if obrigatorio:
                erros += 1
            else:
                avisos += 1
    
    # =============================================================================
    # 3. VERIFICAÇÃO DE INTEGRIDADE DOS MÓDULOS DO SISTEMA
    # =============================================================================
    
    if not verificar_modulos():
        erros += 1
    
    # =============================================================================
    # 4. VERIFICAÇÃO DE CONFIGURAÇÕES DE SEGURANÇA
    # =============================================================================
    
    if not verificar_configuracoes():
        erros += 1
    
    # =============================================================================
    # 5. VERIFICAÇÃO DE DEPENDÊNCIAS CRÍTICAS
    # =============================================================================
    
    if not verificar_dependencias():
        erros += 1
    
    # =============================================================================
    # 6. RELATÓRIO FINAL CONSOLIDADO DE PRONTIDÃO PARA PRODUÇÃO
    # =============================================================================
    
    print("\n" + "=" * 70)
    print("📊 RELATÓRIO FINAL:")
    print("-" * 50)
    
    if erros == 0:
        # =============================================================================
        # PROJETO PRONTO PARA DEPLOY EM PRODUÇÃO
        # =============================================================================
        
        print("🎉 PROJETO PRONTO PARA PRODUÇÃO!")
        print("   ✅ Todos os arquivos obrigatórios estão presentes")
        print("   ✅ Configurações verificadas")
        print("   ✅ Dependências completas")
        
        # Informar sobre avisos não críticos, se houver
        if avisos > 0:
            print(f"   ⚠️  {avisos} arquivo(s) opcional(is) ausente(s)")
        
        # Instruções para próximos passos do deploy
        print("\n🚀 PRÓXIMOS PASSOS:")
        print("   1. Execute: python criar_pacote_producao.py")
        print("   2. Faça upload do ZIP para o servidor")
        print("   3. Extraia e configure conforme README.md")
        
        return True
        
    else:
        # =============================================================================
        # PROJETO NÃO ESTÁ PRONTO - CORREÇÕES NECESSÁRIAS
        # =============================================================================
        
        print(f"❌ PROJETO NÃO ESTÁ PRONTO PARA PRODUÇÃO!")
        print(f"   🔴 {erros} erro(s) crítico(s) encontrado(s)")
        
        # Informar sobre avisos adicionais, se houver
        if avisos > 0:
            print(f"   ⚠️  {avisos} aviso(s)")
        
        # Instruções para resolução de problemas
        print("\n🔧 CORREÇÕES NECESSÁRIAS:")
        print("   • Corrija os erros marcados com ❌")
        print("   • Verifique a documentação do projeto")
        print("   • Execute novamente este script após as correções")
        
        return False

if __name__ == "__main__":
    """
    Ponto de entrada principal do verificador de integridade para produção.
    
    Esta seção coordena a execução completa de todas as verificações
    necessárias para validar prontidão do Sistema Dashboard IFPB-CZ
    para deploy em ambiente de produção, gerando código de saída
    apropriado para integração com sistemas de CI/CD.
    
    EXECUÇÃO REALIZADA:
    1. Verificação de execução direta do script
    2. Chamada da função principal de verificação
    3. Execução de todas as validações de integridade
    4. Determinação de código de saída baseado em resultados
    
    CÓDIGOS DE SAÍDA:
    - 0: projeto pronto para produção (sucesso)
    - 1: correções necessárias antes do deploy (falha)
    
    FINALIDADE:
    -----------
    Permitir execução independente do script para validação
    completa de prontidão para produção, com integração
    apropriada em pipelines de deploy automatizado.
    
    PROCESSO:
    ---------
    - Execução direta: python verificar_deploy.py
    - Validação completa: todos os aspectos críticos
    - Relatório detalhado: status e instruções
    - Código de saída: compatível com automação
    """
    # Executar verificação principal e capturar resultado
    sucesso = main()
    print()
    
    # Definir código de saída baseado no resultado das verificações
    sys.exit(0 if sucesso else 1)
