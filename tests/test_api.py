import unittest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


class TestAPI(unittest.TestCase):

    def test_inicio(self):
        respuesta = client.get("/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(
            respuesta.json()["estado"], "activo"
        )

    def test_health(self):
        respuesta = client.get("/health")
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(
            respuesta.json()["status"], "ok"
        )

    def test_saludo(self):
        respuesta = client.get("/saludo/Felipe")
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(
            "Hola Felipe",
            respuesta.json()["mensaje"]
        )

    def test_ruta_inexistente(self):
        respuesta = client.get("/no-existe")
        self.assertEqual(respuesta.status_code, 404)


if __name__ == "__main__":
    unittest.main()
