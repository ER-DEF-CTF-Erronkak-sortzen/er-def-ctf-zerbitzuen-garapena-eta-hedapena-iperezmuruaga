from pymodbus.client import ModbusTcpClient

# Configuración del cliente Modbus
client = ModbusTcpClient('127.0.0.1', port=502)

def leer_holding_registers(direccion, cantidad):
    lectura = client.read_holding_registers(1024,count=cantidad,slave=1)
    if not lectura.isError():
        return lectura.registers
    else:
        print(f"Error al leer los registros: {lectura}")
        return None

def escribir_holding_register(direccion, valor):
    escritura = client.write_register(direccion, valor)
    if not escritura.isError():
        print(f"Registro en la dirección {direccion} actualizado con el valor {valor}")
    else:
        print(f"Error al escribir en los registros: {escritura}")

if __name__ == "__main__":
    client.connect()

    # Leer registros holding desde la dirección 0x00 (16 registros)
    registros = leer_holding_registers(1024, 16)
    if registros:
        print(f"Registros leídos: {registros}")

    # Escribir un valor en un registro holding en la dirección 0x10
    #escribir_holding_register(0x10, 42)

    # Cerrar la conexión
    client.close()
