
def analizador_lexico(expr):
    i = 0
    while i < len(expr):
        # jump spaces
        if expr[i] == " ":
            i += 1
            continue

        # check if is not a digit or a valid operator
        if not expr[i].isdigit() and expr[i] not in "+-*/":
            return f"Error léxico: Carácter no válido '{expr[i]}' en la expresión."
        i += 1
    
    return "analisis lexico correcto"
