class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collectData(self,data):
        if data is None:
            return
        self.datas.append(data)


    def outputHtml(self):
        #retur
        for data in self.datas:
            print(data)
