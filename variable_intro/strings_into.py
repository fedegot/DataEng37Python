#
#
# double = "double quote"
# single = 'single quote'
#
# print(double, single)
#
# failure = 'I said "oh no!"'
# both = 'I said "oh no david\'s asdasdas"'
# print(both)
#
# h = "hello world!"
# print(h[6]) #Print the caracter we want
# print(h[-1]) #Print the caracter we want backwards
# print(h[1:6]) #print part of the string
#
#
# #from slicing h, print "lo wo"
# print(h[3:8])
# print(h[3:])
# print(h[1:-1:3])
# print(h[4::2])
# print(h[::-1])
#
# # Methods string
#
# print(type(h))
# print(h.lower())


#STRIP
#COUNT
#UPPER
#CAPITALIZE
#REPLACE

#@@@@@@@@@@@@@@@@@@@@ STRIP @@@@@@@@@@@@@@@@@@@@
message = '     Hello World!  '

# remove leading and trailing whitespaces
print('Message:',"from:" + message + "  to: " + message.strip())
#@@@@@@@@@@@@@@@@@@@@ COUNT @@@@@@@@@@@@@@@@@@@@
message2 = 'Hello World!'
print('Count:', message2.count('o'))
#@@@@@@@@@@@@@@@@@@@@ UPPER @@@@@@@@@@@@@@@@@@@@
print('Upper:', message2.upper())
#@@@@@@@@@@@@@@@@@@@@ CAPITALIZE @@@@@@@@@@@@@@@
print('Capitalize:', message2.capitalize())
#@@@@@@@@@@@@@@@@@@@@ REPLACE @@@@@@@@@@@@@@@@@@
print('Capitalize:', message2.replace("World", "Fred"))


#concatenation
a = "mr"
b = "Blue"
c = "Sky"

print(a + " " + b + " " + c)

a = "ciao"
b = 2

print(a + str(b))


