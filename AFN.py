import graphviz

class AFN(object):
    def __init__(self, postfix):
        #Postfix
        self.binary_tree    = []
        self.postfix        = postfix
        self.operators      = ['(',')','|','*','?','+','.']
        self.movement_record = []


        '''AFN consist of:'''
        #The values of these variables will change

        #initial state
        self.q_o = None
        #Transition function
        self.delta = {}
        #Input simbols
        self.sigma = []
        #Finite set of states
        self.que = []
        #Acceptence states
        self.F = []

        #AFN creation
        self.transform_postfix_to_afn()
        self.AFN_graph()

    def children_position(self, node, analisis):
        recorrido = node - 1
        hijos = []

        while (recorrido != -1):
            if analisis[recorrido].analyzed == False and len(hijos) < 2:
                hijos.append(recorrido)
            recorrido -= 1

        return hijos

    def transform_postfix_to_afn(self):

        #STR to LIST
        self.postfix = list(self.postfix)

        #Binary_tree fill
        for symbol in range(len(self.postfix)):
            self.binary_tree.append(AFN_node(self.postfix[symbol],0,0))

        #Lead transition only
        for node in self.binary_tree:
            if node.value not in self.operators:
                node.former = 'q'+str(len(self.que))
                node.after = 'q'+str(len(self.que)+1)
                self.que.append('q'+str(len(self.que)))
                self.que.append('q'+str(len(self.que)))
                self.movement_record.append(AFN_tran(node.value, node.former, node.after))

        #Lead plus operators relantions and transitions

        #For every operator there has to be a transition registration
        #And a new states creation
        for node in range(len(self.binary_tree)):
            if self.binary_tree[node].value == '*':
                print('\nEncontre cerradura Klene')

                #Start and End respectively
                self.binary_tree[node].former = 'q'+str(len(self.que))
                self.binary_tree[node].after= 'q'+str(len(self.que)+1)

                #New states
                self.que.append('q'+str(len(self.que)))
                self.que.append('q'+str(len(self.que)))

                #Transitions
                #EL fin de su hijo se conecta con el inicio de su hijo
                self.movement_record.append(AFN_tran("E",self.binary_tree[self.children_position(node, self.binary_tree)[0]].after, self.binary_tree[self.children_position(node, self.binary_tree)[0]].former))

                #El inicio de Kleene se conecta con el inicio de su hijo
                self.movement_record.append(AFN_tran("E",self.binary_tree[node].former, self.binary_tree[self.children_position(node, self.binary_tree)[0]].former))

                #el fin de su hijo se conecta al fin de Kleene
                self.movement_record.append(AFN_tran("E",self.binary_tree[self.children_position(node, self.binary_tree)[0]].after,self.binary_tree[node].after))

                #El inicio de Klene se conecta con el fin de kleene
                self.movement_record.append(AFN_tran("E",self.binary_tree[node].former,self.binary_tree[node].after))

                #The sons are already analyzed
                self.binary_tree[self.children_position(node, self.binary_tree)[0]].analyzed = True

            elif self.binary_tree[node].value == '.':
                print('\nEncontre concatenacion')

                #Se encuentran los hijos de concatenacion
                # print(self.binary_tree[self.children_position(node, self.binary_tree)[1]])
                # print(self.binary_tree[self.children_position(node, self.binary_tree)[0]])

                # estados_borrar = []
                # estados_borrar.append(self.binary_tree[self.children_position(node, self.binary_tree)[0]].after)
                # estados_borrar.append(self.binary_tree[self.children_position(node, self.binary_tree)[1]].former)

                # for elemento in estados_borrar:
                #     if elemento in self.que:
                #         self.que.remove(elemento)
                # print('\nEncontre concatenacion')

                #Inicio y fin del nodo

                self.binary_tree[node].former = self.binary_tree[self.children_position(node, self.binary_tree)[1]].former
                self.binary_tree[node].after = self.binary_tree[self.children_position(node, self.binary_tree)[0]].after


                #El final del hijo izquierdo se conecta al inico del hijo derecho

                self.movement_record.append(AFN_tran("E",self.binary_tree[self.children_position(node, self.binary_tree)[1]].after,self.binary_tree[self.children_position(node, self.binary_tree)[0]].former))

                self.binary_tree[self.children_position(node, self.binary_tree)[1]].analyzed = True
                self.binary_tree[self.children_position(node, self.binary_tree)[0]].analyzed = True

            elif self.binary_tree[node].value == '|':
                print('\nEncontre or')
                #Inicio y fin del nodo

                self.binary_tree[node].former = 'q'+str(len(self.que))
                self.binary_tree[node].after = 'q'+str(len(self.que) + 1)
                self.que.append('q'+str(len(self.que)))
                self.que.append('q'+str(len(self.que)))

                #Registro de transiciones

                #El inicio de or se conecta a los inicios de sus hijos
                self.movement_record.append(AFN_tran("E",self.binary_tree[node].former, self.binary_tree[self.children_position(node, self.binary_tree)[1]].former))
                self.movement_record.append(AFN_tran("E",self.binary_tree[node].former, self.binary_tree[self.children_position(node, self.binary_tree)[0]].former))

                #Los finales de sus hijos se conectan al final de or

                self.movement_record.append(AFN_tran("E",self.binary_tree[self.children_position(node, self.binary_tree)[1]].after,self.binary_tree[node].after))
                self.movement_record.append(AFN_tran("E",self.binary_tree[self.children_position(node, self.binary_tree)[0]].after,self.binary_tree[node].after))

                #Marcar que ya fue visitado

                self.binary_tree[self.children_position(node, self.binary_tree)[1]].analyzed = True
                self.binary_tree[self.children_position(node, self.binary_tree)[0]].analyzed = True

            elif self.binary_tree[node].value == '+':
                print('\nEncontre cerradua positiva')
            elif self.binary_tree[node].value == '?':
                print('\nEncontre nada o una instancia de lo asociado')


        #Crea el alfabeto
        for x in self.postfix:
            if x not in self.operators:
                self.sigma.append(x)
        self.sigma.append('E')

        # Lee los movimientos de movement_record y los almacena en self.delta
        for x in self.que:
            self.delta[x] = {}
        for x in self.delta:
            for letra in self.sigma:
                self.delta[x][letra] = []
        for x in self.delta:
            for letra in self.sigma:
                for tran in self.movement_record:
                    if x == tran.inicio and tran.dato == letra:
                        self.delta[x][letra].append(tran.fin)

        self.F.append(self.binary_tree[-1].after)
        self.q_o = self.binary_tree[-1].former

        #Limpieza de self.delta
        while True:
            duplicado = False
            for elemento in self.sigma:
                if self.sigma.count(elemento) > 1:
                    self.sigma.remove(elemento)
                    duplicado = True
            if not duplicado:
                break
        for clave, valor in self.delta.items():
            for clave2, valor2 in valor.items():
                valor[clave2] = list(set(valor2))

        '''AFN consist of:'''
        #The final value of the variables
        print(f'\nEstados ->{self.que}')
        print(f'Transiciones ->\n')

        for x in self.delta:
            print(x, "", self.delta[x])
        print(f'\nSimbolos ->{self.sigma}')
        print(f'Estados de aceptacion ->{self.F}')
        print(f'Estado inicial->{self.q_o}\n')

        print("\nMovement_record\n")
        for data in self.movement_record:
            print(data)

    def AFN_graph(self):
        ##Graficas
        f= graphviz.Digraph(name="AFN")
        f.attr(rankdir='LR')

        for x in self.delta:
            if x == self.F[0]:
                f.node(str(x), shape = "doublecircle")
            else:
                f.node(str(x), shape = "circle")

        for x in self.delta:
            for y in self.delta[x]:
                    if len(self.delta[x][y]) != 0:
                        for w in self.delta[x][y]:
                            f.edge(x,w, label = y, arrowhead='vee')

        f.node("", height = "0",width = "0", shape = "box")
        f.edge("",self.q_o, arrowhead='vee', )
        f.render("AFN", view = "True")


class AFN_node:
    def __init__(self, value, former, after):

        self.after = after
        self.value = value
        self.former = former
        self.analyzed = False

    def __str__(self):
        return f'Value -> {self.value}  Antes -> {self.former}  Despues -> {self.after}'

class AFN_tran:
    def __init__(self, dato, inicio, fin):

        self.dato = dato
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        return f'{self.inicio}  --> {self.dato} --> {self.fin}'