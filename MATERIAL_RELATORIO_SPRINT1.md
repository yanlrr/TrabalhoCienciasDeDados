[MATERIAL_RELATORIO_SPRINT1.1.md](https://github.com/user-attachments/files/32868579/MATERIAL_RELATORIO_SPRINT1.1.md)
# Material para Relatório - Sprint 1

Este documento contém todo o material necessário para preencher as **Seções 3 e 4 (Parte 1)** do relatório seguindo o modelo fornecido.

---

## SEÇÃO 3 - PROTOCOLO EXPERIMENTAL

### 3.1 Descrição da Base de Dados

#### Nome da Base de Dados

Microdados do IDD (Indicador de Diferença entre os Desempenhos) - Edição 2023

#### Fonte ou Repositório de Origem

INEP - Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira
URL: <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados>

> O arquivo de dados brutos (`Microdados_idd_2023/2.DADOS/MICRODADOS_IDD_2023_LGPD.txt`) não é versionado neste repositório. Para reproduzir a análise, baixe os microdados do IDD 2023 no portal do INEP e extraia o arquivo nesse caminho.

#### Contexto e Finalidade da Base

O Indicador de Diferença entre os Desempenhos Observado e Esperado (IDD) é uma das medidas utilizadas no Sistema Nacional de Avaliação da Educação Superior (SINAES). O IDD tem por objetivo avaliar a qualidade dos cursos de graduação, considerando o valor agregado pelo curso ao desenvolvimento dos estudantes concluintes.

O IDD mede a diferença entre o desempenho médio observado dos concluintes de um curso e o desempenho médio esperado para esses concluintes. O desempenho esperado é calculado com base no perfil dos estudantes ingressantes do curso, representado pelas suas notas no Exame Nacional do Ensino Médio (ENEM).

**Finalidade**:
- Avaliar a qualidade dos cursos de graduação no Brasil
- Medir o valor agregado pelos cursos ao desenvolvimento dos estudantes
- Fornecer informações para políticas públicas de melhoria da educação superior
- Orientar estudantes e famílias na escolha de cursos e instituições

#### Problema Investigado e Tipo de Tarefa

- **Tipo de tarefa**: **Regressão**
- **Variável-alvo**: `NT_GER` (nota geral do concluinte), variável numérica contínua de 0 a 100
- **Problema**: prever a nota geral do concluinte (`NT_GER`) com base nas características dos estudantes, do curso e da instituição
- **Variáveis preditoras**:
  - Notas do ENEM (Ciências da Natureza, Ciências Humanas, Linguagens e Códigos, Matemática)
  - Ano de início da graduação
  - Características do curso (código, modalidade, grupo)
  - Características da IES (categoria administrativa, organização acadêmica)
  - Localização geográfica (município do curso)
- **Distribuição das classes**: não se aplica, por se tratar de uma tarefa de regressão

#### Objetivo da Análise

O objetivo da equipe nesta Sprint 1 é compreender a base de dados antes da modelagem:
- Carregar e compreender a estrutura da base
- Realizar a análise descritiva das variáveis
- Criar visualizações (histogramas, boxplots, gráficos de dispersão, matriz de correlação)
- Identificar padrões, relações e possíveis problemas nos dados

Com isso, busca-se entender quais características do perfil de ingresso (notas do ENEM) e do contexto institucional estão associadas ao desempenho dos concluintes, preparando a construção dos modelos de regressão das próximas sprints.

#### Número de Instâncias e Atributos

- **Número de instâncias**: 248.889 registros (estudantes)
- **Número de atributos**: 19 variáveis

#### Tipos dos Atributos

**Variáveis Numéricas** (8 variáveis):

Contínuas:
1. `NT_GER` - Nota Geral do IDD
2. `ENEM_NT_CN` - Nota ENEM: Ciências da Natureza
3. `ENEM_NT_CH` - Nota ENEM: Ciências Humanas
4. `ENEM_NT_LC` - Nota ENEM: Linguagens e Códigos
5. `ENEM_NT_MT` - Nota ENEM: Matemática

Discretas (temporais):

6. `ANO_INICIO_GRAD` - Ano de Início da Graduação
7. `ANO_ENEM` - Ano de Realização do ENEM
8. `NU_ANO` - Ano de Referência (2023)

**Variáveis Categóricas** (11 variáveis):
1. `CO_IES` - Código da Instituição de Ensino Superior
2. `CO_CATEGAD` - Código da Categoria Administrativa
3. `CO_ORGACAD` - Código da Organização Acadêmica
4. `CO_GRUPO` - Código do Grupo do Curso
5. `CO_CURSO` - Código do Curso
6. `CO_MODALIDADE` - Código da Modalidade (Presencial/EAD)
7. `CO_MUNIC_CURSO` - Código do Município do Curso
8. `TP_INSCRICAO` - Tipo de Inscrição
9. `IN_REGULAR` - Indicador de Regularidade
10. `TP_INSCRICAO_ADM` - Tipo de Inscrição Administrativa
11. `TP_PRES` - Tipo de Presença

#### Presença de Valores Ausentes

**Análise de completude dos dados**:
- ✓ **Nenhum valor ausente** foi identificado no dataset
- Taxa de completude: **100%**
- Todas as 19 variáveis estão completamente preenchidas
- Total de células: 4.728.891 (248.889 × 19)
- Células com dados: 4.728.891 (100%)

Há, porém, registros com nota igual a zero nas quatro áreas do ENEM, isolados do restante da distribuição, que provavelmente indicam ausência ou eliminação no exame (ver Seção 4.1.2).

#### Outras Características Relevantes

**Formato, Tamanho e Estrutura**:
- Arquivo TXT delimitado por ponto e vírgula (;)
- Arquivo: `MICRODADOS_IDD_2023_LGPD.txt`
- Tamanho: aproximadamente **21 MB**
- Codificação: Latin-1 (ISO-8859-1)
- Primeira linha contém os nomes das variáveis (header)
- Dados estruturados em formato tabular (uma linha por estudante)
- Documentação e dicionário de dados disponíveis na pasta `Microdados_idd_2023/1.LEIA-ME/`

**Distribuição Temporal**:
- Anos de início de graduação: variam de 2009 a 2023 (concentrados em 2018 e 2019)
- Anos de realização do ENEM: variam de 2009 a 2022 (concentrados em 2017 e 2018)
- Representa uma amostra longitudinal de estudantes

**Distribuição Geográfica**:
- Contempla instituições de diferentes municípios brasileiros
- Permite análises regionais e comparativas

**Atributos Constantes**:
- `NU_ANO` (sempre 2023), `TP_INSCRICAO` (sempre 1), `IN_REGULAR` (sempre 1) e `TP_INSCRICAO_ADM` (sempre 0) não variam na base e, portanto, não contribuem para a modelagem

**Desbalanceamento**:
- 95,9% dos estudantes pertencem a cursos presenciais e 4,1% a cursos a distância

**Conformidade com LGPD**:
- Dados anonimizados conforme Lei Geral de Proteção de Dados
- Não contém informações pessoais identificáveis dos estudantes

---

## SEÇÃO 4 - RESULTADOS

### PARTE 1 - ANÁLISE EXPLORATÓRIA DOS DADOS

A análise exploratória foi implementada em Python, em notebooks Jupyter, com as seguintes bibliotecas e versões: pandas 2.1.4, numpy 1.26.3, matplotlib 3.8.2, seaborn 0.13.1, scipy 1.11.4, jupyter 1.0.0, notebook 7.0.6 e openpyxl 3.1.2.

Nos gráficos, os códigos de identificação (`CO_IES`, `CO_GRUPO`, `CO_CURSO` e `CO_MUNIC_CURSO`) aparecem ao lado das variáveis numéricas por estarem armazenados como números. Como são categóricos, suas médias, dispersões e correlações não têm interpretação de magnitude e são comentadas apenas quando revelam algo sobre a estrutura dos dados.

#### 4.1.1 Estatísticas Descritivas das Variáveis Numéricas

**Tabela 1: Estatísticas Descritivas - Variáveis Numéricas**

| Variável | Média | Mediana | Outliers (IQR) |
|----------|-------|---------|----------------|
| NT_GER | 50,64 | 50,60 | 0,04% |
| ENEM_NT_CN | 547,80 | 548,60 | 0,03% |
| ENEM_NT_CH | 586,81 | 599,60 | 0,75% |
| ENEM_NT_LC | 555,96 | 561,90 | 1,34% |
| ENEM_NT_MT | 594,12 | 587,40 | 0,02% |
| ANO_INICIO_GRAD | 2018,48 | 2019 | 11,91% |
| ANO_ENEM | 2017,27 | 2018 | 11,58% |

*Valores obtidos dos histogramas (Figura 1) e dos boxplots (Figura 2).*

**Interpretação**:

- A nota geral (`NT_GER`) tem média de 50,64 e mediana de 50,60, valores praticamente iguais, o que indica distribuição simétrica em torno do centro da escala de 0 a 100.
- Entre as notas do ENEM, Matemática apresenta a maior média (594,12), seguida de Ciências Humanas (586,81), Linguagens e Códigos (555,96) e Ciências da Natureza (547,80).
- Em Ciências Humanas e em Linguagens a mediana supera a média, sinal de assimetria à esquerda; em Matemática ocorre o inverso, com leve assimetria à direita.
- Essas diferenças de perfil de ingresso são a base sobre a qual o IDD procura medir o valor agregado pelos cursos.

#### 4.1.2 Distribuições das Variáveis - Histogramas

**Figura 1: Histogramas das Variáveis Numéricas (média em vermelho, mediana em verde)**

![Histogramas](https://github.com/Lucaslust/TrabalhoCienciasDeDados/raw/main/outputs/histogramas.png)

**Interpretação dos Histogramas**:

1. **NT_GER (Nota Geral)**:
   - Distribuição unimodal, aproximadamente normal e simétrica
   - A maior parte dos estudantes está entre 20 e 80 pontos, com poucos casos próximos de 0 ou de 100
   - Esse formato é favorável a um problema de regressão, pois a variável-alvo cobre toda a escala sem concentração excessiva em uma faixa

2. **Notas do ENEM**:
   - Todas as distribuições são unimodais
   - **Matemática** é a mais dispersa, com valores que chegam perto de 1.000
   - **Linguagens** é a mais concentrada
   - **Ciências Humanas e Linguagens** têm cauda mais longa à esquerda; **Ciências da Natureza** é praticamente simétrica
   - **Notas zero**: em todas as áreas há um pequeno acúmulo de registros com nota 0, isolado do restante da distribuição (que começa por volta de 300 pontos). Como a nota zero no ENEM normalmente corresponde a ausência ou eliminação, e não a desempenho real, esses registros deverão ser investigados e provavelmente tratados como valores ausentes

3. **Variáveis Temporais e Códigos**:
   - `ANO_INICIO_GRAD` varia de 2009 a 2023, concentrando-se em 2018 e 2019
   - `ANO_ENEM` varia de 2009 a 2022, concentrando-se em 2017 e 2018
   - `NU_ANO` assume um único valor (2023)
   - `CO_GRUPO` se divide em duas faixas de valores muito distantes (abaixo de 100 e acima de 5.700), reforçando que se trata de um identificador categórico

#### 4.1.3 Identificação de Outliers - Boxplots

**Figura 2: Boxplots com o número e a proporção de outliers pelo critério do IQR**

![Boxplots](https://github.com/Lucaslust/TrabalhoCienciasDeDados/raw/main/outputs/boxplots.png)

**Interpretação dos Boxplots**:

1. **Variáveis de Desempenho**:
   - A proporção de outliers é pequena
   - **NT_GER**: 0,04% dos registros, nas duas extremidades (notas abaixo de cerca de 6 pontos e acima de 95)
   - **Matemática (0,02%) e Ciências da Natureza (0,03%)**: quase não têm outliers
   - **Linguagens (1,34%) e Ciências Humanas (0,75%)**: concentram outliers na parte inferior, coerente com a assimetria à esquerda observada nos histogramas
   - Em todas as áreas do ENEM há pontos isolados em 0, os mesmos registros de nota zero já identificados

2. **Dispersão Interquartílica**:
   - A caixa de Matemática é a mais larga (aproximadamente de 490 a 690), confirmando a maior dispersão dessa área
   - A caixa de `NT_GER` vai de cerca de 40 a 62 pontos

3. **Variáveis Temporais e Códigos**:
   - `ANO_INICIO_GRAD` (11,91%) e `ANO_ENEM` (11,58%) têm cerca de 12% de outliers, que correspondem aos estudantes que ingressaram muito antes da maioria, ou seja, alunos que levaram mais tempo para concluir o curso
   - Nos códigos, como `CO_IES` (11,06%), os "outliers" apenas refletem a numeração das instituições e não têm significado

4. **Implicações para Modelagem**:
   - Os outliers das notas representam casos reais e raros e não devem ser removidos automaticamente
   - A exceção são as notas zero do ENEM, que devem ser tratadas como possível dado inválido
   - Os outliers temporais carregam informação relevante sobre o tempo de curso, que pode ser explorada como atributo derivado

#### 4.1.4 Relações entre Variáveis - Gráfico de Dispersão

**Figura 3: Dispersão entre ENEM Matemática e Nota Geral, com reta de tendência**

![Scatter Plot MT vs GER](https://github.com/Lucaslust/TrabalhoCienciasDeDados/raw/main/outputs/scatter_mt_vs_ger.png)

**Interpretação do Gráfico de Dispersão**:

1. **Relação Positiva**:
   - A reta de tendência (y = 0,056x + 17,28) indica que cada 100 pontos a mais em Matemática no ENEM correspondem, em média, a cerca de 5,6 pontos a mais na nota geral
   - Um estudante com 400 pontos tem nota geral esperada de aproximadamente 40; um com 800 pontos, de aproximadamente 62

2. **Dispersão dos Pontos**:
   - A dispersão vertical é grande em todas as faixas de nota do ENEM: estudantes com a mesma nota de ingresso obtêm notas gerais que variam de cerca de 20 a 80 pontos
   - A nota de Matemática é um preditor relevante, mas insuficiente sozinho; outros fatores (demais áreas do ENEM, curso, instituição) precisam ser incorporados ao modelo
   - A diferença entre o desempenho previsto pela reta e o observado é justamente o tipo de variação que o IDD interpreta como valor agregado
   - O ponto isolado em x = 0 corresponde novamente a uma nota zero no ENEM

#### 4.1.5 Matriz de Correlação

**Figura 4: Matriz de Correlação de Pearson entre as Variáveis Numéricas**

![Matriz de Correlação](https://github.com/Lucaslust/TrabalhoCienciasDeDados/raw/main/outputs/matriz_correlacao.png)

**Interpretação da Matriz de Correlação**:

1. **Correlações com NT_GER** (variável-alvo):
   - **ENEM_NT_LC**: r = 0,52
   - **ENEM_NT_CN**: r = 0,50
   - **ENEM_NT_CH**: r = 0,50
   - **ENEM_NT_MT**: r = 0,44
   - Linguagens é o preditor individual mais forte e Matemática o mais fraco, embora a diferença entre eles seja pequena
   - Nenhuma correlação ultrapassa 0,52, indicando que o desempenho no ingresso explica apenas parte da nota geral, o que é coerente com a proposta do IDD

2. **Correlações entre Preditores**:
   - As notas do ENEM são fortemente correlacionadas entre si (r entre 0,61 e 0,72; os maiores valores são CN ↔ MT e CH ↔ LC, ambos 0,72), caracterizando multicolinearidade
   - A correlação mais alta da matriz é entre `ANO_INICIO_GRAD` e `ANO_ENEM` (r = 0,93), esperada porque a maioria dos estudantes ingressa logo após o ENEM; essas duas variáveis são praticamente redundantes
   - Os anos de ingresso quase não se correlacionam com `NT_GER` (r = -0,05 e -0,01)
   - `NU_ANO` aparece sem valores porque é constante e sua correlação não é definida

3. **Área do Curso**:
   - `CO_GRUPO` apresenta correlação de -0,28 com `NT_GER`. Por ser um código, esse valor não deve ser interpretado diretamente, mas sugere que a área do curso está associada ao desempenho e deve ser incluída no modelo como variável categórica

4. **Implicações para Modelagem**:
   - Criar uma média das notas do ENEM
   - Manter apenas um dos dois anos (ou derivar o intervalo entre eles)
   - Usar regularização (Ridge, Lasso) ou comitês baseados em árvores, que lidam bem com atributos correlacionados
   - Avaliar a Análise de Componentes Principais (PCA)

#### 4.1.6 Análise de Variáveis Categóricas

**Figura 5: Frequência das Categorias das Variáveis Categóricas**

![Variáveis Categóricas](https://github.com/Lucaslust/TrabalhoCienciasDeDados/raw/main/outputs/variaveis_categoricas.png)

**Interpretação das Variáveis Categóricas**:

1. **CO_MODALIDADE (Modalidade do Curso)**:
   - 238.682 estudantes (95,9%) na categoria 1 e apenas 10.207 (4,1%) na categoria 0, que segundo o dicionário do INEP correspondem a cursos presenciais e a distância, respectivamente

2. **CO_ORGACAD (Organização Acadêmica)**:
   - 10028 (Universidade): 130.541 estudantes (52,4%)
   - 10020 (Centro Universitário): 70.536
   - 10022 (Faculdade): 36.949
   - 10026 (Instituto Federal): 9.781
   - 10019 (CEFET): 1.082

3. **CO_CATEGAD (Categoria Administrativa)**:
   - Categoria 4 é a mais frequente (101.242), seguida das categorias 1 (62.945), 5 (42.819), 8 (22.356) e 2 (16.203)
   - As categorias 3 (2.179) e 7 (1.145) são raras

4. **Variáveis Constantes**:
   - `TP_INSCRICAO` (sempre 1), `IN_REGULAR` (sempre 1) e `TP_INSCRICAO_ADM` (sempre 0) não variam em toda a base
   - Somadas a `NU_ANO`, são quatro atributos sem variabilidade, que não contribuem para a previsão e devem ser removidos, reduzindo o conjunto útil a 15 atributos

5. **Implicações para Modelagem**:
   - O desbalanceamento implica poucos exemplos de cursos EAD e de categorias administrativas raras, o que pode reduzir a qualidade das previsões nesses grupos e deve ser considerado na divisão dos dados (por exemplo, com amostragem estratificada)
   - Variáveis com poucas categorias podem ser codificadas por One-Hot Encoding; as de alta cardinalidade (`CO_IES`, `CO_CURSO`, `CO_MUNIC_CURSO`) exigirão técnicas como Target Encoding

#### 4.1.7 Síntese da Análise Exploratória

- **Qualidade dos dados**: não há valores ausentes declarados, mas existem notas iguais a zero no ENEM que provavelmente representam dados inválidos, e quatro atributos constantes (`NU_ANO`, `TP_INSCRICAO`, `IN_REGULAR`, `TP_INSCRICAO_ADM`)
- **Variável-alvo**: `NT_GER` tem distribuição aproximadamente normal e simétrica (média 50,64; mediana 50,60), com pouquíssimos outliers, adequada à modelagem por regressão
- **Preditores**: as notas do ENEM têm correlação moderada com a nota geral (r de 0,44 a 0,52), com Linguagens como a mais forte; a área do curso também parece associada ao desempenho
- **Desafios**: multicolinearidade entre as notas do ENEM e entre os dois anos de ingresso (r = 0,93), forte desbalanceamento das variáveis categóricas (95,9% de cursos presenciais) e códigos de alta cardinalidade
- **Oportunidades**: a grande variação da nota geral entre estudantes com o mesmo perfil de ingresso indica espaço para identificar fatores de curso e instituição que agregam valor, objetivo das próximas sprints

---

## Referências

1. INEP - Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira. **Microdados do IDD 2023**. Brasília: INEP, 2023.

2. BRASIL. Lei nº 10.861, de 14 de abril de 2004. Institui o Sistema Nacional de Avaliação da Educação Superior – SINAES. Diário Oficial da União, Brasília, DF, 15 abr. 2004.

3. INEP. **Nota Técnica: Indicador de Diferença entre os Desempenhos Observado e Esperado (IDD)**. Brasília: INEP, 2023.

---

**Data de elaboração**: Setembro 2026
**Sprint**: 1 - Análise Exploratória dos Dados
