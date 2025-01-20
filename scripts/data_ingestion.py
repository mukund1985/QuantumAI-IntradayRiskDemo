import blpapi
import pandas as pd
import numpy as np

USE_MOCK_DATA = True  # Toggle between mock and live Bloomberg data

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
        raise ConnectionError("Failed to start Bloomberg session. Ensure the Bloomberg Terminal is running.")
    if not session.openService("//blp/mktdata"):
        raise ConnectionError("Failed to open Bloomberg Market Data service.")
    
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

def mock_bloomberg_data(ticker, start_time, end_time):
    """
    Generate mock intraday data for testing purposes.
    
    Parameters:
        ticker (str): The ticker symbol (mocked, used for consistency).
        start_time (str): Start time in the format "YYYY-MM-DDTHH:MM:SS".
        end_time (str): End time in the format "YYYY-MM-DDTHH:MM:SS".
    
    Returns:
        pd.DataFrame: DataFrame containing generated intraday data with columns:
                      [time, open, high, low, close, volume].
    """
    timestamps = pd.date_range(start=start_time, end=end_time, freq='1min')
    data = {
        "time": timestamps,
        "open": np.random.uniform(100, 200, len(timestamps)),
        "high": np.random.uniform(150, 250, len(timestamps)),
        "low": np.random.uniform(90, 150, len(timestamps)),
        "close": np.random.uniform(100, 200, len(timestamps)),
        "volume": np.random.randint(1000, 5000, len(timestamps)),
    }
    return pd.DataFrame(data)

def get_data(ticker, start_time, end_time):
    """
    Fetch data using either live Bloomberg API or mock data based on the USE_MOCK_DATA flag.
    
    Parameters:
        ticker (str): The Bloomberg ticker symbol.
        start_time (str): Start time in the format "YYYY-MM-DDTHH:MM:SS".
        end_time (str): End time in the format "YYYY-MM-DDTHH:MM:SS".
    
    Returns:
        pd.DataFrame: DataFrame with market data.
    """
    if USE_MOCK_DATA:
        print("Using mock data for demonstration purposes.")
        return mock_bloomberg_data(ticker, start_time, end_time)
    else:
        print("Fetching live data from Bloomberg API...")
        return fetch_bloomberg_data(ticker, start_time, end_time)

# Example Usage
if __name__ == "__main__":
    # Replace these with actual values
    ticker = "AAPL US Equity"
    start_time = "2024-12-29T09:30:00"
    end_time = "2024-12-29T16:00:00"
    
    # Fetch data based on the configuration
    df = get_data(ticker, start_time, end_time)
    print(df.head())
