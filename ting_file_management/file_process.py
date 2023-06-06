import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    for e in instance.queue:
        if e["nome_do_arquivo"] == data["nome_do_arquivo"]:
            return None
    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    if not instance.queue:
        print("Não há elementos", file=sys.stdout)
    else:
        removed = instance.dequeue()
        print(
            f"""
              Arquivo {removed["nome_do_arquivo"]} removido com sucesso
              """,
            file=sys.stdout,
        )


def file_metadata(instance, position):
    if position not in range(len(instance.queue)):
        print("Posição inválida", file=sys.stderr)
    else:
        print(instance.search(position), file=sys.stdout)
