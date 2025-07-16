"""
Configuração para alternância entre dados sintéticos e reais

Para usar dados reais:
1. Execute: python criar_planilhas_exemplo_real.py (para criar exemplos)
2. Substitua os arquivos Excel na pasta 'dados/' pelos seus dados reais
3. Altere USE_REAL_DATA para True
4. Reinicie o sistema Streamlit
"""

# Configuração principal
USE_REAL_DATA = False  # True para usar dados reais, False para dados sintéticos

# Configurações de validação
VALIDAR_DADOS = True  # Validar estrutura dos dados ao carregar
MOSTRAR_LOGS = True   # Mostrar logs de carregamento

# Configurações de cache
CACHE_DADOS = True    # Cache dos dados para melhor performance
CACHE_TIMEOUT = 3600  # Timeout do cache em segundos (1 hora)

# Configurações de erro
CONTINUAR_COM_ERRO = False  # Continuar execução mesmo com erros nos dados
USAR_DADOS_BACKUP = True    # Usar dados sintéticos como backup se houver erro
