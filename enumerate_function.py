# Use of enumerate() and showing the demo of sorting a list with user input

# creating a sort algorithm program
# step 1: create a list
user_input = int(input("Enter the total number of elements you want to compare\t:"))
my_list = []
for i in range(user_input):
    element = int(input(f"Enter the elements {i+1} :"))
    my_list.append(element)


#step 2: compare the elements of list
for index,value in enumerate(my_list):
    if index < index+1:
        print(index+1)