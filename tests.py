# texto_con_espacios = "Este es un ejemplo de texto con   espacios"
# texto_sin_espacios = texto_con_espacios.replace(" ", "")
# print(texto_sin_espacios)

# cadena = input("Ingresa una cadena: ")  # Solicita al usuario que ingrese una cadena
# nueva_cadena = ".".join([caracter for caracter in cadena]) # Crea una lista de caracteres separados por un punto y une los elementos en un string
# # print(nueva_cadena)  # Imprime la nueva cadena con los caracteres separados por puntos
# def shunting_yard(infix):
#     # Crear un diccionario para asociar la precedencia con cada operador
#     precedence = {'*': 100, '+': 90, '?': 100, '.': 80, '|': 60, '(': 40, ')': 20}

#     # Crear dos pilas para operadores y operandos
#     output_queue = []
#     operator_stack = []

#     # Iterar sobre cada caracter en la expresión infix
#     for char in infix:
#         if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or char in '0123456789':
#             # Si el carácter es una letra o un número, agregarlo a la salida
#             output_queue.append(char)
#         elif char == '(':
#             # Si el carácter es un paréntesis izquierdo, agregarlo a la pila de operadores
#             operator_stack.append(char)
#         elif char == ')':
#             # Si el carácter es un paréntesis derecho, desapilar los operadores hasta encontrar el paréntesis izquierdo correspondiente
#             while operator_stack[-1] != '(':
#                 output_queue.append(operator_stack.pop())
#             operator_stack.pop()
#         elif char in precedence:
#             # Si el carácter es un operador, desapilar los operadores de mayor o igual precedencia y agregarlos a la salida
#             while operator_stack and operator_stack[-1] != '(' and precedence[char] <= precedence[operator_stack[-1]]:
#                 output_queue.append(operator_stack.pop())
#             operator_stack.append(char)

#     # Desapilar cualquier operador restante y agregarlo a la salida
#     while operator_stack:
#         output_queue.append(operator_stack.pop())

#     # Unir la salida y devolverla como una cadena
#     return ''.join(output_queue)


# # Definir la expresión regular en notación infix
# infix = "a|b.c"

# # Convertir la expresión regular a notación postfix utilizando el algoritmo Shunting Yard
# postfix = shunting_yard(infix)

# print(postfix)

# Lista = ['q1','q2','q3','q4']
# Transiciones = [['q1','a','q2'], ['q2','E','q3'], ['q3','a','q4']]

# # Eliminar la transición ['q2','E','q3'] de Transiciones
# Transiciones.remove(['q2','E','q3'])

# # Actualizar Lista para unir q2 y q3
# Lista.remove('q3')
# Lista.remove('q2')
# Lista.insert(2, 'q2q3')

# # Actualizar Transiciones para reemplazar q2 y q3 por q2q3
# for i in range(len(Transiciones)):
#     if Transiciones[i][0] == 'q2':
#         Transiciones[i][0] = 'q2q3'
#     elif Transiciones[i][2] == 'q2':
#         Transiciones[i][2] = 'q2q3'
#     elif Transiciones[i][0] == 'q3':
#         Transiciones[i][0] = 'q2q3'
#     elif Transiciones[i][2] == 'q3':
#         Transiciones[i][2] = 'q2q3'

# print(Lista)
# print(Transiciones)

Lista = ['q1','q2','q3','q4']
Transiciones = ['q1','q2']

for elemento in Transiciones:
    if elemento in Lista:
        Lista.remove(elemento)

print(Lista)
