# Inventario inicial de frutas y precios en quetzales
inventario = {
    'Banana': {'precio': 5.0, 'cantidad': 10},
    'Manzana': {'precio': 8.0, 'cantidad': 10},
    'Naranja': {'precio': 7.0, 'cantidad': 10},
    'Fresa': {'precio': 15.0, 'cantidad': 10},
    'Mango': {'precio': 12.0, 'cantidad': 10},
    'Piña': {'precio': 20.0, 'cantidad': 10},
    'Uva': {'precio': 18.0, 'cantidad': 10},
    'Papaya': {'precio': 10.0, 'cantidad': 10},
    'Sandía': {'precio': 25.0, 'cantidad': 10},
    'Limón': {'precio': 4.0, 'cantidad': 10},
}

# Almacenes para los datos del cliente y las compras
compras = []
clientes = []

def mostrar_inventario():
    print("\nInventario:")
    for producto, info in inventario.items():
        print(f"{producto}: Q{info['precio']:.2f} - Cantidad disponible: {info['cantidad']}")

def calcular_total(compras):
    total = sum(cantidad * inventario[producto]['precio'] for producto, cantidad in compras)
    return total

def aplicar_descuento(total):
    # Descuento del 10% si el total es mayor a 100 quetzales
    if total > 100:
        return total * 0.9
    return total

def main():
    nombre_cliente = input("Ingrese su nombre: ")
    seguir_comprando = True
    
    while seguir_comprando:
        mostrar_inventario()
        
        producto = input("Ingrese el nombre del producto que desea comprar (o 'fin' para terminar): ")
        if producto.lower() == 'fin':
            seguir_comprando = False
            continue
        
        if producto in inventario:
            cantidad = int(input(f"Ingrese la cantidad de {producto} que desea comprar (máximo {inventario[producto]['cantidad']}): "))
            # Verificar si la cantidad es válida y no excede el inventario
            if 0 < cantidad <= inventario[producto]['cantidad']:
                compras.append((producto, cantidad))
                # Reducir la cantidad en el inventario
                inventario[producto]['cantidad'] -= cantidad
            else:
                print(f"La cantidad debe estar entre 1 y {inventario[producto]['cantidad']}.")
        else:
            print("Producto no disponible en el inventario.")
    
    # Calcular el total
    total_compra = calcular_total(compras)
    total_final = aplicar_descuento(total_compra)

    # Mostrar resumen de compra
    print("\nResumen de compras:")
    for producto, cantidad in compras:
        print(f"{producto} x{cantidad}: Q{inventario[producto]['precio'] * cantidad:.2f}")
    
    print(f"Total antes de descuento: Q{total_compra:.2f}")
    print(f"Total final (descuento aplicado): Q{total_final:.2f}")

    # Almacenar información del cliente
    clientes.append((nombre_cliente, total_final))

    # Mostrar productos comprados
    print("\nProductos comprados:")
    for producto, cantidad in compras:
        print(f"{producto}: {cantidad}")

    print("\nClientes que compraron:")
    for cliente, total in clientes:
        print(f"{cliente} - Total: Q{total:.2f}")

if __name__ == "__main__":
    main()
