# Passo a passo para a reprodução

Este repositório contém um guia de como avaliar o [SPABERT](https://github.com/knowledge-computing/spabert/tree/main) na tarefa de **Tipagem Não Supervionada de Geoentidades** .

# 1. Instalação do Miniconda

- Um ambiente virtual python com a versão 3.11 é necessário e para criar esse ambiente vamos utilizar o Miniconda que pode ser instalado no Linux seguido o tutorial presente nesta [documentação](https://www.anaconda.com/docs/getting-started/miniconda/install/linux-install).

# 2. Criação e Ativação do Ambiente Virtual Python

- Com o miniconda instalado, execute o comando abaixo para criar um ambiente python de nome `spabert_reprodution_venv`
  ```bash
  conda  create  -n  spabert_reprodution_venv  python=3.11
  ```
- Agora ative o ambiente criado com o seguinte comando
  ```bash
  conda  activate  spabert_reprodution_venv
  ```

# 3. Clonando Repositório da Reprodução do SPABERT e Instalando Dependências

- Dentro da pasta do ambiente virtual python, clone o repositório do SPABERT e instale as dependências necessárias utilizando os comandos
  ```bash
  git clone https://github.com/GabrielYuriRF0/spabert_reprodution.git
  ```
  ```bash
  cd spabert_reprodution
  pip install -r requirements.txt
  ```

# 4. Baixando Dados de Teste de Londres e California

- Baixe os dados de teste de Londres e California que estão presentes neste [link](https://drive.google.com/drive/folders/1uyvGdiJdu-Cym4dOKhQLIkKpfgHvfo01) e coloque eles na pasta `data/test_data`

# 5. Baixando Modelos Spabert Base e Large

- Baixe o Spabert [base](https://drive.google.com/file/d/1XFcA3sxC4wTlt7VjvMp1zNrWY5rjafzE/view) e [large](https://drive.google.com/file/d/12_FDVeSYkl_HQ61JmuMU6cRjQdKNpgR_/view) e salve eles nas pastas `data/spabert_models` com os nomes `spabert_base.pth` e `spabert_large.pth`, respectivamente

# 6. Avaliando Spabert na Tarefa Supervionada de Tipagem de GeoEntidades

## 6.1 Avaliando Spabert Base

- Para avaliar o `Spabert Base` vamos executar o seguinte comando dentro da pasta `src`:

```bash
python3 test_spabert.py --bert_option='bert-base' --checkpoint_path='../data/spabert_models/spabert_base.pth' --with_type --sep --num_classes=9 --sep_between_neighbors
```

## 6.2 Avaliando Spabert Large

- Para avaliar o `Spabert Large` vamos executar o seguinte comando:

```bash
python3 test_spabert.py --bert_option='bert-large' --checkpoint_path='../data/spabert_models/spabert_large.pth' --with_type --sep --num_classes=9 --sep_between_neighbors
```

- Após a execução dos scripts de avaliação, os resultados vão estar dentro da pasta `data/results`.
