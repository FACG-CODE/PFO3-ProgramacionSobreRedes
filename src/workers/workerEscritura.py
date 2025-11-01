import socket
from models.funcionesSocket import inicializarSocket
import threading
import json
from database.db import guardarLibro

# Configuracion del worker de escritura
HOST = 'localhost'
PORT = 6000

def ejecutarWorkerEscritura():
    socketWorker = inicializarSocket(HOST, PORT)
    if socketWorker is None:
        print("No se pudo iniciar el worker de escritura.")
        return
    print(f"Worker de escritura escuchando en {HOST}:{PORT}")
    try:
        while True:
            conn, addr = socketWorker.accept()
            hilo = threading.Thread(target=procesarSolicitudServidor, args=(conn, addr))
            hilo.start()
    except Exception as e:
        print(f"Error en el worker de escritura: {e}")

def procesarSolicitudServidor(conn, addr):
    print(f"Conexion de escritura establecida desde {addr}")
    try:
        while True:
            mensaje = conn.recv(1024).decode("utf-8")
            if not mensaje:
                print("Mensaje vacío recibido en worker de escritura.")
                break
            # Aqui se procesaria el mensaje para escribir en la base de datos o archivo
            mensaje = json.loads(mensaje.strip())
            print(f"Datos de libro recibidos para escritura: {mensaje}")
            resultadoDb = guardarLibro(mensaje['titulo'], mensaje['autor'], mensaje['genero'])
            if resultadoDb:
                print("Libro guardado exitosamente en la base de datos.")
            # Simular confirmacion de escritura
            conn.send("ok".encode('utf-8'))
    except Exception as e:
        print(f"Error al procesar la solicitud de escritura: {e}")
    finally:
        conn.close()