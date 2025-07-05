
#VAMOS A REALIZAR UN EJEMPLO PRACTICO ACERCA DE UNA CUENTA BANCARIA IMPLEMENTADO EL ENCAPSULAMIENTO.
#CREAR UNA CLASE LLAMADA CUENTA BANCARIA, QUE TENGA LOS TRIBUTOS, NOMBRE, APELLIDO, SALDO, NUMERO_CUENTA.
#QUE TENGA LOS SIGUIENTES METODOS, INGRESAR MONTO, RETIRAR, CONSULTAR SALDO, MOSTRAR INFORMACION COMPLETA
class CuentaBancaria:
    def __init__(self, nombre, apellido, numero_cuenta, saldo_inicial = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial
        
    #Implementar los getter
    def get_numero_cuenta(self):
        return self.__numero_cuenta
    
    def get_saldo(self):
        return self.__saldo
    
    #implementar el metodo para depositar monto
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f'se ha depositado {monto:.2f} con exito. nuevo saldo actual: {self.__saldo}')
            return True
        else:
            print('El monto debe ser mayor a 0')
            return False
        
    #Implementar el metodo para retirar monto
    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            print(f'se ha retirado {monto:.2f} correctamente. nuevo saldo actual: {self.__saldo}')
        else:
            print('El monto debe ser mayor a 0 y menor al saldo actual')
            
    #Imprementar el metodo para enviar monto
    def enviar(self, cuenta_destino, monto):
        if isinstance(cuenta_destino, CuentaBancaria):
            if monto > 0:
                if self.__saldo >= monto:
                    self.__saldo -= monto
                    cuenta_destino.depositar(monto)
                    print(f'Se ha enviado {monto:.2f} a la cuenta de la persona {cuenta_destino.nombre} Numero de cuenta {cuenta_destino.get_numero_cuenta()} con exito: nuevo saldo. {self.__saldo}')
                else:
                    print('Fondos insuficientes al realizar la trasaccion')
            else:
                print('El monto debe ser mayor a 0')
        else:
            print('Cuenta de destino no valida')
     
     #Imprimir el saldo actual
    def imprimir_saldo(self):
        print(f'saldo actual {self.get_saldo()}')
        
    #Imprimir los datos de la cuenta bancaria
    def estado_cuenta(self):
        print(f'Nombre completo {self.nombre} {self.apellido}')
        print(f'Numero de cuenta {self.get_numero_cuenta()}')
        print(f'Saldo actual {self.get_saldo()}')
                 
#Imprimir los objetos
#crear 2 cuentas
cuenta1 = CuentaBancaria("Carlos", 'Guerrero', "123456789", 1000)
cuenta2 = CuentaBancaria("Ana", 'Belen', "987654321", 500)

#depositar a la cuenta
cuenta1.depositar(900)
#Retirar de la cuenta
cuenta1.retirar(200)
#Enviar dinero
cuenta1.enviar(cuenta2, 400)
#Mostrar el estado de cuenta
cuenta1.estado_cuenta()
cuenta2.estado_cuenta()

