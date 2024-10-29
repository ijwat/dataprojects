"""Create a line bar plot in Python using Matplotlib."""

# Import the Matplotlib library
import matplotlib.pyplot as plt

# Create two lists of data corresponding to the x and y axis
x = [10, 20, 30, 40, 50]
y = [5, 10, 15, 20, 25]

# Create a line plot
plt.plot(x, y)


# Add a title to the plot
plt.title("Custom Plot")

# Add labels to the x and y axis
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add a grid to the plot
plt.grid(True)

# Display the plot on the computer
plt.show()




