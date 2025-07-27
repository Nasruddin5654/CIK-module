import requests

class SecEdgar:
    def __init__(self,fileurl):
        self.fileurl=fileurl
        self.namedoct={}
        self.tickerdict={}

        headers={"user-agent": 'MLT fellow nasruddin@mlt.org'}
        r=requests.get(self.fileurl, headers=headers)
        self.filejson=r.json
        print(r.text)
        print(self.filejson)

        self.cik_json_to_dict()

    def cik_json_to_dict(self):
        self.name_dict={}
        self.ticker_dict={}

se=SecEdgar('https://www.sec.gov/files/company_tickers.json')