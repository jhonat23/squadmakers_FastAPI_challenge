from functools import reduce

def str_to_int_list(data: list) -> list:

    numbers = [int(i) for i in data if i.isdigit()]

    return numbers

def mcm(lst: list) -> int:

    if 0 in lst:
        return 0

    # Finding MCM for two numbers
    def mcm(a, b):

        if a > b:
            major = a
        else:
            major = b

        while True:
            if major % a == 0 and major % b == 0:
                mcm = major
                break
            major += 1

        return mcm

    # Applying reduce 
    return reduce(lambda x, y: mcm(x, y), lst)

def give_one(data: int) -> int:
    return data + 1

if __name__ == '__main__':
    s = ['19', '45', '12']
    dat = str_to_int_list(s)
    print(dat)

    print(mcm(str_to_int_list(s)))