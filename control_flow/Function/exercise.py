# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1
def divisor(n):
    for i in range(1, n):
        if n % i == 0:
            print(i)


print(divisor(100))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet

def let(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    if len(letter) < 1:
        return None
    else:
        for l in alphabet:
            if letter == l:
                print(alphabet.index(l))

let("p")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14
def Q2b(name):
    sp = name.strip()
    emp = []
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]
    if len(name) < 0:
        return None
    else:
        for l in alphabet:
            for x in sp:
                if l == x:
                    emp.append(alphabet.index(l))

    string_ints = ''.join(map(str, emp))
    print(string_ints)

Q2b("bob")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

def Q2c(name):
    sp = name.strip()
    emp = []
    count = 0
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]
    if len(name) < 0:
        return None
    else:
        for l in alphabet:
            for x in sp:
                if l == x:
                    emp.append(alphabet.index(l))
    string_ints = ''.join(map(str, emp))
    print(string_ints)
    m = list(string_ints)
    for p in m:
        count += int(p)
    print(int(string_ints) - count)
Q2c("bob")


#Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.
def prime(x):
    if x>1:
        for n in range(2, x):
            if(x % n) == 0:
                return False
        return True
    else:
        return False
print(prime(7))
print(prime(20))


#Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit