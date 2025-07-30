"""
==============================================================================
GERADOR DE PLANILHAS EXEMPLO PARA O SISTEMA DASHBOARD IFPB-CZ
==============================================================================

Este script cria planilhas Excel de exemplo com estrutura compatível
com o sistema de visualização de dados institucionais do IFPB-CZ.

Funcionalidades:
- Cria 9 planilhas Excel no diretório 'dados/'
- Dados de exemplo para todos os módulos do dashboard
- Estrutura de colunas padronizada para compatibilidade
- Remove arquivos existentes antes de criar novos

Execução:
python criar_planilhas_exemplo.py

Autor: Sistema NAI/IFPB-CZ
Data: Julho 2025
==============================================================================
"""

import pandas as pd
import os
from datetime import datetime

def criar_planilhas_exemplo():
    """
    Cria planilhas Excel de exemplo com a estrutura correta para dados fictícios.

    Esta função gera dados sintéticos compatíveis com a estrutura esperada
    pelo sistema dashboard, permitindo testar a funcionalidade com dados
    fictícios em vez de dados totalmente sintéticos.

    Returns:
        None: Cria arquivos Excel no diretório dados/
    """
    
    print("🚀 Iniciando criação de planilhas de exemplo...")
    
    # Criar diretório de dados se não existir
    if not os.path.exists("dados"):
        os.makedirs("dados")
        print("📁 Diretório 'dados' criado.")
    
    # ==========================================================================
    # 1. DADOS DE EXTENSÃO
    # ==========================================================================
    print("📋 Criando dados_extensao.xlsx...")
    dados_extensao = pd.DataFrame({
        'ano': [2023, 2023, 2024, 2024, 2025, 2025] * 3,
        'unidade': [
            'IFPB - Campus Cajazeiras',
            'IFPB - Campus Sousa', 
            'IFPB - Campus Patos',
            'IFPB - Campus Picuí',
            'IFPB - Campus Monteiro',
            'IFPB - Campus Cajazeiras'
        ] * 3,
        'curso': [
            'Técnico em Informática',
            'Técnico em Eletrônica', 
            'Técnico em Agropecuária',
            'Técnico em Edificações',
            'Técnico em Enfermagem',
            'Superior em Sistemas'
        ] * 3,
        'modalidade': ['Presencial', 'Presencial', 'EAD', 'Presencial', 'Presencial', 'Híbrido'] * 3,
        'genero': ['Masculino', 'Feminino'] * 9,
        'estagios_concluidos': [45, 32, 52, 38, 48, 35, 42, 29, 55, 41, 46, 33, 48, 31, 58, 44, 50, 36],
        'pne_ingressantes': [3, 2, 4, 1, 5, 3, 2, 1, 6, 2, 4, 2, 3, 1, 5, 3, 4, 2],
        'tipo_necessidade': ['Física', 'Visual', 'Auditiva', 'Física', 'Visual', 'Intelectual'] * 3
    })
    
    # Remover arquivo existente se houver
    if os.path.exists('dados/dados_extensao.xlsx'):
        os.remove('dados/dados_extensao.xlsx')
    
    dados_extensao.to_excel('dados/dados_extensao.xlsx', index=False, sheet_name='Sheet1')
    
    # ==========================================================================
    # 2. DADOS DE ENSINO
    # ==========================================================================
    print("🎓 Criando dados_ensino.xlsx...")
    dados_ensino = pd.DataFrame({
        'ano': [2023, 2024, 2025] * 6,
        'campus': [
            'Cajazeiras', 'Sousa', 'Patos', 'Picuí', 'Monteiro', 'Cajazeiras'
        ] * 3,
        'curso': [
            'Técnico em Informática',
            'Técnico em Eletrônica',
            'Técnico em Agropecuária', 
            'Técnico em Edificações',
            'Técnico em Enfermagem',
            'Superior em Sistemas'
        ] * 3,
        'modalidade': ['Presencial', 'Presencial', 'Presencial', 'Presencial', 'Presencial', 'Presencial'] * 3,
        'matriculados': [120, 85, 135, 92, 140, 88, 125, 90, 142, 95, 145, 92, 130, 95, 148, 98, 150, 95],
        'formados': [95, 72, 108, 78, 115, 75, 98, 75, 112, 80, 118, 78, 102, 78, 118, 82, 122, 80],
        'desistentes': [15, 8, 18, 10, 12, 9, 16, 9, 19, 11, 14, 10, 17, 10, 20, 12, 15, 11],
        'transferidos': [10, 5, 9, 4, 13, 4, 11, 6, 11, 4, 13, 4, 11, 7, 10, 4, 13, 4]
    })
    
    dados_ensino.to_excel('dados/dados_ensino.xlsx', index=False, sheet_name='Sheet1')
    
    # ==========================================================================
    # 3. DADOS DE PESQUISA
    # ==========================================================================
    print("🔬 Criando dados_pesquisa.xlsx...")
    dados_pesquisa = pd.DataFrame({
        'ano': [2023, 2024, 2025] * 8,
        'tipo_publicacao': [
            'Artigos em Periódicos',
            'Artigos em Anais',
            'Capítulos de Livros',
            'Trabalhos de Conclusão',
            'Dissertações',
            'Teses',
            'Patentes',
            'Software'
        ] * 3,
        'quantidade': [25, 45, 8, 120, 15, 3, 2, 5, 32, 52, 12, 135, 18, 4, 3, 7, 28, 48, 15, 142, 20, 5, 4, 8],
        'area_conhecimento': [
            'Ciências Exatas e da Terra',
            'Ciências Biológicas', 
            'Engenharias',
            'Ciências da Saúde',
            'Ciências Agrárias',
            'Ciências Sociais Aplicadas',
            'Ciências Humanas',
            'Linguística, Letras e Artes'
        ] * 3,
        'autor_principal': [
            'Prof. João Silva',
            'Prof. Maria Santos',
            'Prof. Pedro Oliveira',
            'Prof. Ana Costa', 
            'Prof. Carlos Lima',
            'Prof. Lucia Ferreira',
            'Prof. Roberto Alves',
            'Prof. Fernanda Rocha'
        ] * 3,
        'palavras_chave': [
            'tecnologia, inovação, educação',
            'sustentabilidade, meio ambiente',
            'engenharia, automação, robótica',
            'saúde, enfermagem, cuidados',
            'agricultura, desenvolvimento rural',
            'gestão, administração, economia',
            'educação, pedagogia, ensino',
            'linguagem, comunicação, cultura'
        ] * 3
    })
    
    dados_pesquisa.to_excel('dados/dados_pesquisa.xlsx', index=False, sheet_name='Sheet1')
    
    # ==========================================================================
    # 4. DADOS DE ASSISTÊNCIA ESTUDANTIL
    # ==========================================================================
    print("🤝 Criando dados_assistencia.xlsx...")
    dados_assistencia = pd.DataFrame({
        'ano': [2023, 2024, 2025] * 8,
        'unidade': [
            'Cajazeiras', 'Sousa', 'Patos', 'Picuí', 
            'Monteiro', 'Cajazeiras', 'Sousa', 'Patos'
        ] * 3,
        'programa': [
            'Auxílio Alimentação',
            'Auxílio Transporte',
            'Auxílio Moradia', 
            'Auxílio Creche',
            'Auxílio Material',
            'Bolsa Permanência',
            'Auxílio Digital',
            'Auxílio Emergencial'
        ] * 3,
        'nivel_curso': ['Técnico Integrado', 'Técnico Subsequente', 'Superior'] * 8,
        'parcelas': [450, 320, 280, 85, 150, 200, 180, 95, 480, 340, 290, 88, 160, 210, 190, 100, 520, 350, 310, 92, 170, 220, 200, 105],
        'alunos_beneficiados': [420, 300, 260, 80, 140, 185, 170, 90, 450, 320, 270, 82, 150, 195, 180, 95, 485, 330, 290, 85, 160, 205, 190, 98],
        'valor_total': [180000.00, 96000.00, 112000.00, 25500.00, 37500.00, 80000.00, 54000.00, 28500.00, 192000.00, 102000.00, 116000.00, 26400.00, 40000.00, 84000.00, 57000.00, 30000.00, 208000.00, 105000.00, 124000.00, 27600.00, 42500.00, 88000.00, 60000.00, 31500.00]
    })
    
    dados_assistencia.to_excel('dados/dados_assistencia.xlsx', index=False, sheet_name='Sheet1')
    
    # ==========================================================================
    # 5. DADOS DE AUDITORIA
    # ==========================================================================
    print("🔍 Criando dados_auditoria.xlsx...")
    dados_auditoria = pd.DataFrame({
        'ano': [2023, 2024, 2025] * 4,
        'tipo_auditoria': [
            'Auditoria Interna',
            'Auditoria Externa - CGU', 
            'Auditoria de Gestão',
            'Auditoria de Conformidade'
        ] * 3,
        'numero_auditorias': [12, 4, 8, 6, 15, 5, 10, 7, 18, 6, 12, 8],
        'recomendacoes': [45, 18, 28, 22, 52, 20, 32, 25, 58, 22, 35, 28],
        'nao_conformidades': [8, 12, 15, 10, 6, 10, 12, 8, 4, 8, 10, 6],
        'status': ['Concluída', 'Em Andamento', 'Concluída', 'Concluída'] * 3
    })
    
    dados_auditoria.to_excel('dados/dados_auditoria.xlsx', index=False, sheet_name='Sheet1')
    
    # ==========================================================================
    # 6. DADOS DE MUNDO DO TRABALHO  
    # ==========================================================================
    print("💼 Criando dados_mundo_trabalho.xlsx...")
    dados_mundo_trabalho = pd.DataFrame({
        'ano': [2023, 2024, 2025] * 6,
        'regiao': ['Nordeste'] * 18,
        'campus': [
            'Cajazeiras', 'Sousa', 'Patos',
            'Picuí', 'Monteiro', 'Cajazeiras'
        ] * 3,
        'curso': [
            'Técnico em Informática',
            'Técnico em Eletrônica',
            'Técnico em Agropecuária',
            'Técnico em Edificações', 
            'Técnico em Enfermagem',
            'Superior em Sistemas'
        ] * 3,
        'empregabilidade': [85.5, 78.2, 82.1, 75.8, 88.9, 92.3, 87.3, 80.5, 84.7, 78.1, 90.2, 94.1, 89.7, 82.8, 86.3, 80.4, 91.5, 95.8],
        'salario_medio': [2850.00, 2650.00, 2200.00, 2400.00, 2950.00, 4200.00, 3120.00, 2890.00, 2350.00, 2580.00, 3150.00, 4580.00, 3350.00, 3120.00, 2500.00, 2750.00, 3380.00, 4850.00]
    })
    
    dados_mundo_trabalho.to_excel('dados/dados_mundo_trabalho.xlsx', index=False, sheet_name='Sheet1')
    
    # ==========================================================================
    # 7. DADOS DE ORÇAMENTO
    # ==========================================================================
    print("💰 Criando dados_orcamento.xlsx...")
    dados_orcamento = pd.DataFrame({
        'ano': [2023, 2024, 2025] * 6,
        'categoria': [
            'Pessoal e Encargos',
            'Custeio',
            'Investimento',
            'Bolsas e Auxílios',
            'Obras e Instalações',
            'Equipamentos'
        ] * 3,
        'valor_orcado': [15500000.00, 5500000.00, 1200000.00, 2800000.00, 800000.00, 950000.00, 16800000.00, 6100000.00, 1450000.00, 3200000.00, 1100000.00, 1200000.00, 18200000.00, 6800000.00, 1650000.00, 3600000.00, 1350000.00, 1400000.00],
        'valor_executado': [15200000.00, 5350000.00, 1150000.00, 2750000.00, 720000.00, 880000.00, 16450000.00, 5980000.00, 1380000.00, 3150000.00, 950000.00, 1120000.00, 17800000.00, 6650000.00, 1580000.00, 3520000.00, 1200000.00, 1320000.00],
        'percentual_execucao': [98.1, 97.3, 95.8, 98.2, 90.0, 92.6, 97.9, 98.0, 95.2, 98.4, 86.4, 93.3, 97.8, 97.8, 95.8, 97.8, 88.9, 94.3]
    })
    
    dados_orcamento.to_excel('dados/dados_orcamento.xlsx', index=False, sheet_name='Sheet1')
    
    # ==========================================================================
    # 8. DADOS DE OUVIDORIA
    # ==========================================================================
    print("📢 Criando dados_ouvidoria.xlsx...")
    dados_ouvidoria = pd.DataFrame({
        'ano': [2023, 2024, 2025] * 5,
        'mes': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] + [1, 2, 3] * 1,
        'tipo_manifestacao': [
            'Reclamação',
            'Sugestão', 
            'Elogio',
            'Denúncia',
            'Informação'
        ] * 3,
        'quantidade': [85, 32, 45, 18, 25, 92, 38, 52, 22, 28, 78, 35, 48, 20, 30],
        'tempo_resposta_dias': [8, 12, 5, 15, 7, 6, 10, 4, 12, 6, 7, 11, 5, 14, 6],
        'status': [
            'Resolvido',
            'Em Andamento',
            'Resolvido', 
            'Resolvido',
            'Resolvido'
        ] * 3,
        'canal': ['Portal', 'E-mail', 'Telefone', 'Presencial', 'WhatsApp'] * 3
    })
    
    dados_ouvidoria.to_excel('dados/dados_ouvidoria.xlsx', index=False, sheet_name='Sheet1')
    
    # ==========================================================================
    # 9. DADOS DE SERVIDORES
    # ==========================================================================
    print("👥 Criando dados_servidores.xlsx...")
    dados_servidores = pd.DataFrame({
        'ano': [2023, 2024, 2025] * 6,
        'campus': [
            'Cajazeiras', 'Sousa', 'Patos',
            'Picuí', 'Monteiro', 'Cajazeiras'
        ] * 3,
        'categoria': [
            'Docente EBTT',
            'Técnico Administrativo',
            'Docente Substituto',
            'Terceirizado',
            'Estagiário',
            'Bolsista'
        ] * 3,
        'quantidade': [125, 85, 15, 45, 12, 25, 132, 88, 18, 48, 15, 28, 138, 92, 20, 52, 18, 32],
        'genero_masculino': [68, 42, 8, 28, 7, 12, 72, 44, 10, 30, 8, 14, 75, 46, 11, 32, 9, 16],
        'genero_feminino': [57, 43, 7, 17, 5, 13, 60, 44, 8, 18, 7, 14, 63, 46, 9, 20, 9, 16],
        'regime_40h': [98, 65, 0, 0, 0, 0, 105, 68, 0, 0, 0, 0, 110, 72, 0, 0, 0, 0],
        'regime_20h': [27, 20, 15, 0, 0, 0, 27, 20, 18, 0, 0, 0, 28, 20, 20, 0, 0, 0]
    })
    
    dados_servidores.to_excel('dados/dados_servidores.xlsx', index=False, sheet_name='Sheet1')
    
    # ==========================================================================
    # FINALIZAÇÃO
    # ==========================================================================
    print("\n" + "="*70)
    print("✅ SUCESSO! Todas as planilhas de exemplo foram criadas!")
    print("="*70)
    print(f"📁 Local: {os.path.abspath('dados/')}")
    print(f"📅 Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("\n📋 Planilhas criadas:")
    print("   • dados_extensao.xlsx")
    print("   • dados_ensino.xlsx") 
    print("   • dados_pesquisa.xlsx")
    print("   • dados_assistencia.xlsx")
    print("   • dados_auditoria.xlsx")
    print("   • dados_mundo_trabalho.xlsx")
    print("   • dados_orcamento.xlsx")
    print("   • dados_ouvidoria.xlsx")
    print("   • dados_servidores.xlsx")
    print("\n💡 Dica: Agora você pode habilitar USE_REAL_DATA=True no config.py")
    print("   para usar estes dados no dashboard!")
    print("="*70)

if __name__ == "__main__":
    """
    Executa a criação das planilhas quando o script é chamado diretamente.
    """
    criar_planilhas_exemplo()
