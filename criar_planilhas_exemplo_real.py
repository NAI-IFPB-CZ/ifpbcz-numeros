import pandas as pd
import os

def criar_planilhas_exemplo():
    """
    Cria planilhas Excel de exemplo com a estrutura correta para dados reais
    """
    
    # Criar diretório se não existir
    if not os.path.exists("dados"):
        os.makedirs("dados")
    
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
    
    # Remover arquivo existente se houver
    if os.path.exists('dados/dados_extensao.xlsx'):
        os.remove('dados/dados_extensao.xlsx')
    
    dados_extensao.to_excel('dados/dados_extensao.xlsx', index=False)
    
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
    
    print("\n✅ Todas as planilhas de exemplo foram criadas com sucesso!")
    print("📁 Verifique o diretório 'dados/' para os arquivos Excel")

if __name__ == "__main__":
    criar_planilhas_exemplo()
