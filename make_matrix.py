import sys

num_rows = 501
num_columns = 1001

count_matrix = [[0] * num_columns for _ in range(num_rows)]

for entry in sys.stdin:
    parts = entry.strip().split("\t") 
    if len(parts) < 2:  
        continue  
    
    try:
        index_x = int(parts[0]) 
        index_y = int(parts[1])  
        
    
        count_matrix[index_y][index_x] += 1
    except (ValueError, IndexError):
        continue 
for row in count_matrix:
    print(row)
