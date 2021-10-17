def basic_while_loop(): 
    # Initialize offset
    offset = 8

    # Code the while loop
    while offset != 0: 
        print("correcting...")
        offset = offset - 1
        print(offset)


def add_conditionals(): 
    # Initialize offset
    offset = -6

    # Code the while loop
    while offset != 0 :
        print("correcting...")
        if offset > 0 :
            offset -= 1
        else : 
            offset += 1    
            print(offset)


if __name__  == "__main__": 
    # basic_while_loop()
    add_conditionals()