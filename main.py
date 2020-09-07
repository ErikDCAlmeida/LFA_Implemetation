from Menu import Menu 
from lerArquivo import LerArquivo

if __name__ == "__main__":
    start = Menu()
    start.playMenu()
    print(start.getOpenedFile().getArrOfAlpha)
    print(start.getOpenedFile().getNmbOfStates)
    print(start.getOpenedFile().getNmbOfEdges)
    print(start.getOpenedFile().getMatrix)
    print(start.getOpenedFile().getStart)
    print(start.getOpenedFile().getEnds)

    


