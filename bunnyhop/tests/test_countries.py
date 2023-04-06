import unittest
from datetime import datetime

from unittest.mock import patch, MagicMock

from bunnyhop.base import convert_datetime_str
from bunnyhop.countries import CountryAPI, Country


class TestCountry(unittest.TestCase):
    def test_init(self):
        country_dict = {
            'Id': 1,
            'Name': 'United States',
            'LastModified': '2022-04-01T16:18:34Z',
            'ScriptType': 1,
            'CurrentReleaseId': 1,
            'EdgeScriptVariables': []
        }

        country = Country(country_dict)

        self.assertEqual(country.id, 1)
        self.assertEqual(country.name, 'United States')
        self.assertEqual(country.last_modified, convert_datetime_str('2022-04-01T16:18:34Z'))
        self.assertEqual(country.script_type, 1)
        self.assertEqual(country.current_release_id, 1)
        self.assertEqual(country.edge_script_variables, [])

    @patch('bunnyhop.countries.requests.get')
    def test_list_countries(self, mock_get):
        expected_data = [
            {
                'Id': 1,
                'Name': 'United States',
                'LastModified': '2022-04-01T16:18:34Z',
                'ScriptType': 1,
                'CurrentReleaseId': 1,
                'EdgeScriptVariables': []
            },
            {
                'Id': 2,
                'Name': 'Canada',
                'LastModified': '2022-04-01T16:18:34Z',
                'ScriptType': 1,
                'CurrentReleaseId': 1,
                'EdgeScriptVariables': []
            }
        ]

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        expected_countries = [Country(country_dict) for country_dict in expected_data]

        actual_countries = CountryAPI('test').list_countries()

        self.assertEqual(len(actual_countries), 2)
        self.assertEqual(actual_countries[0].name, expected_countries[0].name)
        self.assertEqual(actual_countries[1].name, expected_countries[1].name)


if __name__ == '__main__':
    unittest.main()