import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os
import warnings
warnings.filterwarnings('ignore')

class DataGenerator:
    def __init__(self):
        self.dados_directory = "dados"
        self.data_atualizacao = datetime.now().strftime("%d/%m/%Y às %H:%M")
        
        # Criar diretório se não existir
        if not os.path.exists(self.dados_directory):
            os.makedirs(self.dados_directory)
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
        
        self.niveis_curso = ["Técnico", "Graduação", "Pós-graduação"]
        self.generos = ["Masculino", "Feminino"]
        self.tipos_necessidades = ["Auditiva", "Visual", "Física", "Intelectual", "Múltipla"]
        
        self.programas_assistencia = [
            "Auxílio Alimentação",
            "Auxílio Transporte", 
            "Auxílio Moradia",
            "Auxílio Didático",
            "Bolsa Monitoria",
            "Bolsa Iniciação Científica"
        ]
        
        self.categorias_orcamento = [
            "Pessoal e Encargos Sociais",
            "Custeio",
            "Investimentos",
            "Manutenção",
            "Equipamentos",
            "Obras"
        ]
        
        self.tipos_publicacao = [
            "Artigos",
            "Capítulos de Livros",
            "Trabalhos em Eventos",
            "Livros",
            "Patentes"
        ]
        
        self.tipos_manifestacao = [
            "Reclamação",
            "Sugestão",
            "Elogio",
            "Denúncia",
            "Solicitação"
        ]
        
        self.tipos_usuario = [
            "Estudante",
            "Servidor",
            "Comunidade Externa",
            "Responsável"
        ]
        
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
        
        random.seed(42)
        np.random.seed(42)
    
    def _salvar_dados_excel(self, df, nome_arquivo, sheet_name="Dados"):
        """Salva DataFrame em arquivo Excel"""
        filepath = os.path.join(self.dados_directory, f"{nome_arquivo}.xlsx")
        
        # Adicionar informações de metadados
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            # Criar planilha de metadados
            metadata = pd.DataFrame({
                'Informação': ['Data de Atualização', 'Total de Registros', 'Período dos Dados'],
                'Valor': [
                    self.data_atualizacao,
                    len(df),
                    f"{df['ano'].min()} - {df['ano'].max()}" if 'ano' in df.columns else "N/A"
                ]
            })
            metadata.to_excel(writer, sheet_name="Metadados", index=False)
        
        return filepath
    
    def _carregar_dados_excel(self, nome_arquivo, sheet_name="Dados"):
        """Carrega dados do arquivo Excel ou gera se não existir"""
        filepath = os.path.join(self.dados_directory, f"{nome_arquivo}.xlsx")
        
        if os.path.exists(filepath):
            try:
                df = pd.read_excel(filepath, sheet_name=sheet_name)
                return df
            except Exception as e:
                print(f"Erro ao carregar {filepath}: {e}")
                return None
        
        return None
    
    def get_data_atualizacao(self, nome_arquivo):
        """Retorna a data de atualização dos dados"""
        filepath = os.path.join(self.dados_directory, f"{nome_arquivo}.xlsx")
        
        if os.path.exists(filepath):
            try:
                metadata = pd.read_excel(filepath, sheet_name="Metadados")
                return metadata.loc[metadata['Informação'] == 'Data de Atualização', 'Valor'].iloc[0]
            except:
                return "Data não disponível"
        
        return "Arquivo não encontrado"
    
    def gerar_dados_ensino(self):
        """Gera dados para o módulo de Ensino"""
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_ensino", "Dados_Ensino")
        if dados_existentes is not None:
            return dados_existentes
        
        # Se não existir, gera dados fictícios
        dados = []
        modalidades = ["Presencial", "EAD", "Semipresencial"]
        
        for ano in range(2019, 2026):
            for campus in self.unidades:
                # Diferentes campus têm diferentes tamanhos
                if "João Pessoa" in campus or "Campina Grande" in campus:
                    fator_tamanho = 1.5  # Campus maiores
                elif "Cajazeiras" in campus or "Sousa" in campus or "Patos" in campus:
                    fator_tamanho = 1.0  # Campus médios
                else:
                    fator_tamanho = 0.6  # Campus menores
                
                # Selecionar cursos por campus (nem todos os campus têm todos os cursos)
                cursos_campus = random.sample(self.cursos, random.randint(8, 15))
                
                for curso in cursos_campus:
                    for modalidade in modalidades:
                        # Nem todos os cursos têm todas as modalidades
                        if modalidade == "EAD" and random.random() < 0.7:
                            continue
                        if modalidade == "Semipresencial" and random.random() < 0.8:
                            continue
                            
                        # Simulando crescimento ao longo dos anos
                        base_matriculados = random.randint(30, 150)
                        fator_crescimento = (ano - 2019) * 0.05
                        
                        matriculados = int(base_matriculados * fator_tamanho * (1 + fator_crescimento))
                        matriculados = max(10, matriculados)  # Mínimo de 10 alunos
                        
                        # Cálculos baseados nos matriculados
                        formados = int(matriculados * random.uniform(0.15, 0.30))
                        desistentes = int(matriculados * random.uniform(0.05, 0.20))
                        transferidos = int(matriculados * random.uniform(0.02, 0.10))
                        
                        # Adicionar alguma variação sazonal
                        if ano >= 2020 and ano <= 2022:  # Impacto da pandemia
                            desistentes = int(desistentes * 1.3)
                            formados = int(formados * 0.8)
                        
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
        
        df = pd.DataFrame(dados)
        
        # Salvar dados no Excel
        self._salvar_dados_excel(df, "dados_ensino", "Dados_Ensino")
        
        return df
    
    def gerar_dados_assistencia(self):
        """Gera dados para o módulo de Assistência Estudantil"""
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
        
        return pd.DataFrame(dados)
    
    def gerar_dados_pesquisa(self):
        """Gera dados para o módulo de Pesquisa"""
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
        
        return pd.DataFrame(dados)
    
    def gerar_dados_extensao(self):
        """Gera dados para o módulo de Extensão"""
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_extensao", "Dados_Extensao")
        if dados_existentes is not None:
            return dados_existentes
        
        # Se não existir, gera dados fictícios
        dados = []
        
        for ano in range(2015, 2026):
            for unidade in self.unidades:
                for curso in self.cursos:
                    for genero in self.generos:
                        estagios = random.randint(5, 40)
                        pne = random.randint(0, 5)
                        
                        dados.append({
                            'ano': ano,
                            'unidade': unidade,
                            'curso': curso,
                            'genero': genero,
                            'estagios_concluidos': estagios,
                            'pne_ingressantes': pne,
                            'tipo_necessidade': random.choice(self.tipos_necessidades) if pne > 0 else None
                        })
        
        return pd.DataFrame(dados)
    
    def gerar_dados_orcamento(self):
        """Gera dados para o módulo de Orçamento"""
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_orcamento", "Dados_Orcamento")
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
        
        return pd.DataFrame(dados)
    
    def gerar_dados_servidores(self):
        """Gera dados para o módulo de Servidores"""
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_servidores", "Dados_Servidores")
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
        
        return pd.DataFrame(dados)
    
    def gerar_dados_ouvidoria(self):
        """Gera dados para o módulo de Ouvidoria"""
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_ouvidoria", "Dados_Ouvidoria")
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
        
        return pd.DataFrame(dados)
    
    def gerar_dados_auditoria(self):
        """Gera dados para o módulo de Auditoria"""
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_auditoria", "Dados_Auditoria")
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
        
        return pd.DataFrame(dados)
    
    def gerar_dados_mundo_trabalho(self):
        """Gera dados para o módulo de Mundo do Trabalho"""
        # Tenta carregar dados do Excel primeiro
        dados_existentes = self._carregar_dados_excel("dados_mundo_trabalho", "Dados_Mundo_Trabalho")
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
        
        return pd.DataFrame(dados)
    
    def _adicionar_palavras_chave(self, df):
        """Adiciona coluna de palavras-chave aos dados de pesquisa"""
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
        df['palavras_chave'] = df['area_pesquisa'].apply(gerar_palavras_chave)
        
        return df
    
    def formatar_valor_monetario(self, valor):
        """Formata valor como moeda brasileira"""
        return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
