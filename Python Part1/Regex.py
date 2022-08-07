'''
A regular expression is a set of characters with highly specialized syntax 
that we can use to find or match other characters or groups of characters.
 In short, regular expressions, or Regex, are widely used in the UNIX world.

 Here's the list of the metacharacters;

. ^ $ * + ? { } [ ] \ | ( )  

re.match(pattern, string, flags=0)  
'''


import re  
line = "Learn Python through tutorials on javatpoint"  
match_object = re.match( r'.w* (.w?) (.w*?)', line, re.M|re.I)  
  
if match_object:  
    print ("match object group : ", match_object.group())  
    print ("match object 1 group : ", match_object.group(1))  
    print ("match object 2 group : ", match_object.group(2))  
else:  
    print ( "There isn't any match!!" )  

search_object = re.search( r' .*t? (.*t?) (.*t?)', line)  
if search_object:  
    print("search object group : ", search_object.group())  
    print("search object group 1 : ", search_object.group(1))  
    print("search object group 2 : ", search_object.group(2))  
else:  
    print("Nothing found!!")  