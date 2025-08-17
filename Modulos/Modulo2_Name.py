import Modulo1_Name
# modulo2.py



def operaciones():
    print("Usando funciones de modulo1 desde modulo2")
    print("7 + 8 =", Modulo1_Name.sumar(7, 8))
    print("9 - 4 =", Modulo1_Name.restar(9, 4))
    print("6 * 6 =", Modulo1_Name.multiplicar(6, 6))
    print("20 / 5 =", Modulo1_Name.dividir(20, 5))

if __name__ == "__main__":
    operaciones()
