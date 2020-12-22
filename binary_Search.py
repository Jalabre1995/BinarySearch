#First thing is that we are going to create a function caled Binary Search
#And its going to take in two arguemnts. Its going to take in the Sequence and the items 

def binary_search(sequence, item):
    # Now we need to call the beginning position and the ending position
    begin_index = 0
    end_index = len(sequence) - 1

    #Create a whilelo loop saying while begin index is greater then the end_index the midpoint is going to equal the begin_index

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        #This will make the midpoint equal the midpoint that is in sequence
        midpoint_value = sequence[midpoint]
        #Next create a condition where if the midpoint equals item selected then retun the midpoint
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

    #Create a sequence that you can test
sequence_test = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
item_test = 10

print(binary_search(sequence_test, item_test))