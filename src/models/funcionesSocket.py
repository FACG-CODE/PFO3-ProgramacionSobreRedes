import socket

# Inicializar socket
def inicializarSocket(HOST, PORT):
    try:
        # Se crea Socket TCP como objeto, debido que al utilizar WITH se cierra automaticamente al salir del bloque
        socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Asociar el socket a la direccion y puerto definidos
        socket_servidor.bind( (HOST, PORT) )
        # Socket en modo escucha
        socket_servidor.listen()
        # Retornar el socket creado
        return socket_servidor
    except OSError as e:
        print(f"Error al iniciar el socket: {e}")
        return None

def conectarSocket(HOST, PORT):
    try:
        # Crear un socket TCP para conectarse al servidor
        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conectar al servidor
        socket_cliente.connect( (HOST, PORT) )
        # Retornar el socket conectado
        return socket_cliente
    except OSError as e:
        print(f"Error al conectar el socket: {e}")
        return None
