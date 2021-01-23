''' he world population has grown over the past years. Will it continue to do so? The world bank has estimates of the world population for the years 1950 up to 2100.
The years are loaded in your workspace as a list called year, and the corresponding populations as a list called pop.'''

# Print the last item from year and pop
print(year[--1])
print(pop[-1])


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()
