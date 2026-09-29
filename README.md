# Projeto de Ciência de Dados - IDD 2023

## Descrição do Projeto

Análise exploratória e modelagem dos microdados do **IDD (Indicador de Diferença entre os Desempenhos) 2023**, disponibilizados pelo INEP.

## Base de Dados

- **Nome**: Microdados do IDD - Edição 2023
- **Fonte**: INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira)
- **Número de instâncias**: 248.889 estudantes
- **Número de atributos**: 19 variáveis
- **Formato**: Arquivo TXT delimitado por ponto e vírgula (;)

> O arquivo de dados brutos (`Microdados_idd_2023/2.DADOS/MICRODADOS_IDD_2023_LGPD.txt`, 21 MB) não é versionado neste repositório.
> Baixe os microdados do IDD 2023 no portal do INEP (https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados) e extraia o arquivo nesse caminho antes de rodar as análises.

## Estrutura do Projeto

```
microdados_IDD_2023/
├── Microdados_idd_2023/        # Dados originais
│   ├── 1.LEIA-ME/              # Documentação e dicionário
│   └── 2.DADOS/                # Arquivo de dados
├── notebooks/                   # Notebooks Jupyter
├── src/                        # Scripts Python
├── outputs/                    # Gráficos e resultados
├── requirements.txt            # Dependências
└── README.md                   # Este arquivo
```

## Instalação

```bash
pip install -r requirements.txt
```

## Sprint 1 - Análise Exploratória

### Objetivos
- Carregar e compreender a base de dados
- Realizar análise descritiva completa
- Criar visualizações (histogramas, boxplots, scatter plots, matriz de correlação)
- Identificar padrões, relações e possíveis problemas nos dados

### Entregas
1. Código da análise exploratória (disponível no GitHub)
2. Gráficos e visualizações com interpretações
3. Relatório seguindo o modelo fornecido (Seção 3 e Seção 4 - Parte 1)
4. Quadro Kanban no Trello

## Oportunidades de Modelagem Preditiva

Os microdados do IDD 2023 oferecem diversas oportunidades para desenvolvimento de modelos preditivos:

### 1. Regressão - Predição de Desempenho

**Objetivo**: Prever a nota geral do IDD (NT_GER) com base nas características dos estudantes

**Variáveis Preditoras**:
- Notas do ENEM (Ciências Naturais, Ciências Humanas, Linguagens, Matemática)
- Ano de início da graduação
- Características do curso (código, modalidade, grupo)
- Características da IES (categoria administrativa, organização acadêmica)
- Localização geográfica (município do curso)

**Aplicações**:
- Identificar fatores que mais influenciam o desempenho acadêmico
- Prever o desempenho esperado de novos ingressantes
- Auxiliar instituições na identificação de alunos em risco
- Orientar políticas de apoio pedagógico

### 2. Classificação - Predição de Faixas de Desempenho

**Objetivo**: Classificar estudantes em categorias de desempenho (baixo, médio, alto)

**Categorias Possíveis**:
- Desempenho Insuficiente (NT_GER < 40)
- Desempenho Adequado (40 ≤ NT_GER < 70)
- Desempenho Excelente (NT_GER ≥ 70)

**Aplicações**:
- Identificação precoce de alunos em risco de baixo desempenho
- Alocação eficiente de recursos de apoio acadêmico
- Avaliação da efetividade de programas de nivelamento

### 3. Clustering - Segmentação de Perfis

**Objetivo**: Identificar grupos homogêneos de estudantes com características similares

**Dimensões de Análise**:
- Perfil de entrada (notas ENEM, ano de ingresso)
- Tipo de instituição e curso
- Desempenho acadêmico (NT_GER)

**Aplicações**:
- Personalização de estratégias pedagógicas
- Identificação de perfis de sucesso acadêmico
- Benchmarking entre instituições

### 4. Análise de Séries Temporais

**Objetivo**: Analisar a evolução do desempenho ao longo dos anos

**Variáveis Temporais**:
- ANO_INICIO_GRAD (ano de início da graduação)
- ANO_ENEM (ano de realização do ENEM)
- Comparação com edições anteriores do IDD

**Aplicações**:
- Identificar tendências de melhoria ou declínio
- Avaliar impacto de mudanças curriculares
- Projetar desempenho futuro

### 5. Análise Comparativa - Benchmarking

**Objetivo**: Comparar o desempenho entre diferentes grupos

**Dimensões de Comparação**:
- Por instituição (CO_IES)
- Por curso (CO_CURSO)
- Por modalidade (presencial vs. EAD)
- Por região geográfica

**Aplicações**:
- Identificar melhores práticas
- Avaliar competitividade institucional
- Orientar decisões estratégicas

### Técnicas de Machine Learning Sugeridas

**Regressão**:
- Regressão Linear (baseline)
- Random Forest Regressor
- Gradient Boosting (XGBoost, LightGBM)
- Redes Neurais (MLP)

**Classificação**:
- Logistic Regression
- Decision Trees
- Random Forest Classifier
- Support Vector Machines (SVM)
- Gradient Boosting Classifier

**Clustering**:
- K-Means
- DBSCAN
- Hierarchical Clustering
- Gaussian Mixture Models

## Equipe

[Adicionar nomes dos membros da equipe]

## Período de Desenvolvimento

Sprint 1: 16 a 30 de setembro de 2026
