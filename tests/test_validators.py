"""Tests para validadores de entrada."""

import pytest
from src.validators import URLValidator


class TestURLValidator:
    """Suite de tests para URLValidator."""

    def test_validate_url_valid_http(self):
        """Test: URL con http:// válida."""
        validator = URLValidator()
        url = "http://www.example.com"

        result = validator.validate_url(url)

        assert result is True

    def test_validate_url_valid_https(self):
        """Test: URL con https:// válida."""
        validator = URLValidator()
        url = "https://www.example.com"

        result = validator.validate_url(url)

        assert result is True

    def test_validate_url_without_protocol(self):
        """Test: URL sin protocolo debe ser inválida."""
        validator = URLValidator()
        url = "www.example.com"

        with pytest.raises(ValueError, match="URL debe comenzar con http:// o https://"):
            validator.validate_url(url)

    def test_validate_url_empty_string(self):
        """Test: String vacío debe lanzar excepción."""
        validator = URLValidator()
        url = ""

        with pytest.raises(ValueError, match="URL no puede estar vacía"):
            validator.validate_url(url)

    def test_validate_url_whitespace_only(self):
        """Test: Solo espacios en blanco debe lanzar excepción."""
        validator = URLValidator()
        url = "   "

        with pytest.raises(ValueError, match="URL no puede estar vacía"):
            validator.validate_url(url)

    def test_validate_url_invalid_protocol(self):
        """Test: Protocolo inválido (ftp, etc) debe fallar."""
        validator = URLValidator()
        url = "ftp://example.com"

        with pytest.raises(ValueError, match="URL debe comenzar con http:// o https://"):
            validator.validate_url(url)

    def test_validate_batch_urls_valid_list(self):
        """Test: Lista válida de URLs debe retornar True."""
        validator = URLValidator()
        urls = [
            "https://example1.com",
            "http://example2.com",
            "https://example3.com"
        ]

        result = validator.validate_batch_urls(urls)

        assert result is True

    def test_validate_batch_urls_empty_list(self):
        """Test: Lista vacía debe lanzar excepción."""
        validator = URLValidator()
        urls = []

        with pytest.raises(ValueError, match="La lista de URLs no puede estar vacía"):
            validator.validate_batch_urls(urls)

    def test_validate_batch_urls_exceeds_limit(self):
        """Test: Más de 20 URLs debe lanzar excepción."""
        validator = URLValidator()
        urls = [f"https://example{i}.com" for i in range(21)]

        with pytest.raises(ValueError, match="Máximo 20 URLs permitidas"):
            validator.validate_batch_urls(urls)

    def test_validate_batch_urls_exactly_20(self):
        """Test: Exactamente 20 URLs debe ser válido."""
        validator = URLValidator()
        urls = [f"https://example{i}.com" for i in range(20)]

        result = validator.validate_batch_urls(urls)

        assert result is True

    def test_validate_batch_urls_with_invalid_url(self):
        """Test: Lista con URL inválida debe lanzar excepción."""
        validator = URLValidator()
        urls = [
            "https://example1.com",
            "invalid-url",
            "https://example3.com"
        ]

        with pytest.raises(ValueError, match="URL debe comenzar con http:// o https://"):
            validator.validate_batch_urls(urls)

    def test_validate_batch_urls_with_empty_url(self):
        """Test: Lista con URL vacía debe lanzar excepción."""
        validator = URLValidator()
        urls = [
            "https://example1.com",
            "",
            "https://example3.com"
        ]

        with pytest.raises(ValueError, match="URL no puede estar vacía"):
            validator.validate_batch_urls(urls)

    def test_sanitize_url_removes_whitespace(self):
        """Test: Sanitizar debe remover espacios en blanco."""
        validator = URLValidator()
        url = "  https://example.com  "

        result = validator.sanitize_url(url)

        assert result == "https://example.com"

    def test_sanitize_url_list(self):
        """Test: Sanitizar lista de URLs."""
        validator = URLValidator()
        urls = [
            "  https://example1.com  ",
            "https://example2.com",
            "  http://example3.com"
        ]

        result = validator.sanitize_url_list(urls)

        assert result == [
            "https://example1.com",
            "https://example2.com",
            "http://example3.com"
        ]

    def test_sanitize_url_list_removes_empty_lines(self):
        """Test: Sanitizar lista debe remover líneas vacías."""
        validator = URLValidator()
        urls = [
            "https://example1.com",
            "  ",
            "https://example2.com",
            "",
            "https://example3.com"
        ]

        result = validator.sanitize_url_list(urls)

        assert result == [
            "https://example1.com",
            "https://example2.com",
            "https://example3.com"
        ]
