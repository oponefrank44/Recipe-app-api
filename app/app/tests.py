
"""  sample tests for the calc module"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Teste the calc module """
    
    def test_add_numbers(self):
        """returns the sum of two numbers"""
        res=calc.add(5, 6)
        self.assertEqual(res, 11)
        
    def test_substract_numbers(self):
        """returns the subtraction of two numbers"""
        res=calc.subtract(10, 15)
        self.assertEqual(res, -5)