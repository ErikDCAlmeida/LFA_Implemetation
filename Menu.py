from lerArquivo import LerArquivo

class Menu:

    def __init__(self):
        self.__choice = -1
        self.__automaton = None
        self.__openedFile = None

    def playMenu(self):
        while True:
            self.__choice = int(input(
                 "===============Automaton's Test===============\n"
                 "Escolha uma das opções abaixo para criar seu autômato:\n"
                 "1- Carregar autômato a partir de um arquivo.\n"
                 "0- Sair.\n"
                 "Escolha: "))
            if self.__choice == 0:
                print("Programa finalizado!")
                break
            elif self.__choice == 1:
                self.__openedFile = LerArquivo()
                self.__automaton = self.__openedFile.getAutomatonInfo()
                self.__post_creation__()
            else:
                print("Opção inválida. Digite uma opção válida!")
    
    # Menu de pos criação do automato
    def __post_creation__(self):
        while True:
            self.__choice = int(input(
                    "===============Automaton's Test===============\n"
                    "Escolha uma das opções abaixo para testar seu autômato:\n"
                    "1- Testar palavra.\n"
                    "2- Verificar automato cadastrado.\n"
                    "0- Voltar para menu de criação do automato.\n"
                    "Escolha: "))
            if self.__choice == 0:
                break
            elif self.__choice == 1:
                #Chamada para criar manualmente o autômato.
                palavra = str(input("Digite a palavra a ser testada no automato: "))
                retorno = self.__automaton.verify_world_automaton(palavra)
                if retorno:
                    print("A palavra informada faz parte da linguagem mapeada pelo automato.\nACEITA")
                    continue
                print("A palavra informada não faz parte da linguagem mapeada pelo automato.\nREJEITADA")
            elif self.__choice == 2:
                print(self.__automaton.print_automaton())
                pass
            else: 
                print("Opção inválida. Digite uma opção válida!")

    # Menu de criação do automato de forma manual
    def __manual_creation__(self):
        pass

    def getOpenedFile(self):
        return self.__openedFile