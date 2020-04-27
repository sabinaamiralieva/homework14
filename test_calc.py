import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')

    def test_exponent(self):
        """Возведение в степень"""
        self.assertEqual(calc_me(2,3,'^'), 8)

    def test_oper_neg(self):
        """Негативный, логарифм"""
        self.assertEqual(calc_me(4, 2,"log"), 'ERROR: Uknow operation')

    def test_symbol_x_neg(self):
        """Негативный, х - символ"""
        self.assertEqual(calc_me('a',1,'-'), 'ERROR: now it is does not supported')   

    def test_symbol_y_neg(self):
        """Негативный, y - символ"""
        self.assertEqual(calc_me(2,'b','+'), 'ERROR: now it is does not supported')   

    def test_none_x_neg(self):
        """Негативный, х отсутствует"""
        self.assertEqual(calc_me(None,5,'-'), 'ERROR: send me Number1')

    def test_none_y_neg(self):
        """Негативный, y отсутствует"""
        self.assertEqual(calc_me(3,None,'+'), 'ERROR: send me Number2')   
        

if __name__ == '__main__':
    unittest.main(verbosity=2)