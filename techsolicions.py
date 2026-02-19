
import os

# Servicios disponibles
SERVICIOS = {
    'Desarrollo de software': 2000,
    'Soporte técnico': 500,
    'Consultoría tecnológica': 1500,
    'Auditoría de sistemas': 800
}

def mostrar_servicios():
    """Muestra servicios con for"""
    print("\n=== SERVICIOS ===")
    for i, (nombre, precio) in enumerate(SERVICIOS.items(), 1):
        print(f"{i}. {nombre}: ${precio}")
    print("==================\n")

def registrar_cliente(**datos):
    """Registra cliente con **kwargs y múltiples servicios"""
    if datos:
        return {**datos}
    
    os.system('clear')
    print("=== REGISTRO ===\n")
    
    cliente = {}
    campos = ['nombre', 'telefono', 'email', 'direccion']
    
    for campo in campos:
        cliente[campo] = input(f"{campo.capitalize()}: ")
    
    mostrar_servicios()
    print("Ingrese los números de servicios separados por comas (ej: 1,2)")
    opciones = input("Servicios: ").split(',')
    
    servicios_elegidos = []
    total_precio = 0
    
    for opcion in opciones:
        idx = int(opcion.strip()) - 1
        servicio = list(SERVICIOS.keys())[idx]
        precio = SERVICIOS[servicio]
        servicios_elegidos.append(servicio)
        total_precio += precio
    
    return {**cliente, 'servicios': servicios_elegidos, 'precio': total_precio}

def facturacion_descuentos(*args, **kwargs):
    """Facturación con *args/**kwargs - descuento 30% por 2+ servicios"""
    cliente = args[0] if args else kwargs
    nombre, email = cliente['nombre'], cliente['email']
    servicios, precio = cliente['servicios'], cliente['precio']
    
    # Descuento del 30% si eligió 2 o más servicios
    descuento = 30 if len(servicios) >= 2 else 0
    total = precio * (1 - descuento / 100)
    
    os.system('clear')
    print(f"\n=== FACTURACIÓN ===")
    print(f"Cliente: {nombre}")
    print(f"Servicios contratados:")
    for servicio in servicios:
        print(f"  - {servicio}")
    print(f"\nSubtotal: ${precio}")
    if descuento > 0:
        print(f"Descuento (2+ servicios): {descuento}%")
    print(f"Total: ${total}\n")
    
    def notificar(*msg):
        print(f"📧 {nombre} ({email}): {msg[0]}\n")
    
    return total, notificar

if __name__ == "__main__":
    os.system('clear')
    print("=== TECHSOLUCIONES ===\n")
    
    cliente = registrar_cliente()
    input("\n✓ Registrado. Enter...")
    
    total, notificar = facturacion_descuentos(cliente)
    input("Enter...")
    
    notificar(input("\nMensaje: "))
    input("Enter para salir...")
    
    total, notificar = facturacion_descuentos(cliente)
    input("Enter...")
    
    notificar(input("\nMensaje: "))
    input("Enter para salir...")








