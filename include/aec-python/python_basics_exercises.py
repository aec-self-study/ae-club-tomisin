# Write a loop that uses while instead of the built-in looping structure.

y = 0
while y < 20:
    print(y)
    y += 2

# Write a loop that loops over the keys in a dictionary and prints the values.

test_dict = {'a':5, 'b':8, 'c': 89}

for key in test_dict.keys():
    print(test_dict[key])

# Write the functions is_odd and is_even that are shown in the lecture.

def is_odd(num):
    return(num % 2 != 0)

def is_even(num):
    return(num % 2 == 0)

is_odd(7)
is_odd(10)
is_even(7)
is_even(10)

# Loop over my_first_list and square the value if the value is a number, and print the calories of the fruit if it’s a fruit (hint: use the dictionary to look up the calories).

my_first_list = ['apple', 1, 'banana', 2]
cal_lookup = {'apple': 95, 'banana': 105, 'orange':45}

for x in my_first_list:
    if type(x) == int:
        print(x**2)
    else:
        print(cal_lookup[x])



# Write a function that:
    # Takes a dictionary as an argument.
    # Loops over the keys in the dictionary.
    # Prints the square of the value in the value.
    # Hint: use the cal_lookup dictionary for testing.

def dict_fun(dict):
    for x in dict.keys():
        print(dict[x]**2)

dict_fun(cal_lookup)
# Share your work in your cohort Slack channel or in #self-study!