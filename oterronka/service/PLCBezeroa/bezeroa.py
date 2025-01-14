from pymodbus.client import ModbusTcpClient

def create_client():
    # Create a Modbus TCP client (replace with your Modbus server IP and port)
    client = ModbusTcpClient('127.0.0.1', port=502)  # Replace with the Modbus server IP address and port
    return client

def read_modbus_data(client, address, count):
	#Reads 'count' number of holding registers starting from 'address'
    try:
        # Connect to the Modbus server
        client.connect()

        # Read holding registers
        response = client.read_holding_registers(address, count, 1)  # Address, number of registers, unit ID
        #response = client.read_coils(0,10)
        if response.isError():
            print(f"Error: {response}")
        else:
                print(f"Data from address {address}: {response.registers}")
                #print(response)
                #print(response.bits[0])
                #print(response.bits[1])
                #print(response.bits[2])
    except Exception as e:
        print(f"Error reading Modbus data: {e}")
    finally:
    	# Always close the connection
    	client.close()



if __name__ == "__main__":
	# Create a client object
	modbus_client = create_client()

	# Read data from Modbus
	read_modbus_data(modbus_client, address=1024, count=8)  # Read 2 registers from address 0
