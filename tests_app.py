from app import *
from unittest import TestCase

class ConversionTestCase(TestCase):
    """Unit test for Conversion App"""

    def test_conversion(self):
        """Testing conversion between the same from/to currency Codes matches original amount."""
        with app.test_client() as client:
            res = client.post('/conversion', data={'currcode_from': 'USD', 'currcode_to': 'USD', 'amount':1} )
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 200)

            self.assertIn('<p id="conversion">\n  $1 (USD) is equal to\n  $1.00 (USD)\n</p>', html)

    def test_flash_error(self):
        with app.test_client() as client:
            res = client.post('/conversion',data={'currcode_from': 'usd', 'currcode_to': 'inr', 'amount':1},follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p id="error">Not a valid Code: usd Please visit https://www.iban.com/currency-codes for a full list of Currency Codes</p>\n      \n        <p id="error">Not a valid Code: inr Please visit https://www.iban.com/currency-codes for a full list of Currency Codes</p>', html)
        
    