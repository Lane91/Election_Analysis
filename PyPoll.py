# The data we need to retrieve.
# 1. The toatl number of votes cast
# 2. A complete list of candiates who received votes
# 3. The percentage of votes each candidate won
# 4. The toatl number of votes each candidate won 
# 5. The winner of the elcetion based on pupular vote

# Add our dependencies.
import csv
import os


# Assign a variable to load file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to sve the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader funciton.
    file_reader = csv.reader(election_data)

    # Read and print the header row,
    headers = next(file_reader)
    print(headers)
    # print each row in CSV file.
    for row in file_reader:
        print(row)

# Close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

   
# Close the file
txt_file.close() 