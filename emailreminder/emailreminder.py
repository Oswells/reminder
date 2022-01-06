import os
import time
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
        assert 'Error' not in kwargs.keys(), 'Error should not be given'
        assert 'CostTime' not in kwargs.keys(), 'CostTime should not be given'
        assert 'FilePath' not in kwargs.keys(), 'FilePath should not be given'
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
        self.t1 = time.time()
        
    def __call__(self, func):
        @wraps(func)
        def do(*args, **kwargs):
            self.data['FilePath'] = os.getcwdb()
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
        self.data['Ppid'] = os.getppid()
        self.post_error(error)
        self.post_time_cost()
        files = self.post_files()
        session.post(url=self.url, data=self.data, headers=session.headers, cookies=session.cookies,files=files)
    
    def post_error(self, error=None):
        if error != None:
            self.data['Error'] = error
    
    def post_time_cost(self):
        time_cost = time.time() - self.t1
        h = int(time_cost // 3600)
        m = int((time_cost - h * 3600) // 60)
        s = int(time_cost - time_cost // 60 * 60)
        self.data['CostTime'] = f'{h}h {m}m {s}s'
    
    def post_files(self):
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
        return files

