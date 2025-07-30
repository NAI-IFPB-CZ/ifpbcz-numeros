# ============================================================================
# MÓDULO DE UTILITÁRIOS - DASHBOARD IFPB CAMPUS CAJAZEIRAS
# ============================================================================
"""
DESCRIÇÃO DO MÓDULO:
Este módulo contém funções utilitárias compartilhadas para padronização visual 
e funcional do sistema de dashboard do IFPB Campus Cajazeiras. Fornece componentes
reutilizáveis para cabeçalhos, rodapés e manipulação de recursos visuais.

FUNCIONALIDADES PRINCIPAIS:
1. Conversão de imagens para formato Base64 (embedding inline)
2. Exibição de cabeçalho institucional padronizado com logomarca
3. Renderização de rodapé customizado com identidade visual
4. Tratamento de recursos visuais e fallbacks para casos de erro

PADRÕES VISUAIS:
- Cores institucionais IFPB: #0d5a4e, #1a8c73 (gradiente principal)
- Layout responsivo com bordas arredondadas (border-radius: 10px)
- Tipografia padronizada com hierarquia visual clara
- Logomarca oficial do campus integrada via Base64

ESTRUTURA DE RECURSOS:
- Diretório: logo-ifpb/IFPB-cz.png (logomarca principal)
- Encoding: Base64 para embedding direto no HTML
- Fallback: Cabeçalho sem logo em caso de erro de carregamento

DEPENDÊNCIAS:
- Streamlit: Framework web para componentes de interface
- Base64: Codificação de imagens para embedding HTML
- OS: Manipulação de caminhos de arquivos multiplataforma

USO TÍPICO:
- Importado por todos os módulos principais do dashboard
- Aplicado no início (cabeçalho) e final (rodapé) de cada página
- Garante consistência visual em toda a aplicação
"""

import streamlit as st
import base64
import os

def get_base64_image(image_path):
    """
    Converte uma imagem local para formato Base64 para embedding em HTML.
    
    Esta função realiza a codificação de imagens em Base64, permitindo
    o embedding direto em elementos HTML sem necessidade de servidor
    de arquivos externo. Essencial para logotipos e recursos visuais.
    
    FUNCIONALIDADE:
    - Leitura de arquivo de imagem em modo binário
    - Codificação Base64 para string utilizável em HTML
    - Tratamento de erros com retorno None em caso de falha
    
    PARÂMETROS:
    -----------
    image_path : str
        Caminho relativo ou absoluto para o arquivo de imagem
        Formatos suportados: PNG, JPG, JPEG, GIF, SVG
    
    RETORNO:
    --------
    str or None
        String Base64 da imagem se sucesso, None se erro
        
    EXEMPLO DE USO:
    ---------------
    >>> logo_b64 = get_base64_image("logo-ifpb/IFPB-cz.png")
    >>> if logo_b64:
    >>>     html = f'<img src="data:image/png;base64,{logo_b64}">'
    
    TRATAMENTO DE ERROS:
    - FileNotFoundError: Arquivo não encontrado
    - PermissionError: Sem permissão de leitura
    - IOError: Erro de entrada/saída
    """
    try:
        # Abertura do arquivo de imagem em modo binário
        # Necessário para preservar a integridade dos dados da imagem
        with open(image_path, "rb") as img_file:
            # Leitura completa do arquivo e codificação Base64
            # Conversão para string decodificada (UTF-8) para uso em HTML
            return base64.b64encode(img_file.read()).decode()
    except:
        # Retorno None em caso de qualquer erro (arquivo não encontrado, permissões, etc.)
        # Permite implementação de fallbacks nos componentes que utilizam esta função
        return None

def display_header_with_logo(title):
    """
    Exibe cabeçalho institucional padronizado com logomarca do IFPB.
    
    Esta função renderiza o cabeçalho principal das páginas do dashboard,
    integrando a identidade visual institucional com a logomarca oficial
    do IFPB Campus Cajazeiras. Implementa fallback graceful em caso de
    erro no carregamento da imagem.
    
    FUNCIONALIDADE:
    - Carregamento e embedding da logomarca institucional
    - Renderização de cabeçalho HTML customizado com CSS inline
    - Fallback para cabeçalho sem logo em caso de erro
    - Integração com sistema de estilos do Streamlit
    
    ESTRUTURA VISUAL:
    - Container principal: div.main-header
    - Logo container: div.header-logo com imagem Base64
    - Título dinâmico baseado no parâmetro recebido
    - Estilização consistente com identidade IFPB
    
    PARÂMETROS:
    -----------
    title : str
        Título da página/seção a ser exibido no cabeçalho
        Exemplos: "Ensino", "Pesquisa", "Extensão", "Servidores"
    
    RETORNO:
    --------
    None
        Renderiza diretamente no Streamlit via st.markdown()
        
    EXEMPLO DE USO:
    ---------------
    >>> display_header_with_logo("Análise de Ensino")
    >>> # Resultado: Cabeçalho com logo IFPB + título "Análise de Ensino"
    
    IMPLEMENTAÇÃO TÉCNICA:
    - HTML inline com CSS para máximo controle visual
    - Base64 embedding para independência de servidor de arquivos
    - Atributo unsafe_allow_html=True para renderização HTML
    """
    # Definição do caminho padrão para a logomarca institucional
    # Estrutura de diretórios: logo-ifpb/IFPB-cz.png
    logo_path = os.path.join("logo-ifpb", "IFPB-cz.png")
    
    # Tentativa de carregamento e conversão da logomarca para Base64
    # Utiliza função utilitária para encoding seguro
    logo_base64 = get_base64_image(logo_path)
    
    # Renderização condicional baseada no sucesso do carregamento da imagem
    if logo_base64:
        # CASO 1: Logo carregado com sucesso
        # Renderização completa com cabeçalho + logomarca + título
        st.markdown(f"""
        <div class="main-header">
            <div class="header-logo">
                <img src="data:image/png;base64,{logo_base64}" alt="IFPB Logo">
            </div>
            {title}
        </div>
        """, unsafe_allow_html=True)
    else:
        # CASO 2: Fallback - erro no carregamento da logo
        # Renderização simplificada apenas com título estilizado
        st.markdown(f'<div class="main-header">{title}</div>', unsafe_allow_html=True)

