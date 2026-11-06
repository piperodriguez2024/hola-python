import unittest
from io import StringIO
from unittest.mock import patch

from main import main, saludar


class TestCasosBorde(unittest.TestCase):

    @patch("builtins.input", return_value="  Ana  ")
    @patch("sys.stdout", new_callable=StringIO)
    def test_nombre_con_espacios(self, salida, entrada):
        main()
        self.assertEqual(
            salida.getvalue().strip(),
            saludar("Ana")
        )

    def test_nombre_con_tilde(self):
        resultado = saludar("María")
        self.assertIn("Hola María,", resultado)


if __name__ == "__main__":
    unittest.main()
