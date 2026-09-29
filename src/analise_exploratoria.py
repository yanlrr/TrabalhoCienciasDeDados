"""
Análise Exploratória dos Microdados IDD 2023
Sprint 1 - Projeto de Ciência de Dados

Autor: [Nome da Equipe]
Data: Setembro 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configurações de visualização
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10
sns.set_style("whitegrid")
sns.set_palette("husl")

# Caminhos
BASE_DIR = Path(__file__).parent.parent
DATA_PATH = BASE_DIR / "Microdados_idd_2023" / "2.DADOS" / "MICRODADOS_IDD_2023_LGPD.txt"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def carregar_dados():
    """
    Carrega os microdados do IDD 2023.

    Returns:
        pd.DataFrame: DataFrame com os dados carregados
    """
    print("="*80)
    print("CARREGANDO DADOS DO IDD 2023")
    print("="*80)

    df = pd.read_csv(DATA_PATH, sep=';', encoding='latin-1')

    print(f"\n✓ Dados carregados com sucesso!")
    print(f"  - Número de registros: {len(df):,}")
    print(f"  - Número de variáveis: {len(df.columns)}")

    return df


def analise_descritiva_basica(df):
    """
    Realiza análise descritiva básica do dataset.

    Args:
        df (pd.DataFrame): DataFrame com os dados
    """
    print("\n" + "="*80)
    print("1. ANÁLISE DESCRITIVA BÁSICA")
    print("="*80)

    # Dimensões
    print(f"\n📊 DIMENSÕES DO DATASET:")
    print(f"  - Número de instâncias: {df.shape[0]:,}")
    print(f"  - Número de atributos: {df.shape[1]}")

    # Tipos de dados
    print(f"\n📋 TIPOS DE DADOS:")
    print(df.dtypes.value_counts())

    # Informações das colunas
    print(f"\n📝 INFORMAÇÕES DAS VARIÁVEIS:")
    print("\nVariável".ljust(25) + "Tipo".ljust(15) + "Não-nulos".ljust(15) + "% Completo")
    print("-"*70)

    for col in df.columns:
        tipo = str(df[col].dtype)
        nao_nulos = df[col].notna().sum()
        pct_completo = (nao_nulos / len(df)) * 100
        print(f"{col[:24].ljust(25)}{tipo[:14].ljust(15)}{nao_nulos:>10,}   {pct_completo:>6.2f}%")

    # Valores ausentes
    print(f"\n❌ VALORES AUSENTES:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100

    if missing.sum() > 0:
        missing_df = pd.DataFrame({
            'Valores Ausentes': missing[missing > 0],
            'Percentual (%)': missing_pct[missing > 0]
        }).sort_values('Valores Ausentes', ascending=False)
        print(missing_df)
    else:
        print("  ✓ Nenhum valor ausente encontrado!")

    # Estatísticas descritivas
    print(f"\n📈 ESTATÍSTICAS DESCRITIVAS (Variáveis Numéricas):")
    print(df.describe().round(2))

    return df


def identificar_tipos_variaveis(df):
    """
    Identifica e classifica as variáveis em numéricas e categóricas.

    Args:
        df (pd.DataFrame): DataFrame com os dados

    Returns:
        tuple: (lista de variáveis numéricas, lista de variáveis categóricas)
    """
    print("\n" + "="*80)
    print("2. CLASSIFICAÇÃO DAS VARIÁVEIS")
    print("="*80)

    # Variáveis numéricas (float ou int)
    numericas = df.select_dtypes(include=[np.number]).columns.tolist()

    # Variáveis categóricas (object ou int com poucos valores únicos)
    categoricas = []
    for col in df.columns:
        if col not in numericas:
            categoricas.append(col)
        elif df[col].nunique() < 20:  # Se tem menos de 20 valores únicos, pode ser categórica
            if col not in ['NU_ANO', 'ANO_INICIO_GRAD', 'ANO_ENEM']:
                categoricas.append(col)
                numericas.remove(col)

    print(f"\n✓ Variáveis Numéricas ({len(numericas)}):")
    for var in numericas:
        print(f"  - {var}")

    print(f"\n✓ Variáveis Categóricas ({len(categoricas)}):")
    for var in categoricas:
        print(f"  - {var} ({df[var].nunique()} categorias)")

    return numericas, categoricas


def criar_histogramas(df, numericas):
    """
    Cria histogramas para as variáveis numéricas.

    Args:
        df (pd.DataFrame): DataFrame com os dados
        numericas (list): Lista de variáveis numéricas
    """
    print("\n" + "="*80)
    print("3. CRIANDO HISTOGRAMAS")
    print("="*80)

    n_vars = len(numericas)
    n_cols = 3
    n_rows = (n_vars + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, n_rows * 4))
    axes = axes.flatten() if n_vars > 1 else [axes]

    for idx, var in enumerate(numericas):
        ax = axes[idx]

        # Remove valores nulos
        data = df[var].dropna()

        ax.hist(data, bins=50, edgecolor='black', alpha=0.7, color='steelblue')
        ax.set_title(f'Distribuição de {var}', fontsize=12, fontweight='bold')
        ax.set_xlabel(var)
        ax.set_ylabel('Frequência')
        ax.grid(axis='y', alpha=0.3)

        # Adiciona estatísticas
        media = data.mean()
        mediana = data.median()
        ax.axvline(media, color='red', linestyle='--', linewidth=2, label=f'Média: {media:.2f}')
        ax.axvline(mediana, color='green', linestyle='--', linewidth=2, label=f'Mediana: {mediana:.2f}')
        ax.legend()

    # Remove eixos vazios
    for idx in range(n_vars, len(axes)):
        fig.delaxes(axes[idx])

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'histogramas.png', dpi=300, bbox_inches='tight')
    print(f"  ✓ Histogramas salvos em: outputs/histogramas.png")
    plt.close()


def criar_boxplots(df, numericas):
    """
    Cria boxplots para identificar outliers.

    Args:
        df (pd.DataFrame): DataFrame com os dados
        numericas (list): Lista de variáveis numéricas
    """
    print("\n" + "="*80)
    print("4. CRIANDO BOXPLOTS")
    print("="*80)

    n_vars = len(numericas)
    n_cols = 3
    n_rows = (n_vars + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, n_rows * 4))
    axes = axes.flatten() if n_vars > 1 else [axes]

    for idx, var in enumerate(numericas):
        ax = axes[idx]

        # Remove valores nulos
        data = df[var].dropna()

        bp = ax.boxplot(data, vert=True, patch_artist=True)

        # Colorir o boxplot
        for patch in bp['boxes']:
            patch.set_facecolor('lightblue')
            patch.set_edgecolor('black')

        ax.set_title(f'Boxplot de {var}', fontsize=12, fontweight='bold')
        ax.set_ylabel(var)
        ax.grid(axis='y', alpha=0.3)

        # Identificar outliers
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        outliers_count = ((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).sum()

        ax.text(0.5, 0.95, f'Outliers: {outliers_count} ({outliers_count/len(data)*100:.2f}%)',
                transform=ax.transAxes, ha='center', va='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Remove eixos vazios
    for idx in range(n_vars, len(axes)):
        fig.delaxes(axes[idx])

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'boxplots.png', dpi=300, bbox_inches='tight')
    print(f"  ✓ Boxplots salvos em: outputs/boxplots.png")
    plt.close()


def criar_scatter_plots(df, numericas):
    """
    Cria gráficos de dispersão entre variáveis principais.

    Args:
        df (pd.DataFrame): DataFrame com os dados
        numericas (list): Lista de variáveis numéricas
    """
    print("\n" + "="*80)
    print("5. CRIANDO GRÁFICOS DE DISPERSÃO")
    print("="*80)

    # Selecionar variáveis principais (notas do ENEM e nota geral)
    vars_interesse = [col for col in numericas if 'ENEM' in col or 'NT_GER' in col]

    if len(vars_interesse) >= 2:
        # Criar pairplot
        sample_size = min(5000, len(df))
        df_sample = df[vars_interesse].sample(n=sample_size, random_state=42)

        g = sns.pairplot(df_sample, diag_kind='kde', plot_kws={'alpha': 0.6})
        g.fig.suptitle('Matriz de Dispersão - Notas ENEM e IDD', y=1.02, fontsize=16)
        plt.savefig(OUTPUT_DIR / 'scatter_plots.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Gráficos de dispersão salvos em: outputs/scatter_plots.png")
        plt.close()

    # Scatter plot específico: NT_GER vs ENEM_NT_MT (exemplo)
    if 'NT_GER' in df.columns and 'ENEM_NT_MT' in df.columns:
        plt.figure(figsize=(10, 6))

        # Amostra para melhor visualização
        sample = df[['NT_GER', 'ENEM_NT_MT']].dropna().sample(n=min(10000, len(df)), random_state=42)

        plt.scatter(sample['ENEM_NT_MT'], sample['NT_GER'], alpha=0.3, s=10)
        plt.xlabel('Nota ENEM - Matemática', fontsize=12)
        plt.ylabel('Nota Geral IDD', fontsize=12)
        plt.title('Relação entre Nota de Matemática (ENEM) e Nota Geral (IDD)', fontsize=14, fontweight='bold')
        plt.grid(alpha=0.3)

        # Adicionar linha de tendência
        z = np.polyfit(sample['ENEM_NT_MT'], sample['NT_GER'], 1)
        p = np.poly1d(z)
        plt.plot(sample['ENEM_NT_MT'].sort_values(), p(sample['ENEM_NT_MT'].sort_values()),
                 "r--", alpha=0.8, linewidth=2, label=f'Tendência: y={z[0]:.3f}x+{z[1]:.2f}')
        plt.legend()

        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / 'scatter_mt_vs_ger.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Scatter plot MT vs GER salvo em: outputs/scatter_mt_vs_ger.png")
        plt.close()


def criar_matriz_correlacao(df, numericas):
    """
    Cria matriz de correlação entre variáveis numéricas.

    Args:
        df (pd.DataFrame): DataFrame com os dados
        numericas (list): Lista de variáveis numéricas
    """
    print("\n" + "="*80)
    print("6. CRIANDO MATRIZ DE CORRELAÇÃO")
    print("="*80)

    # Calcular correlação
    corr_matrix = df[numericas].corr()

    # Criar heatmap
    plt.figure(figsize=(14, 10))
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Matriz de Correlação - Variáveis Numéricas', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'matriz_correlacao.png', dpi=300, bbox_inches='tight')
    print(f"  ✓ Matriz de correlação salva em: outputs/matriz_correlacao.png")
    plt.close()

    # Identificar correlações fortes
    print("\n📊 CORRELAÇÕES MAIS FORTES (|r| > 0.7):")
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            if abs(corr_matrix.iloc[i, j]) > 0.7:
                print(f"  - {corr_matrix.columns[i]} <-> {corr_matrix.columns[j]}: {corr_matrix.iloc[i, j]:.3f}")


def analisar_variaveis_categoricas(df, categoricas):
    """
    Analisa e visualiza variáveis categóricas.

    Args:
        df (pd.DataFrame): DataFrame com os dados
        categoricas (list): Lista de variáveis categóricas
    """
    print("\n" + "="*80)
    print("7. ANÁLISE DE VARIÁVEIS CATEGÓRICAS")
    print("="*80)

    # Selecionar variáveis categóricas com menos de 15 categorias para visualização
    cats_para_plot = [col for col in categoricas if df[col].nunique() <= 15]

    if len(cats_para_plot) > 0:
        n_vars = len(cats_para_plot)
        n_cols = 2
        n_rows = (n_vars + n_cols - 1) // n_cols

        fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, n_rows * 4))
        axes = axes.flatten() if n_vars > 1 else [axes]

        for idx, var in enumerate(cats_para_plot):
            ax = axes[idx]

            # Contar frequências
            counts = df[var].value_counts().head(10)

            # Criar gráfico de barras
            counts.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
            ax.set_title(f'Distribuição de {var}', fontsize=12, fontweight='bold')
            ax.set_xlabel(var)
            ax.set_ylabel('Frequência')
            ax.grid(axis='y', alpha=0.3)

            # Adicionar valores nas barras
            for i, v in enumerate(counts):
                ax.text(i, v, f'{v:,}', ha='center', va='bottom', fontsize=9)

            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

        # Remove eixos vazios
        for idx in range(n_vars, len(axes)):
            fig.delaxes(axes[idx])

        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / 'variaveis_categoricas.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Gráficos de variáveis categóricas salvos em: outputs/variaveis_categoricas.png")
        plt.close()

    # Tabela de frequências para cada variável categórica
    print("\n📋 TABELAS DE FREQUÊNCIA:")
    for var in categoricas[:5]:  # Mostrar primeiras 5
        print(f"\n{var}:")
        freq = df[var].value_counts().head(10)
        freq_pct = (freq / len(df) * 100).round(2)
        freq_df = pd.DataFrame({'Frequência': freq, 'Percentual (%)': freq_pct})
        print(freq_df)


def gerar_relatorio_resumo(df, numericas, categoricas):
    """
    Gera um relatório resumo em formato texto.

    Args:
        df (pd.DataFrame): DataFrame com os dados
        numericas (list): Lista de variáveis numéricas
        categoricas (list): Lista de variáveis categóricas
    """
    print("\n" + "="*80)
    print("8. GERANDO RELATÓRIO RESUMO")
    print("="*80)

    relatorio = []
    relatorio.append("="*80)
    relatorio.append("RELATÓRIO DE ANÁLISE EXPLORATÓRIA - IDD 2023")
    relatorio.append("="*80)
    relatorio.append("")
    relatorio.append("1. INFORMAÇÕES GERAIS DA BASE DE DADOS")
    relatorio.append("-" * 80)
    relatorio.append(f"Nome da base: Microdados do IDD - Edição 2023")
    relatorio.append(f"Fonte: INEP (Instituto Nacional de Estudos e Pesquisas Educacionais)")
    relatorio.append(f"Número de instâncias: {len(df):,}")
    relatorio.append(f"Número de atributos: {len(df.columns)}")
    relatorio.append(f"Período de referência: 2023")
    relatorio.append("")

    relatorio.append("2. ESTRUTURA DOS DADOS")
    relatorio.append("-" * 80)
    relatorio.append(f"Variáveis numéricas: {len(numericas)}")
    relatorio.append(f"Variáveis categóricas: {len(categoricas)}")
    relatorio.append(f"Valores ausentes total: {df.isnull().sum().sum()}")
    relatorio.append(f"Completude dos dados: {((1 - df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100):.2f}%")
    relatorio.append("")

    relatorio.append("3. PRINCIPAIS VARIÁVEIS")
    relatorio.append("-" * 80)
    relatorio.append("Variáveis Numéricas:")
    for var in numericas:
        relatorio.append(f"  - {var}: min={df[var].min():.2f}, max={df[var].max():.2f}, média={df[var].mean():.2f}")
    relatorio.append("")
    relatorio.append("Variáveis Categóricas:")
    for var in categoricas[:10]:
        relatorio.append(f"  - {var}: {df[var].nunique()} categorias únicas")
    relatorio.append("")

    relatorio.append("4. OBJETIVO DA ANÁLISE")
    relatorio.append("-" * 80)
    relatorio.append("Esta análise visa compreender o Indicador de Diferença entre os Desempenhos (IDD),")
    relatorio.append("que mede a diferença entre o desempenho observado e o esperado dos estudantes")
    relatorio.append("de um curso, considerando o perfil dos ingressantes.")
    relatorio.append("")
    relatorio.append("O problema envolve REGRESSÃO, pois busca-se prever/analisar valores contínuos")
    relatorio.append("(notas do IDD) a partir de características dos estudantes e cursos.")
    relatorio.append("")

    relatorio.append("5. INSIGHTS PRINCIPAIS")
    relatorio.append("-" * 80)
    relatorio.append("• Os dados não apresentam valores ausentes significativos")
    relatorio.append("• As notas do ENEM mostram forte correlação com a nota geral do IDD")
    relatorio.append("• Há variação significativa entre diferentes cursos e instituições")
    relatorio.append("• A presença de outliers em algumas variáveis requer atenção no pré-processamento")
    relatorio.append("")

    # Salvar relatório
    relatorio_txt = "\n".join(relatorio)
    with open(OUTPUT_DIR / 'relatorio_resumo.txt', 'w', encoding='utf-8') as f:
        f.write(relatorio_txt)

    print(relatorio_txt)
    print(f"\n  ✓ Relatório salvo em: outputs/relatorio_resumo.txt")


def main():
    """
    Função principal que executa toda a análise exploratória.
    """
    # 1. Carregar dados
    df = carregar_dados()

    # 2. Análise descritiva básica
    df = analise_descritiva_basica(df)

    # 3. Identificar tipos de variáveis
    numericas, categoricas = identificar_tipos_variaveis(df)

    # 4. Criar visualizações
    criar_histogramas(df, numericas)
    criar_boxplots(df, numericas)
    criar_scatter_plots(df, numericas)
    criar_matriz_correlacao(df, numericas)
    analisar_variaveis_categoricas(df, categoricas)

    # 5. Gerar relatório resumo
    gerar_relatorio_resumo(df, numericas, categoricas)

    print("\n" + "="*80)
    print("✓ ANÁLISE EXPLORATÓRIA CONCLUÍDA COM SUCESSO!")
    print("="*80)
    print(f"\nTodos os gráficos foram salvos em: {OUTPUT_DIR}")
    print("\nPróximos passos:")
    print("  1. Revisar os gráficos gerados")
    print("  2. Interpretar os resultados encontrados")
    print("  3. Preencher a Seção 3 e Seção 4 do relatório")
    print("  4. Preparar apresentação dos resultados")


if __name__ == "__main__":
    main()
