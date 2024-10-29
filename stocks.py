"""META Stock Price Visualization"""

import requests
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Polygon API Key
API_KEY = "elRUkSNSr4_gdZ3xYJqOBrjSlKshPPUI"
TICKER = 'META'
URL = f'https://api.polygon.io/v2/aggs/ticker/{TICKER}/range/1/day/2021-02-04/2024-10-08?adjusted=true&sort=asc&limit=50000&apiKey={API_KEY}'

# Fetch the data from the Polygon.io API
response = requests.get(URL)
data = response.json()

# Check for successful response
if response.status_code == 200: 
    data=response.json()
    # Convert the results into a DataFrame
    df = pd.DataFrame(data['results'])

    # Convert the 't' column (timestamp) to datetime format
    df['date'] = pd.to_datetime(df['t'], unit='ms')

    # Select only the date and closing price columns
    df = df[['date', 'c']]  # 'c' is the closing price

    # Rename columns for clarity
    df.columns = ['Date', 'Close']


    # Create a scatter plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Close'],
        mode='lines',
        name='Stock Price',
        line=dict(color='red', width=2),
    ))



    # Update layout outside the loop
    fig.update_layout(
        title='META Stock Price (Oct. 2022 - Oct. 2024)',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        showlegend=True,
        xaxis=dict(showgrid=True, gridcolor='lightslategrey', gridwidth=2.5, dtick='M3', ticks="outside", ticklen=10),  # Gridlines every 3 months
        yaxis=dict(showgrid=True, gridcolor='lightslategrey', gridwidth=2.5, dtick=40, ticks="outside", ticklen=10),
        plot_bgcolor='white',
    )


    # Add ijwat annotation on the plot
    fig.add_annotation(
        text="ijwat",  
        font=dict(size=20, color='rgba(0, 0, 0, 0.5)'), 
        showarrow=False,
        xref="paper",
        yref="paper",
        x=0.9,  
        y=0.1,  
        align="center",
        opacity=0.3  
    )

    # Show the figure 
    fig.show()

else:
    print("Error fetching data:", data.get('error', 'Unknown error'))