import blpapi
import pandas as pd

def fetch_bloomberg_data(ticker, start_time, end_time):
    """
    Fetch live intraday data from Bloomberg API.
    
    Parameters:
        ticker (str): The Bloomberg ticker symbol (e.g., "AAPL US Equity").
        start_time (str): Start time in the format "YYYY-MM-DDTHH:MM:SS".
        end_time (str): End time in the format "YYYY-MM-DDTHH:MM:SS".
    
    Returns:
        pd.DataFrame: DataFrame containing intraday bar data with columns:
                      [time, open, high, low, close, volume].
    """
    session = blpapi.Session()
    
    # Start the Bloomberg session
    if not session.start():
        raise ConnectionError("Failed to start Bloomberg session")
    if not session.openService("//blp/mktdata"):
        raise ConnectionError("Failed to open Bloomberg Market Data service")
    
    # Access the Bloomberg Market Data service
    service = session.getService("//blp/mktdata")
    request = service.createRequest("IntradayBarRequest")
    request.set("security", ticker)
    request.set("eventType", "TRADE")
    request.set("interval", 1)  # Interval in minutes
    request.set("startDateTime", start_time)
    request.set("endDateTime", end_time)
    
    # Send the request
    session.sendRequest(request)
    
    # Process the response
    data = []
    while True:
        event = session.nextEvent()
        for msg in event:
            if msg.hasElement("barData"):
                bar_data = msg.getElement("barData").getElement("barTickData")
                for i in range(bar_data.numValues()):
                    bar = bar_data.getValue(i)
                    data.append({
                        "time": bar.getElementAsString("time"),
                        "open": bar.getElementAsFloat("open"),
                        "high": bar.getElementAsFloat("high"),
                        "low": bar.getElementAsFloat("low"),
                        "close": bar.getElementAsFloat("close"),
                        "volume": bar.getElementAsInteger("volume")
                    })
        if event.eventType() == blpapi.Event.RESPONSE:
            break
    
    # Convert to a Pandas DataFrame
    return pd.DataFrame(data)

# Example Usage
if __name__ == "__main__":
    # Replace these with actual values
    ticker = "AAPL US Equity"
    start_time = "2024-12-29T09:30:00"
    end_time = "2024-12-29T16:00:00"
    
    df = fetch_bloomberg_data(ticker, start_time, end_time)
    print(df.head())
