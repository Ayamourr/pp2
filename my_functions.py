def palindrome(string):
    s=string[::-1]
    if s==string:
        print(True)
    else:
        print(False)
    
def unique_elements(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

def histogram(lst):
    for number in lst:
        print('*' * number)