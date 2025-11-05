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
