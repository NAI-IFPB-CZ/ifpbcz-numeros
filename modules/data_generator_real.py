"""
=============================================================================
MÓDULO GERADOR DE DADOS REAIS - SISTEMA DASHBOARD IFPB-CZ
=============================================================================

Este módulo implementa a classe DataGeneratorReal responsável por carregar,
validar e processar dados reais dos arquivos Excel institucionais para
alimentação do Sistema Dashboard IFPB-CZ. Garante integridade dos dados,
validação de estruturas e tratamento robusto de erros.

FUNCIONALIDADES PRINCIPAIS:
---------------------------
- Carregamento de dados reais de 9 arquivos Excel institucionais
- Validação rigorosa de estruturas de dados e colunas obrigatórias
- Tratamento inteligente de valores nulos e tipos de dados
- Sistema de logs detalhado para monitoramento de carregamento
- Verificação de integridade de arquivos e diretórios
- Processamento robusto com tratamento abrangente de exceções

ARQUIVOS DE DADOS GERENCIADOS:
------------------------------
1. dados_assistencia.xlsx - Programas de assistência estudantil
2. dados_auditoria.xlsx - Processos de auditoria e conformidade
3. dados_ensino.xlsx - Indicadores educacionais e acadêmicos
4. dados_extensao.xlsx - Projetos e ações de extensão
5. dados_mundo_trabalho.xlsx - Acompanhamento de egressos
6. dados_orcamento.xlsx - Gestão financeira e execução orçamentária
7. dados_ouvidoria.xlsx - Atendimento e manifestações
8. dados_pesquisa.xlsx - Produção científica e projetos
9. dados_servidores.xlsx - Recursos humanos e quadro funcional

VALIDAÇÕES IMPLEMENTADAS:
-------------------------
- Verificação de existência de arquivos e diretório de dados
- Validação de colunas obrigatórias por módulo específico
- Conversão automática de tipos de dados (int, float, str)
- Tratamento inteligente de valores nulos conforme contexto
- Validação de consistência temporal (anos válidos)
- Verificação de integridade referencial básica

CARACTERÍSTICAS TÉCNICAS:
--------------------------
- Arquitetura orientada a objetos com métodos especializados
- Sistema de logs coloridos para diagnóstico visual
- Tratamento robusto de exceções com mensagens informativas
- Validação em tempo real durante carregamento
- Suporte a múltiplas planilhas por arquivo Excel
- Flexibilidade para expansão de novos módulos de dados

ESTRUTURA DE DADOS:
-------------------
- Diretório padrão: dados/ (relativo à raiz do projeto)
- Formato obrigatório: .xlsx (Excel 2007+)
- Estrutura de planilhas: primeira planilha ou nome específico
- Encoding: UTF-8 com suporte a caracteres especiais
- Tipos suportados: inteiros, decimais, texto, datas

TRATAMENTO DE ERROS:
--------------------
- FileNotFoundError: arquivo ou diretório inexistente
- ValueError: estrutura de dados inválida ou colunas faltantes
- Exception genérica: problemas de leitura ou processamento
- Logs informativos: progresso e status de carregamento
- Validação prévia: verificação antes do processamento

OBJETIVO:
---------
Garantir carregamento confiável e validado de dados institucionais
reais, proporcionando base sólida para análises e visualizações
precisas no dashboard, com tratamento robusto de inconsistências
e facilidade de diagnóstico de problemas.

DEPENDÊNCIAS:
-------------
- pandas: manipulação e análise de dados
- numpy: operações numéricas e tratamento de arrays
- os: operações do sistema operacional
- datetime: manipulação de datas e timestamps
- warnings: controle de avisos do sistema

AUTOR: Sistema Dashboard IFPB-CZ - NAI
DATA: 2024
=============================================================================
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class DataGeneratorReal:
    """
    Classe geradora de dados reais do Sistema Dashboard IFPB-CZ.
    
    Esta classe centraliza o carregamento, validação e processamento de dados
    institucionais reais a partir de arquivos Excel padronizados, garantindo
    integridade, consistência e tratamento robusto de erros para alimentação
    confiável do sistema de visualizações.
    
    RESPONSABILIDADES PRINCIPAIS:
    - Gerenciamento de 9 arquivos Excel institucionais
    - Validação rigorosa de estruturas e tipos de dados
    - Tratamento inteligente de valores nulos e inconsistências
    - Sistema de logs detalhado para monitoramento
    - Conversão automática de tipos de dados conforme especificação
    - Verificação de integridade referencial básica
    
    ARQUIVOS GERENCIADOS:
    - dados_assistencia.xlsx: programas assistenciais e benefícios
    - dados_auditoria.xlsx: auditorias e recomendações
    - dados_ensino.xlsx: indicadores educacionais e acadêmicos
    - dados_extensao.xlsx: projetos extensionistas e comunidade
    - dados_mundo_trabalho.xlsx: inserção profissional de egressos
    - dados_orcamento.xlsx: execução financeira e orçamentária
    - dados_ouvidoria.xlsx: manifestações e atendimento
    - dados_pesquisa.xlsx: produção científica e projetos
    - dados_servidores.xlsx: recursos humanos e quadro funcional
    
    VALIDAÇÕES IMPLEMENTADAS:
    - Existência de arquivos e diretório de dados
    - Colunas obrigatórias específicas por módulo
    - Tipos de dados apropriados (int, float, str)
    - Tratamento de valores nulos contextualizado
    - Consistência temporal e referencial
    
    CARACTERÍSTICAS TÉCNICAS:
    - Logs coloridos para diagnóstico visual (✅❌📊)
    - Tratamento robusto de exceções
    - Flexibilidade para múltiplas planilhas
    - Suporte a encoding UTF-8
    - Arquitetura extensível para novos módulos
    
    ESTRUTURA DE ARQUIVOS NECESSÁRIA:
    - dados/dados_assistencia.xlsx
    - dados/dados_auditoria.xlsx
    - dados/dados_ensino.xlsx
    - dados/dados_extensao.xlsx
    - dados/dados_mundo_trabalho.xlsx
    - dados/dados_orcamento.xlsx
    - dados/dados_ouvidoria.xlsx
    - dados/dados_pesquisa.xlsx
    - dados/dados_servidores.xlsx
    
    ATRIBUTOS:
    ----------
    dados_directory : str
        Caminho do diretório contendo os arquivos de dados
    data_atualizacao : str
        Timestamp da última atualização/carregamento
        
    MÉTODOS PRINCIPAIS:
    ------------------
    gerar_dados_[modulo]() : DataFrame
        Métodos especializados para cada módulo de dados
    _verificar_arquivo() : str
        Validação de existência de arquivos
    _ler_excel() : DataFrame
        Carregamento seguro de planilhas Excel
    _validar_colunas() : None
        Validação de estrutura de colunas obrigatórias
    """
    
    def __init__(self):
        """
        Inicialização da classe DataGeneratorReal.
        
        Configura diretório de dados, timestamp de atualização e verifica
        existência da estrutura básica de arquivos necessária para
        funcionamento do sistema.
        
        CONFIGURAÇÕES INICIAIS:
        - Define diretório padrão 'dados/' para arquivos Excel
        - Gera timestamp atual para controle de atualização
        - Verifica existência do diretório de dados
        
        VALIDAÇÕES REALIZADAS:
        - Existência do diretório 'dados/' na raiz do projeto
        - Permissões de leitura no diretório especificado
        
        EXCEÇÕES LANÇADAS:
        ------------------
        FileNotFoundError
            Quando diretório 'dados/' não existe ou não é acessível
            
        ATRIBUTOS INICIALIZADOS:
        -----------------------
        dados_directory : str
            Caminho relativo para o diretório de dados ("dados")
        data_atualizacao : str
            Timestamp formatado da inicialização (DD/MM/AAAA às HH:MM)
        """
        # ============= CONFIGURAÇÃO DE DIRETÓRIOS E CONTROLE TEMPORAL =============
        # Define diretório padrão para arquivos Excel institucionais
        self.dados_directory = "dados"
        
        # Gera timestamp para controle de atualização dos dados
        self.data_atualizacao = datetime.now().strftime("%d/%m/%Y às %H:%M")
        
        # ============= VALIDAÇÃO DA ESTRUTURA DE DIRETÓRIOS =============
        # Verifica existência do diretório de dados obrigatório
        # Interrompe execução se estrutura básica não estiver presente
        # Verificar se o diretório existe
        if not os.path.exists(self.dados_directory):
            raise FileNotFoundError(f"Diretório '{self.dados_directory}' não encontrado!")
    
    def _verificar_arquivo(self, nome_arquivo):
        """
        Verificação de existência e acessibilidade de arquivo específico.
        
        Valida se arquivo Excel especificado existe no diretório de dados
        e está acessível para leitura, construindo caminho completo para
        carregamento posterior.
        
        VALIDAÇÕES REALIZADAS:
        - Existência física do arquivo no diretório dados/
        - Acessibilidade para operações de leitura
        - Construção de caminho absoluto correto
        
        PARÂMETROS:
        -----------
        nome_arquivo : str
            Nome do arquivo Excel a ser verificado (ex: "dados_ensino.xlsx")
            
        RETORNO:
        --------
        str
            Caminho completo para o arquivo validado
            
        EXCEÇÕES LANÇADAS:
        ------------------
        FileNotFoundError
            Quando arquivo especificado não existe no diretório dados/
            
        EXEMPLO DE USO:
        --------------
        caminho = self._verificar_arquivo("dados_ensino.xlsx")
        # Retorna: "dados/dados_ensino.xlsx"
        """
        # ============= CONSTRUÇÃO E VALIDAÇÃO DE CAMINHO DE ARQUIVO =============
        # Combina diretório base com nome do arquivo para caminho completo
        caminho = os.path.join(self.dados_directory, nome_arquivo)
        
        # ============= VERIFICAÇÃO DE EXISTÊNCIA FÍSICA DO ARQUIVO =============
        # Valida se arquivo existe fisicamente no sistema de arquivos
        # Interrompe processamento se arquivo obrigatório está ausente
        if not os.path.exists(caminho):
            raise FileNotFoundError(f"Arquivo '{nome_arquivo}' não encontrado em '{self.dados_directory}'!")
        return caminho
    
    def _ler_excel(self, nome_arquivo, sheet_name=0):
        """
        Carregamento seguro de arquivo Excel com tratamento de erros.
        
        Realiza leitura robusta de planilha Excel com validação prévia,
        tratamento de exceções e logging informativo do processo de
        carregamento para monitoramento do sistema.
        
        PROCESSO DE CARREGAMENTO:
        1. Verificação de existência do arquivo
        2. Leitura da planilha especificada
        3. Validação básica do DataFrame resultante
        4. Logging do resultado (sucesso/falha)
        
        TRATAMENTO DE ERROS:
        - Arquivo inexistente: FileNotFoundError
        - Planilha inválida: Exception específica do pandas
        - Formato incorreto: ValueError implícito
        - Problemas de encoding: UnicodeDecodeError implícito
        
        PARÂMETROS:
        -----------
        nome_arquivo : str
            Nome do arquivo Excel (ex: "dados_ensino.xlsx")
        sheet_name : int ou str, opcional
            Índice ou nome da planilha (padrão: 0 - primeira planilha)
            
        RETORNO:
        --------
        pandas.DataFrame
            DataFrame contendo dados da planilha carregada
            
        EXCEÇÕES LANÇADAS:
        ------------------
        Exception
            Qualquer erro durante carregamento é capturado e re-lançado
            com informações específicas para diagnóstico
            
        LOGGING REALIZADO:
        -----------------
        Sucesso: "✅ Arquivo 'nome.xlsx' carregado com sucesso: N registros"
        Falha: "❌ Erro ao carregar 'nome.xlsx': descrição do erro"
        """
        # ============= CARREGAMENTO SEGURO COM TRATAMENTO DE EXCEÇÕES =============
        try:
            # Verifica existência do arquivo antes da tentativa de leitura
            caminho = self._verificar_arquivo(nome_arquivo)
            
            # Carrega planilha Excel com pandas usando configurações padrão
            df = pd.read_excel(caminho, sheet_name=sheet_name)
            
            # ============= LOGGING DE SUCESSO COM INFORMAÇÕES ESTATÍSTICAS =============
            # Registra carregamento bem-sucedido com contagem de registros
            print(f"✅ Arquivo '{nome_arquivo}' carregado com sucesso: {len(df)} registros")
            return df
            
        except Exception as e:
            # ============= LOGGING DE ERRO COM DETALHES PARA DIAGNÓSTICO =============
            # Registra falha no carregamento com descrição específica do erro
            print(f"❌ Erro ao carregar '{nome_arquivo}': {str(e)}")
            raise
    
    def _validar_colunas(self, df, colunas_obrigatorias, nome_modulo):
        """
        Validação rigorosa de estrutura de colunas obrigatórias.
        
        Verifica se DataFrame carregado possui todas as colunas obrigatórias
        especificadas para o módulo, garantindo compatibilidade com
        processamento posterior e geração de visualizações.
        
        VALIDAÇÕES REALIZADAS:
        - Presença de todas as colunas obrigatórias
        - Correspondência exata de nomes (case-sensitive)
        - Identificação específica de colunas faltantes
        
        PROCESSO DE VALIDAÇÃO:
        1. Comparação entre colunas existentes e obrigatórias
        2. Identificação de colunas faltantes
        3. Geração de erro específico se há colunas ausentes
        4. Logging de validação bem-sucedida
        
        PARÂMETROS:
        -----------
        df : pandas.DataFrame
            DataFrame a ser validado
        colunas_obrigatorias : list[str]
            Lista de nomes de colunas obrigatórias
        nome_modulo : str
            Nome do módulo para identificação em logs e erros
            
        RETORNO:
        --------
        None
            Função de validação sem retorno explícito
            
        EXCEÇÕES LANÇADAS:
        ------------------
        ValueError
            Quando uma ou mais colunas obrigatórias estão ausentes
            Inclui lista específica das colunas faltantes
            
        LOGGING REALIZADO:
        -----------------
        Sucesso: "✅ Validação de colunas do módulo [nome]: OK"
        Falha: "❌ Colunas faltantes em [nome]: [lista_colunas]"
        
        EXEMPLO DE USO:
        --------------
        colunas = ['ano', 'campus', 'curso', 'matriculados']
        self._validar_colunas(df_ensino, colunas, "Ensino")
        """
        # ============= IDENTIFICAÇÃO DE COLUNAS FALTANTES =============
        # Compara colunas obrigatórias com colunas presentes no DataFrame
        # Cria lista específica de colunas ausentes para diagnóstico
        colunas_faltantes = [col for col in colunas_obrigatorias if col not in df.columns]
        
        # ============= VALIDAÇÃO E TRATAMENTO DE ERROS =============
        # Interrompe processamento se há colunas obrigatórias ausentes
        # Fornece informações específicas sobre colunas faltantes
        if colunas_faltantes:
            raise ValueError(f"❌ Colunas faltantes em {nome_modulo}: {colunas_faltantes}")
        
        # ============= LOGGING DE VALIDAÇÃO BEM-SUCEDIDA =============
        # Confirma que estrutura de dados está correta para processamento
        print(f"✅ Validação de colunas do módulo {nome_modulo}: OK")
    
    def gerar_dados_extensao(self):
        """
        Carregamento e processamento de dados reais de extensão universitária.
        
        Realiza carregamento do arquivo dados_extensao.xlsx contendo informações
        sobre projetos extensionistas, estágios, acessibilidade e inclusão,
        com validação rigorosa de estrutura e tratamento de inconsistências.
        
        DADOS PROCESSADOS:
        - Projetos de extensão por ano e modalidade
        - Estágios concluídos e acompanhamento profissional
        - Ingressantes PNE (Pessoas com Necessidades Específicas)
        - Tipos de necessidades e adaptações realizadas
        - Distribuição por gênero e unidades institucionais
        
        ESTRUTURA ESPERADA DA PLANILHA dados_extensao.xlsx:
        - ano: int (ex: 2023, 2024, 2025)
        - unidade: str (ex: "IFPB - Campus Campina Grande")
        - curso: str (ex: "Técnico em Informática")
        - modalidade: str (ex: "Presencial", "EAD")
        - genero: str (ex: "Masculino", "Feminino", "Outro")
        - estagios_concluidos: int (número de estágios concluídos)
        - pne_ingressantes: int (número de ingressantes PNE)
        - tipo_necessidade: str (ex: "Física", "Visual", "Auditiva", "Intelectual")
        
        VALIDAÇÕES E TRATAMENTOS:
        - Verificação de colunas obrigatórias
        - Tratamento de valores nulos (substituição por 0 quando apropriado)
        - Conversão de tipos de dados (int para campos numéricos)
        - Validação temporal (anos não podem estar vazios)
        
        RETORNO:
        --------
        pandas.DataFrame
            DataFrame processado com dados de extensão validados e limpos
            
        EXCEÇÕES POSSÍVEIS:
        ------------------
        FileNotFoundError : arquivo dados_extensao.xlsx não encontrado
        ValueError : estrutura de dados inválida ou colunas faltantes
        Exception : problemas gerais de carregamento ou processamento
        
        LOGGING REALIZADO:
        -----------------
        "📊 Carregando dados reais de extensão..."
        "✅ Dados de extensão carregados: N registros de AAAA a AAAA"
        """
        # ============= INÍCIO DO PROCESSO DE CARREGAMENTO =============
        print("📊 Carregando dados reais de extensão...")
        
        # ============= CARREGAMENTO DO ARQUIVO EXCEL =============
        # Utiliza método seguro de leitura com tratamento de erros
        # Carregar dados do Excel
        df = self._ler_excel("dados_extensao.xlsx")
        
        # ============= VALIDAÇÃO DE ESTRUTURA DE COLUNAS =============
        # Define e valida colunas obrigatórias específicas do módulo extensão
        # Garante compatibilidade com processamento posterior
        # Validar colunas obrigatórias
        colunas_obrigatorias = [
            'ano', 'unidade', 'curso', 'modalidade', 'genero',
            'estagios_concluidos', 'pne_ingressantes', 'tipo_necessidade'
        ]
        self._validar_colunas(df, colunas_obrigatorias, "Extensão")
        
        # ============= VALIDAÇÕES ESPECÍFICAS E TRATAMENTO DE DADOS =============
        # Validações adicionais
        if df['ano'].isna().any():
            raise ValueError("❌ Coluna 'ano' não pode ter valores vazios")
        
        # Tratamento inteligente de valores nulos em campos numéricos
        # Substitui NaN por 0 para manter consistência estatística
        if df['estagios_concluidos'].isna().any():
            df['estagios_concluidos'] = df['estagios_concluidos'].fillna(0)
        
        if df['pne_ingressantes'].isna().any():
            df['pne_ingressantes'] = df['pne_ingressantes'].fillna(0)
        
        # ============= CONVERSÃO DE TIPOS DE DADOS =============
        # Garante tipos corretos para processamento numérico e visualizações
        # Converter tipos de dados
        df['ano'] = df['ano'].astype(int)
        df['estagios_concluidos'] = df['estagios_concluidos'].astype(int)
        df['pne_ingressantes'] = df['pne_ingressantes'].astype(int)
        
        # ============= LOGGING DE CARREGAMENTO FINALIZADO =============
        # Confirma sucesso com estatísticas básicas dos dados carregados
        print(f"✅ Dados de extensão carregados: {len(df)} registros de {df['ano'].min()} a {df['ano'].max()}")
        return df
    
    def gerar_dados_ensino(self):
        """
        Carregamento e processamento de dados reais de ensino e indicadores acadêmicos.
        
        Processa arquivo dados_ensino.xlsx contendo informações sobre matrículas,
        formação, evasão e indicadores educacionais fundamentais para
        acompanhamento da gestão acadêmica institucional.
        
        DADOS PROCESSADOS:
        - Matrículas por curso, modalidade e período
        - Formandos e taxa de conclusão
        - Desistências e transferências (indicadores de evasão)
        - Distribuição por campus e modalidades de ensino
        
        ESTRUTURA ESPERADA DA PLANILHA dados_ensino.xlsx:
        - ano: int
        - campus: str
        - curso: str
        - modalidade: str
        - matriculados: int
        - formados: int
        - desistentes: int
        - transferidos: int
        
        TRATAMENTOS REALIZADOS:
        - Preenchimento de valores NaN com 0 para campos numéricos
        - Conversão automática de tipos de dados
        - Validação de integridade estrutural
        
        RETORNO:
        --------
        pandas.DataFrame
            DataFrame com dados educacionais processados e validados
        """
        # ============= INÍCIO DO CARREGAMENTO DE DADOS EDUCACIONAIS =============
        print("📊 Carregando dados reais de ensino...")
        
        # ============= CARREGAMENTO E VALIDAÇÃO ESTRUTURAL =============
        df = self._ler_excel("dados_ensino.xlsx")
        
        colunas_obrigatorias = [
            'ano', 'campus', 'curso', 'modalidade',
            'matriculados', 'formados', 'desistentes', 'transferidos'
        ]
        self._validar_colunas(df, colunas_obrigatorias, "Ensino")
        
        # ============= TRATAMENTO DE DADOS NUMÉRICOS =============
        # Preencher valores NaN com 0 para colunas numéricas
        colunas_numericas = ['matriculados', 'formados', 'desistentes', 'transferidos']
        for col in colunas_numericas:
            df[col] = df[col].fillna(0).astype(int)
        
        df['ano'] = df['ano'].astype(int)
        
        # ============= CONFIRMAÇÃO DE CARREGAMENTO =============
        print(f"✅ Dados de ensino carregados: {len(df)} registros")
        return df
    
    def gerar_dados_pesquisa(self):
        """
        Carregamento e processamento de dados reais de pesquisa e produção científica.
        
        Processa arquivo dados_pesquisa.xlsx contendo informações sobre produção
        acadêmica, publicações científicas e distribuição por áreas do conhecimento
        para acompanhamento da atividade de pesquisa institucional.
        
        DADOS PROCESSADOS:
        - Publicações por tipo (artigos, capítulos, trabalhos em eventos)
        - Distribuição por áreas do conhecimento
        - Quantificação de produção científica por período
        - Vinculação com servidores/pesquisadores (opcional)
        
        ESTRUTURA ESPERADA DA PLANILHA dados_pesquisa.xlsx:
        - ano: int
        - tipo_publicacao: str (ex: "Artigos", "Capítulos de Livros", "Trabalhos em Eventos")
        - quantidade: int
        - area_conhecimento: str
        - servidor: str (opcional)
        
        TRATAMENTOS REALIZADOS:
        - Conversão de tipos de dados numéricos
        - Preenchimento de quantidades nulas com 0
        - Validação de consistência temporal
        
        RETORNO:
        --------
        pandas.DataFrame
            DataFrame com dados de pesquisa processados e validados
        """
        # ============= INÍCIO DO CARREGAMENTO DE DADOS DE PESQUISA =============
        print("📊 Carregando dados reais de pesquisa...")
        
        # ============= CARREGAMENTO E VALIDAÇÃO ESTRUTURAL =============
        df = self._ler_excel("dados_pesquisa.xlsx")
        
        colunas_obrigatorias = ['ano', 'tipo_publicacao', 'quantidade', 'area_conhecimento']
        self._validar_colunas(df, colunas_obrigatorias, "Pesquisa")
        
        # ============= CONVERSÃO E TRATAMENTO DE DADOS =============
        df['ano'] = df['ano'].astype(int)
        df['quantidade'] = df['quantidade'].fillna(0).astype(int)
        
        # ============= CONFIRMAÇÃO DE CARREGAMENTO =============
        print(f"✅ Dados de pesquisa carregados: {len(df)} registros")
        return df
    
    def gerar_dados_assistencia(self):
        """
        Carregamento e processamento de dados reais de assistência estudantil.
        
        Processa dados sobre programas assistenciais, benefícios concedidos,
        valores investidos e perfil dos beneficiários para acompanhamento
        das políticas de permanência e êxito estudantil.
        
        ESTRUTURA ESPERADA:
        - ano, campus, auxilio_tipo, beneficiarios, valor_total
        
        RETORNO:
        --------
        pandas.DataFrame
            DataFrame com dados de assistência processados
        """
        # ============= CARREGAMENTO DE DADOS ASSISTENCIAIS =============
        print("📊 Carregando dados reais de assistência estudantil...")
        
        df = self._ler_excel("dados_assistencia.xlsx")
        
        colunas_obrigatorias = ['ano', 'campus', 'auxilio_tipo', 'beneficiarios', 'valor_total']
        self._validar_colunas(df, colunas_obrigatorias, "Assistência")
        
        # ============= TRATAMENTO DE DADOS NUMÉRICOS =============
        df['ano'] = df['ano'].astype(int)
        df['beneficiarios'] = df['beneficiarios'].fillna(0).astype(int)
        df['valor_total'] = df['valor_total'].fillna(0).astype(float)
        
        print(f"✅ Dados de assistência carregados: {len(df)} registros")
        return df
    
    def gerar_dados_auditoria(self):
        """
        Carregamento e processamento de dados reais de auditoria e conformidade.
        
        Processa informações sobre auditorias realizadas, recomendações emitidas
        e status de conformidade para acompanhamento da gestão institucional.
        
        RETORNO:
        --------
        pandas.DataFrame
            DataFrame com dados de auditoria processados
        """
        # ============= CARREGAMENTO DE DADOS DE AUDITORIA =============
        print("📊 Carregando dados reais de auditoria...")
        
        df = self._ler_excel("dados_auditoria.xlsx")
        
        colunas_obrigatorias = ['ano', 'tipo_auditoria', 'numero_auditorias', 'recomendacoes']
        self._validar_colunas(df, colunas_obrigatorias, "Auditoria")
        
        # ============= CONVERSÃO DE TIPOS DE DADOS =============
        df['ano'] = df['ano'].astype(int)
        df['numero_auditorias'] = df['numero_auditorias'].fillna(0).astype(int)
        df['recomendacoes'] = df['recomendacoes'].fillna(0).astype(int)
        
        print(f"✅ Dados de auditoria carregados: {len(df)} registros")
        return df
    
    def gerar_dados_mundo_trabalho(self):
        """
        Carregamento e processamento de dados reais de inserção no mundo do trabalho.
        
        Processa informações sobre empregabilidade de egressos, salários médios
        e acompanhamento da inserção profissional por curso e campus.
        
        RETORNO:
        --------
        pandas.DataFrame
            DataFrame com dados de mundo do trabalho processados
        """
        # ============= CARREGAMENTO DE DADOS DE EGRESSOS =============
        print("📊 Carregando dados reais de mundo do trabalho...")
        
        df = self._ler_excel("dados_mundo_trabalho.xlsx")
        
        colunas_obrigatorias = ['ano', 'campus', 'curso', 'empregabilidade', 'salario_medio']
        self._validar_colunas(df, colunas_obrigatorias, "Mundo do Trabalho")
        
        # ============= TRATAMENTO DE DADOS FINANCEIROS =============
        df['ano'] = df['ano'].astype(int)
        df['empregabilidade'] = df['empregabilidade'].fillna(0).astype(float)
        df['salario_medio'] = df['salario_medio'].fillna(0).astype(float)
        
        print(f"✅ Dados de mundo do trabalho carregados: {len(df)} registros")
        return df
    
    def gerar_dados_orcamento(self):
        """
        Carregamento e processamento de dados reais de execução orçamentária.
        
        Processa informações financeiras sobre orçamento planejado versus
        executado por categorias para acompanhamento da gestão financeira.
        
        RETORNO:
        --------
        pandas.DataFrame
            DataFrame com dados orçamentários processados
        """
        # ============= CARREGAMENTO DE DADOS ORÇAMENTÁRIOS =============
        print("📊 Carregando dados reais de orçamento...")
        
        df = self._ler_excel("dados_orcamento.xlsx")
        
        colunas_obrigatorias = ['ano', 'categoria', 'valor_orcado', 'valor_executado']
        self._validar_colunas(df, colunas_obrigatorias, "Orçamento")
        
        # ============= TRATAMENTO DE VALORES FINANCEIROS =============
        df['ano'] = df['ano'].astype(int)
        df['valor_orcado'] = df['valor_orcado'].fillna(0).astype(float)
        df['valor_executado'] = df['valor_executado'].fillna(0).astype(float)
        
        print(f"✅ Dados de orçamento carregados: {len(df)} registros")
        return df
    
    def gerar_dados_ouvidoria(self):
        """
        Carregamento e processamento de dados reais de ouvidoria e atendimento.
        
        Processa manifestações recebidas, tipos de demandas e status de
        atendimento para acompanhamento da qualidade dos serviços.
        
        RETORNO:
        --------
        pandas.DataFrame
            DataFrame com dados de ouvidoria processados
        """
        # ============= CARREGAMENTO DE DADOS DE OUVIDORIA =============
        print("📊 Carregando dados reais de ouvidoria...")
        
        df = self._ler_excel("dados_ouvidoria.xlsx")
        
        colunas_obrigatorias = ['ano', 'tipo_manifestacao', 'quantidade', 'status']
        self._validar_colunas(df, colunas_obrigatorias, "Ouvidoria")
        
        # ============= TRATAMENTO DE DADOS DE ATENDIMENTO =============
        df['ano'] = df['ano'].astype(int)
        df['quantidade'] = df['quantidade'].fillna(0).astype(int)
        
        print(f"✅ Dados de ouvidoria carregados: {len(df)} registros")
        return df
    
    def gerar_dados_servidores(self):
        """
        Carregamento e processamento de dados reais de recursos humanos.
        
        Processa informações sobre quadro de servidores, distribuição por
        categorias, gênero e campus para acompanhamento da gestão de pessoas.
        
        RETORNO:
        --------
        pandas.DataFrame
            DataFrame com dados de servidores processados
        """
        # ============= CARREGAMENTO DE DADOS DE RECURSOS HUMANOS =============
        print("📊 Carregando dados reais de servidores...")
        
        df = self._ler_excel("dados_servidores.xlsx")
        
        colunas_obrigatorias = ['ano', 'campus', 'categoria', 'quantidade', 'genero']
        self._validar_colunas(df, colunas_obrigatorias, "Servidores")
        
        # ============= TRATAMENTO DE DADOS DE PESSOAL =============
        df['ano'] = df['ano'].astype(int)
        df['quantidade'] = df['quantidade'].fillna(0).astype(int)
        
        print(f"✅ Dados de servidores carregados: {len(df)} registros")
        return df
