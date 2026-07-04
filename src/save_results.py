import os
import csv
from datetime import datetime


def save_results_to_csv(
    args, precisions, recalls, fscores, supports, precision, recall, f1
):
    """
    Salva as métricas de avaliação em um CSV, incrementando os dados a cada
    execução (não sobrescreve os resultados anteriores).

    O nome do arquivo depende do --bert_option:
        bert-base  -> data/results/teste_spabert_base_results.csv
        bert-large -> data/results/teste_spabert_large_results.csv

    O diretório data/ fica na raiz do projeto (fora de src/), então o
    caminho é montado a partir da localização deste arquivo, garantindo
    que funcione independentemente de onde o script é executado.

    Cada linha do CSV corresponde a uma execução do script de teste.
    """

    if args.bert_option == "bert-base":
        model_name = "spabert_base"
    elif args.bert_option == "bert-large":
        model_name = "spabert_large"
    else:
        model_name = args.bert_option.replace("-", "_")

    # Diretório deste arquivo (src/) -> sobe um nível para a raiz do projeto
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(project_root, "data", "results")
    os.makedirs(results_dir, exist_ok=True)

    csv_path = os.path.join(results_dir, f"teste_{model_name}_results.csv")

    file_exists = os.path.isfile(csv_path)

    row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "bert_option": args.bert_option,
        "num_classes": args.num_classes,
        "checkpoint_path": args.checkpoint_path,
        "micro_precision": "{:.3f}".format(precision),
        "micro_recall": "{:.3f}".format(recall),
        "micro_f1": "{:.3f}".format(f1),
        "precisions": ["{:.3f}".format(p) for p in precisions],
        "recalls": ["{:.3f}".format(r) for r in recalls],
        "fscores": ["{:.3f}".format(fs) for fs in fscores],
        "supports": [int(s) for s in supports],
    }

    fieldnames = list(row.keys())

    # abre em modo "a" (append) para incrementar os dados sem remover os antigos
    with open(csv_path, mode="a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)

    print(f"\nResultados salvos em: {csv_path}")
