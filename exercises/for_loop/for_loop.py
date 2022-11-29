# GOAL 
# Making a 5 row number list from one to 5

# how mony rows do i have
row = 5 

# Every time it will increase itself with 1 
# create a foor loop
# in this we are starting with 1
# we are increasing every row one by one
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")