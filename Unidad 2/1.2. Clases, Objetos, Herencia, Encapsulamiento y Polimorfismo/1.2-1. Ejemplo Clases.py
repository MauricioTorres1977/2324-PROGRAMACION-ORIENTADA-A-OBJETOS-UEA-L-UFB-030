class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self._propietario = None  # Encapsulación

    def obtener_informacion(self):
        return f"{self.año} {self.marca} {self.modelo}"

    def asignar_propietario(self, propietario):
        self._propietario = propietario

    def obtener_propietario(self):
        return self._propietario


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_carroceria):
        super().__init__(marca, modelo, año)
        self.tipo_carroceria = tipo_carroceria

    def obtener_informacion(self):  # Polimorfismo (método sobrescrito)
        return f"{super().obtener_informacion()} - Carrocería: {self.tipo_carroceria}"


# Crear instancias de las clases
vehiculo1 = Vehiculo("Toyota", "Corolla", 2022)
automovil1 = Automovil("Honda", "Civic", 2021, "Sedán")

# Asignar propietario
vehiculo1.asignar_propietario("Mauricio Torres")
automovil1.asignar_propietario("Mauricio Torres")

# Obtener información de los vehículos y sus propietarios
print("Información del Vehículo 1:")
print(vehiculo1.obtener_informacion())
print(f"Propietario: {vehiculo1.obtener_propietario()}")

print("\nInformación del Automóvil 1:")
print(automovil1.obtener_informacion())
print(f"Propietario: {automovil1.obtener_propietario()}")

