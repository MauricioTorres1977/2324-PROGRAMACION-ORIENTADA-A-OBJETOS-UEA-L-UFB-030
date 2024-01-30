class RegistroPintura:
    def __init__(self, codigo_color, tipo_pintura):
        """
        Constructor de la clase RegistroPintura.
        
        Parameters:
        - codigo_color (str): El código de color asociado al registro.
        - tipo_pintura (str): El tipo de pintura asociado al registro.
        """
        self.codigo_color = codigo_color
        self.tipo_pintura = tipo_pintura
        print(f"Nuevo registro de pintura creado. Código de color: {self.codigo_color}, Tipo de pintura: {self.tipo_pintura}")

    def __del__(self):
        """
        Destructor de la clase RegistroPintura.
        Se ejecuta cuando el objeto está a punto de ser destruido.
        """
        print(f"Registro de pintura eliminado. Código de color: {self.codigo_color}, Tipo de pintura: {self.tipo_pintura}")

# Crear instancias de la clase RegistroPintura para tres tipos de pintura
satinada = RegistroPintura("FF5733", "Satinada")
mate = RegistroPintura("00A86B", "Mate")
esmalte = RegistroPintura("89609E", "Esmalte")

# Acceder a los atributos de las instancias
print(f"Pintura satinada - Código de color: {satinada.codigo_color}, Tipo de pintura: {satinada.tipo_pintura}")
print(f"Pintura mate - Código de color: {mate.codigo_color}, Tipo de pintura: {mate.tipo_pintura}")
print(f"Pintura esmalte - Código de color: {esmalte.codigo_color}, Tipo de pintura: {esmalte.tipo_pintura}")

# Eliminar instancias (esto activará los destructores)
del satinada
del mate
del esmalte

