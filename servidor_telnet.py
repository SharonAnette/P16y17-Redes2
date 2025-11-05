import socket 
 
# Configuración del servidor 
HOST = '0.0.0.0'  # Escuchar en todas las interfaces d>
PORT = 5000       # Puerto arbitrario que no requiere >
 
# Crear el socket del servidor 
server_socket = socket.socket(socket.AF_INET, socket.S>
server_socket.bind((HOST, PORT)) 
server_socket.listen(1) 
print(f"Servidor Telnet escuchando en {HOST}:{PORT}...>
 
while True: 
    client_socket, client_address = server_socket.acce>
    print(f"Conexión desde {client_address}") 
 
    client_socket.sendall("Bienvenido al servidor Teln>
 
    # Recibir nombre de usuario 
    username = client_socket.recv(1024).strip().decode>
 
    # Pedir contraseña 
    client_socket.sendall("Password: ".encode('utf-8')>
    password = client_socket.recv(1024).strip().decode>
 
    # Autenticación simple 
    if username == 'escom' and password == 'escom': 
        client_socket.sendall("\nAutenticación exitosa>
    else: 
        client_socket.sendall("\nAutenticación fallida>
 
    client_socket.close()