def display_footer():
    """
    Exibe rodapé institucional customizado para o dashboard.
    
    Esta função renderiza o rodapé padronizado que aparece em todas as
    páginas do sistema, fornecendo informações institucionais, créditos
    de desenvolvimento e aplicando a identidade visual oficial do IFPB.
    
    CARACTERÍSTICAS VISUAIS:
    - Gradiente de cores institucionais (#0d5a4e → #1a8c73)
    - Texto centralizado em cor branca contrastante
    - Padding generoso para respiração visual (1rem)
    - Margem superior para separação do conteúdo (3rem)
    - Bordas arredondadas para modernidade visual (10px)
    - Tipografia reduzida para função secundária (0.9rem)
    
    CONTEÚDO INFORMATIVO:
    - Nome completo do sistema e instituição
    - Créditos de desenvolvimento para equipe NAI
    - Ano atual de referência (2025)
    - Emoji visual para humanização (❤️)
    
    ESTRUTURA TÉCNICA:
    - HTML inline com CSS para controle total de estilização
    - Uso de CSS Grid/Flexbox implícito via text-align: center
    - Hierarquia visual com <strong> para destaque do título
    - Quebra de linha <br> para organização das informações
    
    PARÂMETROS:
    -----------
    Nenhum
        Função sem parâmetros, renderização fixa e padronizada
    
    RETORNO:
    --------
    None
        Renderiza diretamente no Streamlit via st.markdown()
        
    EXEMPLO DE USO:
    ---------------
    >>> display_footer()
    >>> # Resultado: Rodapé institucional fixo no final da página
    
    APLICAÇÃO:
    - Chamado no final de todos os módulos principais
    - Garante consistência visual em todo o sistema
    - Reforça identidade institucional e créditos de desenvolvimento
    """
    # Renderização do rodapé institucional com HTML e CSS inline
    # Aplicação da identidade visual IFPB com gradiente e tipografia padronizada
    st.markdown("""
    <div style="
        background: linear-gradient(90deg, #0d5a4e, #1a8c73);  /* Gradiente institucional IFPB */
        color: white;                                           /* Texto branco para contraste */
        padding: 1rem;                                          /* Espaçamento interno generoso */
        text-align: center;                                     /* Centralização do conteúdo */
        margin-top: 3rem;                                       /* Separação do conteúdo principal */
        border-radius: 10px;                                    /* Bordas arredondadas modernas */
        font-size: 0.9rem;                                      /* Tamanho reduzido para função secundária */
    ">
        <p style="margin: 0;">                                  <!-- Remoção de margem padrão do parágrafo -->
            <strong>Sistema de Visualização de Dados Institucionais - IFPB Campus Cajazeiras</strong><br>
            Desenvolvido com ❤️ pela equipe NAI | 2025           <!-- Créditos com emoji humanizado -->
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# NOTAS DE IMPLEMENTAÇÃO E MANUTENÇÃO
# ============================================================================
"""
CONSIDERAÇÕES TÉCNICAS:

1. PERFORMANCE:
   - Base64 embedding aumenta o tamanho do HTML mas elimina requisições HTTP
   - Ideal para logos pequenos e recursos críticos
   - Cache automático do navegador para strings Base64

2. MANUTENIBILIDADE:
   - Centralização de componentes visuais facilita atualizações
   - Modificações de estilo refletem em todo o sistema
   - Separação clara entre lógica e apresentação

3. COMPATIBILIDADE:
   - HTML/CSS inline garante funcionamento independente de CSS externo
   - Fallbacks implementados para robustez do sistema
   - Suporte universal a navegadores modernos

4. SEGURANÇA:
   - unsafe_allow_html=True requer confiança no conteúdo
   - Strings HTML são controladas internamente (sem input externo)
   - Base64 é seguro para embedding de imagens

5. FUTURAS MELHORIAS:
   - Considerar CSS externo para aplicações maiores
   - Implementar cache de Base64 para otimização
   - Adicionar suporte a temas claro/escuro
   - Internacionalização (i18n) para múltiplos idiomas
"""
