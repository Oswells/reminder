import os
import requests
import urllib3
from functools import wraps
urllib3.disable_warnings()

class reminder():
    def __init__(self, **kwargs):
        assert 'url' in kwargs.keys(), 'url should be given'
        assert 'email' in kwargs.keys(), 'email should be given'
        assert '@' in kwargs['email'], f'The email address should have the correct format,got {kwargs["email"]}'
        assert 'mode' not in kwargs.keys(), 'mode should not be given'
        assert 'csrfmiddlewaretoken' not in kwargs.keys(), 'csrfmiddlewaretoken should not be given'
        assert 'error' not in kwargs.keys(), 'error should not be given'
        if 'url' in kwargs.keys():
            setattr(self,'url',kwargs['url'])
        self.data = dict()
        for k,v in kwargs.items():
            if k == 'url':
                continue
            elif k == "files":
                self.files = v
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
                e_copy = e
            finally:
                self.post(error=error)
                if error == None:
                    return result
                else:
                    raise e_copy
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
        files = dict()
        if hasattr(self,"files"):
            for file in self.files:
                if os.path.isdir(file):
                    for filename in os.listdir(file):
                        if os.path.isfile(os.path.join(file,filename)):
                            files[filename] = open(os.path.join(file,filename),'rb')
                elif os.path.isfile(file):
                    filename = file[file.rfind(os.sep)+1:]
                    files[filename] = open(file,'rb')
        session.post(url=self.url, data=self.data, headers=session.headers, cookies=session.cookies,files=files)
