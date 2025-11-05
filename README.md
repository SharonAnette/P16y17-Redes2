# Práctica 16 — Ejemplo Telnet en GNS3

## Objetivo
Familiarizarse con el uso del protocolo Telnet para administrar routers de forma remota en un entorno simulado con GNS3. La práctica busca establecer una conexión Telnet desde Router 1 hacia Router 2, permitiendo acceder a la configuración en tiempo real de Router 2.

## Cómo funciona
La práctica se desarrolla en GNS3 mediante una topología simple de dos routers conectados por un enlace serial o Ethernet.  
- Se asignan direcciones IP a las interfaces de ambos routers para permitir la comunicación.  
- En Router 2 se habilita el servicio Telnet configurando usuarios y contraseñas.  
- Desde Router 1 se establece la conexión Telnet hacia Router 2, ingresando las credenciales configuradas.  
- Una vez autenticado, se pueden ejecutar comandos como `show running-config` para visualizar o modificar la configuración de Router 2.

Esta simulación demuestra cómo se puede administrar remotamente un dispositivo de red utilizando Telnet en entornos de laboratorio con GNS3.

---

# Práctica 17 — Ejemplo Telnet en Python

## Objetivo
Desarrollar un cliente y un servidor Telnet en Python utilizando la biblioteca `socket`, para comprender el funcionamiento básico del protocolo en la autenticación y administración remota de sistemas.

## Cómo funciona
Se implementan dos versiones de cliente-servidor Telnet:

1. **Versión con `socket`:**  
   - El servidor escucha en un puerto específico, solicita usuario y contraseña al cliente, y verifica las credenciales.  
   - El cliente se conecta al servidor, envía los datos y recibe un mensaje indicando si la autenticación fue exitosa o fallida.

2. **Versión con `telnetlib`:**  
   - Se utiliza la biblioteca `telnetlib` para gestionar la conexión y el intercambio de datos de manera más automatizada.  
   - El cliente se conecta, envía las credenciales y recibe la respuesta del servidor.

El ejercicio permite comprender la estructura del protocolo Telnet y cómo realizar autenticaciones simples mediante Python.

