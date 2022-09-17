
class Url:

    def __init__(self, scheme = str(), authority = str(), path = list(), query = dict(), fragment = list()):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, object):
        return str(self) == str(object)

    def __str__(self):
        text = str()
        if len(self.scheme) > 0:
            text += f"{self.scheme}://"
        if len(self.authority) > 0:
            text += self.authority
        if len(self.path) > 0:
            for pathes in self.path:
                text += f"/{pathes}"
        if len(self.query) > 0:
            text += "?"
            for key,value in self.query.items():
                text += f"{key}={value}&"
            text = text[:-1]
        if len(self.fragment) > 0:
            text += "#"
            for fragments in self.fragment:
                text += f"{fragments}#"
            text = text[:-1]
        return text

class HttpUrl(Url):

    def __init__(self, scheme="http", authority=str(), path=list(), query=dict(), fragment=list()):
        super().__init__(scheme, authority, path, query, fragment)

class HttpsUrl(Url):

    def __init__(self, scheme="https", authority=str(), path=list(), query=dict(), fragment=list()):
        super().__init__(scheme, authority, path, query, fragment)

class GoogleUrl(HttpsUrl):

    def __init__(self, scheme="https", authority="google.com", path=list(), query=dict(), fragment=list()):
        super().__init__(scheme, authority, path, query, fragment)

class WikiUrl(HttpsUrl):

    def __init__(self, scheme="https", authority="wikipedia.org", path=list(), query=dict(), fragment=list()):
        super().__init__(scheme, authority, path, query, fragment)

class UrlCreator:

    def __init__(self, scheme=str(), authority=str(), path=list(), query=dict(), fragment=list()):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def _create(self):
        return UrlCreator(self.scheme, self.authority, self.path, self.query, self.fragment)
    
    def __eq__(self, object):
        return str(self) == str(object)

    def __str__(self):
        text = str()
        if len(self.scheme) > 0:
            text += f"{self.scheme}://"
        if len(self.authority) > 0:
            text += self.authority
        if len(self.path) > 0:
            for pathes in self.path:
                text += f"/{pathes}"
            self.path.clear()
        if len(self.query) > 0:
            text += "?"
            for key,value in self.query.items():
                text += f"{key}={value}&"
            text = text[:-1]
            self.query.clear()
        if len(self.fragment) > 0:
            text += "#"
            for fragments in self.fragment:
                text += f"{fragments}#"
            text = text[:-1]
            self.fragment.clear()
        return text

    def __call__(self, *args, **kwds):
        for arg in args:
            self.path.append(arg)
        for key, value in kwds.items():
            self.query.update({key: value})
        return UrlCreator(self.scheme, self.authority, self.path, self.query)
            
    def __getattr__(self, name):
        self.path.append(name)
        return UrlCreator(self.scheme, self.authority, self.path)

assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'

url_creator = UrlCreator(scheme='https', authority='docs.python.org')
assert url_creator.docs.v1.api.list == 'https://docs.python.org/docs/v1/api/list'
assert url_creator("api","v1","list") == 'https://docs.python.org/api/v1/list'
assert url_creator("api","v1","list", q='my_list') == 'https://docs.python.org/api/v1/list?q=my_list'
assert url_creator('3').search(q='getattr', check_keywords='yes', area='default')._create() == 'https://docs.python.org/3/search?q=getattr&check_keywords=yes&area=default'
