from tkinter import Tk
from tkinter.filedialog import askopenfilename
from Automaton import Automaton
from Graph.vertice import Vertice
from Graph.aresta import Aresta

class LerArquivo:

    def __init__(self):
        self.__nmbOfStates = 0
        self.__nmbOfEdges = 0
        self.__file = None
        self.__start = None
        self.__ends = []
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
        self.__enfOfTransitions = False
        self.__file = self.__loadFile()
        lines = self.__file.readlines()
        for index in range(0,len(lines)):
            rsltLine = lines[index].split(";")
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
                    self.__enfOfTransitions = True
                elif self.__enfOfTransitions == False:
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
                elif self.__enfOfTransitions == True:
                    if rsltLine[1] == "<":
                        self.__ends.append(rsltLine[0])
                    elif rsltLine[1] == ">":
                        self.__start = rsltLine[0]
                elif rsltLine[0] == []:
                    break
        
        return self.__generate_automaton__()
            

    def __generate_automaton__(self):
        automaton = Automaton(alphabet=self.__arrOfAlphaAuto,states=[Vertice(state) for state in self.__arrState],nmbOfStates=self.__nmbOfStates,initial_state=Vertice(self.__start),final_states=[Vertice(state) for state in self.__ends])
        for transition in self.__matrixOfLines:
            automaton.add_transition(Aresta(vertice_inicio=Vertice(transition[0]),vertice_fim=Vertice(transition[2]),id=transition[1]))

        return automaton

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

    @property
    def getEnds(self):
        return self.__ends