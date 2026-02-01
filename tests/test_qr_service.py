"""Tests para el servicio de generación de códigos QR."""

import io
import pytest
from PIL import Image
from src.qr_service import QRService


class TestQRService:
    """Suite de tests para QRService."""

    def test_generate_qr_png_default_options(self):
        """Test: Generar QR en formato PNG con opciones por defecto."""
        qr_service = QRService()
        url = "https://www.example.com"

        result = qr_service.generate_qr(url, format="png")

        assert result is not None
        assert isinstance(result, io.BytesIO)

        # Verificar que es una imagen PNG válida
        result.seek(0)
        img = Image.open(result)
        assert img.format == "PNG"
        assert img.size[0] > 0
        assert img.size[1] > 0

    def test_generate_qr_svg_format(self):
        """Test: Generar QR en formato SVG."""
        qr_service = QRService()
        url = "https://www.example.com"

        result = qr_service.generate_qr(url, format="svg")

        assert result is not None
        assert isinstance(result, io.BytesIO)

        # Verificar que contiene contenido SVG
        result.seek(0)
        content = result.read().decode('utf-8')
        assert content.startswith('<?xml')
        assert '<svg' in content
        assert '</svg>' in content

    def test_generate_qr_with_custom_box_size(self):
        """Test: Generar QR con tamaño de caja personalizado."""
        qr_service = QRService()
        url = "https://www.example.com"

        result_small = qr_service.generate_qr(url, format="png", box_size=5)
        result_large = qr_service.generate_qr(url, format="png", box_size=15)

        result_small.seek(0)
        result_large.seek(0)

        img_small = Image.open(result_small)
        img_large = Image.open(result_large)

        # El QR con box_size mayor debe tener dimensiones mayores
        assert img_large.size[0] > img_small.size[0]
        assert img_large.size[1] > img_small.size[1]

    def test_generate_qr_with_custom_border(self):
        """Test: Generar QR con borde personalizado."""
        qr_service = QRService()
        url = "https://www.example.com"

        result_small_border = qr_service.generate_qr(url, format="png", border=1)
        result_large_border = qr_service.generate_qr(url, format="png", border=10)

        result_small_border.seek(0)
        result_large_border.seek(0)

        img_small = Image.open(result_small_border)
        img_large = Image.open(result_large_border)

        # El QR con border mayor debe tener dimensiones mayores
        assert img_large.size[0] > img_small.size[0]

    def test_generate_qr_with_custom_colors(self):
        """Test: Generar QR con colores personalizados (negro/blanco)."""
        qr_service = QRService()
        url = "https://www.example.com"

        result = qr_service.generate_qr(
            url,
            format="png",
            fill_color="black",
            back_color="white"
        )

        assert result is not None
        result.seek(0)
        img = Image.open(result)
        assert img.format == "PNG"

    def test_generate_batch_qr_png(self):
        """Test: Generar múltiples QR codes y retornar lista de BytesIO."""
        qr_service = QRService()
        urls = [
            "https://www.example1.com",
            "https://www.example2.com",
            "https://www.example3.com"
        ]

        results = qr_service.generate_batch_qr(urls, format="png")

        assert len(results) == 3
        for i, result in enumerate(results):
            assert isinstance(result, dict)
            assert "filename" in result
            assert "data" in result
            assert result["filename"] == f"qr_code_{i+1}.png"
            assert isinstance(result["data"], io.BytesIO)

            # Verificar que cada uno es una imagen válida
            result["data"].seek(0)
            img = Image.open(result["data"])
            assert img.format == "PNG"

    def test_generate_batch_qr_svg(self):
        """Test: Generar múltiples QR codes en formato SVG."""
        qr_service = QRService()
        urls = [
            "https://www.example1.com",
            "https://www.example2.com"
        ]

        results = qr_service.generate_batch_qr(urls, format="svg")

        assert len(results) == 2
        for i, result in enumerate(results):
            assert result["filename"] == f"qr_code_{i+1}.svg"
            result["data"].seek(0)
            content = result["data"].read().decode('utf-8')
            assert '<svg' in content

    def test_generate_qr_empty_url(self):
        """Test: Manejar URL vacía debe lanzar excepción."""
        qr_service = QRService()

        with pytest.raises(ValueError, match="URL no puede estar vacía"):
            qr_service.generate_qr("", format="png")

    def test_generate_qr_invalid_format(self):
        """Test: Formato inválido debe lanzar excepción."""
        qr_service = QRService()

        with pytest.raises(ValueError, match="Formato debe ser 'png' o 'svg'"):
            qr_service.generate_qr("https://example.com", format="jpg")

    def test_generate_batch_empty_list(self):
        """Test: Lista vacía debe retornar lista vacía."""
        qr_service = QRService()

        results = qr_service.generate_batch_qr([], format="png")

        assert results == []
