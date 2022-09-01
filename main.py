from posto import Posto
def gas():
    if __name__ == "__main__":
        tipo="gasolina"
        preco=6.50
        qtdlitro=100.00
        gasolina=Posto(tipo,qtdlitro, preco)
    print("bomba de gasolina")
    i=""
    while(i!="s"):
        print('quantidade disponível: %.2f'%(qtdlitro))
        print("preço do combustível: %.2f"%(preco))
        print("digite sua opção")
        print("a: para auterar quantidade\n b: para abastecer informando quantos litros\n c: para abastecer informando o valor\n d: para alterar o valor \n s para sair")
        i=(input())
        if i=="b":  
            qtdlitro=gasolina.abastecer(tipo, preco, qtdlitro)
        elif i=="a":
            qtdlitro= gasolina.mudarQuantidade(qtdlitro)
        elif i=="c":
            qtdlitro=gasolina.aValor(preco,qtdlitro)
        elif i=="d":
            preco=gasolina.mudar_Preco(preco)
        elif i=="s":
            print("voltando ao menu")
        else:
            print("opção errada, digite outra")
def diesel():
    if __name__ == "__main__":
        tipo="diesel"
        preco=7.00
        qtdlitro=100.00
        diesel=Posto(tipo,qtdlitro,preco)
        print("bomba de diesel")
        i=""
        while(i!="s"):
            print("quantidade disponível: %.2f"%(qtdlitro))
            print("preço do combustível: %.2f"%(preco))
            print("digite sua opção")
            print("a: para auterar quantidade\n b: para abastecer informando quantos litros\n c: para abastecer informando o valor\n d: para alterar o valor \n s para sair")
            i=(input())
            if i=="b":  
                qtdlitro=diesel.abastecer(tipo, preco, qtdlitro)
            elif i=="a":
                qtdlitro= diesel.mudarQuantidade(qtdlitro)
            elif i=="c":
                qtdlitro=diesel.aValor(preco,qtdlitro)
            elif i=="d":
                preco=diesel.mudar_Preco(preco)
            elif i=="s":
                print("voltando ao menu principal")
            else:
                print("opção errada, digite outra")


def menu():
    print("bem vindo")
    i="a"
    while i!="s":
        print("digite g: para entrar na bomba de gasolina\n d: para entrar na bonba de diesel \n s para sair.")
        i=(input("digite sua opção"))
        if i=="g":
            gas()
        elif i=="d":
            diesel()
        elif i=="s":
            print("saindo, obrigado por usar o programa")
        else:
            print("opção errada, por favor digite outra.")

menu()