#!/home/fernando/Projects/python_script/venv/bin/python


from tkinter import Tk
from tkinter.filedialog import askopenfilenames


# função que faz o prompt para o usuário pedindo para selecionar os arquivos


def selecionarArquivos():
    Tk().withdraw()
    return list(askopenfilenames())


# função que le um arquivo json e retorna uma lista de dicionarios com os campos


def lerArquivoJson(nomeArquivo):
    import json

    with open(nomeArquivo) as arquivo:
        return json.load(arquivo)


# função que lista todos os nomes de campos e de subitens de um arquivo json e retorna uma lista com os nomes


def listarCampos(item):
    campos = []
    if isinstance(item, list):
        for i in item:
            campos.extend(listarCampos(i))
    elif isinstance(item, dict):
        for k, v in item.items():
            campos.append(k)
            if isinstance(v, (dict, list)):
                campos.extend(listarCampos(v))
    return campos


# função que faz um prompt para o usuário pedindo para selecionar o campo que deseja substituir a partir do retorno
# da função listarCampos sem mostrar campos repetidos. Os campos são numerados e organizados em linhas e colunas
# para evitar ter uma lista muito comprida


def selecionarCampo(campos):
    campos = list(set(campos))
    for i in range(len(campos)):
        print(f"{i+1} - {campos[i]}", end="  ")
        if (i + 1) % 5 == 0:
            print()
    return campos[int(input("\nDigite o número do campo que deseja substituir: ")) - 1]


# função que faz um prompt para o usuário pedindo o conteúdo que deseja substituir


def selecionarValor():
    return input("Digite o valor que deseja substituir: ")


# função que substitui os campos de um arquivo json a partir do campo selecionado e do valor que deseja substituir


def substituiCampos(arquivos, valor, campo):
    if isinstance(arquivos, list):
        for i in arquivos:
            substituiCampos(i, valor, campo)
    elif isinstance(arquivos, dict):
        for k, v in arquivos.items():
            if k == campo:
                arquivos[k] = valor
            if isinstance(v, (dict, list)):
                substituiCampos(v, valor, campo)
    return arquivos


"""

for arquivo in selecionarArquivos():
    arq = lerArquivoJson(arquivo)
    substituiCampos('testando123', 'nome')

"""

arquivos_json = list(map(lerArquivoJson, selecionarArquivos()))
campo = selecionarCampo(listarCampos(arquivos_json))
valor = selecionarValor()
substituiCampos(arquivos_json, valor, campo)
print(arquivos_json)
