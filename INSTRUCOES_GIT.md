# Instruções para Configurar o Repositório GitHub

## 1. Inicializar o Repositório Git Localmente

Abra o terminal na pasta do projeto e execute:

```bash
# Inicializar repositório Git
git init

# Adicionar todos os arquivos ao staging
git add .

# Criar o primeiro commit
git commit -m "Sprint 1: Análise exploratória completa dos microdados IDD 2023

- Estrutura inicial do projeto
- Scripts de análise exploratória (Python)
- Notebook Jupyter com análise completa
- Visualizações: histogramas, boxplots, scatter plots, matriz de correlação
- Material para relatório (Seções 3 e 4)
- README com oportunidades de modelagem preditiva
- Requirements.txt com dependências
- Outputs gerados pela análise"
```

## 2. Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name**: `projeto-idd-2023` (ou nome de sua preferência)
   - **Description**: "Análise exploratória e modelagem preditiva dos microdados do IDD 2023"
   - **Visibility**: Public ou Private (conforme preferir)
   - **NÃO marque**: "Initialize this repository with a README" (já temos um README)
3. Clique em "Create repository"

## 3. Conectar Repositório Local ao GitHub

Após criar o repositório no GitHub, execute os comandos que aparecem na tela:

```bash
# Adicionar o remote (substitua <seu-usuario> pelo seu nome de usuário do GitHub)
git remote add origin https://github.com/<seu-usuario>/projeto-idd-2023.git

# Renomear branch para main (se necessário)
git branch -M main

# Fazer push do código para o GitHub
git push -u origin main
```

**Exemplo completo**:
```bash
git remote add origin https://github.com/joaosilva/projeto-idd-2023.git
git branch -M main
git push -u origin main
```

## 4. Verificar Upload

Acesse o repositório no GitHub e verifique se todos os arquivos foram enviados:
- ✓ README.md
- ✓ requirements.txt
- ✓ .gitignore
- ✓ src/analise_exploratoria.py
- ✓ notebooks/analise_exploratoria_idd2023.ipynb
- ✓ MATERIAL_RELATORIO_SPRINT1.md

## 5. Executar a Análise (Opcional)

Se quiser executar a análise e gerar os gráficos:

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar o script de análise
python src/analise_exploratoria.py
```

Ou abrir o notebook Jupyter:

```bash
jupyter notebook notebooks/analise_exploratoria_idd2023.ipynb
```

## 6. Adicionar Colaboradores (se for trabalho em equipe)

1. No GitHub, vá em: **Settings** → **Collaborators**
2. Clique em **Add people**
3. Digite o username ou email dos membros da equipe
4. Eles receberão um convite por email

## 7. Commits Futuros

Para adicionar novas mudanças:

```bash
# Ver status das modificações
git status

# Adicionar arquivos modificados
git add .

# Criar commit com mensagem descritiva
git commit -m "Descrição das mudanças"

# Enviar para o GitHub
git push
```

## 8. Estrutura de Branches (Recomendado para Sprints)

```bash
# Criar branch para Sprint 2
git checkout -b sprint2-preprocessamento

# Fazer modificações e commits
git add .
git commit -m "Sprint 2: Implementação do pré-processamento"

# Enviar branch para GitHub
git push -u origin sprint2-preprocessamento

# No GitHub, criar Pull Request para merge na main
```

## 9. Boas Práticas

**Commits Frequentes**:
- Faça commits pequenos e frequentes
- Use mensagens descritivas
- Exemplo: "Adiciona tratamento de outliers nas notas ENEM"

**Organização**:
- Use branches para diferentes sprints ou features
- Mantenha a branch `main` sempre funcional
- Revise código antes de fazer merge

**Documentação**:
- Atualize o README quando adicionar funcionalidades
- Documente decisões importantes
- Mantenha o código comentado

## 10. Gitignore - Arquivos Excluídos

O arquivo `.gitignore` está configurado para **não versionar**:
- Arquivos grandes de dados (.csv, .txt, .xlsx) - exceto requirements.txt
- Arquivos temporários Python (__pycache__, *.pyc)
- Notebooks checkpoints (.ipynb_checkpoints)
- Ambientes virtuais (venv/, env/)

**⚠️ IMPORTANTE**: Se quiser versionar os dados ou outputs, você pode:
1. Editar o `.gitignore` e remover as linhas correspondentes
2. Ou usar Git LFS para arquivos grandes: https://git-lfs.github.com/

---

## Troubleshooting

**Erro: "remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/<seu-usuario>/projeto-idd-2023.git
```

**Erro: "src refspec main does not match any"**
```bash
git branch -M main
git push -u origin main
```

**Erro: "failed to push some refs"**
```bash
# Fazer pull primeiro
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

## Links Úteis

- GitHub Docs: https://docs.github.com/
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
- Markdown Guide: https://www.markdownguide.org/

---

**Criado em**: Setembro 2026
**Sprint 1** - Projeto IDD 2023
