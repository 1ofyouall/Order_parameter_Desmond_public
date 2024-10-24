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
            data_list.append(cos3)  

# Enter the chromophore numbers separated by a space                     	
chr_num = input('Chromophore numbers to reverse cos sign (write as: 1 3 5 ... 30) = ').split() 
chr_num = [int(x) for x in chr_num] 

# Changing the cos sign
for n in chr_num:
	data_element_new = [int(k) * (-1) for k in data_list[n - 1]] 
	data_list[n - 1] = data_element_new 

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

plt.savefig(os.path.join(directory, 'Order_av_reverse_cos3.png'))
plt.show()

