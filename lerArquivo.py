from tkinter import Tk
from tkinter.filedialog import askopenfilename

class LerArquivo:

    def __init__(self):
        self.__nmbOfStates = 0
        self.__nmbOfEdges = 0
        self.__file = None
        self.__arrState = []
        self.__arrEdges = []
        self.__arrOfAlphaAuto = []
        self.__matrixOfLines = []

    def __loadFile(self):
        Tk().withdraw()
        fileName = askopenfilename()
        return open(fileName, "r")
         
    def __verifArrAuto(self, state):
        if len(self.__arrState) == 0:
            return False
        else:
            for index in self.__arrState:
                if state == index:
                    return True
        return False

    def getAutomatonInfo(self):
        self.__file = self.__loadFile()
        for line in self.__file.readlines():
            rsltLine = line.split(";")
            if rsltLine[0] == "{":
                for item in rsltLine:
                    if item == "}":
                        self.__arrOfAlphaAuto.pop(0)
                        continue
                    elif item == "\n":
                        continue
                    else:
                        self.__arrOfAlphaAuto.append(item)
            else:
                if rsltLine[0] == ".":
                    self.__nmbOfStates = len(self.__arrState)
                    self.__nmbOfEdges = len(self.__arrEdges)
                    break
                else:
                    vetAux = []
                    vetAux.append(rsltLine[0])
                    vetAux.append(rsltLine[1])
                    strAux = ""
                    for lineI in rsltLine[2]:
                        if lineI == "\n":
                            continue
                        else:
                            strAux += lineI
                    vetAux.append(strAux)
                    self.__matrixOfLines.append(vetAux)
                    if self.__verifArrAuto(rsltLine[0]) == False:
                        self.__arrState.append(rsltLine[0])
                    self.__arrEdges.append(rsltLine[1])

                
    @property
    def getNmbOfStates(self):
        return self.__nmbOfStates

    @property
    def getNmbOfEdges(self):
        return self.__nmbOfEdges
    
    @property
    def getArrOfAlpha(self):
        return self.__arrOfAlphaAuto
    
    @property
    def getMatrix(self):
        return self.__matrixOfLines

    @property
    def getStart(self):
        return self.__start