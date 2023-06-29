import random
checar = False

inputer = "==> "


#classe de itens

class Arma():
    #nome
    nome = ""
    tipo = ""
    atributo = ""
    raridade = ""
    elemento = ""
    #status
    dano = 0
    velocidade = 0

class Armadura():
    #nome
    tipo = ""
    #status
    defesa = 0


#listas
itensdojogador = []
armas = ["Espada", "Faca", "Katana"]
armos = ["Machado", "Cutelo"]
todasasarmas = ["Espada", "Faca", "Katana", "Machado", "Cutelo"]
raridades = ["Normal", "Normal", "Normal", "Normal", "Normal", "Normal", "Normal","Raro", "Raro", "Raro","Raro", "Épico", "Épico", "Épico", "Lendario", "Lendario", "Divino"]
raridadas = ["Normal", "Normal","Normal", "Normal", "Normal", "Normal", "Normal", "Rara", "Rara", "Rara","Rara", "Épica", "Épica", "Épica", "Lendaria", "Lendaria", "Divina"]
atributo = ["longo", "curto", "rápido", "forte", "quebrado"]
atributa = ["longa", "curta", "rápida", "forte", "quebrada"]
elementos = ["dos ventos", "de rocha", "de ferro", "em chamas", "de vinhas", "sombrio", "profundo", "congelado", "demoniaco" , "angelical"]
elementas = ["dos ventos", "de rocha", "de ferro", "em chamas", "de vinhas", "sombria", "profunda", "congelada", "demoniaca" , "angelical"]

#funções

def menu():
    print("Este é o menu principal")
    print("Digite 1 para começar o jogo")
    while True:
        a = str(input(inputer))
        if a == "1":
            b = armaaleatoria()
            print(b.nome)
            itensdojogador.append(b)
        elif a == "2":
            for i in range(len(itensdojogador)):
                print(itensdojogador[i].nome)
                print(f"dano da arma: {itensdojogador[i].dano}")
                print(f"velocidade da arma: {itensdojogador[i].velocidade}")
        elif a == "d":
            checar = True
        else:
            print("comando n encontrado, tente novamente")


def armaaleatoria():
    #criando o nome
    item = Arma()
    arma = random.choice(todasasarmas)
    item.tipo = arma
    if arma in armas:
        item.atributo = random.choice(atributa)
        item.elemento = random.choice(elementas)
        item.raridade = random.choice(raridadas)
    else:
        item.atributo = random.choice(atributo)
        item.elemento = random.choice(elementos)
        item.raridade = random.choice(raridades)

    #registrando nome
    item.nome = str(item.tipo + " " + item.atributo + " " + item.elemento + " " + "(" +item.raridade + ")")

    #registrando dano e vel
    if arma == "Faca":
        item.dano = 0
        item.velocidade = 4
    elif arma == "Katana":
        item.dano = 1
        item.velocidade = 3
    elif arma == "Espada":
        item.dano = 2
        item.velocidade = 2
    elif arma == "Cutelo":
        item.dano = 3
        item.velocidade = 1
    elif arma == "Machado":
        item.dano = 4
        item.velocidade = 0


    #estado da arma:

    if item.atributo == "rápido" or item.atributo == "rápida":
        item.velocidade += 1

    elif item.atributo == "forte":
        item.dano += 1

    elif item.atributo == "quebrado" or item.atributo == "quebrada":
        item.dano -= 1

    if checar == True:
        print("dano inicial")
        print("velocidade inicial")
        print(item.dano)
        print(item.velocidade)



    #dano e velocidade da raridade
    if item.raridade == "Raro" or item.raridade == "Rara":
        item.dano += 1
        item.velocidade += 1
        if checar == True:
            print("dano adicionaç raridade")
            print("velocidade adicional raridade")
            print(item.dano)
            print(item.velocidade)
    elif item.raridade == "Épico" or item.raridade == "Épica":
        item.dano += 2
        item.velocidade += 2
        if checar == True:
            print("dano adicionaç raridade")
            print("velocidade adicional raridade")
            print(item.dano)
            print(item.velocidade)
    elif item.raridade == "Lendario" or item.raridade == "Lendaria":
        item.dano += 3
        item.velocidade += 3
        if checar == True:
            print("dano adicionaç raridade")
            print("velocidade adicional raridade")
            print(item.dano)
            print(item.velocidade)
    elif item.raridade == "Divino" or item.raridade == "Divina":
        item.dano += 4
        item.velocidade += 4
        if checar == True:
            print("dano adicionaç raridade")
            print("velocidade adicional raridade")
            print(item.dano)
            print(item.velocidade)



    #dano elemenal e vel
    if item.elemento == "demoniaco" or item.elemento == "demoniaca":
        item.dano += 5
        item.velocidade -= 1
        if checar == True:
            print("dano adicional elemento")
            print("velocidade adicional elemento")
            print(item.dano)
            print(item.velocidade)

    elif item.elemento == "dos ventos":
        item.dano -= 1
        item.velocidade += 5
        if checar == True:
            print("dano adicional elemento")
            print("velocidade adicional elemento")
            print(item.dano)
            print(item.velocidade)

    elif item.elemento == "de rocha":
        item.dano += 4
        if checar == True:
            print("dano adicional elemento")
            print("velocidade adicional elemento")
            print(item.dano)
            print(item.velocidade)

    elif item.elemento == "em chamas" or item.elemento == "de vinhas":
        item.dano += 3
        item.velocidade += 1
        if checar == True:
            print("dano adicional elemento")
            print("velocidade adicional elemento")
            print(item.dano)
            print(item.velocidade)

    elif item.elemento == "congelado" or item.elemento == "congelada" or item.elemento == "profundo" or item.elemento == "profunda" or item.elemento == "angelical":
        item.dano += 2
        item.velocidade += 2
        if checar == True:
            print("dano adicional elemento")
            print("velocidade adicional elemento")
            print(item.dano)
            print(item.velocidade)

    elif item.elemento == "sombrio" or item.elemento == "sombria" :
        item.dano += 1
        item.velocidade += 3
        if checar == True:
            print("dano adicional elemento")
            print("velocidade adicional elemento")
            print(item.dano)
            print(item.velocidade)

    return (item)

menu()