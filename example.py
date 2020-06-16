import sys
import demaster

print ("")
print ("")
print ("Demaster script example - checks online API first, and if that fails runs locally")
print ("/offline to set offline mode")
print ("/quit to quit")
print ("")


offline_only = False
while True:
    name_to_check = input (">> ")
    if name_to_check == "/quit":
        sys.exit("")
    
    if name_to_check == "//offline":
        offline_only = True

    text_to_print = demaster.strip_name(name_to_check, offline_only)
    print (text_to_print)
    print ("")
    print ("")
