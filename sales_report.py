"""Generate sales report showing total melons each salesperson sold."""


# Create blank lists for salespeople and the melons sold 


salespeople = []
melons_sold = []

# Opens the file 'sales-report.txt;
f = open('sales-report.txt')

# Suggestion:
# Step 1: Create a blank dictionary called sales_report
"""
sales_report = {}
"""

# Loops over the text in file f 
for line in f:

    # Removes any whitespaces on the right side of each line
    # and save the string under the variable name line
    line = line.rstrip()

    # Remove '\' from each line and 
    # store each list under variable name entries
    entries = line.split('|')

    # Use indexing to find the salesperson in each list
    salesperson = entries[0]

    # Use indexing to find the melons in each list and 
    # converting data type to integer
    melons = int(entries[2])

    

    # Use a conditional statement to see if the salesperson is in salespeople list

    # Suggestions: 
    # Step 2: Rather than appending in two separate lists, salespeople and melons_sold,
    # we should create a dictionary and the logic is: 
    # If the salesperson's name is present, take the existing melons from the specific salesperson and add the current melons for the same salesperson
    # If the salesperson's name is not present, insert their name as a key and the melons as the value
    """
    if salesperson in sales_report:
        existing_melons = sales_report.get(salesperson)
        new_melons = existing_melons + melons
        sales_report[salesperson] = new_melons
    else:
        sales_report[salesperson] = melons
    """
    if salesperson in salespeople:
        
        # Find the index value for each salesperson in the list salespeople
        position = salespeople.index(salesperson)

        # Adds the the number of melons sold by 
        # salesperson individually  
        melons_sold[position] += melons
        
        # if the salesperson is not in the list 
    else:

        # Append the salesperson to the list salespeople
        salespeople.append(salesperson)
        
        
        # Append the melons sold in the list melons_sold 
        melons_sold.append(melons)
        

print('-' * 50)
# Loop over salespeople to find the index 
# using range(len())
for i in range(len(salespeople)):
    # Print a string containing the name of the salesperson and 
    # the number of melons they have sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')