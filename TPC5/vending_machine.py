import json
import ply.lex as lex
import re

saldo = 0
stock = {}

tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR'
]

def listar(t):
    print("maq: Lista de produtos disponíveis:")
    print("Código\tNome\tQuantidade\tPreço")
    for cod, values in stock.items():
        print(f"{cod}\t{values[0]}\t{values[1]}\t{values[2] / 100:.2f}")

def adicionar_saldo(valor):
    global saldo
    saldo += valor
    print(f"Saldo = {saldo // 100}e{saldo % 100}c")

def selecionar_produto(codigo):
    global saldo
    item = stock.get(codigo)
    if not item:
        print(f"Não existe nenhum produto com código {codigo}")
        return
    if item[2] > saldo:
        print("Saldo insuficiente para satisfazer o seu pedido")
        print(f"Saldo = {saldo // 100}e{saldo % 100}c; Pedido = {item[2] // 100}e{item[2] % 100}c")
        return
    print(f"Pode retirar o produto dispensado \"{item[0]}\"")
    saldo -= item[2]
    print(f"Saldo = {saldo // 100}e{saldo % 100}c")
    if item[1] == 1:
        del stock[codigo]
    else:
        stock[codigo] = (item[0], item[1] - 1, item[2])

def dar_troco():
    global saldo
    if saldo == 0:
        print("Sem troco para dar")
        return
    output = "Pode retirar o troco: "
    moedas = [200, 100, 50, 20, 10, 5, 2]
    i = 0
    while i < 2 and saldo != 0:
        quoc, resto = divmod(saldo, moedas[i])
        if quoc != 0:
            output += f"{quoc}x {moedas[i] // 100}e, "
        saldo = resto
        i += 1
    while saldo != 0:
        quoc, resto = divmod(saldo, moedas[i])
        if quoc != 0:
            output += f"{quoc}x {moedas[i]}c, "
        saldo = resto
        i += 1
    print(output[:-2])

def t_MOEDA(t):
    r"MOEDA\s+((2|5|10|20|50)c|(1|2)e)(?:\s*,\s*((2|5|10|20|50)c|(1|2)e))*"
    for moeda in re.finditer(r'(?:(?P<cent>2|5|10|20|50)c|(?P<euro>1|2)e)', t.value):
        if moeda.lastgroup == "cent":
            adicionar_saldo(int(moeda.group("cent")))
        else:
            adicionar_saldo(int(moeda.group("euro")) * 100)
    return t

def t_SELECIONAR(t):
    r"SELECIONAR\s+.+"
    selecionar_produto(t.value.replace(" ", "")[10:])
    return t

def t_SAIR(t):
    r'SAIR'
    dar_troco()
    print("Até à próxima")
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Unsupported character '{t.value[:-1]}'")
    t.lexer.skip(len(t.value))

def main():
    global stock
    lexer = lex.lex()
    with open("stock.json", "r") as stock_file:
        data = json.load(stock_file)
    for item in data["stock"]:
        key = item['cod']
        value = (item['nome'], int(item['quant']), int(float(item['preco']) * 100))
        stock[key] = value

    print("maq: Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        line = input()
        lexer.input(line)
        for tok in lexer:
            if tok.type in tokens:
                if tok.type == 'LISTAR':
                    listar(tok)
                lexer.token()  # Skip one token ahead
                break

if __name__ == "__main__":
    main()
