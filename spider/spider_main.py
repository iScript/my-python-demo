# encoding:utf-8
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.url_manager = url_manager.UrlManager()
        self.html_downloader = html_downloader.HtmlDownloader()
        self.html_parser = html_parser.HtmlParser()
        self.html_outputer = html_outputer.HtmlOutputer()

    def craw(self,url):
        count = 1
        self.url_manager.addNewUrl(url)
        while self.url_manager.hasNewUrl():
            try:
                print(count)
                new_url = self.url_manager.getNewUrl()
                html_content = self.html_downloader.download(new_url)
                new_urls,new_data = self.html_parser.parse(new_url,html_content)
                self.url_manager.addNewUrls(new_urls)
                self.html_outputer.collectData(new_data)
                if count == 4 :
                    break
                count = count + 1
            except:
                print("爬取失败 ： error")
        self.html_outputer.outputHtml()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/%E9%95%BF%E5%BE%81%E4%B8%89%E5%8F%B7%E4%B9%99%E8%BF%90%E8%BD%BD%E7%81%AB%E7%AE%AD/7619249"
    spider = SpiderMain();
    spider.craw(root_url);
