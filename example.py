import sys
import demaster

print ("")
print ("")
print ("Demaster script example")
print ("/quit to quit"/)
print ("")

while True:
    name_to_check = input (">> ")
    if name_to_check == "/quit":
        sys.exit("")

    text_to_print = demaster.strip_name(name_to_check)
    print (text_to_print)
    print ("")
    print ("")

    f = open ("unremaster-output.txt", "a")
    f.write (name_to_check + " >>> " + text_to_print)
    f.close
