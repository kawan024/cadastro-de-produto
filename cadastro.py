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
    except FileNotFoundError:
        print("nenhum produto cadastrado ainda.")
        
while True:
    print("\n1 - cadastrar produtos")
    print("2 - listar produtos")
    print("0 - sair")
    opção = input("escolha: ")
    
    if opção == "1":
        produto = cadastrar_produto()
        salvar_produto(produto)
    elif opção == "2":
        listar_produtos()
    elif opção == "0":
        break
    