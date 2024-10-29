import plotly.graph_objects as go

# Data for the chart
democrats = {
   "Democrats": (50_281_000, "DEM"),
   "Republicans": (1_281_000, "REP")
}

# Prepare data and colors
names = list(democrats.keys())
jobs = [data[0] for data in democrats.values()]
parties = [data[1] for data in democrats.values()]
colors = ['blue' if party == 'DEM' else 'red' for party in parties]

# Create a vertical bar chart with adjusted bar width and formatted text
fig = go.Figure(data=[
    go.Bar(
        x=names,
        y=jobs,
        marker=dict(color=colors),
        text=[f"{job:,}" for job in jobs],  # Format numbers with commas
        textposition='outside',
        width=0.3  # Adjust bar width here
    )
])

# Update layout with source information
fig.update_layout(
    title={
        'text': "Job Creation by Party since 1989<br><sup>Data from the Bureau of Labor Statistics</sup>",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title="Party",
    yaxis_title="Jobs Created (in millions)",
    yaxis=dict(tickformat=",.0f"),
    template="plotly_white"
)

    # Add watermark annotation
fig.add_annotation(
        text="ijwat",  # Change to your watermark text
        font=dict(size=20, color='rgba(0, 0, 0, 0.5)'),  # Corrected color format
        showarrow=False,
        xref="paper",
        yref="paper",
        x=0.9,  # Center of the plot
        y=1.05,  # Center of the plot
        align="center",
        opacity=0.3  # Transparency level for watermark
    )

# Show the plot
fig.show()
