import unittest
from unittest.mock import MagicMock, patch
from bunnyhop import core, abuse


class TestAbuseAPI(unittest.TestCase):

    @patch.object(abuse, 'requests')
    def test_list_cases(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'Items': [
                {
                    'Id': 1,
                    'PullZoneId': 1
                },
                {
                    'Id': 2,
                    'PullZoneId': 2
                }
            ]
        }
        mock_requests.request.return_value = mock_response

        api_key = 'test_api_key'
        api = abuse.Abuse(api_key)
        cases = api.list_cases()

        self.assertEqual(len(cases), 2)
        self.assertIsInstance(cases[0], abuse.AbuseCase)
        self.assertEqual(cases[0].id, 1)
        self.assertEqual(cases[0].pull_zone_id, 1)

    @patch.object(abuse, 'requests')
    def test_resolve_dmca(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'Id': 1,
            'PullZoneId': 1,
            'Status': 2
        }
        mock_requests.request.return_value = mock_response

        api_key = 'test_api_key'
        api = abuse.Abuse(api_key)
        case = abuse.AbuseCase(api_key, {'id': 1})
        case.resolve('dmca')

        self.assertEqual(case.status, 2)

    @patch.object(abuse, 'requests')
    def test_resolve_abuse_case(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'Id': 1,
            'PullZoneId': 1,
            'Status': 2
        }
        mock_requests.request.return_value = mock_response

        api_key = 'test_api_key'
        api = abuse.Abuse(api_key)
        case = abuse.AbuseCase(api_key, {'id': 1})
        case.resolve('abuse_case')

        self.assertEqual(case.status, 2)

    @patch.object(abuse, 'requests')
    def test_check(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'Id': 1,
            'PullZoneId': 1,
            'Status': 2
        }
        mock_requests.request.return_value = mock_response

        api_key = 'test_api_key'
        api = abuse.Abuse(api_key)
        case = abuse.AbuseCase(api_key, {'id': 1})
        case.check()

        self.assertEqual(case.status, 2)


class TestBunnyAPI(unittest.TestCase):

    def test_init(self):
        api_key = 'test_api_key'
        api = core.Bunny(api_key)

        self.assertEqual(api.api_key, api_key)
        self.assertEqual(api.base_url, 'https://api.bunny.net')
        self.assertIsInstance(api.headers, dict)
        self.assertIsInstance(api.Abuse, abuse.Abuse)


if __name__ == '__main__':
    unittest.main()
