class Posto():
    def __init__(self,tipo,qtdlitro,preco):
        self.tipo=tipo
        self.qtdlitro=qtdlitro
        self.preco=preco
    def abastecer(self,tipo,preco, qtdlitro):
        print ("digite quantos litros deseja abastecer:")
        litro=float(input())
        if litro > qtdlitro:
            print("conbustível não disponível")
            return qtdlitro
        else:
            preco=litro*preco
            qtdlitro=qtdlitro-litro
            print ("valor total do abastecimento: %.2f"%(preco))
            return qtdlitro
    def mudarQuantidade(self,qtdlitro):
        quantidade=float(input(("digite a quantidade a ser auterada")))
        i="f"
        while i!="s":
            i=(input("digite a: para aumentar \n d: para diminuir \n e s para voltar ao menu"))
            if i == "a":
                qtdlitro=quantidade+qtdlitro
                print("nova quantidade: %.2f"%(qtdlitro))
                return qtdlitro
            if i== "d":
                if quantidade >qtdlitro:
                    print("não tem como tirar mais que tem")
                    return qtdlitro
                else:
                    qtdlitro=qtdlitro-quantidade
                    print("nova quantidade: %.2f"%(qtdlitro))
                    return qtdlitro
            if i=="s":
                print("voltando ao menuu")
            else:
                print("opção errada,digite outra")
    def aValor(self, preco,qtdlitro):
        valor=float(input("digite quanto deseja colocar"))
        plitro=(valor/preco)
        if plitro> qtdlitro:
            print ("conbustível não disponível")
            return qtdlitro
        else:
            qtdlitro=qtdlitro-plitro
            print("em litros vai dar: %.2f"%(plitro))
            return qtdlitro
    def mudar_Preco(self,preco):
        print ("digite o novo preço.")
        novo=float(input())
        preco=novo
        print("novo preço: %.2f"%(preco))
        return preco