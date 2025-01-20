# QuantumAI-IntradayRiskDemo

This project demonstrates the use of Quantum AI for intraday risk modeling, combining live data ingestion, AI predictions, and quantum optimization.

## Features

1. **Live Data Ingestion**: Fetch real-time financial data using Bloomberg API for accurate market insights. Alternatively, use mock data for testing purposes.
2. **Volatility Prediction**: Leverage LSTM models to forecast intraday market volatility.
3. **Quantum Optimization**: Use quantum computing to optimize portfolio risk and sensitivities dynamically.
4. **Real-Time Portfolio Adjustments**: Integrate live data and predictions to make real-time actionable decisions.

---

## Setup

1. **Create a Python Environment**:

   - Use `conda` or `virtualenv` to create an isolated Python environment.
   - Example:
     ```bash
     conda create -n quantum_ai_demo python=3.8
     conda activate quantum_ai_demo
     ```

2. **Install Dependencies**:

   - Install all required libraries using `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Demo Notebook**:

   - Launch Jupyter Notebook and execute the `demo_notebook.ipynb` step by step:
     ```bash
     jupyter notebook
     ```

4. **Bloomberg API Configuration** (Optional):
   - **Note for macOS Users**: Bloomberg Terminal software is not natively available for macOS. macOS users must access Bloomberg via [Bloomberg Anywhere](https://bba.bloomberg.net/) using a web browser. Alternatively, use a Windows system for full Bloomberg Terminal functionality.
   - **Windows Users**: Install the Bloomberg Terminal software and ensure it is running and logged in before using the API.
   - For both platforms, the Bloomberg Python API (`blpapi`) must be installed in the Python environment:
     ```bash
     pip install blpapi
     ```
   - Refer to the [Bloomberg Developer Portal](https://www.bloomberg.com/professional/support/api-library/) for setup instructions.
   - Alternatively, the demo can use mock data by default to simplify execution.

---

## Repository Structure

```plaintext
QuantumAI-IntradayRiskDemo/
├── README.md                 # Project documentation
├── demo_notebook.ipynb       # Jupyter notebook for the full demo
├── requirements.txt          # Python dependencies
├── scripts/                  # Modular Python scripts
│   ├── data_ingestion.py     # Fetch live Bloomberg data or mock data
│   ├── lstm_prediction.py    # AI-based volatility prediction
│   ├── quantum_optimization.py # Quantum optimization functions
│   └── integrated_solution.py # Integrated quantum + AI workflow
├── tests/                    # Unit tests for scripts
│   ├── test_data_ingestion.py
│   ├── test_lstm_prediction.py
│   ├── test_quantum_optimization.py
│   └── test_integrated_solution.py
├── data/                     # Pre-generated datasets for quick testing
│   └── pre_generated_data.csv
└── images/                   # Visualizations and diagrams
    ├── architecture_diagram.png  # Workflow architecture diagram
    └── example_visual.png       # Example output visualizations
```

---

## Workflow Overview

### **1. Data Ingestion**

- Use the Bloomberg API to fetch real-time market data (e.g., stock prices, volatility). Alternatively, mock data can be used for demonstration purposes.

### **2. AI Model for Predictions**

- Train an LSTM model on historical price data to predict future volatility trends.

### **3. Quantum Optimization**

- Solve optimization problems, such as risk sensitivity adjustments, using a QUBO formulation and D-Wave’s quantum annealer.

### **4. Integrated Workflow**

- Combine live data, AI predictions, and quantum optimization to deliver actionable insights for intraday portfolio adjustments.

---

## Outputs

1. **Predicted Volatility**: AI-generated forecasts for intraday market trends.
2. **Quantum Optimization Results**: Optimized portfolio adjustments for risk sensitivities.
3. **Visualizations**: Graphs showing market trends, volatility predictions, and optimization results.

---

## Future Enhancements

- **Multi-Asset Support**: Extend the workflow to handle multi-asset portfolios.
- **Regulatory Stress Testing**: Incorporate regulatory stress scenarios into the workflow.
- **Enhanced Visualization**: Integrate outputs with dashboards like Power BI or Tableau.

---
