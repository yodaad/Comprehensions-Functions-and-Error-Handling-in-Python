# Description: This file contains utility functions that are used in the application. 

# Get the population data  
def get_population(country_dict):   
    labels = ["2022", "2020", "2015", "2010", "2000", "1990", "1980", "1970"]
    values = [int(country_dict.get(label + " Population", 0)) for label in labels]
    return labels, values 

# Get the population data for a specific country
def population_by_country(data, country):
    result = list(filter(lambda item: item["Country/Territory"] == country, data))
    return result
