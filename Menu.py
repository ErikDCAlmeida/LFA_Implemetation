from lerArquivo import LerArquivo

class Menu:

    def __init__(self):
        self.__choice = -1
        self.__openedFile = None

    def playMenu(self):
        while True:
            self.__choice = int(input(
                 "===============Automaton's Test===============\n"
                 "Escolha uma das opções abaixo para testar seu autômato:\n"
                 "1- Carregar autômato a partir de um arquivo.\n"
                 "2- Criar seu próprio autômato.\n"
                 "0- Sair.\n"
                 "Escolha: "))
            if self.__choice == 0:
                print("Programa finalizado!")
                break
            elif self.__choice == 1:
                self.__openedFile = LerArquivo()
                self.__openedFile.getAutomatonInfo()
            elif self.__choice == 2:
                #Chamada para criar manualmente o autômato.
                break
            else:
                print("Opção inválida. Digite uma opção válida!")
            
    def getOpenedFile(self):
        return self.__openedFile