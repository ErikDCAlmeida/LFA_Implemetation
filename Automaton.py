from Graph.grafo import Grafo
from Graph.vertice import Vertice
from Graph.aresta import Aresta

class Automaton:

    def __init__(self,alphabet :list, states :list, nmbOfStates:int,initial_state :Vertice,final_states :list):
        self.__alphabet = alphabet
        self.__initial_state = initial_state
        self.__final_states = final_states
        self.__number_states = nmbOfStates
        self.__grafo = Grafo(states,orientado=True)
    
    def add_state(self,state :Vertice):
        self.__grafo.add_vertice(state)

    def add_transition(self, transicao :Aresta):
        self.__grafo.add_aresta(transicao)

    #Metodo responsavel por verificar se uma determinada palavra é aceita ou não no automato em especifico
    def verify_world_automaton(self,world: str):
        findTrasition = False
        self.__convert_automaton__()
        actualState = self.__grafo.procurarVertice(self.__initial_state)
        for letter in world:
            for key in actualState.arestas:
                aresta = actualState.arestas[key][0]
                if aresta.id == letter:
                    actualState = aresta.vertice_fim
                    findTrasition = True
                    break
            
            if not findTrasition:
                return False
        
        if actualState in self.__final_states:
            return True
        
        return False

    #Retorna verdadeiro se o automato cadastrado é um automato finito deterministico
    def __verify_deterministic_automaton__(self):
        for state in self.__grafo.vertices:
            arestas = state.arestas
            #Vetor para armazenar os alfabetos ja lidos e posteriormente verificar se o vertice atual possui arestas de saida para todos os simbolos do alfabeto
            alphabets_read = []
            for key in arestas:
                aresta = arestas[key][0]
                if aresta.id in alphabets_read:
                    return False

                alphabets_read.append(aresta.id)
        
        return True
            
    #Metodo responsavel por realizar a conversao de autômato finito não determinístico para automato finito deterministico
    def __convert_automaton__(self):
        incremental_id_new_states = 0
        isDeterministic = self.__verify_deterministic_automaton__()
        if isDeterministic:
            return

        converted_graph = Grafo(orientado=True)
        states_analise = [self.__grafo.procurarVertice(self.__initial_state)]
        new_states = {}
        while len(states_analise) != 0:
            actual_state = states_analise.pop(0)
            new_states_processed,new_transitions_processed = self.__get_new_states__(actual_state,new_states)
            converted_graph.add_vertice(Vertice(actual_state.id))
            new_states[actual_state.id] = [transition for transition in new_transitions_processed]
            for new_state_found in new_states_processed:
                if not self.__verify_states_in_new_states__(new_states,new_state_found):
                    states_analise.append(new_state_found)

        # Adicionando as transicoes  no novo automato convertido. As transicoes sao adicionadas apos todos os
        # estados terem sido adicionados pois caso contrario poderiamos ter transicoes que nao apontam para nenhum estado
        for key in new_states:
            actual_transitions = new_states[key]
            for transition in actual_transitions:
                converted_graph.add_aresta(transition)
        
        print("-------------FOI REALIZADA A CONVERSÃO DO AUTOMATO PARA UM AUTOMATO FINITO DETERMINISTICO--------------------")
        print("-------------------------------AUTOMATO ANTES DA CONVERSÃO(NÃO DETERMINISTICO)-------------------------------")
        print(self.print_automaton())
        self.__final_states = self.__return_new_final_states__(converted_graph.vertices)
        self.__grafo = converted_graph
        self.__number_states = len(converted_graph.vertices)
        print("-------------------------------AUTOMATO DEPOIS DA CONVERSÃO(DETERMINISTICO)-------------------------------")
        print(self.print_automaton())

    def __get_new_states__(self,state :Vertice,new_states :dict):
        new_states_not_processed = {}
        #Caso contenha ;, sera um vertice formado por outros dois ou mais vertices(conjunto de vertices)
        #print(state.id)
        if ';' in state.id:
            state_ids = state.id.split(";")
            for state_id in state_ids:
                rec_new_states_processed,rec_new_transitions_processed = self.__get_new_states__(self.__grafo.procurarVertice(Vertice(state_id)),new_states)
                for transition in rec_new_transitions_processed:
                    if transition.id not in new_states_not_processed:
                        new_states_not_processed[transition.id] = transition.vertice_fim.id.split(";")
                    else:
                        actual_stages_transition_ids = transition.vertice_fim.id.split(";")
                        for actual_stages_transition_id in actual_stages_transition_ids:
                            if actual_stages_transition_id not in new_states_not_processed[transition.id]:
                                new_states_not_processed[transition.id].append(actual_stages_transition_id)
            
            new_states_processed = []
            new_transitions_processed = []
            for key in new_states_not_processed:
                new_state = Vertice(";".join([str(state_a) for state_a in new_states_not_processed[key]]))
                key_existent_id = self.__verify_states_in_new_states__(new_states,new_state)
                if key_existent_id:
                    new_state = Vertice(key_existent_id)
                new_states_processed.append(new_state)
                new_transitions_processed.append(Aresta(vertice_inicio=state,vertice_fim=new_state,id=key))
            return new_states_processed,new_transitions_processed

        else:
            for key in state.arestas:   
                arestas = state.arestas[key]
                for aresta in arestas:
                    if aresta.id not in new_states_not_processed:
                        new_states_not_processed[aresta.id] = [aresta.vertice_fim]
                        continue
                    new_states_not_processed[aresta.id].append(aresta.vertice_fim)

            new_states_processed = []
            new_transitions_processed = []
            for key in new_states_not_processed:
                new_state = Vertice(";".join([str(state_a) for state_a in new_states_not_processed[key]]))
                new_states_processed.append(new_state)
                new_transitions_processed.append(Aresta(vertice_inicio=state,vertice_fim=new_state,id=key))
            return new_states_processed,new_transitions_processed

    #Funcao utilizada exclusivamente na transformacao do grafo com o objetivo de verficar se no dicionario de novos estados ja existe um estado com id igual ao informado
    # Retorna o estado correspondente caso o estado ja exista no dicionario de novos estados
    #Obs: Um estado q1;q2 é o mesmo que q2;q1 pois em conjuntos a ordem não importa
    def __verify_states_in_new_states__(self,new_states :dict,new_state :Vertice):
        new_state_id = new_state.id.split(';')
        if '' in new_state_id:
            new_state_id.remove('')
        for key in new_states:
            equals_states_count = 0
            actual_new_state_id = key.split(";")
            if '' in actual_new_state_id:
                actual_new_state_id.remove('')
            if len(new_state_id) == len(actual_new_state_id):
                for separeted_state in actual_new_state_id:
                    if separeted_state in new_state_id:
                        equals_states_count += 1
                
                if equals_states_count == len(actual_new_state_id):
                    return key
        
        return None
    
    # Retorna os novos estados finais do novo automato convertido gerado
    # OBS: Funcao utilizada exclusivamente na conversão do automato
    def __return_new_final_states__(self,states :list):
        new_final_states = []
        acutal_final_states_id = [stateId.id for stateId in self.__final_states]
        for state in states:
            states_processed = state.id.split(";")
            for state_processed in states_processed:
                if state_processed in acutal_final_states_id:
                    new_final_states.append(state)
                    break
        
        return new_final_states

    def print_automaton(self):
        estado_inicial_info = "ESTADO INICIAL: {0}\n".format(str(self.__initial_state))
        estados_finais_info = "ESTADOS FINAIS: {0}\n".format([str(estado_final) for estado_final in self.__final_states])  
        estados_info = "ESTADOS:\n"
        for estados in range(0,len(self.__grafo.vertices)):
            estados_info += "{0}) {1}\n".format(estados+1,self.__grafo.vertices[estados])
        transicoes_info = "TRANSIÇÔES:\n"
        cont_transicoes = 1
        for estado in self.__grafo.vertices:
            arestasVertice = estado.arestas
            for key in arestasVertice:
                arestas = arestasVertice[key]
                for aresta in arestas:
                    transicoes_info += "{0}) {1} -> {2} = {3}\n".format(cont_transicoes,aresta.vertice_inicio,aresta.vertice_fim,aresta.id)
                    cont_transicoes+=1

        return estado_inicial_info + estados_finais_info + estados_info + transicoes_info