class Producto:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self):
        return (f"Código: {self.codigo}\n"
                f"Nombre: {self.nombre}\n"
                f"Precio: {self.precio}\n"
                f"Existencia: {self.existencia}")