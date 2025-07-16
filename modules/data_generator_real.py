import pandas as pd
import numpy as np
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class DataGeneratorReal:
    """
    Gerador de dados que lê planilhas Excel com dados reais
    
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
    """
    
    def __init__(self):
        self.dados_directory = "dados"
        self.data_atualizacao = datetime.now().strftime("%d/%m/%Y às %H:%M")
        
        # Verificar se o diretório existe
        if not os.path.exists(self.dados_directory):
            raise FileNotFoundError(f"Diretório '{self.dados_directory}' não encontrado!")
    
    def _verificar_arquivo(self, nome_arquivo):
        """Verifica se o arquivo existe"""
        caminho = os.path.join(self.dados_directory, nome_arquivo)
        if not os.path.exists(caminho):
            raise FileNotFoundError(f"Arquivo '{nome_arquivo}' não encontrado em '{self.dados_directory}'!")
        return caminho
    
    def _ler_excel(self, nome_arquivo, sheet_name=0):
        """Lê arquivo Excel e retorna DataFrame"""
        try:
            caminho = self._verificar_arquivo(nome_arquivo)
            df = pd.read_excel(caminho, sheet_name=sheet_name)
            print(f"✅ Arquivo '{nome_arquivo}' carregado com sucesso: {len(df)} registros")
            return df
        except Exception as e:
            print(f"❌ Erro ao carregar '{nome_arquivo}': {str(e)}")
            raise
    
    def _validar_colunas(self, df, colunas_obrigatorias, nome_modulo):
        """Valida se as colunas obrigatórias existem no DataFrame"""
        colunas_faltantes = [col for col in colunas_obrigatorias if col not in df.columns]
        if colunas_faltantes:
            raise ValueError(f"❌ Colunas faltantes em {nome_modulo}: {colunas_faltantes}")
        print(f"✅ Validação de colunas do módulo {nome_modulo}: OK")
    
    def gerar_dados_extensao(self):
        """
        Carrega dados reais de extensão
        
        ESTRUTURA ESPERADA DA PLANILHA dados_extensao.xlsx:
        - ano: int (ex: 2023, 2024, 2025)
        - unidade: str (ex: "IFPB - Campus Campina Grande")
        - curso: str (ex: "Técnico em Informática")
        - modalidade: str (ex: "Presencial", "EAD")
        - genero: str (ex: "Masculino", "Feminino", "Outro")
        - estagios_concluidos: int (número de estágios concluídos)
        - pne_ingressantes: int (número de ingressantes PNE)
        - tipo_necessidade: str (ex: "Física", "Visual", "Auditiva", "Intelectual")
        """
        print("📊 Carregando dados reais de extensão...")
        
        # Carregar dados do Excel
        df = self._ler_excel("dados_extensao.xlsx")
        
        # Validar colunas obrigatórias
        colunas_obrigatorias = [
            'ano', 'unidade', 'curso', 'modalidade', 'genero',
            'estagios_concluidos', 'pne_ingressantes', 'tipo_necessidade'
        ]
        self._validar_colunas(df, colunas_obrigatorias, "Extensão")
        
        # Validações adicionais
        if df['ano'].isna().any():
            raise ValueError("❌ Coluna 'ano' não pode ter valores vazios")
        
        if df['estagios_concluidos'].isna().any():
            df['estagios_concluidos'] = df['estagios_concluidos'].fillna(0)
        
        if df['pne_ingressantes'].isna().any():
            df['pne_ingressantes'] = df['pne_ingressantes'].fillna(0)
        
        # Converter tipos de dados
        df['ano'] = df['ano'].astype(int)
        df['estagios_concluidos'] = df['estagios_concluidos'].astype(int)
        df['pne_ingressantes'] = df['pne_ingressantes'].astype(int)
        
        print(f"✅ Dados de extensão carregados: {len(df)} registros de {df['ano'].min()} a {df['ano'].max()}")
        return df
    
    def gerar_dados_ensino(self):
        """
        Carrega dados reais de ensino
        
        ESTRUTURA ESPERADA DA PLANILHA dados_ensino.xlsx:
        - ano: int
        - campus: str
        - curso: str
        - modalidade: str
        - matriculados: int
        - formados: int
        - desistentes: int
        - transferidos: int
        """
        print("📊 Carregando dados reais de ensino...")
        
        df = self._ler_excel("dados_ensino.xlsx")
        
        colunas_obrigatorias = [
            'ano', 'campus', 'curso', 'modalidade',
            'matriculados', 'formados', 'desistentes', 'transferidos'
        ]
        self._validar_colunas(df, colunas_obrigatorias, "Ensino")
        
        # Preencher valores NaN com 0 para colunas numéricas
        colunas_numericas = ['matriculados', 'formados', 'desistentes', 'transferidos']
        for col in colunas_numericas:
            df[col] = df[col].fillna(0).astype(int)
        
        df['ano'] = df['ano'].astype(int)
        
        print(f"✅ Dados de ensino carregados: {len(df)} registros")
        return df
    
    def gerar_dados_pesquisa(self):
        """
        Carrega dados reais de pesquisa
        
        ESTRUTURA ESPERADA DA PLANILHA dados_pesquisa.xlsx:
        - ano: int
        - tipo_publicacao: str (ex: "Artigos", "Capítulos de Livros", "Trabalhos em Eventos")
        - quantidade: int
        - area_conhecimento: str
        - servidor: str (opcional)
        """
        print("📊 Carregando dados reais de pesquisa...")
        
        df = self._ler_excel("dados_pesquisa.xlsx")
        
        colunas_obrigatorias = ['ano', 'tipo_publicacao', 'quantidade', 'area_conhecimento']
        self._validar_colunas(df, colunas_obrigatorias, "Pesquisa")
        
        df['ano'] = df['ano'].astype(int)
        df['quantidade'] = df['quantidade'].fillna(0).astype(int)
        
        print(f"✅ Dados de pesquisa carregados: {len(df)} registros")
        return df
    
    def gerar_dados_assistencia(self):
        """Carrega dados reais de assistência estudantil"""
        print("📊 Carregando dados reais de assistência estudantil...")
        
        df = self._ler_excel("dados_assistencia.xlsx")
        
        colunas_obrigatorias = ['ano', 'campus', 'auxilio_tipo', 'beneficiarios', 'valor_total']
        self._validar_colunas(df, colunas_obrigatorias, "Assistência")
        
        df['ano'] = df['ano'].astype(int)
        df['beneficiarios'] = df['beneficiarios'].fillna(0).astype(int)
        df['valor_total'] = df['valor_total'].fillna(0).astype(float)
        
        print(f"✅ Dados de assistência carregados: {len(df)} registros")
        return df
    
    def gerar_dados_auditoria(self):
        """Carrega dados reais de auditoria"""
        print("📊 Carregando dados reais de auditoria...")
        
        df = self._ler_excel("dados_auditoria.xlsx")
        
        colunas_obrigatorias = ['ano', 'tipo_auditoria', 'numero_auditorias', 'recomendacoes']
        self._validar_colunas(df, colunas_obrigatorias, "Auditoria")
        
        df['ano'] = df['ano'].astype(int)
        df['numero_auditorias'] = df['numero_auditorias'].fillna(0).astype(int)
        df['recomendacoes'] = df['recomendacoes'].fillna(0).astype(int)
        
        print(f"✅ Dados de auditoria carregados: {len(df)} registros")
        return df
    
    def gerar_dados_mundo_trabalho(self):
        """Carrega dados reais de mundo do trabalho"""
        print("📊 Carregando dados reais de mundo do trabalho...")
        
        df = self._ler_excel("dados_mundo_trabalho.xlsx")
        
        colunas_obrigatorias = ['ano', 'campus', 'curso', 'empregabilidade', 'salario_medio']
        self._validar_colunas(df, colunas_obrigatorias, "Mundo do Trabalho")
        
        df['ano'] = df['ano'].astype(int)
        df['empregabilidade'] = df['empregabilidade'].fillna(0).astype(float)
        df['salario_medio'] = df['salario_medio'].fillna(0).astype(float)
        
        print(f"✅ Dados de mundo do trabalho carregados: {len(df)} registros")
        return df
    
    def gerar_dados_orcamento(self):
        """Carrega dados reais de orçamento"""
        print("📊 Carregando dados reais de orçamento...")
        
        df = self._ler_excel("dados_orcamento.xlsx")
        
        colunas_obrigatorias = ['ano', 'categoria', 'valor_orcado', 'valor_executado']
        self._validar_colunas(df, colunas_obrigatorias, "Orçamento")
        
        df['ano'] = df['ano'].astype(int)
        df['valor_orcado'] = df['valor_orcado'].fillna(0).astype(float)
        df['valor_executado'] = df['valor_executado'].fillna(0).astype(float)
        
        print(f"✅ Dados de orçamento carregados: {len(df)} registros")
        return df
    
    def gerar_dados_ouvidoria(self):
        """Carrega dados reais de ouvidoria"""
        print("📊 Carregando dados reais de ouvidoria...")
        
        df = self._ler_excel("dados_ouvidoria.xlsx")
        
        colunas_obrigatorias = ['ano', 'tipo_manifestacao', 'quantidade', 'status']
        self._validar_colunas(df, colunas_obrigatorias, "Ouvidoria")
        
        df['ano'] = df['ano'].astype(int)
        df['quantidade'] = df['quantidade'].fillna(0).astype(int)
        
        print(f"✅ Dados de ouvidoria carregados: {len(df)} registros")
        return df
    
    def gerar_dados_servidores(self):
        """Carrega dados reais de servidores"""
        print("📊 Carregando dados reais de servidores...")
        
        df = self._ler_excel("dados_servidores.xlsx")
        
        colunas_obrigatorias = ['ano', 'campus', 'categoria', 'quantidade', 'genero']
        self._validar_colunas(df, colunas_obrigatorias, "Servidores")
        
        df['ano'] = df['ano'].astype(int)
        df['quantidade'] = df['quantidade'].fillna(0).astype(int)
        
        print(f"✅ Dados de servidores carregados: {len(df)} registros")
        return df
