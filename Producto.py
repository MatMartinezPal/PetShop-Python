class Producto():
    """
        Producto: Información de los productos ofertados en la tienda
        Atributos: id, nombre, descripcion, valor, cantidadInventario, pedidos, comentarios
    """
    productos = []
    contador_ids = 0

    def __init__(self, nombre="", descripcion="", valor=0, cantidadInventario=0):
        """
            Id: self._id
            Name: self._nombre
            Description: self._descripcion
            Price: self._valor
            Amount in inventory: self._cantidadInventario
        """
        Producto.contador_ids += 1
        self.setId(Producto.contador_ids)
        self.setNombre(nombre)
        self.setDescripcion(descripcion)
        self.setValor(valor)
        self.setCantidadInventario(cantidadInventario)
        self.setPedidos([])
        self.setComentarios([])

    def setId(self, id):
        self._id = id

    def getId(self):
        return self._id

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def getDescripcion(self):
        return self._descripcion

    def setValor(self, valor):
        self._valor = valor

    def getValor(self):
        return self._valor

    def setCantidadInventario(self, cantidadInventario):
        self._cantidadInventario = cantidadInventario

    def getCantidadInventario(self):
        return self._cantidadInventario

    def setPedidos(self, pedidos):
        self._pedidos = pedidos

    def getPedidos(self):
        return self._pedidos

    def setComentarios(self, comentarios):
        self._comentarios = comentarios

    def getComentarios(self):
        return self._comentarios

    def toString(self, mensajes):
        return mensajes["ID"] + str(self.getId()) + mensajes["user_name"] + self.getNombre() + mensajes["value"] + str(
            self.getValor()) + mensajes["description"] + self.getDescripcion() + mensajes["amount_inventory"] + str(
            self.getCantidadInventario())

    def validarExistenciaEnLista(self, listamensajes):
        for productoActual in Producto.productos:
            if productoActual.getNombre().lower() == self.getNombre().lower():
                return listamensajes["product_with_same_name"]

        Producto.productos.append(self)
        return listamensajes["product_added"]

    def actualizarProducto(self, nombre, valor, descripcion, cantidadInventario):
        self._nombre = nombre
        self._valor = valor
        self._descripcion = descripcion
        self._cantidadInventario = cantidadInventario

    @staticmethod
    def buscarProductoNombre(nombreBuscar):
        listadoProductosBuscados = []
        for productoActual in Producto.productos:
            if productoActual.getNombre().lower().find(nombreBuscar.lower()) != -1:
                listadoProductosBuscados.append(productoActual)
        return listadoProductosBuscados

    @staticmethod
    def seleccionarProducto(numeroId):
        for productoActual in Producto.productos:
            if productoActual.getId() == numeroId:
                return productoActual

        return None

    @staticmethod
    def borrarProducto(numeroId, mensajes):
        for productoActual in Producto.productos:
            if productoActual.getId() == numeroId:
                Producto.productos.remove(productoActual)
                return mensajes["product_deleted"]

        return mensajes["product_not_found"]
