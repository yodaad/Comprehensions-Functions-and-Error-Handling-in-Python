# Create, Read, Update, Delete (CRUD) operations in a set

set_countries = {"col", "mex", "bol"}

# verify the length of a set
size = len(set_countries)
print(size)
print(len(set_countries))

# Verify if a value is in the set
print("col" in set_countries)
print("per" in set_countries)

# Add  (adds a single element)
set_countries.add("per")
print(set_countries)

# Update (adds multiple elements)
set_countries.update({"arg", "ecu"})
print(set_countries)

# Delete (raises an error if the element does not exist)
set_countries.remove("col")
print(set_countries)

# Discard (does not raise an error if the element does not exist)
set_countries.discard("ar")
print(set_countries)

set_countries.clear()
print(set_countries)