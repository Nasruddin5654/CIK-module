import requests
from datetime import datetime
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
            name = data.get("title")
            #dict's gets name as a key and returns cik or ticker as a value
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
    
    
    def annual_filing(self, cik, year):
        
        headers = {"User-Agent": "nas@gmail.org"}
        padded_cik = str(cik).zfill(10) #pads numbers for you to add extra leading zeros to sum it to 10 digits 

        # Fetch the company's submissions JSON from the SEC
        submissions_url = f'https://data.sec.gov/submissions/CIK{padded_cik}.json'
        response = requests.get(submissions_url, headers=headers)
        data = response.json()

        # Find the first 10-K for the given year
        filings = data.get("filings", {}).get("recent", {})
        forms = filings.get("form", [])
        accession_numbers = filings.get("accessionNumber", [])
        primary_documents = filings.get("primaryDocument", [])
        filing_dates = filings.get("filingDate", [])

        for i, form_type in enumerate(forms):
            if form_type == "10-K" and filing_dates[i].startswith(str(year)):
                accession = accession_numbers[i].replace("-", "")
                document = primary_documents[i]
                url = f'https://www.sec.gov/Archives/edgar/data/{padded_cik}/{accession}/{document}'
                print(f"10-K URL for {year}: {url}")
                break
        
        #fetch the accession number and primary document
        
    def quarterly_filing(self, cik, year, quarter):
    # Same setup as annual_filing
        headers = {"User-Agent": "nas@gmail.org"}
        padded_cik = str(cik).zfill(10)
        
        # Fetch submissions (same as before)
        submissions_url = f'https://data.sec.gov/submissions/CIK{padded_cik}.json'
        response = requests.get(submissions_url, headers=headers)
        data = response.json()
        
        # Find 10-Q for specific year AND quarter
        filings = data.get("filings", {}).get("recent", {})
        forms = filings.get("form", [])
        accession_numbers = filings.get("accessionNumber", [])
        primary_documents = filings.get("primaryDocument", [])
        filing_dates = filings.get("filingDate", [])
        
        for i, form_type in enumerate(forms):
            if form_type == "10-Q":  # Only change this from "10-K" to "10-Q"
                filing_date = filing_dates[i]
                # Check year AND quarter
                if (filing_date.startswith(str(year)) and 
                    self._get_quarter_from_date(filing_date) == quarter):
                    accession = accession_numbers[i].replace("-", "")
                    document = primary_documents[i]
                    url = f'https://www.sec.gov/Archives/edgar/data/{padded_cik}/{accession}/{document}'
                    print(f"10-K URL for {year}: {url}")
        
        return None

    # Helper method to get quarter from date (YYYY-MM-DD)
    def _get_quarter_from_date(self, date_str):
        month = int(date_str.split("-")[1])  # Extract month (1-12)
        return (month - 1) // 3 + 1  # Returns 1, 2, 3, or 4

se = SecEdgar('https://www.sec.gov/files/company_tickers.json')






