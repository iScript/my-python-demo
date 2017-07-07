class UrlManager(object):

    def __init__(self):
        self.new_urls = set()   # 待爬取url
        self.old_urls = set()   # 已抓取url

    # 添加单个url
    def addNewUrl(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 添加多个url
    def addNewUrls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addNewUrl(url)


    def hasNewUrl(self):
        return len(self.new_urls) != 0

    def getNewUrl(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
