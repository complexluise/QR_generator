"""Servicio para generación de códigos QR en diferentes formatos."""

import io
import qrcode
import qrcode.image.svg


class QRService:
    """Servicio para generar códigos QR en formato PNG o SVG."""

    def generate_qr(
        self,
        url: str,
        format: str = "png",
        box_size: int = 10,
        border: int = 5,
        fill_color: str = "black",
        back_color: str = "white"
    ) -> io.BytesIO:
        """
        Genera un código QR a partir de una URL.

        Args:
            url: URL para codificar en el QR
            format: Formato de salida ('png' o 'svg')
            box_size: Tamaño de cada caja/módulo del QR
            border: Tamaño del borde (quiet zone)
            fill_color: Color de primer plano
            back_color: Color de fondo

        Returns:
            BytesIO con la imagen del QR generado

        Raises:
            ValueError: Si la URL está vacía o el formato es inválido
        """
        if not url or url.strip() == "":
            raise ValueError("URL no puede estar vacía")

        if format not in ["png", "svg"]:
            raise ValueError("Formato debe ser 'png' o 'svg'")

        # Crear el QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Generar según el formato
        buffer = io.BytesIO()

        if format == "svg":
            # Generar SVG
            factory = qrcode.image.svg.SvgPathImage
            img = qr.make_image(image_factory=factory)
            img.save(buffer)
        else:
            # Generar PNG (default)
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            img.save(buffer, format="PNG")

        buffer.seek(0)
        return buffer

    def generate_batch_qr(
        self,
        urls: list[str],
        format: str = "png",
        box_size: int = 10,
        border: int = 5,
        fill_color: str = "black",
        back_color: str = "white"
    ) -> list[dict]:
        """
        Genera múltiples códigos QR a partir de una lista de URLs.

        Args:
            urls: Lista de URLs para codificar
            format: Formato de salida ('png' o 'svg')
            box_size: Tamaño de cada caja/módulo del QR
            border: Tamaño del borde
            fill_color: Color de primer plano
            back_color: Color de fondo

        Returns:
            Lista de diccionarios con 'filename' y 'data' (BytesIO)
        """
        if not urls:
            return []

        results = []
        extension = "svg" if format == "svg" else "png"

        for i, url in enumerate(urls, start=1):
            qr_data = self.generate_qr(
                url=url,
                format=format,
                box_size=box_size,
                border=border,
                fill_color=fill_color,
                back_color=back_color
            )

            results.append({
                "filename": f"qr_code_{i}.{extension}",
                "data": qr_data
            })

        return results
