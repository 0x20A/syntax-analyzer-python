
def analizador_sintactico(expr):
    # error: if the end is a operator
    if expr[-1] in "+-*/":
        return "Error sintáctico: No es posible terminar la expresión con un operador."
    
    # error: if the beggin is a operator
    if expr[0] in "+-*/":
        return "Error sintáctico: No es posible iniciar la expresión con un operador."
    
    i = 0
    while i < len(expr):
        # jump spaces
        if expr[i] == " ":
            i += 1
            continue

        # error: consecutive operators
        if i > 0 and expr[i] in "+-*/" and expr[i - 1] in "+-*/":
            return "Error sintáctico: No puede haber operadores seguidos."
        
        # error: space between values
        if i < len(expr) - 1 and expr[i].isdigit() and expr[i + 1] == " " and expr[i + 2].isdigit():
            return "Error sintáctico: Debe haber un operador entre los valores."
        
        i += 1

    return "analisis sintactico correcto"
