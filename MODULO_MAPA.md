# Módulo de Mapa dos Campus IFPB

O módulo de mapa foi criado com sucesso! Ele oferece as seguintes funcionalidades:

## 🗺️ Características Principais

### 📍 **Localização dos Campus**
- Visualização de **25 campus** do IFPB distribuídos na Paraíba
- Coordenadas geográficas precisas de cada campus
- Informações detalhadas em popups interativos

### 🎯 **Funcionalidades Implementadas**

#### **1. Mapa Interativo**
- Mapa centralizado na Paraíba
- Marcadores verdes com ícone de graduação
- Popups informativos com nome, cidade e coordenadas
- Tooltip com nome do campus ao passar o mouse

#### **2. Filtros por Região**
- **Todas as Regiões**: Visualização completa
- **Região Metropolitana**: João Pessoa, Cabedelo, Santa Rita, Sapé, etc.
- **Agreste**: Campina Grande, Esperança, Guarabira, etc.
- **Borborema**: Monteiro, Picuí, Soledade
- **Cariri**: Patos, Princesa Isabel, Santa Luzia
- **Sertão**: Cajazeiras, Catolé do Rocha, Itaporanga, Sousa
- **Litoral**: Mamanguape, Pedras de Fogo, Areia

#### **3. Estilos de Mapa**
- **OpenStreetMap**: Padrão com ruas e estradas
- **Satélite**: Imagens de satélite para visão aérea
- **Terreno**: Topografia e relevo da região

#### **4. Estatísticas e Informações**
- **KPIs**: Total de campus, cidades atendidas, cobertura estadual
- **Tabela de Campus**: Lista completa com coordenadas
- **Distribuição por Região**: Métricas por área geográfica
- **Informações Institucionais**: História e missão do IFPB

## 🏛️ Campus Incluídos

### **Região Metropolitana (6 campus)**
- João Pessoa, Cabedelo, Cabedelo Centro, Mangabeira, Santa Rita, Sapé

### **Agreste (6 campus)**
- Campina Grande, Esperança, Guarabira, Itabaiana, Queimadas, Alagoa Grande

### **Borborema (3 campus)**
- Monteiro, Picuí, Soledade

### **Cariri (3 campus)**
- Patos, Princesa Isabel, Santa Luzia

### **Sertão (4 campus)**
- Cajazeiras, Catolé do Rocha, Itaporanga, Sousa

### **Litoral (3 campus)**
- Mamanguape, Pedras de Fogo, Areia

## 🛠️ Tecnologias Utilizadas

- **Folium**: Biblioteca para mapas interativos
- **Streamlit-Folium**: Integração com Streamlit
- **Pandas**: Manipulação de dados
- **Coordenadas GPS**: Localização precisa dos campus

## 📱 Como Usar

1. **Acesse o Sistema**: Execute o dashboard do IFPB-CZ
2. **Navegue para o Mapa**: Clique no botão "🗺️ Mapa dos Campus" na barra lateral
3. **Explore as Opções**:
   - Selecione uma região específica no filtro
   - Escolha o estilo de mapa desejado
   - Clique nos marcadores para ver informações detalhadas
4. **Consulte a Tabela**: Visualize a lista completa de campus abaixo do mapa

## 🎨 Interface

O módulo segue o padrão visual do sistema IFPB-CZ:
- **Cores institucionais**: Verde IFPB (#1a8c73)
- **Design responsivo**: Adapta-se a diferentes tamanhos de tela
- **Navegação intuitiva**: Filtros e controles claros
- **Informações organizadas**: KPIs, mapa e tabela bem estruturados

## 🔧 Instalação

As dependências necessárias foram adicionadas ao `requirements.txt`:
```
folium>=0.14.0
streamlit-folium>=0.14.0
openpyxl>=3.1.0
```

O módulo está totalmente integrado ao sistema principal e pode ser acessado através do menu lateral de navegação.

## 🎯 Resultado

O módulo de mapa está **100% funcional** e oferece uma visualização completa e interativa da rede de campus do IFPB na Paraíba, permitindo aos usuários:

- Visualizar geograficamente todos os campus
- Filtrar por região de interesse
- Obter informações detalhadas de cada campus
- Compreender a distribuição territorial do IFPB
- Acessar dados técnicos e estatísticos

**Status**: ✅ Implementado e Funcional
