import socket
from models.funcionesSocket import inicializarSocket
import threading
import json
from database.db import obtenerUltimoLibro

# Configuracion del worker de lectura
HOST = 'localhost'
PORT = 7000

def ejecutarWorkerLectura():
    socketWorker = inicializarSocket(HOST, PORT)
    if socketWorker is None:
        print("No se pudo iniciar el worker de lectura.")
        return
    print(f"Worker de lectura escuchando en {HOST}:{PORT}")
    try:
        while True:
            conn, addr = socketWorker.accept()
            hilo = threading.Thread(target=procesarSolicitudServidor, args=(conn, addr))
            hilo.start()
    except Exception as e:
        print(f"Error en el worker de lectura: {e}")

def procesarSolicitudServidor(conn, addr):
    print(f"Conexion de lectura establecida desde {addr}")
    try:
        while True:
            mensaje = conn.recv(1024).decode("utf-8")
            if mensaje == "ok":
                idLibro = obtenerUltimoLibro()
                if idLibro is None:
                    print("No se pudo obtener el ID del último libro.")
                    conn.send("Error al obtener el ID del libro.".encode('utf-8'))
                else:
                    conn.send(f"Libro registrado con ID: {idLibro[0]}".encode('utf-8'))
            else:
                print("Mensaje no reconocido en worker de lectura.")
                conn.send("Mensaje no reconocido.".encode('utf-8')) 
                break
    except Exception as e:
        print(f"Error al procesar la solicitud de lectura: {e}")
    finally:
        conn.close()