import socket
import sys
Dox_owo = socket.gethostname()
ip = socket.gethostbyname(Dox_owo)
print("Jajajaja, el nombre de tu pc es: "+ Dox_owo)
print("Y tu dirección de IP es: " + ip)
print("Escaneando")
obj = socket.gethostbyname(ip)
try:
    for port in range(1,150):
        s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((ip, port))
        if resultado == 0:
            print("El puerto {} está abierto".format(port))
            print("Recopilando datos y mandándolos a la nube...")
        s.close()
except:
    print("\n Saliendo..")
    sys.exit(0)
