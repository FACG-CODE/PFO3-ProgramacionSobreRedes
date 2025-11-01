import threading
from models.funcionesSocket import inicializarSocket, conectarSocket
import json

# Configuracion del servidor
HOST = 'localhost'
PORT = 5000

# Funcion principal para ejecutar el servidor
def ejecutarServidor(): 
    # Inicializar el socket del servidor
    socketServidor = inicializarSocket(HOST, PORT)
    if socketServidor is None:
        print("No se pudo iniciar uno o ambos servidores.")
        return # Salir si no se pudo inicializar el socket
    print (f"Servidor escuchando en {HOST}:{PORT}")
    try:
        while True:
            # Aceptar una conexion en ambos servidores
            conn, addr = socketServidor.accept()
            # Procesar la conexion del cliente en un hilo separado
            hilo = threading.Thread(target=procesarSolicitudCliente, args=(conn, addr))
            # Iniciar el hilo
            hilo.start()
    except Exception as e:
        print(f"Error: {e}")

# Procesar la conexion con el cliente
def procesarSolicitudCliente(conn, addr):
    print(f"Conexion establecida desde {addr}")
    socketWorkerEscritura = None
    socketWorkerLectura = None
    try: 
        while True:
            mensaje = conn.recv(1024).decode("utf-8")
            if mensaje.lower() == "off":
                print("Cerrando conexion con el cliente.")
                conn.send("Conexión terminada.".encode('utf-8'))
                break
            # CONECTAR CON WORKERS DESDE AQUI
            socketWorkerEscritura = conectarSocket('localhost', 6000)
            if socketWorkerEscritura is None:
                print("No se pudo conectar al worker de escritura.")
                conn.send("Error: No se pudo avanzar con el registro.".encode('utf-8'))
                break
            # Enviar mensaje al worker de escritura
            socketWorkerEscritura.send(mensaje.encode('utf-8'))
            # Recibir confirmacion del worker de escritura
            confirmacion = socketWorkerEscritura.recv(1024).decode('utf-8')
            if confirmacion != "ok":
                print("Error al registrar el libro.")
                conn.send("Error al registrar el libro.".encode('utf-8'))
            else:
                socketWorkerLectura = conectarSocket('localhost', 7000)
                if socketWorkerLectura is None:
                    print("No se pudo conectar al worker de lectura.")
                    conn.send("Error: No se pudo obtener el ID del libro.".encode('utf-8'))
                    break
                # Solicitar ID del libro al worker de lectura
                socketWorkerLectura.send("ok".encode('utf-8'))
                respuesta = socketWorkerLectura.recv(1024).decode('utf-8')
                conn.send(respuesta.encode('utf-8'))
    except Exception as e:
        print(f"Error al procesar la solicitud del cliente: {e}")
    finally:
        if socketWorkerEscritura:
            socketWorkerEscritura.close()
        if socketWorkerLectura:
            socketWorkerLectura.close()
        conn.close()
        print("Fin del Programa.")
      
        
            