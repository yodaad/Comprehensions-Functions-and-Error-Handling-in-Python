# Create a graph using matplotlib

# Importing the matplotlib module to create graphs and charts in Python 
import matplotlib.pyplot as plt

# Function to generate a bar chart
def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

# Function to generate a pie chart
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis("equal")
    plt.show()

# Main function to test the generate_bar_chart and generate_pie_chart functions
if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [100, 200, 800]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)