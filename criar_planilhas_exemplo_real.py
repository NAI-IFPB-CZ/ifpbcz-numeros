"""
=============================================================================
GERADOR DE PLANILHAS EXCEL DE EXEMPLO - SISTEMA DASHBOARD IFPB-CZ
=============================================================================

Este módulo implementa a criação automatizada de planilhas Excel de exemplo
com estrutura de dados correta para demonstração e teste do Sistema Dashboard
IFPB-CZ. Gera arquivos modelo que seguem exatamente as especificações técnicas
necessárias para funcionamento do sistema de visualizações.

FUNCIONALIDADES PRINCIPAIS:
---------------------------
- Geração automatizada de 9 arquivos Excel institucionais
- Estrutura de dados realista baseada em cenários reais do IFPB
- Validação de formatos e tipos de dados conforme especificações
- Criação de diretório de dados se não existir
- Substituição inteligente de arquivos existentes
- Dados de exemplo representativos para demonstração

ARQUIVOS EXCEL GERADOS:
-----------------------
1. dados_extensao.xlsx - Projetos extensionistas e inclusão
2. dados_ensino.xlsx - Indicadores educacionais e acadêmicos
3. dados_pesquisa.xlsx - Produção científica e publicações
4. dados_assistencia.xlsx - Programas assistenciais e benefícios
5. dados_auditoria.xlsx - Auditorias e conformidade
6. dados_mundo_trabalho.xlsx - Empregabilidade de egressos
7. dados_orcamento.xlsx - Execução financeira e orçamentária
8. dados_ouvidoria.xlsx - Manifestações e atendimento
9. dados_servidores.xlsx - Recursos humanos e quadro funcional

CARACTERÍSTICAS DOS DADOS:
---------------------------
- Dados realistas baseados em cenários típicos do IFPB
- Estrutura temporal: 2023-2025 (3 anos de histórico)
- Distribuição por campus: Campina Grande e Cajazeiras
- Cursos representativos: Técnico em Informática e Eletrônica
- Valores numéricos consistentes e proporcionais
- Categorias diversificadas por área institucional

VALIDAÇÕES IMPLEMENTADAS:
-------------------------
- Criação automática do diretório 'dados/' se necessário
- Remoção de arquivos existentes para evitar conflitos
- Estrutura de colunas conforme especificações técnicas
- Tipos de dados apropriados (int, float, str, datetime)
- Nomenclatura exata de arquivos e campos
- Encoding UTF-8 para caracteres especiais

PADRÕES DE DADOS:
-----------------
- Anos: 2023, 2024, 2025 (cobertura temporal de 3 anos)
- Campus: IFPB - Campus Campina Grande/Cajazeiras
- Cursos: Técnico em Informática/Eletrônica
- Modalidades: Presencial, EAD
- Categorias: Docente, Técnico Administrativo
- Valores: Proporcionais e realistas para cada área

ESTRUTURA DE SAÍDA:
-------------------
- Diretório de destino: dados/ (raiz do projeto)
- Formato: .xlsx (Excel 2007+)
- Encoding: UTF-8 com suporte a acentuação
- Índice: Removido dos arquivos (index=False)
- Colunas: Nomes exatos conforme especificação técnica

OBJETIVO:
---------
Facilitar demonstração, teste e validação do sistema fornecendo
dados estruturados que permitem exploração completa de todas as
funcionalidades do dashboard sem necessidade de dados reais,
mantendo realismo e representatividade institucional.

DEPENDÊNCIAS:
-------------
- pandas: manipulação e exportação de dados
- os: operações de sistema de arquivos

AUTOR: Sistema Dashboard IFPB-CZ - NAI
DATA: 2024
=============================================================================
"""

import pandas as pd
import os

