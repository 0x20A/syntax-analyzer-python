
# operators precedence:
# + and -: 1
# / and *: 2
def precedence(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    return 0

# do the operations
def do_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Error semántico: No se puede dividir entre 0.")
        return a / b

def analizador_semantico(expr):
    valores = [] # values stack
    operadores = [] # operators stack
    i = 0 # index

    # jump spaces
    while i < len(expr):
        if expr[i] == " ":
            i += 1
            continue
        # store more than 1 digit with a buffer (it'll multiply by 10 to add the other digits)
        elif expr[i].isdigit():
            buffer = 0
            while i < len(expr) and expr[i].isdigit():
                buffer = buffer * 10 + int(expr[i])
                i += 1
            valores.append(buffer) 
            i -= 1 # it'll store on the values stack and the index decrease
        elif expr[i] in "+-*/":
            # while the last operator >= precedence:
            while operadores and precedence(operadores[-1]) >= precedence(expr[i]):
                val2 = valores.pop()
                val1 = valores.pop()
                operador = operadores.pop()
                valores.append(do_op(val1, val2, operador)) # do the operation popping the last to values and the operator
            operadores.append(expr[i])
 
        i += 1

    # do the operation with the last values
    while operadores:
        val2 = valores.pop()
        val1 = valores.pop()
        operador = operadores.pop()
        valores.append(do_op(val1, val2, operador))

    return valores[0]
