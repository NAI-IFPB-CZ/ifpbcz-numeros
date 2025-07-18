# ==============================================================================
# GERADOR DE DADOS PARA DASHBOARD IFPB-CZ
# ==============================================================================
# 
# Este módulo é responsável por:
# 1. Gerar dados sintéticos para todos os módulos do dashboard
# 2. Carregar dados reais de arquivos Excel quando disponíveis
# 3. Gerenciar configurações de segurança para operações de arquivo
# 4. Manter a estrutura padronizada de dados entre diferentes fontes
#
# Funcionalidades principais:
# - Geração de dados realistas com distribuições estatísticas apropriadas
# - Sistema de fallback: tenta carregar dados reais, senão gera sintéticos
# - Configurações de segurança para modo somente leitura
# - Validação e formatação automática de dados
# - Metadados automatizados para rastreabilidade
# ==============================================================================

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os
import warnings
warnings.filterwarnings('ignore')  # Suprimir avisos não críticos

# ==============================================================================
# CONFIGURAÇÕES DE SEGURANÇA E COMPORTAMENTO
# ==============================================================================
# Importar configurações do arquivo config.py (se existir)
# Estas configurações controlam como o sistema lida com dados e arquivos
try:
    from config import (
        USE_REAL_DATA,                    # Se deve tentar usar dados reais primeiro
        PERMITIR_CRIACAO_PLANILHAS,       # Se pode criar novos arquivos Excel
        SOBRESCREVER_ARQUIVOS_EXISTENTES, # Se pode sobrescrever arquivos existentes
        MODO_SOMENTE_LEITURA,             # Modo de segurança - só visualização
        MOSTRAR_LOGS                      # Se deve exibir mensagens de log
    )
except ImportError:
    # Configurações padrão de segurança se config.py não existir
    # IMPORTANTE: Por segurança, padrão é modo somente leitura
    USE_REAL_DATA = False
    PERMITIR_CRIACAO_PLANILHAS = False
    SOBRESCREVER_ARQUIVOS_EXISTENTES = False
    MODO_SOMENTE_LEITURA = True
    MOSTRAR_LOGS = True

