# Passo a passo para a reprodução

Este repositório contém um guia de como retreinar o modelo [SPABERT](https://github.com/knowledge-computing/spabert/tree/main) em suas duas variantes (**base** e **large**) e avaliar ele na tarefa de **Tipagem Não Supervionada de Geoentidades**.

## 1. Instalação do Miniconda

- Um ambiente virtual python com a versão 3.11 é necessário e para criar esse ambiente vamos utilizar o Miniconda que pode ser instalado no Linux seguido o tutorial presente nesta [documentação](https://www.anaconda.com/docs/getting-started/miniconda/install/linux-install).

## 2. Criação e Ativação do Ambiente Virtual Python

- Com o miniconda instalado, execute o comando abaixo para criar um ambiente python de nome `spabert_reprodution_venv`
  ```bash
  conda  create  -n  spabert_reprodution_venv  python=3.11
  ```
- Agora ative o ambiente criado com o seguinte comando
  ```bash
  conda  activate  spabert_reprodution_venv
  ```

## 3. Clonando Repositório do SPABERT e Instalando Dependências

- Dentro da pasta do ambiente virtual python, clone o repositório do SPABERT e instale as dependências necessárias utilizando os comandos
  ```bash
  git  clone  https://github.com/knowledge-computing/spabert.git
  ```
  ```bash
  cd  spabert
  pip  install  -r  requirements.txt
  ```

## 4. Configurando Projeto Para a Execução

### 4.1 Configurando Caminho Correto do arquivo `dataset_loader.py`

- Dentro do projeto, você deve ir no arquivo `osm_sample_loader.py` e realizar a configuração correta do caminho do arquivo `dataset_loader.py`, trocando o código abaixo
  ```python
  sys.path.append("/home/zekun/spatial_bert/spatial_bert/datasets")
  ```
  por esse
  ```python
  sys.path.append(str(Path(__file__).parent))
  ```
  Além de adicionar o seguinte import
  ```python
  from  pathlib  import  Path
  ```

## 5. Obtendo o Spabert Base e Large

- Dentro da pasta `models`, crie as pastas `pretrained-base` e `pretrained-large` que vão guardar os modelos pré-treinados.

### 5.1 Baixando Modelos já Pré-Treinados

- Caso prefira já baixar os modelos pré-treinados e não executar os treinamentos, você baixar diretamente o modelo [base](https://drive.google.com/file/d/1l44FY3DtDxzM_YVh3RR6PJwKnl80IYWB/view) e [large](https://drive.google.com/file/d/1LeZayTR92R5bu9gH_cGCwef7nnMX35cR/view) e salver eles nas suas respectivas pastas

## 6. Obtendo Modelos Treinados com Dados de Londres e California

- Dentro da pasta `models` crie as pastas `trained_base` `trained_large` que vão guardar os modelos treinados.

### 6.1 Baixando Modelos Treinados

- Caos prefira já baixar os modelos treinados e não executar o treinamento com os dados de Londres e California, você pode baixar diretamente os modelos [base](https://drive.google.com/file/d/1XFcA3sxC4wTlt7VjvMp1zNrWY5rjafzE/view) e [large](https://drive.google.com/file/d/12_FDVeSYkl_HQ61JmuMU6cRjQdKNpgR_/view) e salvar os modelos nas pastas anteriomente criadas.

### 6.2 Treinando Modelos com Dados de Londres e California (Opcional)

- Dentro da pasta `data`, crie a pasta `training_data` e salve nela os 2 arquivos presentes neste [link](https://drive.google.com/drive/folders/1uyvGdiJdu-Cym4dOKhQLIkKpfgHvfo01)

- No arquivo `train_csl_spatialbert.py` troque o código abaixo
  ```python
        london_file_path = '../../semantic_typing/data/sql_output/osm-point-london-typing.json'
        california_file_path = '../../semantic_typing/data/sql_output/osm-point-california-typing.json'
  ```
- Por esse
  ```python
      london_file_path = "../../../../data/training_data/osm-point-london-typing.json"
      california_file_path = "../../../../data/training_data/osm-point-california-typing.json"
  ```
- Para treinar o modelo base use o seguinte comando

  ```bash
  python3 train_cls_spatialbert.py --lr=5e-5 --sep_between_neighbors --bert_option='bert-base'  --with_type --mlm_checkpoint_path='../../../models/pretrained_base/mlm_mem_keeppos_ep0_iter06000_0.2936.pth' --model_save_dir='../../../models/trained_base'

  ```

  - Já para treinar o modelo large use o seguinte comando

  ```bash
  python3 train_cls_spatialbert.py --lr=1e-6  --sep_between_neighbors --bert_option='bert-large'  --with_type --mlm_checkpoint_path='../../../models/pretrained_large/mlm_mem_keeppos_ep1_iter02000_0.4400.pth --model_save_dir='../../../models/trained_large'
  ```

# 7. Avaliando Spabert na Tarefa Supervionada de Tipagem de GeoEntidades
