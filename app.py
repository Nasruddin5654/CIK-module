import requests

class SecEdgar:
    def __init__(self,fileurl):
        self.fileurl=fileurl
        self.namedoct={}
        self.tickerdict={}

        headers={"user-agent": 'MLT fellow name@mlt.org'}
        r=requests.get(self.fileurl, headers=headers)
        self.filejson=r.json()
        

        self.cik_json_to_dict()

    def cik_json_to_dict(self):
        self.name_dict = {} #empty dicts
        self.ticker_dict = {}

        for data in self.filejson.values():
            #iterates through the file and initalizes cik, ticker and name
            cik = data.get("cik_str")
            ticker = data.get("ticker")
            name = str(data.get("title"))
            #dict's name as a key and returns cik or ticker as a value
            self.name_dict[name] = {"name": name, "ticker": ticker, "cik":cik} 


            #finds cik or name by searching it up with the ticker
            self.ticker_dict[ticker]={"ticker":ticker ,"name": name, "cik": cik} 
       
    # method that returns tuple of CIK, NAME, TICKER
    def name_to_cik(self, name):
        if name in self.name_dict:
            data = self.name_dict[name]
            return (data["cik"], name, data["ticker"])
        else:
            return None
        
    def ticker_to_cik(self, ticker):
        if ticker in self.ticker_dict:
            data = self.ticker_dict[ticker]
            return (data["cik"], data["name"], ticker)
        else:
            return None
    
    

se = SecEdgar('https://www.sec.gov/files/company_tickers.json')

#test cases
print(se.name_to_cik("Apple Inc."))
print(se.ticker_to_cik("MSFT"))