"""Aplicación Streamlit para generación de códigos QR."""

import streamlit as st
from src.qr_service import QRService
from src.validators import URLValidator
from src.utils import create_zip_from_files


def main():
    """Función principal de la aplicación."""
    st.set_page_config(
        page_title="Generador de Códigos QR",
        page_icon="📱",
        layout="centered"
    )

    st.title("📱 Generador de Códigos QR")
    st.markdown("---")

    # Inicializar servicios
    qr_service = QRService()
    validator = URLValidator()

    # Crear tabs
    tab1, tab2 = st.tabs(["🔷 QR Único", "📦 QR por Lote"])

    # ========== TAB 1: QR ÚNICO ==========
    with tab1:
        st.subheader("Generar un código QR")

        # Input de URL
        url_input = st.text_input(
            "📝 Ingresa la URL:",
            placeholder="https://ejemplo.com",
            key="single_url"
        )

        # Selector de formato
        format_single = st.selectbox(
            "📄 Formato de salida:",
            options=["PNG", "SVG"],
            key="format_single"
        )

        # Opciones de personalización (expandable)
        with st.expander("⚙️ Opciones de personalización"):
            box_size_single = st.slider(
                "Tamaño de módulo (box size):",
                min_value=5,
                max_value=20,
                value=10,
                key="box_size_single"
            )

            border_single = st.slider(
                "Tamaño de borde:",
                min_value=1,
                max_value=10,
                value=5,
                key="border_single"
            )

        # Botón para generar
        if st.button("🚀 Generar QR", key="btn_single", type="primary"):
            if not url_input:
                st.error("❌ Por favor ingresa una URL")
            else:
                try:
                    # Validar URL
                    sanitized_url = validator.sanitize_url(url_input)
                    validator.validate_url(sanitized_url)

                    # Generar QR
                    with st.spinner("Generando código QR..."):
                        qr_data = qr_service.generate_qr(
                            url=sanitized_url,
                            format=format_single.lower(),
                            box_size=box_size_single,
                            border=border_single
                        )

                    st.success("✅ ¡Código QR generado exitosamente!")

                    # Preview
                    st.subheader("👁️ Vista previa:")

                    if format_single == "PNG":
                        st.image(qr_data, width=300)
                    else:
                        # Para SVG, mostrar el contenido
                        qr_data.seek(0)
                        svg_content = qr_data.read().decode('utf-8')
                        st.code(svg_content[:500] + "...", language="xml")

                    # Botón de descarga
                    qr_data.seek(0)
                    file_extension = format_single.lower()
                    st.download_button(
                        label=f"📥 Descargar {format_single}",
                        data=qr_data,
                        file_name=f"qr_code.{file_extension}",
                        mime=f"image/{file_extension}",
                        key="download_single"
                    )

                except ValueError as e:
                    st.error(f"❌ Error: {str(e)}")
                except Exception as e:
                    st.error(f"❌ Error inesperado: {str(e)}")

    # ========== TAB 2: QR POR LOTE ==========
    with tab2:
        st.subheader("Generar múltiples códigos QR")
        st.info("💡 Ingresa una URL por línea (máximo 20)")

        # Text area para múltiples URLs
        urls_input = st.text_area(
            "📝 Ingresa las URLs (una por línea):",
            placeholder="https://ejemplo1.com\nhttps://ejemplo2.com\nhttps://ejemplo3.com",
            height=200,
            key="batch_urls"
        )

        # Selector de formato
        format_batch = st.selectbox(
            "📄 Formato de salida:",
            options=["PNG", "SVG"],
            key="format_batch"
        )

        # Opciones de personalización
        with st.expander("⚙️ Opciones de personalización"):
            box_size_batch = st.slider(
                "Tamaño de módulo (box size):",
                min_value=5,
                max_value=20,
                value=10,
                key="box_size_batch"
            )

            border_batch = st.slider(
                "Tamaño de borde:",
                min_value=1,
                max_value=10,
                value=5,
                key="border_batch"
            )

        # Botón para generar
        if st.button("🚀 Generar QRs por Lote", key="btn_batch", type="primary"):
            if not urls_input:
                st.error("❌ Por favor ingresa al menos una URL")
            else:
                try:
                    # Parsear y sanitizar URLs
                    urls_list = urls_input.strip().split('\n')
                    sanitized_urls = validator.sanitize_url_list(urls_list)

                    # Validar
                    validator.validate_batch_urls(sanitized_urls)

                    # Generar QRs
                    with st.spinner(f"Generando {len(sanitized_urls)} códigos QR..."):
                        qr_files = qr_service.generate_batch_qr(
                            urls=sanitized_urls,
                            format=format_batch.lower(),
                            box_size=box_size_batch,
                            border=border_batch
                        )

                    st.success(f"✅ ¡{len(qr_files)} códigos QR generados exitosamente!")

                    # Mostrar preview de los primeros 3
                    st.subheader("👁️ Vista previa:")

                    if format_batch == "PNG":
                        cols = st.columns(min(3, len(qr_files)))
                        for i, qr_file in enumerate(qr_files[:3]):
                            with cols[i]:
                                qr_file['data'].seek(0)
                                st.image(qr_file['data'], caption=qr_file['filename'], width=150)

                        if len(qr_files) > 3:
                            st.info(f"... y {len(qr_files) - 3} más")
                    else:
                        st.info(f"✅ {len(qr_files)} archivos SVG generados")

                    # Crear ZIP y ofrecer descarga
                    with st.spinner("Creando archivo ZIP..."):
                        zip_data = create_zip_from_files(qr_files)

                    st.download_button(
                        label=f"📥 Descargar ZIP con {len(qr_files)} QRs",
                        data=zip_data,
                        file_name="codigos_qr.zip",
                        mime="application/zip",
                        key="download_batch"
                    )

                except ValueError as e:
                    st.error(f"❌ Error: {str(e)}")
                except Exception as e:
                    st.error(f"❌ Error inesperado: {str(e)}")

    # Footer
    st.markdown("---")
    st.markdown(
        "Hecho con ❤️ usando [Streamlit](https://streamlit.io) | "
        "[GitHub](https://github.com/complexluise/QR_generator)"
    )


if __name__ == "__main__":
    main()
