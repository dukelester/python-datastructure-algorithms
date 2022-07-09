def getBinaryGap(number):

    #convert the number into binary
    number = format(number, "b")
    print(number)
    #convert the number to string
    str_number = str(number)
    print(str_number)
    #strip
    stripped = str_number.strip('0')
    splitted = stripped.split('1')
    print( max(splitted))
    length = len(max(splitted))
    print(length)
    
# getBinaryGap(1052)
getBinaryGap(32)