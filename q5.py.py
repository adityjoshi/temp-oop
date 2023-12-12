li = [1,2,3,4,5]
del li[0:]
print(li)

def remove_first_and_last_char(input_str):
    if len(input_str) < 2:
        print("String is too short to remove first and last characters.")
    else:
        result_str = input_str[1:-1]
        print(result_str)

# Example usage:
input_string = "Hello, World!"
remove_first_and_last_char(input_string)
