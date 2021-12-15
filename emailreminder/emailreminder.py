import os
import requests
import urllib3
from functools import wraps
urllib3.disable_warnings()

class reminder():
    def __init__(self, **kwargs):
        assert 'url' in kwargs.keys(), 'url should be given'
        assert 'email' in kwargs.keys(), 'email should be given'
        if 'url' in kwargs.keys():
            setattr(self,'url',kwargs['url'])
        self.data = dict()
        for k,v in kwargs.items():
            if k == 'url':
                continue
            self.data[k] = v
        self.data['mode'] = 'remind'
        
    def __call__(self, func):
        @wraps(func)
        def do(*args, **kwargs):
            self.data['filepath'] = os.getcwdb()
            try:
                error = None
                result = func(*args, **kwargs)
            except Exception as e:
                error = str(e.__class__) + str(e)
            finally:
                self.post(error=error)
                return result
        return do

    def post(self, error=None):
        session = requests.session()
        session.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/51.0.2704.63 Safari/537.36','Referer':self.url}
        session.get(self.url)
        token = session.cookies.get('csrftoken')
        self.data['csrfmiddlewaretoken'] = token
        if error != None:
            self.data['error'] = error
        session.post(url=self.url, data=self.data, headers=session.headers, cookies=session.cookies)
