# Generador de Códigos QR

Este programa simple te permite crear códigos QR a partir de enlaces (URLs) o de un archivo de texto que contenga múltiples enlaces.

## Requisitos previos

Antes de usar este programa, necesitas tener instalado:

1. Python (versión 3.9 o superior)
2. La biblioteca qrcode

## Instalación

1. Instala Python:
   - Ve a [python.org](https://www.python.org/downloads/) y descarga la última versión para tu sistema operativo.
   - Sigue las instrucciones de instalación.

2. Instala la biblioteca qrcode:
   - Abre la línea de comandos (Command Prompt en Windows, Terminal en Mac/Linux)
   - Escribe el siguiente comando y presiona Enter:
     ```
     pip install qrcode[pil]
     ```

3. Descarga el archivo `generador_qr.py` y guárdalo en tu computadora.

## Cómo usar

### Para crear un código QR de un solo enlace:

1. Abre la línea de comandos.
2. Navega hasta la carpeta donde guardaste `generador_qr.py`.
3. Escribe el siguiente comando (reemplaza la URL con tu enlace):
   ```
   python generador_qr.py https://www.tuenlace.com
   ```
4. El programa creará un archivo llamado `qr_code.png` en la misma carpeta.

### Para crear códigos QR de múltiples enlaces en un archivo de texto:

1. Crea un archivo de texto (por ejemplo, `enlaces.txt`).
2. Escribe cada enlace en una línea separada en este archivo.
3. Guarda el archivo en la misma carpeta que `generador_qr.py`.
4. Abre la línea de comandos.
5. Navega hasta la carpeta donde guardaste los archivos.
6. Escribe el siguiente comando:
   ```
   python generador_qr.py enlaces.txt
   ```
7. El programa creará una carpeta llamada `qr_codes` y guardará un código QR para cada enlace dentro de esta carpeta.

## Consejos

- Asegúrate de que los enlaces en tu archivo de texto comiencen con "http://" o "https://".
- Si tienes problemas, verifica que hayas escrito correctamente los comandos y los nombres de los archivos.
- Los códigos QR generados se pueden escanear con la mayoría de las aplicaciones de cámara de smartphones o aplicaciones específicas de lectura de códigos QR.

¡Disfruta creando tus códigos QR!