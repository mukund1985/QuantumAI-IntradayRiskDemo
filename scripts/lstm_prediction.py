import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


def train_lstm(data, time_steps=10, epochs=5, batch_size=32):
    """
    Train an LSTM model to predict market volatility.
    
    Parameters:
        data (np.ndarray): Time-series data (e.g., close prices) as a 1D array.
        time_steps (int): Number of time steps for each input sample.
        epochs (int): Number of training epochs.
        batch_size (int): Batch size for training.
    
    Returns:
        np.ndarray: Predicted volatility values for the last time steps.
    """
    # Prepare the data for the LSTM model
    print("Preparing data for LSTM model...")
    X = np.array([data[i:i+time_steps] for i in range(len(data) - time_steps)])
    y = data[time_steps:]
    X = X.reshape((X.shape[0], X.shape[1], 1))  # Reshape for LSTM input
    print(f"Input Shape: {X.shape}, Output Shape: {y.shape}\n")

    # Define the LSTM model
    print("Defining the LSTM model...")
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(time_steps, 1)),
        LSTM(50),
        Dense(1)  # Output layer
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    print("Model compiled successfully.\n")

    # Train the model
    print("Training the LSTM model...")
    model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=1)
    print("Model training completed.\n")

    # Make predictions
    print("Generating predictions...\n")
    predictions = model.predict(X[-time_steps:])
    return predictions

# Example Usage
if __name__ == "__main__":
    # Generate synthetic data for testing
    synthetic_data = np.sin(np.linspace(0, 100, 1000))  # Example time-series data
    predictions = train_lstm(synthetic_data, time_steps=10, epochs=5, batch_size=32)
    print("Predicted Volatility:")
    print(predictions)
