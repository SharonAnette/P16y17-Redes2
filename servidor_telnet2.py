import socket

# Configuración del servidor
HOST = '0.0.0.0'  # Escuchar en todas las interfaces disponibles
PORT = 5001       # Puerto arbitrario que no requiere privilegi>

# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREA>
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Servidor Telnet escuchando en {HOST}:{PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexión desde {client_address}")

    # Enviar mensaje de bienvenida
    client_socket.sendall(b"Bienvenido al servidor Telnet\n")
    

    # Recibir nombre de usuario
    username_data = client_socket.recv(1024)
    print(f"Datos recibidos en bruto: {username_data}")
    username = username_data.decode('utf-8').strip()
    print(f"Nombre de usuario recibido: {username}")


    # Pedir contraseña
    client_socket.sendall(b"Password: ")
    password = client_socket.recv(1024).strip().decode('utf-8')

    # Autenticación simple
    if username == 'escom' and password == 'escom':
        client_socket.sendall(b"Autenticacion exitosa\n")
    else:
        client_socket.sendall(b"Autenticacion fallida\n")

    client_socket.close()