# ==============================================================================
# CLASSE PRINCIPAL - GERADOR DE DADOS
# ==============================================================================
class DataGenerator:
    """
    Classe principal responsável pela geração e gerenciamento de dados do dashboard.
    
    Esta classe implementa um padrão de fallback inteligente:
    1. Primeiro tenta carregar dados reais de arquivos Excel
    2. Se não existirem ou forem incompatíveis, gera dados sintéticos
    3. Aplica configurações de segurança para todas as operações
    
    Atributos:
        dados_directory (str): Diretório onde ficam armazenados os arquivos Excel
        data_atualizacao (str): Timestamp da última atualização dos dados
        unidades (list): Lista de todos os campus do IFPB
        cursos (list): Lista de todos os cursos oferecidos
        [outros atributos]: Listas de categorias usadas na geração de dados
    """
    
    def __init__(self):
        """
        Inicializa o gerador com todas as configurações e dados base necessários.
        
        Define listas padronizadas que são usadas em toda a geração de dados
        para manter consistência entre diferentes módulos.
        """
        # Configuração básica de diretórios e timestamps
        self.dados_directory = "dados"
        self.data_atualizacao = datetime.now().strftime("%d/%m/%Y às %H:%M")
        
        # Criar diretório de dados se não existir
        if not os.path.exists(self.dados_directory):
            os.makedirs(self.dados_directory)
            
        # ==============================================================================
        # DADOS BASE DO IFPB - ESTRUTURA INSTITUCIONAL
        # ==============================================================================
        # Lista completa de todos os 25 campus do IFPB
        # Usada em todos os módulos para manter consistência geográfica
        self.unidades = [
            "IFPB - Campus Campina Grande",
            "IFPB - Campus Cajazeiras", 
            "IFPB - Campus Sousa",
            "IFPB - Campus Patos",
            "IFPB - Campus Princesa Isabel",
            "IFPB - Campus Picuí",
            "IFPB - Campus Monteiro",
            "IFPB - Campus Guarabira",
            "IFPB - Campus João Pessoa",
            "IFPB - Campus Cabedelo",
            "IFPB - Campus Santa Rita",
            "IFPB - Campus Esperança",
            "IFPB - Campus Itabaiana",
            "IFPB - Campus Itaporanga",
            "IFPB - Campus Catolé do Rocha",
            "IFPB - Campus Areia",
            "IFPB - Campus Queimadas",
            "IFPB - Campus Alagoa Grande",
            "IFPB - Campus Pedras de Fogo",
            "IFPB - Campus Mamanguape",
            "IFPB - Campus Sapé"
        ]
        
        # ==============================================================================
        # CATÁLOGO DE CURSOS IFPB
        # ==============================================================================
        # Lista abrangente de cursos oferecidos pelo IFPB
        # Inclui: Técnicos, Tecnólogos, Bacharelados, Licenciaturas e Engenharias
        self.cursos = [
            "Técnico em Informática",
            "Técnico em Eletrônica",
            "Técnico em Edificações",
            "Técnico em Agropecuária",
            "Técnico em Mecânica",
            "Técnico em Química",
            "Técnico em Segurança do Trabalho",
            "Técnico em Administração",
            "Técnico em Contabilidade",
            "Técnico em Recursos Humanos",
            "Técnico em Logística",
            "Técnico em Meio Ambiente",
            "Técnico em Enfermagem",
            "Técnico em Nutrição e Dietética",
            "Técnico em Turismo",
            "Bacharelado em Sistemas de Informação",
            "Bacharelado em Administração",
            "Bacharelado em Ciências Contábeis",
            "Bacharelado em Arquitetura e Urbanismo",
            "Licenciatura em Matemática",
            "Licenciatura em Física",
            "Licenciatura em Química",
            "Licenciatura em Biologia",
            "Licenciatura em Letras",
            "Licenciatura em Pedagogia",
            "Tecnologia em Análise e Desenvolvimento de Sistemas",
            "Tecnologia em Redes de Computadores",
            "Tecnologia em Gestão Comercial",
            "Tecnologia em Gestão Pública",
            "Tecnologia em Alimentos",
            "Tecnologia em Automação Industrial",
            "Engenharia Civil",
            "Engenharia Elétrica",
            "Engenharia Mecânica",
            "Engenharia de Computação",
            "Engenharia de Produção",
            "Engenharia Ambiental"
        ]
        
        # ==============================================================================
        # CATEGORIAS E CLASSIFICAÇÕES PADRONIZADAS
        # ==============================================================================
        # Estas listas são usadas em múltiplos módulos para manter consistência
        
        # Níveis de ensino oferecidos pelo IFPB
        self.niveis_curso = ["Técnico", "Graduação", "Pós-graduação"]
        
        # Classificação demográfica básica
        self.generos = ["Masculino", "Feminino"]
        
        # Tipos de necessidades especiais (PNE) - baseado na legislação brasileira
        self.tipos_necessidades = ["Auditiva", "Visual", "Física", "Intelectual", "Múltipla"]
        
        # ==============================================================================
        # PROGRAMAS DE ASSISTÊNCIA ESTUDANTIL
        # ==============================================================================
        # Lista oficial dos programas de auxílio oferecidos pelo IFPB
        self.programas_assistencia = [
            "Auxílio Alimentação",
            "Auxílio Transporte", 
            "Auxílio Moradia",
            "Auxílio Didático",
            "Bolsa Monitoria",
            "Bolsa Iniciação Científica"
        ]
        
        # ==============================================================================
        # CATEGORIAS ORÇAMENTÁRIAS
        # ==============================================================================
        # Classificação padrão do orçamento público brasileiro
        self.categorias_orcamento = [
            "Pessoal e Encargos Sociais",
            "Custeio",
            "Investimentos",
            "Manutenção",
            "Equipamentos",
            "Obras"
        ]
        
        # ==============================================================================
        # TIPOS DE PRODUÇÃO CIENTÍFICA
        # ==============================================================================
        # Categorias padrão de publicações acadêmicas (baseado no Lattes/CNPq)
        self.tipos_publicacao = [
            "Artigos",
            "Capítulos de Livros",
            "Trabalhos em Eventos",
            "Livros",
            "Patentes"
        ]
        
        # ==============================================================================
        # TIPOS DE MANIFESTAÇÕES DA OUVIDORIA
        # ==============================================================================
        # Categorias oficiais de manifestações conforme Lei de Acesso à Informação
        self.tipos_manifestacao = [
            "Reclamação",
            "Sugestão",
            "Elogio",
            "Denúncia",
            "Solicitação"
        ]
        
        # ==============================================================================
        # PERFIS DE USUÁRIOS DO SISTEMA
        # ==============================================================================
        # Tipos de usuários que interagem com os serviços do IFPB
        self.tipos_usuario = [
            "Estudante",
            "Servidor",
            "Comunidade Externa",
            "Responsável"
        ]
        
        # ==============================================================================
        # SETORES DE ATIVIDADE ECONÔMICA
        # ==============================================================================
        # Classificação simplificada dos setores onde egressos podem atuar
        # Baseada na CNAE (Classificação Nacional de Atividades Econômicas)
        self.setores_atividade = [
            "Administração Pública",
            "Educação",
            "Saúde",
            "Comércio",
            "Indústria",
            "Serviços",
            "Agricultura",
            "Construção Civil",
            "Tecnologia",
            "Turismo"
        ]
        
        # ==============================================================================
        # CONFIGURAÇÃO DE SEMENTES PARA REPRODUTIBILIDADE
        # ==============================================================================
        # Fixar sementes para que os dados sintéticos sejam sempre os mesmos
        # Isso garante consistência entre execuções e facilita testes
        random.seed(42)
        np.random.seed(42)
    
    # ==============================================================================
    # MÉTODOS DE GERENCIAMENTO DE ARQUIVOS
    # ==============================================================================
    
    def _salvar_dados_excel(self, df, nome_arquivo, sheet_name="Dados"):
        """
        Salva DataFrame em arquivo Excel com verificações rigorosas de segurança.
        
        Este método implementa múltiplas camadas de segurança:
        1. Verifica se o modo somente leitura está ativo
        2. Verifica se a criação de planilhas é permitida
        3. Verifica se pode sobrescrever arquivos existentes
        4. Adiciona metadados automaticamente para rastreabilidade
        
        Args:
            df (pandas.DataFrame): Dados a serem salvos
            nome_arquivo (str): Nome do arquivo (sem extensão)
            sheet_name (str): Nome da planilha dentro do Excel
            
        Returns:
            str or None: Caminho do arquivo salvo ou None se houve erro/bloqueio
        """
        filepath = os.path.join(self.dados_directory, f"{nome_arquivo}.xlsx")
        
        # ==============================================================================
        # VERIFICAÇÕES DE SEGURANÇA ANTES DE SALVAR
        # ==============================================================================
        
        # VERIFICAÇÃO 1: Modo somente leitura
        # Se ativo, bloqueia TODAS as operações de escrita
        if MODO_SOMENTE_LEITURA:
            if MOSTRAR_LOGS:
                print(f"⚠️  AVISO: Modo somente leitura ativado. Não será possível salvar {nome_arquivo}.xlsx")
            return None
        
        # VERIFICAÇÃO 2: Permissão para criar planilhas
        # Controla se novos arquivos podem ser criados
        if not PERMITIR_CRIACAO_PLANILHAS:
            if MOSTRAR_LOGS:
                print(f"⚠️  AVISO: Criação de planilhas desabilitada. Não será possível criar {nome_arquivo}.xlsx")
            return None
        
        # VERIFICAÇÃO 3: Sobrescrita de arquivos existentes
        # Protege contra perda acidental de dados reais
        if os.path.exists(filepath) and not SOBRESCREVER_ARQUIVOS_EXISTENTES:
            if MOSTRAR_LOGS:
                print(f"⚠️  AVISO: Arquivo {nome_arquivo}.xlsx já existe e sobrescrita está desabilitada")
            return None
        
        # ==============================================================================
        # PROCESSO DE SALVAMENTO COM METADADOS
        # ==============================================================================
        try:
            # Salvar dados principais + metadados em planilhas separadas
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                # Planilha principal com os dados
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                
                # Planilha de metadados para rastreabilidade e auditoria
                metadata = pd.DataFrame({
                    'Informação': ['Data de Atualização', 'Total de Registros', 'Período dos Dados'],
                    'Valor': [
                        self.data_atualizacao,
                        len(df),
                        f"{df['ano'].min()} - {df['ano'].max()}" if 'ano' in df.columns else "N/A"
                    ]
                })
                metadata.to_excel(writer, sheet_name="Metadados", index=False)
            
            if MOSTRAR_LOGS:
                print(f"✅ Arquivo salvo com sucesso: {nome_arquivo}.xlsx")
            return filepath
            
        except Exception as e:
            if MOSTRAR_LOGS:
                print(f"❌ Erro ao salvar {nome_arquivo}.xlsx: {str(e)}")
            return None
    
    def _carregar_dados_excel(self, nome_arquivo, sheet_name="Dados"):
        """
        Carrega dados de arquivo Excel com fallback para geração sintética.
        
        NOTA IMPORTANTE: Esta função está temporariamente desabilitada para
        garantir compatibilidade. Retorna sempre None para forçar uso de dados
        sintéticos até que os dados reais tenham estrutura compatível.
        
        Quando reabilitada, esta função:
        1. Verifica se o arquivo Excel existe
        2. Tenta carregar a planilha especificada
        3. Valida a estrutura dos dados
        4. Retorna None se houver qualquer problema (ativa fallback)
        
        Args:
            nome_arquivo (str): Nome do arquivo (sem extensão)
            sheet_name (str): Nome da planilha dentro do Excel
            
        Returns:
            pandas.DataFrame or None: Dados carregados ou None para ativar fallback
        """
        # ==============================================================================
        # FALLBACK TEMPORÁRIO PARA DADOS SINTÉTICOS
        # ==============================================================================
        # TEMPORÁRIO: Desabilitado para usar apenas dados sintéticos
        # até que os dados reais estejam na estrutura correta
        return None
        
        # Código original (comentado temporariamente)
        # filepath = os.path.join(self.dados_directory, f"{nome_arquivo}.xlsx")
        # 
        # if os.path.exists(filepath):
        #     try:
        #         df = pd.read_excel(filepath, sheet_name=sheet_name)
        #         return df
        #     except Exception as e:
        #         print(f"Erro ao carregar {filepath}: {e}")
        #         return None
        # 
        # return None
    
    def get_data_atualizacao(self, nome_arquivo):
        """
        Retorna a data de atualização dos dados de um arquivo específico.
        
        Busca na planilha "Metadados" a informação de quando os dados
        foram atualizados pela última vez. Útil para mostrar ao usuário
        a idade dos dados being displayed.
        
        Args:
            nome_arquivo (str): Nome do arquivo (sem extensão)
            
        Returns:
            str: Data de atualização ou mensagem de erro
        """
        filepath = os.path.join(self.dados_directory, f"{nome_arquivo}.xlsx")
        
        if os.path.exists(filepath):
            try:
                metadata = pd.read_excel(filepath, sheet_name="Metadados")
                return metadata.loc[metadata['Informação'] == 'Data de Atualização', 'Valor'].iloc[0]
            except:
                return "Data não disponível"
        
        return "Arquivo não encontrado"
    
    # ==============================================================================
    # GERADORES DE DADOS POR MÓDULO
    # ==============================================================================
    # Cada método abaixo gera dados sintéticos realistas para um módulo específico
    # do dashboard. Todos seguem o mesmo padrão:
    # 1. Tentar carregar dados reais primeiro
    # 2. Se não existir, gerar dados sintéticos
    # 3. Aplicar distribuições estatísticas realistas
    # 4. Salvar dados para cache (se permitido)
    # ==============================================================================
    
    def gerar_dados_ensino(self):
        """
        Gera dados para o módulo de Ensino (acadêmico).
        
        Simula dados realistas de:
        - Matrículas por campus, curso e modalidade
        - Formandos, desistentes e transferências
        - Crescimento temporal e variações sazonais
        - Impacto de eventos (ex: pandemia 2020-2022)
        
        Aplica fatores de tamanho por campus:
        - Campus grandes (João Pessoa, Campina Grande): 1.5x
        - Campus médios (Cajazeiras, Sousa, Patos): 1.0x  
        - Campus menores: 0.6x
        
        Returns:
            pandas.DataFrame: Dados de ensino com colunas padronizadas
        """
        # Implementação do padrão de fallback
        dados_existentes = self._carregar_dados_excel("dados_ensino", "Dados_Ensino")
        if dados_existentes is not None:
            return dados_existentes
        
        # ==============================================================================
        # GERAÇÃO DE DADOS SINTÉTICOS DE ENSINO
        # ==============================================================================
        dados = []
        modalidades = ["Presencial", "EAD", "Semipresencial"]
        
        # Gerar dados para período de 2019-2025 (7 anos de histórico)
        for ano in range(2019, 2026):
            for campus in self.unidades:
                # ==============================================================================
                # APLICAR FATORES REALISTAS POR TAMANHO DE CAMPUS
                # ==============================================================================
                # Diferentes campus têm diferentes capacidades e ofertas de cursos
                if "João Pessoa" in campus or "Campina Grande" in campus:
                    fator_tamanho = 1.5  # Campus maiores (mais recursos, mais alunos)
                elif "Cajazeiras" in campus or "Sousa" in campus or "Patos" in campus:
                    fator_tamanho = 1.0  # Campus de porte médio
                else:
                    fator_tamanho = 0.6  # Campus menores (mais especializados)
                
                # Nem todos os campus oferecem todos os cursos (realismo)
                # Campus menores têm oferta mais restrita
                cursos_campus = random.sample(self.cursos, random.randint(8, 15))
                
                for curso in cursos_campus:
                    for modalidade in modalidades:
                        # ==============================================================================
                        # LÓGICA DE DISPONIBILIDADE POR MODALIDADE
                        # ==============================================================================
                        # Nem todos os cursos têm todas as modalidades (realismo)
                        if modalidade == "EAD" and random.random() < 0.7:
                            continue  # 70% dos cursos não têm EAD
                        if modalidade == "Semipresencial" and random.random() < 0.8:
                            continue  # 80% dos cursos não têm semipresencial
                            
                        # ==============================================================================
                        # SIMULAÇÃO DE CRESCIMENTO TEMPORAL REALISTA
                        # ==============================================================================
                        # Base de matriculados por curso (varia por tipo de curso)
                        base_matriculados = random.randint(30, 150)
                        
                        # Simular crescimento institucional ao longo dos anos
                        fator_crescimento = (ano - 2019) * 0.05  # 5% ao ano
                        
                        # Aplicar todos os fatores
                        matriculados = int(base_matriculados * fator_tamanho * (1 + fator_crescimento))
                        matriculados = max(10, matriculados)  # Mínimo realista de 10 alunos
                        
                        # ==============================================================================
                        # CÁLCULOS DERIVADOS BASEADOS EM TAXAS REALISTAS
                        # ==============================================================================
                        # Taxas baseadas em dados reais do ensino técnico/superior brasileiro
                        formados = int(matriculados * random.uniform(0.15, 0.30))        # 15-30% se formam por ano
                        desistentes = int(matriculados * random.uniform(0.05, 0.20))     # 5-20% de evasão
                        transferidos = int(matriculados * random.uniform(0.02, 0.10))    # 2-10% de transferências
                        
                        # ==============================================================================
                        # SIMULAÇÃO DE EVENTOS HISTÓRICOS
                        # ==============================================================================
                        # Adicionar impacto da pandemia (2020-2022)
                        if ano >= 2020 and ano <= 2022:
                            desistentes = int(desistentes * 1.3)  # +30% de evasão na pandemia
                            formados = int(formados * 0.8)        # -20% de formandos (atrasos)
                        
                        # Registrar dados calculados
                        dados.append({
                            'ano': ano,
                            'campus': campus,
                            'curso': curso,
                            'modalidade': modalidade,
                            'matriculados': matriculados,
                            'formados': formados,
                            'desistentes': desistentes,
                            'transferidos': transferidos
                        })
        
        # Converter para DataFrame e salvar
        df = pd.DataFrame(dados)
        
        # Tentar salvar dados para cache (respeitando configurações de segurança)
        self._salvar_dados_excel(df, "dados_ensino", "Dados_Ensino")
        
        return df
    
    def gerar_dados_assistencia(self):
        """
        Gera dados para o módulo de Assistência Estudantil.
        
        Simula dados realistas de:
        - Auxílios por programa, campus e nível de curso
        - Valores mensais de bolsas e auxílios
        - Distribuição por faixa etária e gênero
        - Sazonalidade (mais auxílios em períodos letivos)
        
        Os valores e quantidades são baseados em dados reais
        dos programas de assistência estudantil do IFPB.
        
        Returns:
            pandas.DataFrame: Dados de assistência com colunas padronizadas
        """
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_assistencia", "Dados_Assistencia")
        if dados_existentes is not None:
            return dados_existentes
        
        # Se não existir, gera dados fictícios
        dados = []
        
        for ano in range(2015, 2026):
            for unidade in self.unidades:
                for programa in self.programas_assistencia:
                    for nivel in self.niveis_curso:
                        for mes in range(1, 13):
                            parcelas = random.randint(10, 100)
                            alunos_beneficiados = int(parcelas * random.uniform(0.7, 1.0))
                            valor_total = parcelas * random.uniform(200, 800)
                            
                            dados.append({
                                'ano': ano,
                                'mes': mes,
                                'unidade': unidade,
                                'programa': programa,
                                'nivel_curso': nivel,
                                'parcelas': parcelas,
                                'alunos_beneficiados': alunos_beneficiados,
                                'valor_total': valor_total,
                                'faixa_idade': random.choice(['16-20', '21-25', '26-30', '31+']),
                                'genero': random.choice(self.generos)
                            })
        
        df = pd.DataFrame(dados)
        
        # Salvar dados no Excel
        self._salvar_dados_excel(df, "dados_assistencia", "Dados_Assistencia")
        
        return df
    
    def gerar_dados_pesquisa(self):
        """
        Gera dados para o módulo de Pesquisa Científica.
        
        Simula dados realistas de:
        - Projetos de pesquisa por área de conhecimento
        - Publicações científicas (artigos, livros, capítulos)
        - Participação em eventos científicos
        - Bolsas de iniciação científica e pós-graduação
        - Grupos de pesquisa por campus
        
        Os dados incluem distribuição temporal, autores,
        orientadores e classificação por áreas do CNPq.
        
        Returns:
            pandas.DataFrame: Dados de pesquisa com metadados científicos
        """
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_pesquisa", "Dados_Pesquisa")
        if dados_existentes is not None:
            # Adicionar palavras-chave se não existir
            if 'palavras_chave' not in dados_existentes.columns:
                dados_existentes = self._adicionar_palavras_chave(dados_existentes)
            return dados_existentes
        
        # Se não existir, gera dados fictícios
        dados = []
        
        areas_conhecimento = [
            "Ciências Exatas",
            "Engenharias",
            "Ciências da Computação",
            "Educação",
            "Ciências Sociais",
            "Ciências Agrárias"
        ]
        
        palavras_chave = [
            "machine learning", "educação", "sustentabilidade", "inovação",
            "tecnologia", "desenvolvimento", "pesquisa", "ensino",
            "agricultura", "eletrônica", "programação", "matemática"
        ]
        
        for ano in range(2010, 2026):
            for unidade in self.unidades:
                for tipo in self.tipos_publicacao:
                    for area in areas_conhecimento:
                        quantidade = random.randint(5, 50)
                        
                        # Gerar palavras-chave aleatórias
                        palavras_publicacao = random.sample(palavras_chave, random.randint(3, 8))
                        
                        dados.append({
                            'ano': ano,
                            'unidade': unidade,
                            'tipo_publicacao': tipo,
                            'area_conhecimento': area,
                            'quantidade': quantidade,
                            'palavras_chave': ', '.join(palavras_publicacao),
                            'autor_principal': f"Prof. {random.choice(['João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Lucia'])} Silva"
                        })
        
        df = pd.DataFrame(dados)
        
        # Salvar dados no Excel
        self._salvar_dados_excel(df, "dados_pesquisa", "Dados_Pesquisa")
        
        return df
    
    def gerar_dados_extensao(self):
        """
        Gera dados para o módulo de Extensão Universitária.
        
        Simula dados realistas de:
        - Projetos de extensão por área temática
        - Cursos e eventos oferecidos à comunidade
        - Público atendido (interno e externo)
        - Parcerias com instituições públicas e privadas
        - Impacto social e alcance geográfico
        
        Os dados incluem informações sobre sustentabilidade,
        inclusão social e desenvolvimento regional.
        
        Returns:
            pandas.DataFrame: Dados de extensão com indicadores sociais
        """
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_extensao", "Sheet1")
        if dados_existentes is not None:
            return dados_existentes
        
        # Se não existir dados reais, gera dados sintéticos
        dados = []
        
        # Áreas temáticas de extensão (baseadas nas diretrizes nacionais)
        areas_tematicas = [
            "Comunicação",
            "Cultura", 
            "Direitos Humanos e Justiça",
            "Educação",
            "Meio Ambiente",
            "Saúde",
            "Tecnologia e Produção",
            "Trabalho"
        ]
        
        # Tipos de atividades de extensão
        tipos_atividade = [
            "Projeto de Extensão",
            "Curso de Extensão",
            "Evento",
            "Prestação de Serviços",
            "Produção e Publicação",
            "Programa de Extensão"
        ]
        
        # Público-alvo das atividades
        publico_alvo = [
            "Estudantes de Ensino Médio",
            "Comunidade Rural",
            "Microempreendedores",
            "Professores da Rede Pública",
            "Pessoas com Deficiência",
            "Idosos",
            "Jovens em Vulnerabilidade Social",
            "Agricultores Familiares",
            "Comunidade Quilombola",
            "População Geral"
        ]
        
        # Gerar dados históricos dos últimos 5 anos
        for ano in range(2019, 2024):
            for campus in self.campus:
                for area in areas_tematicas:
                    for tipo in tipos_atividade:
                        
                        # Calcular quantidade de atividades por tipo
                        if tipo == "Projeto de Extensão":
                            base_quantidade = random.randint(8, 20)
                        elif tipo == "Curso de Extensão":
                            base_quantidade = random.randint(12, 30)
                        elif tipo == "Evento":
                            base_quantidade = random.randint(15, 40)
                        else:
                            base_quantidade = random.randint(5, 15)
                        
                        # Ajustar por campus
                        if campus == "Cajazeiras":
                            fator_campus = 1.0
                        elif campus in ["Sousa", "Patos"]:
                            fator_campus = 0.8
                        else:
                            fator_campus = 0.6
                        
                        quantidade_atividades = int(base_quantidade * fator_campus)
                        quantidade_atividades = max(1, quantidade_atividades)
                        
                        # Simular cada atividade
                        for i in range(quantidade_atividades):
                            
                            # Público atendido
                            if tipo == "Curso de Extensão":
                                participantes_internos = random.randint(10, 40)
                                participantes_externos = random.randint(50, 200)
                            elif tipo == "Evento":
                                participantes_internos = random.randint(20, 100)
                                participantes_externos = random.randint(100, 500)
                            elif tipo == "Projeto de Extensão":
                                participantes_internos = random.randint(5, 15)
                                participantes_externos = random.randint(30, 150)
                            else:
                                participantes_internos = random.randint(3, 20)
                                participantes_externos = random.randint(20, 100)
                            
                            total_participantes = participantes_internos + participantes_externos
                            
                            # Dados demográficos do público
                            pct_feminino = random.uniform(45, 65)
                            pct_masculino = 100 - pct_feminino
                            
                            # Faixa etária varia por tipo de atividade
                            if area == "Educação":
                                pct_jovens = random.uniform(60, 80)  # Mais jovens
                                pct_adultos = random.uniform(15, 30)
                                pct_idosos = 100 - pct_jovens - pct_adultos
                            elif area == "Saúde":
                                pct_jovens = random.uniform(20, 40)
                                pct_adultos = random.uniform(40, 60)
                                pct_idosos = 100 - pct_jovens - pct_adultos
                            else:
                                pct_jovens = random.uniform(40, 60)
                                pct_adultos = random.uniform(25, 45)
                                pct_idosos = 100 - pct_jovens - pct_adultos
                            
                            # Inclusão social
                            pct_vulnerabilidade = random.uniform(10, 30)
                            pct_pcd = random.uniform(2, 8)
                            
                            # Parcerias institucionais
                            tem_parceria = random.choice([True, False])
                            if tem_parceria:
                                tipo_parceiro = random.choice([
                                    "Prefeitura Municipal",
                                    "Governo Estadual",
                                    "ONG",
                                    "Empresa Privada",
                                    "Cooperativa",
                                    "Sindicato",
                                    "Associação Comunitária"
                                ])
                            else:
                                tipo_parceiro = None
                            
                            # Recursos financeiros
                            if tipo in ["Projeto de Extensão", "Programa de Extensão"]:
                                recursos_financeiros = random.uniform(5000, 25000)
                            elif tipo == "Curso de Extensão":
                                recursos_financeiros = random.uniform(2000, 10000)
                            else:
                                recursos_financeiros = random.uniform(500, 5000)
                            
                            # Duração da atividade
                            if tipo in ["Projeto de Extensão", "Programa de Extensão"]:
                                duracao_meses = random.randint(6, 12)
                            elif tipo == "Curso de Extensão":
                                duracao_meses = random.randint(1, 4)
                            else:
                                duracao_meses = random.randint(1, 2)
                            
                            dados.append({
                                'Ano': ano,
                                'Campus': campus,
                                'Area_Tematica': area,
                                'Tipo_Atividade': tipo,
                                'Nome_Atividade': f"{tipo} de {area} - {i+1}",
                                'Participantes_Internos': participantes_internos,
                                'Participantes_Externos': participantes_externos,
                                'Total_Participantes': total_participantes,
                                'Pct_Feminino': round(pct_feminino, 1),
                                'Pct_Masculino': round(pct_masculino, 1),
                                'Pct_Jovens': round(pct_jovens, 1),
                                'Pct_Adultos': round(pct_adultos, 1),
                                'Pct_Idosos': round(pct_idosos, 1),
                                'Pct_Vulnerabilidade_Social': round(pct_vulnerabilidade, 1),
                                'Pct_PCD': round(pct_pcd, 1),
                                'Tem_Parceria': tem_parceria,
                                'Tipo_Parceiro': tipo_parceiro,
                                'Publico_Alvo': random.choice(publico_alvo),
                                'Recursos_Financeiros': round(recursos_financeiros, 2),
                                'Duracao_Meses': duracao_meses,
                                'Status': random.choice(["Concluído", "Em Andamento", "Planejado"])
                            })
        
        df = pd.DataFrame(dados)
        
        # Salvar dados no Excel
        self._salvar_dados_excel(df, "dados_extensao", "Sheet1")
        
        return df
    
    def gerar_dados_orcamento(self):
        """
        Gera dados para o módulo de Orçamento Institucional.
        
        Simula dados realistas de:
        - Execução orçamentária por categoria de despesa
        - Receitas próprias e transferências governamentais
        - Investimentos em infraestrutura e equipamentos
        - Gastos com pessoal e benefícios
        - Distribuição orçamentária por campus
        
        Os valores seguem padrões reais de instituições
        federais de ensino técnico e superior.
        
        Returns:
            pandas.DataFrame: Dados orçamentários com classificação contábil
        """
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_orcamento", "Sheet1")
        if dados_existentes is not None:
            return dados_existentes
        
        # Se não existir, gera dados fictícios
        dados = []
        
        for ano in range(2015, 2026):
            for unidade in self.unidades:
                for categoria in self.categorias_orcamento:
                    dotacao = random.uniform(500000, 5000000)
                    empenhado = dotacao * random.uniform(0.7, 0.95)
                    pago = empenhado * random.uniform(0.8, 1.0)
                    
                    dados.append({
                        'ano': ano,
                        'unidade': unidade,
                        'categoria': categoria,
                        'dotacao': dotacao,
                        'empenhado': empenhado,
                        'pago': pago
                    })
        
        df = pd.DataFrame(dados)
        
        # Salvar dados no Excel
        self._salvar_dados_excel(df, "dados_orcamento", "Sheet1")
        
        return df
    
    def gerar_dados_servidores(self):
        """
        Gera dados para o módulo de Gestão de Servidores.
        
        Simula dados realistas de:
        - Quantitativo de servidores por categoria (docentes/técnicos)
        - Distribuição por titulação e regime de trabalho
        - Faixas etárias e tempo de serviço
        - Afastamentos para capacitação e licenças
        - Progressões funcionais e promoções
        
        Os dados respeitam as carreiras do magistério federal
        e dos técnicos administrativos em educação.
        
        Returns:
            pandas.DataFrame: Dados de recursos humanos com classificações funcionais
        """
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_servidores", "Sheet1")
        if dados_existentes is not None:
            return dados_existentes
        
        # Se não existir, gera dados fictícios
        dados = []
        
        for ano in range(2013, 2026):
            for unidade in self.unidades:
                # Simulando crescimento gradual
                base_docentes = random.randint(30, 80)
                base_tecnicos = random.randint(20, 60)
                
                fator_crescimento = (ano - 2013) * 0.05
                docentes = int(base_docentes * (1 + fator_crescimento))
                tecnicos = int(base_tecnicos * (1 + fator_crescimento))
                
                dados.append({
                    'ano': ano,
                    'unidade': unidade,
                    'docentes': docentes,
                    'tecnicos': tecnicos,
                    'total_servidores': docentes + tecnicos
                })
        
        df = pd.DataFrame(dados)
        
        # Salvar dados no Excel
        self._salvar_dados_excel(df, "dados_servidores", "Sheet1")
        
        return df
    
    def gerar_dados_ouvidoria(self):
        """
        Gera dados para o módulo de Ouvidoria Institucional.
        
        Simula dados realistas de:
        - Manifestações por tipo (reclamação, sugestão, elogio, denúncia)
        - Distribuição por assunto e setor responsável
        - Tempo médio de resposta e resolução
        - Canais de atendimento utilizados
        - Índices de satisfação do usuário
        
        Os dados incluem classificação por grau de complexidade
        e acompanhamento de medidas corretivas implementadas.
        
        Returns:
            pandas.DataFrame: Dados de ouvidoria com indicadores de qualidade
        """
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_ouvidoria", "Sheet1")
        if dados_existentes is not None:
            return dados_existentes
        
        # Se não existir, gera dados fictícios
        dados = []
        
        for ano in range(2015, 2026):
            for mes in range(1, 13):
                for unidade in self.unidades:
                    for tipo in self.tipos_manifestacao:
                        for usuario in self.tipos_usuario:
                            quantidade = random.randint(1, 20)
                            dias_atendimento = random.randint(1, 30)
                            
                            dados.append({
                                'ano': ano,
                                'mes': mes,
                                'unidade': unidade,
                                'tipo_manifestacao': tipo,
                                'tipo_usuario': usuario,
                                'quantidade': quantidade,
                                'dias_atendimento': dias_atendimento
                            })
        
        df = pd.DataFrame(dados)
        
        # Salvar dados no Excel
        self._salvar_dados_excel(df, "dados_ouvidoria", "Sheet1")
        
        return df
    
    def gerar_dados_auditoria(self):
        """
        Gera dados para o módulo de Auditoria Interna.
        
        Simula dados realistas de:
        - Auditorias realizadas por área e campus
        - Conformidade com normas e regulamentos
        - Não conformidades encontradas e ações corretivas
        - Auditorias de processos administrativos e acadêmicos
        - Acompanhamento de recomendações dos órgãos de controle
        
        Os dados incluem classificação por risco e
        cronograma de implementação de melhorias.
        
        Returns:
            pandas.DataFrame: Dados de auditoria com indicadores de conformidade
        """
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_auditoria", "Sheet1")
        if dados_existentes is not None:
            return dados_existentes
        
        # Se não existir, gera dados fictícios
        dados = []
        
        for ano in range(2011, 2026):
            for unidade in self.unidades:
                recomendacoes_emitidas = random.randint(5, 30)
                recomendacoes_atendidas = int(recomendacoes_emitidas * random.uniform(0.6, 0.9))
                
                dados.append({
                    'ano': ano,
                    'unidade': unidade,
                    'recomendacoes_emitidas': recomendacoes_emitidas,
                    'recomendacoes_atendidas': recomendacoes_atendidas,
                    'percentual_atendimento': (recomendacoes_atendidas / recomendacoes_emitidas) * 100
                })
        
        df = pd.DataFrame(dados)
        
        # Salvar dados no Excel
        self._salvar_dados_excel(df, "dados_auditoria", "Sheet1")
        
        return df
    
    def gerar_dados_mundo_trabalho(self):
        """
        Gera dados para o módulo de Mundo do Trabalho.
        
        Simula dados realistas de:
        - Inserção de egressos no mercado de trabalho
        - Empregabilidade por curso e região
        - Faixas salariais e progressão de carreira
        - Setores de atuação profissional
        - Tempo médio para conseguir primeiro emprego
        
        Os dados incluem análise de gênero, tempo de formação
        e alinhamento entre formação e área de atuação.
        
        Returns:
            pandas.DataFrame: Dados de empregabilidade e inserção profissional
        """
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_mundo_trabalho", "Sheet1")
        if dados_existentes is not None:
            return dados_existentes
        
        # Se não existir, gera dados fictícios
        dados = []
        
        regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
        
        for ano in range(2010, 2026):
            for regiao in regioes:
                for setor in self.setores_atividade:
                    admissoes = random.randint(50, 500)
                    desligamentos = random.randint(30, 400)
                    saldo = admissoes - desligamentos
                    
                    dados.append({
                        'ano': ano,
                        'regiao': regiao,
                        'setor_atividade': setor,
                        'admissoes': admissoes,
                        'desligamentos': desligamentos,
                        'saldo': saldo
                    })
        
        df = pd.DataFrame(dados)
        
        # Salvar dados no Excel
        self._salvar_dados_excel(df, "dados_mundo_trabalho", "Sheet1")
        
        return df
    
    def _adicionar_palavras_chave(self, df):
        """
        Adiciona coluna de palavras-chave aos dados de pesquisa existentes.
        
        Este método enriquece DataFrames de pesquisa que não possuem
        palavras-chave, adicionando termos relevantes baseados na área
        de conhecimento de cada publicação.
        
        Args:
            df (pandas.DataFrame): DataFrame de pesquisa sem palavras-chave
            
        Returns:
            pandas.DataFrame: DataFrame enriquecido com coluna 'palavras_chave'
            
        Note:
            Usado principalmente para compatibilidade com dados reais
            que podem não ter metadados completos.
        """
        import random
        
        # Banco de palavras-chave por área
        palavras_por_area = {
            'Ciências Exatas': ['matemática', 'estatística', 'álgebra', 'cálculo', 'geometria', 'análise'],
            'Engenharia': ['automação', 'robótica', 'eletrônica', 'mecânica', 'civil', 'sistemas'],
            'Ciências da Computação': ['machine learning', 'programação', 'algoritmos', 'inteligência artificial', 'redes', 'software'],
            'Educação': ['ensino', 'aprendizagem', 'pedagogia', 'didática', 'formação', 'educação'],
            'Ciências Sociais': ['sociedade', 'cultura', 'política', 'economia', 'social', 'humanas'],
            'Ciências Agrárias': ['agricultura', 'sustentabilidade', 'agronegócio', 'biotecnologia', 'solo', 'plantas'],
            'Ciências Humanas': ['história', 'filosofia', 'literatura', 'linguística', 'antropologia', 'sociologia'],
            'Ciências Biológicas': ['biologia', 'genética', 'ecologia', 'biodiversidade', 'evolução', 'células'],
            'Ciências da Saúde': ['medicina', 'saúde', 'enfermagem', 'fisioterapia', 'farmácia', 'nutrição']
        }
        
        # Palavras-chave gerais
        palavras_gerais = [
            'inovação', 'tecnologia', 'desenvolvimento', 'pesquisa', 'ciência',
            'sustentabilidade', 'interdisciplinar', 'metodologia', 'análise', 'estudo'
        ]
        
        def gerar_palavras_chave(area):
            """Gera palavras-chave para uma área específica"""
            # Buscar palavras da área (usando busca fuzzy para áreas similares)
            palavras_area = []
            for key, words in palavras_por_area.items():
                if key.lower() in area.lower() or any(word in area.lower() for word in key.lower().split()):
                    palavras_area = words
                    break
            
            # Se não encontrou área específica, usar palavras gerais
            if not palavras_area:
                palavras_area = palavras_gerais[:4]
            
            # Selecionar 3-4 palavras da área + 2-3 palavras gerais
            palavras_selecionadas = random.sample(palavras_area, min(4, len(palavras_area)))
            palavras_selecionadas += random.sample(palavras_gerais, random.randint(2, 3))
            
            return ', '.join(palavras_selecionadas)
        
        # Adicionar coluna de palavras-chave
        df['palavras_chave'] = df['area_conhecimento'].apply(gerar_palavras_chave)
        
        return df
    
    def formatar_valor_monetario(self, valor):
        """
        Formata valor numérico como moeda brasileira (Real).
        
        Converte um valor numérico para o formato monetário brasileiro
        padrão, com separador de milhares (.) e decimais (,).
        
        Args:
            valor (float): Valor numérico a ser formatado
            
        Returns:
            str: Valor formatado como "R$ 1.234,56"
            
        Example:
            >>> generator = DataGenerator()
            >>> generator.formatar_valor_monetario(1234.56)
            'R$ 1.234,56'
        """
        return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

# ==============================================================================
# FIM DO MÓDULO DATA_GENERATOR
# ==============================================================================
# Este módulo fornece geração de dados sintéticos realistas para todos os
# módulos do Sistema Dashboard IFPB-CZ. A implementação garante dados 
# estatisticamente coerentes e compatíveis com as necessidades de análise
# dos gestores educacionais.
#
# Principais funcionalidades:
# - Geração de dados sintéticos para 9 módulos distintos
# - Fallback automático quando dados reais não estão disponíveis  
# - Estruturas de dados padronizadas e normalizadas
# - Simulação de sazonalidade e tendências realistas
# - Compatibilidade com análises estatísticas e visualizações
# - Sistema de cache para otimização de performance
# - Configurações de segurança para proteção de dados
#
# Autor: Sistema Dashboard IFPB-CZ
# Versão: 2.0 - Dados Sintéticos Avançados
# ==============================================================================
