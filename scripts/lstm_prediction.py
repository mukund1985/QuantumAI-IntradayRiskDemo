import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import time
import matplotlib.pyplot as plt

def train_lstm_with_timing(data, time_steps=10, epochs=5, batch_size=32, validation_split=0.2):
    """
    Train an LSTM model to predict market volatility and measure execution time.

    Parameters:
        data (np.ndarray): Time-series data (e.g., close prices) as a 1D array.
        time_steps (int): Number of time steps for each input sample.
        epochs (int): Number of training epochs.
        batch_size (int): Batch size for training.
        validation_split (float): Fraction of data to be used for validation.

    Returns:
        dict: Contains predicted volatility values, loss history, and timing information.
    """
    if len(data) <= time_steps:
        raise ValueError("Insufficient data for the given time_steps.")

    # Start timing
    start_time = time.time()

    # Prepare the data for the LSTM model
    print("Preparing data for LSTM model...")
    X = np.array([data[i:i + time_steps] for i in range(len(data) - time_steps)])
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
    history = model.fit(X, y, epochs=epochs, batch_size=batch_size, validation_split=validation_split, verbose=1)
    print("Model training completed.\n")

    # Make predictions
    print("Generating predictions...\n")
    predictions = model.predict(X[-time_steps:])

    # End timing
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"LSTM Workflow Execution Time: {execution_time:.2f} seconds\n")

    return {
        "predictions": predictions,
        "execution_time": execution_time,
        "loss_history": history.history  # Include training and validation loss
    }

# Example Usage
if __name__ == "__main__":
    # Generate synthetic data for testing
    synthetic_data = np.sin(np.linspace(0, 100, 1000))  # Example time-series data
    result = train_lstm_with_timing(synthetic_data, time_steps=10, epochs=5, batch_size=32)

    print("Predicted Volatility:")
    print(result['predictions'])

    print("Loss History:")
    print(result['loss_history'])

    print(f"Execution Time: {result['execution_time']:.2f} seconds")

    # Visualization: Loss History
    loss = result['loss_history']['loss']
    val_loss = result['loss_history']['val_loss']
    epochs = range(1, len(loss) + 1)

    # Save Loss History Plot
    plt.figure(figsize=(8, 5))
    plt.plot(epochs, loss, label="Training Loss", marker='o')
    plt.plot(epochs, val_loss, label="Validation Loss", marker='o')
    plt.title("Training and Validation Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig("images/training_validation_loss.png")
    plt.show()

    # Save Predictions vs True Data Plot
    plt.figure(figsize=(8, 5))
    plt.plot(range(len(synthetic_data)), synthetic_data, label="True Data")
    plt.plot(range(len(synthetic_data) - 10, len(synthetic_data)), result['predictions'], label="Predictions", marker='o')
    plt.title("LSTM Predictions vs True Data")
    plt.legend()
    plt.savefig("images/lstm_predictions_vs_true_data.png")
    plt.show()

    # Save Predictions to CSV
    pd.DataFrame(result['predictions'], columns=["Predicted Volatility"]).to_csv("data/predictions.csv", index=False)
