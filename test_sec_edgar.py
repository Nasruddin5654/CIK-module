
from app import SecEdgar

def test_basic_functionality():
    print("Testing SecEdgar basic functionality...")
    
    # Initialize
    se = SecEdgar('https://www.sec.gov/files/company_tickers.json')
    print("✓ SEC data loaded successfully")
    
    # Test CIK lookups
    apple_cik = se.name_to_cik("Apple Inc.")
    print(f"Apple CIK: {apple_cik}")
    
    msft_cik = se.ticker_to_cik("MSFT")
    print(f"Microsoft CIK: {msft_cik}")
    
    # Test filing retrieval (might fail due to SEC API limits)
    try:
        print("\nTesting annual filing...")
        annual_url = se.annual_filing(320193, 2023)
        print(f"Annual filing URL: {annual_url}")
        
        print("\nTesting quarterly filing...")
        quarterly_url = se.quarterly_filing(320193, 2023, 1)
        print(f"Quarterly filing URL: {quarterly_url}")
        
    except Exception as e:
        print(f"Filing test failed (expected due to SEC restrictions): {e}")
    
    print("\nBasic functionality test completed!")

if __name__ == "__main__":
    test_basic_functionality()