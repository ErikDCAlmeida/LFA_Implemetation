from Menu import Menu 
from lerArquivo import LerArquivo

if __name__ == "__main__":
    start = Menu()
    start.playMenu()
    print(start.getOpenedFile().getArrOfAlpha)
    print(start.getOpenedFile().getNmbOfStates)
    print(start.getOpenedFile().getNmbOfEdges)


    '''teste = open("C:/Users/EriikD/Desktop/Teste.txt","r")
    linha = teste.readline()
    for x in linha.split(";"):
        if x == "}":
            print(x, "AAAAAAAAAAAAAAAAAAAAAAAA")'''


    


