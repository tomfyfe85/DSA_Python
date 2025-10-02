def item_in_common(list1, list2):
    my_dict = {}
    for num in list1:
        my_dict[num] = True

    for num in list2:
        if num in my_dict:
            return True
    return False

def find_duplicates(nums):
    my_dict = {}
    for num in nums:
        if num in my_dict:
            my_dict[num] = False
        else:
            my_dict[num] = True

    return [k for k,v in my_dict.items() if v is False]

print ( find_duplicates([1, 2, 3, 3, 3,5,5] ))
