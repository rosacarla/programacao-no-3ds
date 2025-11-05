# test_calculadora.py
import unittest
from calculadora import soma, subtrai, multiplica, divide

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        casos = [(1, 2, 3), (-1, 1, 0), (-1, -1, -2)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = soma(a, b)
                self.assertEqual(resultado, esperado)
                print(f"✅ Teste de soma({a}, {b}) = {resultado} passou!")

    def test_subtrai(self):
        casos = [(10, 5, 5), (-1, -1, 0), (0, 1, -1)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = subtrai(a, b)
                self.assertEqual(resultado, esperado)
                print(f"✅ Teste de subtrai({a}, {b}) = {resultado} passou!")

    def test_multiplica(self):
        casos = [(3, 7, 21), (-1, 1, -1), (0, 10, 0)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = multiplica(a, b)
                self.assertEqual(resultado, esperado)
                print(f"✅ Teste de multiplica({a}, {b}) = {resultado} passou!")

    def test_divide(self):
        casos = [(10, 2, 5), (-10, 2, -5)]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = divide(a, b)
                self.assertEqual(resultado, esperado)
                print(f"✅ Teste de divide({a}, {b}) = {resultado} passou!")

        with self.assertRaises(ValueError):
            divide(10, 0)
            print("✅ Teste de divide(10, 0) lançou ValueError como esperado!")

if __name__ == '__main__':
    unittest.main()
