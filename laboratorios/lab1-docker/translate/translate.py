import sys
import logging
from typing import Optional
from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound, LanguageNotSupportedException

# Configuración de Logging para auditoría y seguridad
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TranslationService:
    """Clase encargada de la lógica de traducción siguiendo estándares de seguridad."""
    
    def __init__(self, source_lang: str = 'en', target_lang: str = 'es'):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self._translator = GoogleTranslator(source=self.source_lang, target=self.target_lang)

    def translate_text(self, text: str) -> Optional[str]:
        """
        Traduce una cadena de texto.
        Incluye validaciones de entrada para evitar procesamientos innecesarios.
        """
        if not text or not isinstance(text, str):
            logging.warning("Intento de traducción con entrada vacía o inválida.")
            return None
            
        if len(text) > 5000:
            logging.warning("Texto demasiado largo. Se excede el límite de 5000 caracteres.")
            return None

        # Sanitización básica: Eliminar espacios en blanco innecesarios
        clean_text = text.strip()

        try:
            result = self._translator.translate(clean_text)
            return result
        except (TranslationNotFound, LanguageNotSupportedException) as e:
            logging.error(f"Error en los parámetros de traducción: {e}")
            return None
        except Exception as e:
            # Captura cualquier otro error de red o cambios en la API
            logging.error(f"Error inesperado de conexión o ejecución: {e}")
            return None

def main():
    """Punto de entrada principal con manejo de flujo seguro."""
    translator = TranslationService()

    print("--- Traductor Seguro Inglés -> Español ---")
    print("Escriba 'salir' para finalizar.\n")

    try:
        while True:
            user_input = input("Texto en Inglés: ")
            
            if user_input.lower() in ['salir', 'exit', 'quit']:
                print("Cerrando el programa de forma segura...")
                break

            translation = translator.translate_text(user_input)

            if translation:
                print(f"Traducción: {translation}\n")
            else:
                print("No se pudo realizar la traducción. Verifique su conexión o entrada.\n")

    except KeyboardInterrupt:
        logging.info("Programa interrumpido por el usuario.")
        sys.exit(0)

if __name__ == "__main__":
    main()