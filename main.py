"""
Autor: Gabriel Vicente (20498)
Proyecto: Laboratorio A

Descripción:
Laboratorio A para la clase Diseño de Lenguajes
Generar AFN a partir de una expresión regular

Tomando en cuenta operaciones y abreviaturas
[* , + , . , ? , |]

Al igual que la jerarquia de los parentesis
"""

from InfixToPostfix import *
from AFN import *
#REGEX EXAMPLES

#"ab*ab*"
#"0?(1?)?0*"
#"(a*|b*)c"
#"(b|b)*abb(a|b)*"
#"(a|ε)b(a+)c?"
#"(a|b)*a(a|b)(a|b)"

#Solicitud de regex
regex = "(a|b)*a(a|b)(a|b)"

#Postfix
print(InfixToPostfix(regex))
AFN(InfixToPostfix(regex).postfix)

























#AFN

#Validación de AFN

#AFD a partir de AFN

#Validacion de AFD a partir de AFN

#AFD directo

#Validacion de AFD directo
