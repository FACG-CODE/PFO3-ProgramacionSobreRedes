import threading
from database.db import inicializarBaseDatos
from server.servidor import ejecutarServidor
from workers.workerEscritura import ejecutarWorkerEscritura
from workers.workerLectura import ejecutarWorkerLectura
from client.cliente import ejecutarCliente

if __name__ == "__main__":
    inicializarBaseDatos()
    threading.Thread(target=ejecutarServidor).start()
    threading.Thread(target=ejecutarWorkerEscritura).start()
    threading.Thread(target=ejecutarWorkerLectura).start()
    threading.Thread(target=ejecutarCliente).start()
