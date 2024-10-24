import csv
import os
import math

# Define the directory containing the CSV files
directory = 'your_path'

data_list = []
sum = 0

# Loop through each file in the directory
for filename in os.listdir(directory):    
    if filename.endswith('.csv'):
       with open(os.path.join(directory, filename)) as csvfile:            
            reader = csv.reader(csvfile)
            next(reader)
            
            # Cos calculation
                  
            data = [float(row[1]) for row in reader]
            #cos = [(math.sqrt((2 * i + 1)/3)) for i in data] 
            cos3 = [((math.sqrt((2 * i + 1)/3)) ** 3) for i in data]
            
            # List of lists from all files in directory
            data_list.append(cos3)  
                       	
#print(len(data_list),len(data_list[2])) 

out = []
for i in range(len(cos3) - 1):
    sum = 0
    for j in range(len(data_list) - 1):
        sum = sum + data_list[j][i]
    out.append(sum / len(data_list))

import matplotlib.pyplot as plt

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(out)
ax.set_xlabel('Frame')
ax.set_ylabel('Order parameter')
ax.set_title('Average order parameter')

plt.savefig(os.path.join(directory, 'Order_av.png'))
plt.show()

