def exists_word(word, instance):
    result = []
    for dicts in instance.queue:
        data = {
            "palavra": word,
            "arquivo": dicts["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for i, s in enumerate(dicts["linhas_do_arquivo"]):
            if word.lower() in s.lower():
                data["ocorrencias"].append({"linha": i + 1})
        if len(data["ocorrencias"]):
            result.append(data)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
