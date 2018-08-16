from unittest import TestCase
from JSON_Util import JSONUtil
from api_util import MakeRequest


class SendRequest(TestCase):
    expected_json = JSONUtil()
    request = MakeRequest()

    def test_01_negative_authorization(self):
        response = self.request.authorize(login='hello@world.com', password='12345678')
        self.expected_json.validate_json(message=response)


