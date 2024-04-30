"""CSV reader function that reads a CSV file and returns a list of dictionaries where each dictionary represents a row in the CSV file. 
The keys of the dictionary are the column names and the values are the cell values."""

"""
First way of doing the csv reading

# Importing the csv module to read the CSV file
import csv

# Defining the read_csv function that reads the CSV file and returns a list of dictionaries
def read_csv(path):
    
    # Opening the CSV file in read mode and reading the file using the csv.reader() function
    with open(path, "r") as csvfile:
        
        # Using the csv.reader() function to read the CSV file and specifying the delimiter as ","
        reader = csv.reader(csvfile, delimiter = ",")
        
        # Extracting the header row from the CSV file and storing it in the header variable
        header = next(reader)
        
        # Initializing an empty list to store the data
        data = []
        
        # Iterating over the rows in the CSV file and creating a dictionary for each row
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

# Main function to test the read_csv function by reading the data.csv file          
if __name__ == "__main__":
    data = read_csv("./data.csv")
    print(data)"""


# Second way of doing the csv reading

# Importing the csv module to read the CSV file
import csv

# Defining the read_csv function that reads the CSV file and returns a list of dictionaries
def read_csv(path):
    
    # Initializing an empty list to store the data
    data = []
    
    # Opening the CSV file in read mode and reading the file using the csv.DictReader() function
    with open(path, "r", newline="") as csvfile:
        
        # Using the csv.DictReader() function to read the CSV file
        reader = csv.DictReader(csvfile)
        
        # Iterating over the rows in the CSV file and appending each row as a dictionary to the data list
        for row in reader:
            data.append(dict(row))  
    return data

# Main function to test the read_csv function by reading the data.csv file
if __name__ == "__main__":
    data = read_csv("./data.csv")
    print(data)
