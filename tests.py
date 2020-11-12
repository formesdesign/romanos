import unittest
#modulo de python para text unitarios

from romanos import *

class RomanosTest(unittest.TestCase):
    #crear un metodo para los test

    def test_single_simbol(self):
        self.assertEqual(romano_a_entero("M"), 1000)
        self.assertEqual(romano_a_entero("D"), 500)
        self.assertEqual(romano_a_entero("C"), 100)


        self.assertRaises(ValueError, romano_a_entero, 23)