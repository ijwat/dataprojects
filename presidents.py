"""President debt analysis."""

import plotly.graph_objects as go

presidents = {
    "Ronald Reagan": (160.8, "Republican"),
    "George W. Bush": (72.6, "Republican"),
    "Barack Obama": (64.4, "Democrat"),
    "George H.W. Bush": (42.3, "Republican"),
    "Donald Trump": (33.1, "Republican"),
    "Bill Clinton": (28.6, "Democrat"),
    "Joe Biden": (16.7, "Democrat")

}


# Prepare data and colors
names = list(presidents.keys())
percentages = [data[0] for data in presidents.values()]
parties = [data[1] for data in presidents.values()]

# Color coding
colors = ['blue' if party == 'Democrat' else 'red' for party in parties]


import plotly.graph_objects as go

# Create a horizontal bar chart
fig = go.Figure(data=[
    go.Bar(
        x=percentages,
        y=names,
        orientation='h',
        marker=dict(color=colors),
    )
])

# Update layout
fig.update_layout(
    title='Percentage Increase in National Debt by U.S. Presidents',
    xaxis_title='Percentage (%)',
    yaxis_title='Presidents',
    xaxis=dict(showgrid=False),
        plot_bgcolor='white',  # Set plot area background color to white
    paper_bgcolor='white',  # Set the overall figure background color to white
)

# Add percentage labels
for i, percentage in enumerate(percentages):
    fig.add_annotation(
        x=percentage,
        y=names[i],
        text=f"{percentage}%",
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-60,
        font=dict(size=14)
    )

    # Add watermark annotation
    fig.add_annotation(
        text="ijwat",  # Change to your watermark text
        font=dict(size=20, color='rgba(0, 0, 0, 0.5)'),
        showarrow=False,
        xref="paper",
        yref="paper",
        x=0.9,
        y=0.4,
        align="center",
        opacity=0.3
    )

# Show the figure
fig.show()
