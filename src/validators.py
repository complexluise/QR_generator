"""Validadores para entrada de datos de la aplicación."""


class URLValidator:
    """Validador para URLs y listas de URLs."""

    MAX_BATCH_SIZE = 20

    def validate_url(self, url: str) -> bool:
        """
        Valida que una URL sea válida.

        Args:
            url: URL a validar

        Returns:
            True si la URL es válida

        Raises:
            ValueError: Si la URL es inválida
        """
        if not url or url.strip() == "":
            raise ValueError("URL no puede estar vacía")

        url_clean = url.strip()

        if not (url_clean.startswith("http://") or url_clean.startswith("https://")):
            raise ValueError("URL debe comenzar con http:// o https://")

        return True

    def validate_batch_urls(self, urls: list[str]) -> bool:
        """
        Valida una lista de URLs.

        Args:
            urls: Lista de URLs a validar

        Returns:
            True si todas las URLs son válidas

        Raises:
            ValueError: Si la lista está vacía, excede el límite o contiene URLs inválidas
        """
        if not urls or len(urls) == 0:
            raise ValueError("La lista de URLs no puede estar vacía")

        if len(urls) > self.MAX_BATCH_SIZE:
            raise ValueError(f"Máximo {self.MAX_BATCH_SIZE} URLs permitidas")

        # Validar cada URL individualmente
        for url in urls:
            self.validate_url(url)

        return True

    def sanitize_url(self, url: str) -> str:
        """
        Limpia espacios en blanco de una URL.

        Args:
            url: URL a limpiar

        Returns:
            URL limpia
        """
        return url.strip()

    def sanitize_url_list(self, urls: list[str]) -> list[str]:
        """
        Limpia una lista de URLs removiendo espacios y líneas vacías.

        Args:
            urls: Lista de URLs a limpiar

        Returns:
            Lista de URLs limpias (sin líneas vacías)
        """
        cleaned_urls = []

        for url in urls:
            cleaned = url.strip()
            if cleaned:  # Solo agregar si no está vacío
                cleaned_urls.append(cleaned)

        return cleaned_urls
