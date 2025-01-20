import pandas as pd
import numpy as np

USE_MOCK_DATA = True  # Use mock data for demonstration purposes

def mock_bloomberg_data(ticker, start_time, end_time):
    """
    Generate mock intraday data for testing purposes.

    Parameters:
        ticker (str): The ticker symbol (used to label the mock data).
        start_time (str): Start time in the format "YYYY-MM-DDTHH:MM:SS".
        end_time (str): End time in the format "YYYY-MM-DDTHH:MM:SS".

    Returns:
        pd.DataFrame: DataFrame containing generated intraday data with columns:
                      [ticker, time, open, high, low, close, volume].
    """
    timestamps = pd.date_range(start=start_time, end=end_time, freq='1min')
    data = {
        "ticker": [ticker] * len(timestamps),  # Add ticker as a column
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
    Fetch data using mock Bloomberg data for demonstration purposes.

    Parameters:
        ticker (str): The ticker symbol.
        start_time (str): Start time in the format "YYYY-MM-DDTHH:MM:SS".
        end_time (str): End time in the format "YYYY-MM-DDTHH:MM:SS".

    Returns:
        pd.DataFrame: DataFrame with mock market data.
    """
    print("Using mock data for demonstration purposes.")
    data = mock_bloomberg_data(ticker, start_time, end_time)

    # Simple Data Preview
    print("Preview of generated data:")
    print(data.head())

    # Data Summary
    print("Data summary:")
    print(data.describe(include='all'))

    return data

# Example Usage
if __name__ == "__main__":
    ticker = "AAPL US Equity"
    start_time = "2024-12-29T09:30:00"
    end_time = "2024-12-29T16:00:00"

    df = get_data(ticker, start_time, end_time)
