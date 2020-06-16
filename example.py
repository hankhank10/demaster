import sys
import demaster

print ("")
print ("")
print ("Demaster script example - checks online API first, and if that fails runs locally")
print ("/quit to quit")
print ("")

while True:
    name_to_check = input (">> ")
    if name_to_check == "/quit":
        sys.exit("")

    text_to_print = demaster.strip_name(name_to_check)
    print (text_to_print)
    print ("")
    print ("")
