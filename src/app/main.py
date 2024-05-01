# Main function to test the generate_bar_chart and generate_pie_chart functions

# Importing utils.py, read_csv.py, and charts.py
import utils
import read_csv
import charts

# Run the main function 
def run(): 
    
    # Read the data from the CSV file
    data = read_csv.read_csv("./data.csv")
    country = input("Type country: ").title()
    
    result = utils.population_by_country(data, country)
    
    # If the result is not empty, generate a bar chart
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
    
    print(result)

# Main function to test the generate_bar_chart and generate_pie_chart functions
if __name__ == "__main__":
    run()