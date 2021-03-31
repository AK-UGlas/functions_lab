def return_10():
    return 10

def add(first_num_add, second_num_add):
    add = first_num_add + second_num_add
    return add


def subtract(first_num_sub, second_num_sub):
    subtract = first_num_sub - second_num_sub
    return subtract

def multiply(first_num_multi, second_num_multi):
    multiply = first_num_multi * second_num_multi
    return multiply

def divide(first_num_div, second_num_div):
    divide = first_num_div / second_num_div
    return divide

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(month_index):
    months = [
        "January","February", "March",
        "April", "May", "June", "July",
        "August", "September", "October",
        "November", "December"
        ]
    return months [month_index - 1]

def number_to_short_month_name(month_index):
    months = [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun", "Jul",
        "Aug", "Sep", "Oct",
        "Nov", "Dec"
        ]

    return months[month_index - 1]

def cubic_volume(length_of_side):
    #return length_of_side * length_of_side * length_of_side
    return length_of_side ** 3

def rev_string(input_string):
    return input_string[::-1]

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)