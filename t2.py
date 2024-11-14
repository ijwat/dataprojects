"""Market Capitalization Analysis of TSMC (2020-2024)"""


import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Fetch historical data for TSMC from Yahoo Finance
ticker = 'TSM'
df = yf.download(ticker, start="2020-01-01", end="2024-10-13")

# Assuming the closing price is used and adding shares outstanding
shares_outstanding = 5187e6  
df['MarketCap'] = df['Close'] * shares_outstanding  

# Select only the date and market cap columns
df = df.reset_index()[['Date', 'MarketCap']]

# Create a scatter plot
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['MarketCap'],
    mode='lines',
    name='TSM',
    line=dict(color='blue', width=2),
))

# Update layout
fig.update_layout(
    title='Taiwan Semiconductor Manufacturing Co. Market Capitalization (Jan. 2020 - Oct. 2024)',
    xaxis_title='Date',
    yaxis_title='Market Cap (USD)',
    showlegend=True,
    xaxis=dict(showgrid=True, gridcolor='lightgrey', gridwidth=0.5, ticks="outside", ticklen=10),
    yaxis=dict(showgrid=True, gridcolor='lightgrey', gridwidth=0.5, ticks="outside", ticklen=10),
    plot_bgcolor='white',
)

# Add watermark annotation
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
