import logging
from typing import Optional
from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound, LanguageNotSupportedException

# Logger a nivel de módulo, sin basicConfig (lo configura la app principal)
logger = logging.getLogger(__name__)

MAX_TEXT_LENGTH = 5000

class TranslationService:
    """Servicio de traducción con validación y manejo de errores."""

    def __init__(self, source_lang: str = "en", target_lang: str = "es"):
        self.source_lang = source_lang
        self.target_lang = target_lang

    def translate_text(self, text: str) -> Optional[str]:
        """Traduce texto del idioma origen al destino."""
        if not text or not isinstance(text, str):
            logger.warning("Entrada de traducción vacía o inválida.")
            return None

        if len(text) > MAX_TEXT_LENGTH:
            logger.warning("Texto excede el límite de %d caracteres.", MAX_TEXT_LENGTH)
            return None

        clean_text = text.strip()

        try:
            # Crear instancia por llamada para evitar estado compartido entre requests
            translator = GoogleTranslator(source=self.source_lang, target=self.target_lang)
            result = translator.translate(clean_text)
            logger.info("Traducción exitosa. Longitud: %d caracteres.", len(clean_text))
            return result
        except (TranslationNotFound, LanguageNotSupportedException) as e:
            logger.error("Error en parámetros de traducción: %s", e)
            return None
        except Exception as e:
            logger.error("Error inesperado en traducción: %s", e)
            return None
