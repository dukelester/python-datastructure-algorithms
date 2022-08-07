# print(dir(int))
# a regex is a squence of characters that defines a search pattern. used to find and replace operations

#using the re module in python
import re

# print(re)

#raw string is a strring prefixed by r or R

raw_string1 = r'Hello duke lester'
raw_string2 = R'Hello again duke lester \n\t\a'
print(raw_string1, raw_string2)

#meta characters: . ^$*+[]\|()  ==> alphanumerics are put inside the [] eg [adv], [ab],[hello duke], [a-zA-Z0-9] etc
#[0-9] ony digits
'''
[0-9] ony digits
[a-z] only a to z small letters
\d ==> digit characters
\D non digit characters
\s ==> white space characters
\S ==>non white space characters
\w ==> alphanumeric characters
\W ==> non alphanumeric characters
. ==> any single character  except '\n'
? ==> occurrence of a pattern
+ ==> occurrence of pattern more than 1 times
\b ==> boundary btwn words
[..] ==> any single character in the square brackets
\ ==> special characters
{n, m} ==> matches at least n and at most m occurrences
a|b ==> matches a or b 

'''

#the re.match() function ==> tries to find if  specified pattern is in the beginning of the string

pattern = "duke"
string_ = "Welcome duke is a good programmer"
print(re.match(pattern, string_))

for str in string_:
    obj = re.match("W[a-z]", str)
    print(obj)

print(re.search("duke", string_))

print(re.findall('o', string_))

#get the list of words

find_all = re.findall(r"\w*", string_)
print(find_all)

for word in find_all:
    if len(word) > 0:
        print(word)