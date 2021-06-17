class Seller: #Creamos el objeto "Seller" para que pueda ser utilizada con diferentes vendedores
    def __init__(self, id):
        self.id = i
    def __str__(self):
        return f"Seller [{self.id}]; "

class Product: #Creamos el objeto "Producto" para poder agregarlo luego a su respectivo vendedor 
    nProducts = 0 #Definimos una variable que irá incrementando en la linea 11 para generar un id de vendedor
    def __init__(self, title, categoryId, name):
        self.idItem = self.nProducts + 1
        self.title = title
        self.categoryId = categoryId
        self.name = name
    def __str__(self): #Definimos el output para luego utilizarlo en los logs
        return f" {sellerTest.__str__()}Item [{self.idItem}]: {self.title}, Category: [{self.categoryId}] - {self.name}; "

option = 1 #Acumulador para bucle
sellers = [] #Creamos la lista de vendedores
while option != 2: #Creamos un bucle para agregar más de un vendedor
    seller_id = int(input("Seller Id? ")) # Se pregunta el ID del vendedor para luego ser utilizado en la impresión y en la generación de los logs
    sellers.append(seller_id) #Agregamos los vendedores a la lista "sellers"
    option = int(input("Quieres agregar otro seller? 1: Si, 2: No. ")) #Preguntamos mediante un condicional si se desea agregar un nuevo vendedor

products = [] #Creamos una lista para ir agregando los productos creados
for i in sellers:
    sellerTest = Seller(i) #Creamos el Seller "sellerTest"
    optionP = 1 #Acumulador para bucle de productos
    while optionP != 2: #Bucle para agregar productos
        productTest = Product(input("Nombre del producto"),int(input("Id de la categoría")),input("Categoría")) #Creamos el Product "productTest"
        products.append(productTest.__str__()) #Agregamos el producto a la lista
        optionP = int(input("Quieres agregar otro producto? 1: Si, 2: No."))
    for i in products: #Creamos un bucle en el cual se leerán los productos de la lista y a su vez se agregarán a los logs
        print(i.__str__()) #Imprimimos en pantalla el respectivo vendedor con su producto
        Ruta = "C:\\Users\\AgusB\\Downloads\\Descargas\\Python\\PYTHON\\MLA\\example.log" #Generamos una variable con la ruta de salida de los logs
        with open(Ruta, 'a', encoding= 'UTF8') as log: #Abrimos/creamos el archivo de log para luego modificarlo
            log.write(i.__str__() + '\n') #Se agrega el output del producto deseado y un salto de linea para mantener un orden.
    products.clear() 