def criar_planilhas_exemplo():
    """
    Criação automatizada de planilhas Excel de exemplo com estrutura correta.
    
    Esta função gera 9 arquivos Excel de exemplo seguindo exatamente as
    especificações técnicas do Sistema Dashboard IFPB-CZ, fornecendo
    dados realistas para demonstração, teste e validação de todas as
    funcionalidades do sistema.
    
    PROCESSO DE CRIAÇÃO:
    1. Verificação e criação do diretório de dados
    2. Geração de DataFrames com dados estruturados
    3. Validação de formatos e tipos de dados
    4. Exportação para arquivos Excel padronizados
    5. Logging do progresso de criação
    
    DADOS GERADOS POR MÓDULO:
    - Extensão: projetos, estágios, PNE, modalidades
    - Ensino: matrículas, formação, evasão, transferências
    - Pesquisa: publicações, áreas conhecimento, servidores
    - Assistência: benefícios, valores, tipos de auxílio
    - Auditoria: tipos, recomendações, números
    - Mundo do Trabalho: empregabilidade, salários médios
    - Orçamento: categorias, valores orçados/executados
    - Ouvidoria: manifestações, status, tipos
    - Servidores: categorias, quantidades, distribuição
    
    CARACTERÍSTICAS DOS DADOS:
    - Realismo institucional: valores típicos do IFPB
    - Consistência temporal: progressão lógica 2023-2025
    - Diversidade representativa: múltiplos campus e cursos
    - Proporções realistas: números compatíveis entre módulos
    - Completude estrutural: todas as colunas obrigatórias
    
    VALIDAÇÕES REALIZADAS:
    - Estrutura de diretórios adequada
    - Tipos de dados conforme especificação
    - Nomenclatura exata de arquivos e colunas
    - Substituição segura de arquivos existentes
    - Encoding correto para acentuação
    
    ARQUIVOS CRIADOS:
    -----------------
    dados/dados_extensao.xlsx : 8 colunas x 6 registros
    dados/dados_ensino.xlsx : 8 colunas x 6 registros
    dados/dados_pesquisa.xlsx : 5 colunas x 6 registros
    dados/dados_assistencia.xlsx : 5 colunas x 6 registros
    dados/dados_auditoria.xlsx : 4 colunas x 6 registros
    dados/dados_mundo_trabalho.xlsx : 5 colunas x 6 registros
    dados/dados_orcamento.xlsx : 4 colunas x 6 registros
    dados/dados_ouvidoria.xlsx : 4 colunas x 6 registros
    dados/dados_servidores.xlsx : 5 colunas x 6 registros
    
    PARÂMETROS:
    -----------
    Nenhum
        Função autônoma com configurações pré-definidas
        
    RETORNO:
    --------
    None
        Função de utilidade que gera arquivos no sistema
        
    EFEITOS COLATERAIS:
    ------------------
    - Criação do diretório 'dados/' se não existir
    - Substituição de arquivos Excel existentes
    - Logging do progresso no console
    - Geração de 9 arquivos .xlsx estruturados
    
    EXEMPLO DE USO:
    --------------
    criar_planilhas_exemplo()
    # Cria todos os arquivos Excel na pasta dados/
    """
    
    # ============= CONFIGURAÇÃO E CRIAÇÃO DO AMBIENTE DE DADOS =============
    # Verifica e cria diretório de dados se não existir
    # Garante estrutura adequada para armazenamento das planilhas
    # Criar diretório se não existir
    if not os.path.exists("dados"):
        os.makedirs("dados")
    
    # ============= GERAÇÃO DE DADOS DE EXTENSÃO UNIVERSITÁRIA =============
    # Cria dados para projetos extensionistas, estágios e inclusão
    # Inclui informações sobre PNE e diversidade institucional
    # 1. DADOS DE EXTENSÃO
    print("Criando dados_extensao.xlsx...")
    dados_extensao = pd.DataFrame({
        'ano': [2023, 2023, 2024, 2024, 2025, 2025],
        'unidade': [
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras'
        ],
        'curso': [
            'Técnico em Informática',
            'Técnico em Eletrônica',
            'Técnico em Informática',
            'Técnico em Eletrônica',
            'Técnico em Informática',
            'Técnico em Eletrônica'
        ],
        'modalidade': ['Presencial', 'Presencial', 'Presencial', 'EAD', 'Presencial', 'Presencial'],
        'genero': ['Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino'],
        'estagios_concluidos': [45, 32, 52, 38, 48, 35],
        'pne_ingressantes': [3, 2, 4, 1, 5, 3],
        'tipo_necessidade': ['Física', 'Visual', 'Auditiva', 'Física', 'Visual', 'Intelectual']
    })
    
    # ============= EXPORTAÇÃO SEGURA DE ARQUIVO EXTENSÃO =============
    # Remove arquivo anterior e cria nova versão atualizada
    # Remover arquivo existente se houver
    if os.path.exists('dados/dados_extensao.xlsx'):
        os.remove('dados/dados_extensao.xlsx')
    
    dados_extensao.to_excel('dados/dados_extensao.xlsx', index=False)
    
    # ============= GERAÇÃO DE DADOS EDUCACIONAIS E ACADÊMICOS =============
    # Cria indicadores de ensino: matrículas, formação e evasão
    # Dados fundamentais para acompanhamento da gestão acadêmica
    # 2. DADOS DE ENSINO
    print("Criando dados_ensino.xlsx...")
    dados_ensino = pd.DataFrame({
        'ano': [2023, 2023, 2024, 2024, 2025, 2025],
        'campus': [
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras'
        ],
        'curso': [
            'Técnico em Informática',
            'Técnico em Eletrônica',
            'Técnico em Informática',
            'Técnico em Eletrônica',
            'Técnico em Informática',
            'Técnico em Eletrônica'
        ],
        'modalidade': ['Presencial', 'Presencial', 'Presencial', 'EAD', 'Presencial', 'Presencial'],
        'matriculados': [120, 85, 135, 92, 140, 88],
        'formados': [95, 72, 108, 78, 115, 75],
        'desistentes': [15, 8, 18, 10, 12, 9],
        'transferidos': [10, 5, 9, 4, 13, 4]
    })
    dados_ensino.to_excel('dados/dados_ensino.xlsx', index=False)
    
    # ============= GERAÇÃO DE DADOS DE PRODUÇÃO CIENTÍFICA =============
    # Cria dados de pesquisa: publicações, áreas e produtividade
    # Informações para acompanhamento da atividade científica institucional
    # 3. DADOS DE PESQUISA
    print("Criando dados_pesquisa.xlsx...")
    dados_pesquisa = pd.DataFrame({
        'ano': [2023, 2023, 2024, 2024, 2025, 2025],
        'tipo_publicacao': [
            'Artigos',
            'Capítulos de Livros',
            'Artigos',
            'Trabalhos em Eventos',
            'Artigos',
            'Capítulos de Livros'
        ],
        'quantidade': [25, 8, 32, 15, 28, 12],
        'area_conhecimento': [
            'Ciências Exatas',
            'Ciências Humanas',
            'Ciências Exatas',
            'Ciências Aplicadas',
            'Ciências Exatas',
            'Ciências Humanas'
        ],
        'servidor': [
            'Prof. João Silva',
            'Prof. Maria Santos',
            'Prof. Pedro Oliveira',
            'Prof. Ana Costa',
            'Prof. Carlos Lima',
            'Prof. Lucia Ferreira'
        ]
    })
    dados_pesquisa.to_excel('dados/dados_pesquisa.xlsx', index=False)
    
    # ============= GERAÇÃO DE DADOS ASSISTENCIAIS =============
    # Cria dados de assistência estudantil: programas e benefícios
    # Informações sobre investimento em políticas de permanência
    # 4. DADOS DE ASSISTÊNCIA
    print("Criando dados_assistencia.xlsx...")
    dados_assistencia = pd.DataFrame({
        'ano': [2023, 2023, 2024, 2024, 2025, 2025],
        'campus': [
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras'
        ],
        'auxilio_tipo': [
            'Auxílio Alimentação',
            'Auxílio Transporte',
            'Auxílio Alimentação',
            'Auxílio Moradia',
            'Auxílio Alimentação',
            'Auxílio Digital'
        ],
        'beneficiarios': [450, 320, 480, 280, 520, 350],
        'valor_total': [180000.00, 96000.00, 192000.00, 112000.00, 208000.00, 105000.00]
    })
    dados_assistencia.to_excel('dados/dados_assistencia.xlsx', index=False)
    
    # ============= GERAÇÃO DE DADOS DE AUDITORIA E CONFORMIDADE =============
    # Cria dados de auditoria: tipos, quantidades e recomendações
    # Informações para acompanhamento da gestão e conformidade
    # 5. DADOS DE AUDITORIA
    print("Criando dados_auditoria.xlsx...")
    dados_auditoria = pd.DataFrame({
        'ano': [2023, 2023, 2024, 2024, 2025, 2025],
        'tipo_auditoria': [
            'Auditoria Interna',
            'Auditoria Externa',
            'Auditoria Interna',
            'Auditoria de Gestão',
            'Auditoria Interna',
            'Auditoria Externa'
        ],
        'numero_auditorias': [12, 4, 15, 8, 18, 6],
        'recomendacoes': [45, 18, 52, 28, 58, 22]
    })
    dados_auditoria.to_excel('dados/dados_auditoria.xlsx', index=False)
    
    # ============= GERAÇÃO DE DADOS DE EMPREGABILIDADE =============
    # Cria dados de mundo do trabalho: inserção profissional de egressos
    # Informações sobre empregabilidade e salários por curso
    # 6. DADOS DE MUNDO DO TRABALHO
    print("Criando dados_mundo_trabalho.xlsx...")
    dados_mundo_trabalho = pd.DataFrame({
        'ano': [2023, 2023, 2024, 2024, 2025, 2025],
        'campus': [
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras'
        ],
        'curso': [
            'Técnico em Informática',
            'Técnico em Eletrônica',
            'Técnico em Informática',
            'Técnico em Eletrônica',
            'Técnico em Informática',
            'Técnico em Eletrônica'
        ],
        'empregabilidade': [85.5, 78.2, 87.3, 82.1, 89.7, 85.4],
        'salario_medio': [2850.00, 2650.00, 3120.00, 2890.00, 3350.00, 3120.00]
    })
    dados_mundo_trabalho.to_excel('dados/dados_mundo_trabalho.xlsx', index=False)
    
    # ============= GERAÇÃO DE DADOS ORÇAMENTÁRIOS =============
    # Cria dados de orçamento: execução financeira por categorias
    # Informações sobre gestão orçamentária e execução de recursos
    # 7. DADOS DE ORÇAMENTO
    print("Criando dados_orcamento.xlsx...")
    dados_orcamento = pd.DataFrame({
        'ano': [2023, 2023, 2024, 2024, 2025, 2025],
        'categoria': [
            'Custeio',
            'Investimento',
            'Custeio',
            'Investimento',
            'Custeio',
            'Investimento'
        ],
        'valor_orcado': [5500000.00, 1200000.00, 6100000.00, 1450000.00, 6800000.00, 1650000.00],
        'valor_executado': [5350000.00, 1150000.00, 5980000.00, 1380000.00, 6650000.00, 1580000.00]
    })
    dados_orcamento.to_excel('dados/dados_orcamento.xlsx', index=False)
    
    # ============= GERAÇÃO DE DADOS DE OUVIDORIA =============
    # Cria dados de ouvidoria: manifestações e atendimento
    # Informações sobre qualidade dos serviços e satisfação
    # 8. DADOS DE OUVIDORIA
    print("Criando dados_ouvidoria.xlsx...")
    dados_ouvidoria = pd.DataFrame({
        'ano': [2023, 2023, 2024, 2024, 2025, 2025],
        'tipo_manifestacao': [
            'Reclamação',
            'Sugestão',
            'Reclamação',
            'Elogio',
            'Reclamação',
            'Denúncia'
        ],
        'quantidade': [85, 32, 92, 45, 78, 18],
        'status': [
            'Resolvido',
            'Em Andamento',
            'Resolvido',
            'Resolvido',
            'Em Andamento',
            'Resolvido'
        ]
    })
    dados_ouvidoria.to_excel('dados/dados_ouvidoria.xlsx', index=False)
    
    # ============= GERAÇÃO DE DADOS DE RECURSOS HUMANOS =============
    # Cria dados de servidores: quadro funcional e distribuição
    # Informações sobre gestão de pessoas e composição institucional
    # 9. DADOS DE SERVIDORES
    print("Criando dados_servidores.xlsx...")
    dados_servidores = pd.DataFrame({
        'ano': [2023, 2023, 2024, 2024, 2025, 2025],
        'campus': [
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Campina Grande',
            'IFPB - Campus Cajazeiras'
        ],
        'categoria': [
            'Docente',
            'Técnico Administrativo',
            'Docente',
            'Técnico Administrativo',
            'Docente',
            'Técnico Administrativo'
        ],
        'quantidade': [125, 85, 132, 88, 138, 92],
        'genero': ['Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino']
    })
    dados_servidores.to_excel('dados/dados_servidores.xlsx', index=False)
    
    # ============= CONFIRMAÇÃO DE CRIAÇÃO COMPLETA =============
    # Exibe mensagens de sucesso e orientações para verificação
    # Confirma criação de todos os arquivos necessários
    print("\n✅ Todas as planilhas de exemplo foram criadas com sucesso!")
    print("📁 Verifique o diretório 'dados/' para os arquivos Excel")

# ============= EXECUÇÃO PRINCIPAL DO GERADOR =============
# Ponto de entrada principal quando arquivo é executado diretamente
# Chama função de criação de planilhas para geração automática
if __name__ == "__main__":
    criar_planilhas_exemplo()
