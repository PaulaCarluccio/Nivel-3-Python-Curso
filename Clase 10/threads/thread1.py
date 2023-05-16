from threading import Thread
def mifuncion():
    print("¡Hola Mundo de Dami!")
thread1 = Thread(target=mifuncion)
thread1.start()
thread1.join()