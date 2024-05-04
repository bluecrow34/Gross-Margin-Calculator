from unittest import TestCase
from GrossMargin.app import app


class TestCurrencyConverter(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_conversion_successful(self, mock_currency_rates):
        mock_instance = mock_currency_rates.return_value
        mock_instance.get_rate.return_value = 1.5

        response = self.app.post('/converted', data=dict(
            convertfrom='USD',
            convertto='EUR',
            amount='100'
        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'150.00 EUR', response.data)

    def test_conversion_error(self, mock_currency_rates):
        mock_instance = mock_currency_rates.return_value
        mock_instance.get_rate.side_effect = Exception("Error converting currenct")

        response = self.app.post('/converted', data=dict(
            convertfrom='USD',
            convertto='EUR',
            amount='100'
        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error converting currency', response.data)

    def __init__(self):
        self.api_key = open(access_key).readline().strip()
        self.url = f'https://api.exchangerate.host/convert?access_key=a8cbd17cc4589ad040344486d6afdfeb&'
        self.output = ''

access_key = 'a8cbd17cc4589ad040344486d6afdfeb'

if __name__ == '__main__':
    TestCase.main()





