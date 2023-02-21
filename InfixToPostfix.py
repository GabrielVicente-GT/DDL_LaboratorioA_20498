

class InfixToPostfix(object):
    def __init__(self, regex):
        self.regex          = regex
        self.postfix        = ''
        self.regex_array    = []
        self.postfix_operators      = ['(','.','|',')']
        self.regex_operators_ni     = ['(',')','|','*','?','+']
        self.postfix_stack  = []

        self.clean_regex()
        self.transform()


    def clean_regex(self):
        self.regex = self.regex.replace(' ','')
        self.regex = '.'.join([caracter for caracter in self.regex])
        self.regex = list(self.regex)
        for symbol, char in enumerate(self.regex):
            if char == '.' and 0 < symbol < len(self.regex) - 1:
                prev_char = self.regex[symbol - 1]
                next_char = self.regex[symbol + 1]
                if prev_char not in self.regex_operators_ni and next_char not in self.regex_operators_ni:
                    self.regex[symbol] = '.'
                elif prev_char == '*' and next_char not in self.regex_operators_ni:
                    self.regex[symbol] = '.'
                elif prev_char == '*' and next_char == '(':
                    self.regex[symbol] = '.'
                elif prev_char == ')' and next_char not in self.regex_operators_ni:
                    self.regex[symbol] = '.'
                elif prev_char == '?' and next_char not in self.regex_operators_ni:
                    self.regex[symbol] = '.'
                elif prev_char == '?' and next_char == '(':
                    self.regex[symbol] = '.'
                elif prev_char not in self.regex_operators_ni and next_char == '(':
                    self.regex[symbol] = '.'
                elif prev_char == ')' and next_char == '(':
                    self.regex[symbol] = '.'
                else:
                    self.regex[symbol] = ''
        self.regex = ''.join(self.regex)

    def priority(self, operando, pilalast):
        valor = -1
        if operando== '.' and pilalast == '|':
            valor = 1
        elif pilalast == '.' and operando == '|':
            valor = 0
        elif pilalast == operando:
            valor = 0
        return valor

    def transform(self):
        #Creacion del arreglo a convertir
        self.regex = '('+self.regex+')'
        self.regex = list(self.regex)
        for symbol in self.regex:
            self.regex_array.append(Nodo(symbol))

        #Logica postfix
        for nodo in self.regex_array:
            #si es un alfabeto se agrega al stack
            if nodo.value not in self.postfix_operators:
                self.postfix += nodo.value
            #Si el carácter leído es un paréntesis izquierdo este se agrega al stack
            elif nodo.value == '(':
                self.postfix_stack.append(nodo.value)
            # Si el carácter leído corresponde a un paréntesis derecho, se agregan todos los operadores dentro de la self.postfix_stack a la expresión postfix hasta encontrar su paréntesis izquierdo y dentro de la self.postfix_stack se eliminan todos los paréntesis utilizados y operadores agregados a la expresión postfix
            elif nodo.value == ')':
                while(self.postfix_stack[-1] !='('):
                    self.postfix += self.postfix_stack.pop()
                self.postfix_stack.pop()
            #Si el carácter leído es una operación, utilizando la función priority, si la priority del carácter leído es mayor a la priority del operador encima de la self.postfix_stack, el caracter leido se agrega al postfix, en caso contrario, se agrega el operador en la cima de la self.postfix_stack al postfix y el caracter leido se agrega a la self.postfix_stack
            else:
                if len(self.postfix_stack)==0:
                    self.postfix_stack.append(nodo.value)
                else:
                    if self.priority(nodo.value, self.postfix_stack[-1]) == 1 or self.priority(nodo.value, self.postfix_stack[-1]) == -1:
                        self.postfix_stack.append(nodo.value)

                    elif self.priority(nodo.value, self.postfix_stack[-1]) == 0 :
                        self.postfix += self.postfix_stack.pop()
                        self.postfix_stack += nodo.value
        self.regex = ''.join(self.regex)
    def __str__(self):
        return f'Regex -> {self.regex} || Postfix -> {self.postfix}'

class Nodo:
    def __init__(self, value):

        self.value = value
        self.ascii_value = ord(value)

    def __str__(self):
        return f'Valor -> {self.value} ASCII -> {self.ascii_value}'