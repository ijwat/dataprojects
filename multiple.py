"""Analyzing Stock Trends: AMD, TSM, NVDA, INTC"""

import requests
import pandas as pd
import plotly.graph_objs as go

# List of tickers 
tickers = ['AMD', 'TSM', 'NVDA', 'INTC']
api_key = 'elRUkSNSr4_gdZ3xYJqOBrjSlKshPPUI'

# Dictionary to store DataFrames for each ticker
stock_data = {}

for ticker in tickers:
    # Fetch stock prices for each ticker
    url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2021-02-04/2024-10-08?adjusted=true&sort=asc&limit=50000&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and 'results' in data:
        # Convert the results into a DataFrame
        df = pd.DataFrame(data['results'])
        
        
        df['Date'] = pd.to_datetime(df['t'], unit='ms')
        
        # Select only the date and closing price columns
        df = df[['Date', 'c']]  
        df.columns = ['Date', 'Close']  
        
        # Add a column for the ticker
        df['Ticker'] = ticker
        
        # Store the DataFrame in the dictionary
        stock_data[ticker] = df
    else:
        print(f"Error fetching data for {ticker}: {data.get('error', 'Unknown error')}")

# Combine all DataFrames into a single DataFrame
df_combined = pd.concat(stock_data.values(), ignore_index=True)


# Initialize Plotly figure
fig = go.Figure()

# Loop through each ticker and plot its data
for ticker in tickers:
   
    df_ticker = df_combined[df_combined['Ticker'] == ticker]
    
    # Add a trace for each company
    fig.add_trace(go.Scatter(
        x=df_ticker['Date'],
        y=df_ticker['Close'],
        mode='lines',
        name=f'{ticker} Prices',
        line=dict(width=2)  
    ))

# Customize layout
fig.update_layout(
    title='Stock Prices for AAPL, GOOGL, and NVDA (2021-2024)',
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    showlegend=True,
    xaxis=dict(showgrid=True, gridwidth=2),
    yaxis=dict(showgrid=True, gridwidth=2),
    plot_bgcolor='white'
)

# Show the figure
fig.show()
