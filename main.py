start_number = int(input("Please enter an even number "))

knit_pat = [] 

i = 0

if(start_number % 2 == 0):
    print(start_number)
else:
    print("This is not an even number")
    
while start_number > 0 :
    knit_pat.append(start_number)
    knit_pat.append(start_number)
    start_number = start_number - 1 
stitches = sum(knit_pat) -1 
s_total = stitches * 4
row_counter = len(knit_pat)
total_row_count = row_counter * 4
final_row = total_row_count - 4

print("The total number of stitches is: " + str(s_total))
print("The total number of rows is: " + str(final_row))
print(knit_pat)
