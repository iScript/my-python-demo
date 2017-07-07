import urllib.request

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        html = response.read()
        return (html)
