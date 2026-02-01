# 📱 Generador de Códigos QR

Un generador de códigos QR con interfaz web (Streamlit) y línea de comandos (CLI). Soporta generación individual y por lote, con opciones de personalización y múltiples formatos de salida (PNG/SVG).

## 🌟 Características

- **Aplicación Web Interactiva** - Interfaz moderna con Streamlit
- **Generación Individual** - Crea códigos QR únicos con vista previa en tiempo real
- **Generación por Lote** - Hasta 20 códigos QR a la vez, descarga en ZIP
- **Múltiples Formatos** - PNG y SVG
- **Personalización** - Ajusta tamaño de módulo y borde
- **Sin Base de Datos** - Todo en memoria, stateless
- **CLI Disponible** - También puedes usar la línea de comandos

## 🚀 Inicio Rápido (Aplicación Web)

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/complexluise/QR_generator.git
cd QR_generator

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
streamlit run app.py
```

### Uso de la Aplicación Web

1. **QR Único**: Ingresa una URL, personaliza opciones y genera tu código QR
2. **QR por Lote**: Pega múltiples URLs (una por línea, máximo 20) y descarga un ZIP

### Deploy en Streamlit Cloud

1. Haz fork del repositorio
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio y selecciona `app.py`
4. ¡Listo! Tu app estará disponible públicamente

---

## 💻 Uso por Línea de Comandos (CLI)

El programa CLI te permite crear códigos QR a partir de enlaces (URLs) o de un archivo de texto que contenga múltiples enlaces.

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

---

## 🏗️ Arquitectura del Proyecto

```
QR_generator/
├── app.py                    # Aplicación Streamlit
├── qr_generator.py          # CLI (backward compatible)
├── src/                     # Lógica de negocio
│   ├── qr_service.py        # Generación de QR (PNG/SVG)
│   ├── validators.py        # Validación de URLs
│   └── utils.py             # Utilidades (ZIP)
├── tests/                   # Tests unitarios
│   ├── test_qr_service.py
│   └── test_validators.py
├── .streamlit/
│   └── config.toml          # Configuración de Streamlit
└── requirements.txt
```

### Principios de Diseño

- **Separation of Concerns** - UI / Lógica de negocio / Validación separados
- **Stateless** - Sin persistencia, todo en memoria
- **Pure Functions** - Sin efectos secundarios
- **Test-Driven Development** - 100% cobertura de tests

## 🧪 Tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests con verbose
pytest -v

# Ejecutar tests específicos
pytest tests/test_qr_service.py
pytest tests/test_validators.py
```

**Cobertura de Tests:**
- ✅ Generación de QR (PNG/SVG)
- ✅ Validación de URLs (HTTP/HTTPS)
- ✅ Batch con límite de 20 URLs
- ✅ Sanitización de inputs
- ✅ Manejo de errores

## 📦 Dependencias

- `qrcode==7.4.2` - Generación de códigos QR
- `pillow==10.4.0` - Procesamiento de imágenes
- `streamlit==1.41.1` - Framework web
- `pytest==8.3.4` - Testing

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una branch para tu feature (`git checkout -b feature/AmazingFeature`)
3. Escribe tests para tu feature
4. Implementa tu feature
5. Asegúrate de que todos los tests pasen (`pytest`)
6. Commit con mensajes semánticos (`git commit -m 'feat: add amazing feature'`)
7. Push a la branch (`git push origin feature/AmazingFeature`)
8. Abre un Pull Request

### Convenciones de Commits

- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de bug
- `test:` - Agregar o modificar tests
- `docs:` - Cambios en documentación
- `chore:` - Cambios en configuración, dependencies, etc.

## 📄 Licencia

Este proyecto es de código abierto.

---

¡Disfruta creando tus códigos QR! 🎉