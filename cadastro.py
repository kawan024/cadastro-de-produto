def formatar_nome(nome):
    return nome.strip().title()

def cadastrar_produto():
    nome = input("digite o nome do produto: ")
    preço = float(input("digite o preço do produto: "))
    categoria = input("digite a categoria do produto: ")
    return (formatar_nome(nome), preço, categoria)

def salva_produto(produto):
    with open("produto.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{produto[0]};{produto[1]};{produto[2]}\n"
        arquivo.write(linha)
        
def listar_produtos():
    try:
        with open("produtos.txt", "r", encodiing="utf-8") as arquivo:
            for linha in arquivo:
                nome, preço, categoria = linha.strip().split(";")
                print(f"produto: {nome} | preço; R${preço} | categoria: {categoria}")
    except filenotFoundeerror:
        print("nenhum produto cadastrado ainda.")