#coding:utf-8
#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):

    def getNewUrls(self,page_url,soup):
        urls = set()
        links = soup.find_all('a',href=re.compile(r"/item/\w"))
        for link in links:
            url = link["href"]
            full_url = urllib.parse.urljoin(page_url,url)
            #print(full_url)
            urls.add(full_url)
        return urls

    def getNewData(self,page_url,soup):
        res_data = {}

        res_data["url"] = page_url

        title_node = soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"] = title_node.get_text()

        summary_node = soup.find("div",class_="lemma-summary")
        res_data["summary"] = summary_node.get_text()

        return res_data


    def parse(self,page_url,html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content,"html.parser",from_encoding='utf-8')
        #print(soup)
        new_urls = self.getNewUrls(page_url,soup)
        new_data = self.getNewData(page_url,soup)
        return new_urls,new_data
