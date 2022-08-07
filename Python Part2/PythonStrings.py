
#python strings built in methods and functions
#capitalize() => convert the first letter into capital
str_ = "dukE lester is here"
print(str_.capitalize())

string_ = "Site is JKUAT and Duke is a Student no more 8902"
string_.casefold() #the function / method converts the string into lowercase
name = 'MY NAME'
print(name.casefold())

#center(width, fillchar)
print(name.center(18, "*"))

#count() ==> counts the number of occurences of characters in a string
# str.count(substring, start, end)
print( "Duke" in string_)
print(string_.count("e"))

#endswith() ==> if string ends with the specified suffix
print(string_.endswith(('e', 'f', 'g', 'more', 'or more')))

#find() ==> index of the occurences

print(string_.find("e"))

#find all 'es in the string_

def findCountLetter(str, target):
    found_letters = []
    if str == target:
        return str
    for letter in str:
        if letter == target:
            found_letters.append(letter)
    print(found_letters)
    return len(found_letters)

result = findCountLetter(string_, 'D')
print(result)

# index()
print(string_.index('e', 8))

print(string_.isalnum())
num = "hello24324"
print(num.isalnum())

#find non numeric elements in  a string

def findSymbols(mystring):
    for i in mystring:
        if not i.isalnum():
            print(i)

print(findSymbols("hello@duke@=-123"))

print(ord("d"))


def formatPhoneNumber(phone):
    if phone[0] == '0':
        newNumber = "+254" + phone[1:]
        print(newNumber)

formatPhoneNumber('0799443097')

print("254".join("0799443070"))

phone = "+254" + "0799443079".lstrip('0')
print(phone)

full_name = "lester"
new_name = full_name.maketrans('l','D')
new_name = full_name.translate(new_name)
print(new_name)







