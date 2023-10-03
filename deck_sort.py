in_file = "deck_input.txt"
out_file = "deck_output.txt"

def main():
    arr = read_file(in_file)
    arr = split_colon(arr)
    arr = choose_last(arr)
    arr = split_tab(arr)
    arr = choose_first(arr)
    arr = trim_end(arr)
    print_arr(arr)
    write_file(out_file, arr)
    


def split_colon(array):   
    split_arr = []
    for val in array:        
        split_val = val.split(":")
        split_arr.append(split_val)
        
    return split_arr

def choose_last(array):
    last_arr = []
    for val in array:
        if (len(val) > 1):
            last_val = val[len(val) - 1]
            last_arr.append(last_val)
    
    return last_arr
        
def split_tab(array):
    tab_arr = []
    for val in array:
        tab_val = val.split("\t")
        tab_arr.append(tab_val)

    return tab_arr

def choose_first(array):
    first_arr = []
    for val in array:
        first_val = val[0]
        first_arr.append(first_val)
        
    return first_arr

def trim_end(array):
    trim_arr = []
    for val in array:
        index_p = val.rfind("(")
        if (index_p != -1):
            trim_arr.append(val[0: index_p] + " \n")
        else:
            trim_arr.append(val + " \n")
    return trim_arr

def print_arr(array):
    for val in array:
        print(val)

def read_file(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    file.close()
    return lines

def write_file(fileName, array):
    file = open(fileName, 'w')
    file.writelines(array)
    file.close()


main()