from datetime import datetime

class Comprobante:
    def __init__(self, titular, operacion, monto, saldo):
        self.titular = titular
        self.operacion = operacion
        self.monto = monto
        self.saldo = saldo
        self.fecha = datetime.now()

    def imprimir(self):
        print("*********** COMPROBANTE ***********")
        print(f"Fecha: {self.fecha}")
        print(f"Titular: {self.titular}")
        print(f"Operación: {self.operacion}")
        print(f"Monto: {self.monto}")
        print(f"Nuevo saldo: {self.saldo}")
        print("***********************************")


class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.historial_transacciones = []

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            comprobante = Comprobante(self.titular, "Depósito", monto, self.saldo)
            self.historial_transacciones.append(comprobante)
            comprobante.imprimir()
        else:
            print("El monto de depósito debe ser mayor que cero.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            comprobante = Comprobante(self.titular, "Retiro", monto, self.saldo)
            self.historial_transacciones.append(comprobante)
            comprobante.imprimir()
        else:
            print("Fondos insuficientes o monto inválido para retiro.")

    def consultar_saldo(self):
        print(f"Saldo actual de la cuenta de {self.titular}: {self.saldo}")

    def imprimir_historial(self):
        print(f"Historial de transacciones para la cuenta de {self.titular}:")
        for transaccion in self.historial_transacciones:
            transaccion.imprimir()


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una cuenta bancaria para Mauricio Torres
    cuenta_mauricio = CuentaBancaria("Mauricio Torres", 1000)

    # Realizar operaciones y generar comprobantes
    cuenta_mauricio.consultar_saldo()
    cuenta_mauricio.depositar(500)
    cuenta_mauricio.retirar(200)
    cuenta_mauricio.consultar_saldo()

    # Imprimir historial de transacciones
    cuenta_mauricio.imprimir_historial()



