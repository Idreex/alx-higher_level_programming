#!/usr/bin/python3
if __name__ == "__main__": #e y no cuando es importado (ya sea por otro script o lo que sea). La letra del ej nos pide
    # que pongamos esa condicion.
    from add_0 import add #os la funcion "add" del modulo "add_0" que creamos en otro archivo.
    a = 1
    b = 2
    result = add(a, b)
    print(f"{a} + {b} = {result}")
