import unittest
from unittest.mock import patch
from io import StringIO

from main import saludar, main


class TestHolaPython(unittest.TestCase):

    def test_saludo_nombre(self):
        resultado = saludar("Felipe")
        self.assertEqual(
            resultado,
            "Hola Felipe, bienvenido a Python desde mi Steam Deck!"
        )

    @patch("builtins.input", return_value="Ana")
    @patch("sys.stdout", new_callable=StringIO)
    def test_ingreso_nombre(self, salida, entrada):
        main()
        self.assertIn("Hola Ana,", salida.getvalue())

    @patch("builtins.input", return_value="   ")
    @patch("sys.stdout", new_callable=StringIO)
    def test_nombre_vacio(self, salida, entrada):
        main()
        self.assertIn("Hola Mundo,", salida.getvalue())


if __name__ == "__main__":
    unittest.main()
