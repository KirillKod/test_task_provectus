import requests


class MakeRequest(object):
    @staticmethod
    def authorize(login, password):
        payload = {'login': login,
                   'password': password}
        url = 'http://instatestvx.me​/api/auth/login'
        try:
            #fails here on requests exception. Decorator didn't help here.
            r = requests.post(url=url, json=payload, timeout=10)
        except Exception as e:
            raise Exception("Unable to login: {}".format(e))
        # assert r.status_code == 401, 'Expected status code 401 is not equal to actual value {}'.format(r.status_code)
        return r
