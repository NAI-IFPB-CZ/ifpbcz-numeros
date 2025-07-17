# 1. Documentação para o Usuário Final (Guia de Uso)

Este documento explica como usar o sistema. Ele deve ser escrito em uma linguagem clara e não técnica. (prof. Teo ficou responsável por isso)

## Visão Geral do Sistema:
* Qual o objetivo do painel? (Ex: "Oferecer uma visão consolidada e interativa dos principais indicadores da instituição...")

* Quem são os usuários-alvo? (Gestores, comunidade acadêmica, público externo).

## Primeiros Passos:
* Como acessar o dashboard (link da aplicação).
* Breve explicação da interface principal: a barra lateral de navegação e a área de conteúdo.

### Guia dos Módulos:

> Para cada módulo ("Ensino", "Pesquisa", etc.), explique:
* O que ele representa: Que tipo de informação está disponível ali? (Ex: "O módulo Ensino exibe dados sobre matrículas, ingressantes e concluintes.").
* Interatividade: Como usar os filtros (seleção de ano, unidade, tipo de exibição). Explique o que cada filtro faz.
* Leitura dos Gráficos: Descreva o que cada gráfico mostra. (Ex: "O gráfico de barras mostra a distribuição de alunos por campus para o ano selecionado.").
* Fonte dos Dados: Mencione a origem dos dados para dar credibilidade (IFPB, CAED, etc.).

### FAQ (Perguntas Frequentes):
* "Os dados são atualizados em tempo real?"

* "Posso exportar os gráficos ou os dados?"

* "O que significa o indicador 'Saldo de Admissões'?"

* "Com quem devo entrar em contato se encontrar um problema?"

# 2. Documentação Técnica (Para Desenvolvedores)
Este documento explica como o sistema funciona por dentro, como mantê-lo e como estendê-lo. É o manual para a equipe de desenvolvimento.
```
> **Importante**: Este documento deve ser escrito em uma linguagem técnica, com detalhes sobre a arquitetura, dependências e como contribuir. (já foi feito muita coisa, veja os arquivos na pasta `docs`, e os arquivos `README.md`, falta fazer algumas adequações e completar o que falta)
```

## Configuração do Ambiente de Desenvolvimento:
* Pré-requisitos: Versão do Python necessária (ex: Python 3.12+).
* Clone do Repositório: Comando git clone ....
* Ambiente Virtual: Instruções para criar e ativar um ambiente virtual (venv ou conda).
* Instalação de Dependências: Como instalar todas as bibliotecas necessárias (ex: pip install -r requirements.txt).
* Como Executar a Aplicação: O comando para rodar o servidor localmente (ex: streamlit run app.py).
* Arquitetura e Estrutura do Projeto:
Diagrama Simples: Um fluxograma mostrando: Fontes de Dados -> Scripts Python (Pandas/Streamlit) -> Interface Web.
Estrutura de Pastas e Arquivos: Descreva a organização do código.

## Fontes de Dados:
* Liste todas as fontes de dados (SISTEC, NAI, CAED, etc.).
* Para cada fonte, descreva o esquema esperado (colunas, tipos de dados) e como os dados são acessados (API, banco de dados, arquivo estático).
* Detalhe quaisquer tratamentos ou limpezas que são aplicados aos dados antes da visualização.

## Padrões de Código e Boas Práticas:
* Uso de docstrings em funções para explicar o que elas fazem, seus parâmetros e o que retornam.
* Padrão de nomenclatura para variáveis e funções.
* Guia para Adicionar um Novo Módulo:

## Um passo a passo claro:
1. Criar um novo arquivo novo_modulo.py dentro da pasta modules/.
2. Definir uma função principal no arquivo, ex: render_page().
3. Importar essa função no arquivo app.py.
4. Adicionar a chamada ao novo módulo na estrutura de navegação da barra lateral em app.py.
5. Explicar como adicionar os scripts de dados correspondentes.

## Deployment (Implantação):
Instruções sobre como implantar a aplicação em um servidor (ex: Streamlit Community Cloud, Heroku, AWS, servidor interno).