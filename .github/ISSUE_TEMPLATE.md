## 📋 Descripción

Crear una aplicación web interactiva usando Streamlit para facilitar la generación de códigos QR sin necesidad de usar la línea de comandos.

## 🎯 Requerimientos Funcionales

### Generación Individual
- [x] Interfaz para ingresar una URL
- [x] Generar código QR único
- [x] Vista previa en tiempo real
- [x] Descarga en formato PNG o SVG
- [x] Opciones de personalización (tamaño de módulo, borde)

### Generación por Lote
- [x] Entrada de múltiples URLs (textarea)
- [x] Límite máximo de 20 URLs
- [x] Generación batch de códigos QR
- [x] Descarga de todos los QRs en un archivo ZIP
- [x] Soporte para PNG y SVG

## 🏗️ Requerimientos Técnicos

### Arquitectura
- [x] Separación de capas: UI / Lógica de negocio / Validación
- [x] Diseño stateless (sin base de datos)
- [x] Todo en memoria usando BytesIO
- [x] Funciones puras sin efectos secundarios

### Testing
- [x] Test-Driven Development (TDD)
- [x] Tests para servicio de generación QR (10 tests)
- [x] Tests para validadores (15 tests)
- [x] Cobertura de casos edge (URLs vacías, límites, etc)

### Código
- [x] Commits semánticos y atómicos
- [x] Buenas prácticas de código
- [x] Documentación en español
- [x] Backward compatibility con CLI existente

## 🌐 Interfaz de Usuario

- [x] Diseño en español
- [x] Tabs para separar "QR Único" y "QR por Lote"
- [x] Opciones de personalización en expandables
- [x] Mensajes de error claros
- [x] Preview antes de descargar

## 📦 Dependencias

- [x] `streamlit==1.41.1` - Framework web
- [x] `qrcode==7.4.2` - Generación de QR (ya existente)
- [x] `pillow==10.4.0` - Procesamiento de imágenes
- [x] `pytest==8.3.4` - Testing

## ✅ Criterios de Aceptación

1. [x] La aplicación debe ejecutarse con `streamlit run app.py`
2. [x] Debe soportar generación de QR individual y batch
3. [x] Límite estricto de 20 URLs en modo batch
4. [x] Validación de URLs (http:// o https://)
5. [x] Todos los tests deben pasar (25/25 ✅)
6. [x] No usar base de datos ni persistencia
7. [x] Documentación actualizada en README.md

## 🚀 Deploy

- [x] La aplicación es compatible con Streamlit Cloud para deployment público

## 📊 Resultados

**Estructura Creada:**
```
QR_generator/
├── app.py                    # Aplicación Streamlit
├── src/
│   ├── qr_service.py        # Servicio de generación QR
│   ├── validators.py        # Validadores con límite de 20
│   └── utils.py             # Utilidades (ZIP)
├── tests/
│   ├── test_qr_service.py   # 10 tests ✅
│   └── test_validators.py   # 15 tests ✅
├── .streamlit/config.toml
└── .gitignore
```

**Commits Realizados:**
- `9ccf7f7` - chore: add project structure for streamlit app
- `2992710` - chore: update dependencies for streamlit app
- `41a810b` - feat: implement url validators with batch limit
- `7a5da03` - feat: add streamlit web application
- `c869298` - docs: update README with streamlit app documentation
- `f8223f3` - chore: add .gitignore for python and streamlit
