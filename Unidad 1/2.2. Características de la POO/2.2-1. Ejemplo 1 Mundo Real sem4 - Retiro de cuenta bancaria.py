class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de {monto} realizado. Nuevo saldo: {self.saldo}")
            self.imprimir_comprobante("Depósito", monto)
        else:
            print("El monto de depósito debe ser mayor que cero.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Nuevo saldo: {self.saldo}")
            self.imprimir_comprobante("Retiro", monto)
        else:
            print("Fondos insuficientes o monto inválido para retiro.")

    def consultar_saldo(self):
        print(f"Saldo actual de la cuenta de {self.titular}: {self.saldo}")

    def imprimir_comprobante(self, operacion, monto):
        print("*********** COMPROBANTE ***********")
        print(f"Titular: {self.titular}")
        print(f"Operación: {operacion}")
        print(f"Monto: {monto}")
        print(f"Nuevo saldo: {self.saldo}")
        print("***********************************")


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una cuenta bancaria para Mauricio Torres
    cuenta_mauricio = CuentaBancaria("Mauricio Torres", 1000)

    # Realizar operaciones y generar comprobantes
    cuenta_mauricio.consultar_saldo()
    cuenta_mauricio.depositar(500)
    cuenta_mauricio.retirar(200)
    cuenta_mauricio.consultar_saldo()


