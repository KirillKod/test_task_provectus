import json


class JSONUtil(object):
    def __init__(self):
        self.EXPECTED_JSON = {
            "success": False,
            "errors":
                {"email": [""],
                 "password": [""],
                 "message": "The password and email you entered don't match."
                            " If you forgot your password, use \"Forgot Password\""}}

    def validate_json(self, message):
        message = json.dumps(message)
        for k, v in self.EXPECTED_JSON.items():
            assert message[k] == v, "Expected value {} not equal to actual value {}".format(message[k], v)

