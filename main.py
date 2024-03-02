#Task_1
#https://edabit.com/challenge/a55ygB8Bwj9tx6Hym
letters = input("Enter the letters:")

def steps_to_convert(letters):
    upper = 0
    lower = 0
    for item in letters:
        if item.isupper():
            upper += 1
        else:
            lower += 1
    if upper > lower:
        print(letters.upper())
    else:
        print(letters.lower())


steps_to_convert(letters)


#Task_2
#https://edabit.com/challenge/f6LeKowjWQHm5637D
letters = "hApPy"

def cap_to_front(letters):
    string1 = []
    string2 = []
    for x in letters:
        if x.isupper():
            string1.append(x)
        else:
            string2.append(x)
            c= "".join(string1 + string2)
    print(c)



cap_to_front(letters)


#Task_3
#https://edabit.com/challenge/e8TFAMbTTaEr7JSgd
string = "TrAdE2W1n95!"

def left_digit(string):
    lst = []
    for item in string:
        if item.isdigit():
            lst.append(item)

    print(lst[0])


left_digit(string)


#Task_4
#https://edabit.com/challenge/vqMFpARj3DvELLDmZ
string1 = "R!=:~0o0./c&}9k`60=y"

def letters_only(string1):
    lst = []
    for item in string1:
        if item.isalpha():
            lst.append(item)


    print("".join(lst))


letters_only(string1)


#Task_5
#https://edabit.com/challenge/st8HBr2HMup6mD6z5

cost = int(input("Enter the price of cost:"))
sales = int(input("Enter the price of sales:"))

def profit_margin(cost, sales):
    a = ((sales - cost) / sales)*100
    b = round(a , 1)
    print(f"{b}%")

profit_margin(cost, sales)


#Task_6
#https://edabit.com/challenge/Njeob2pNQYsCd69fN
string = ("anime",
"meme",
"vines",
"roasts",
"Danny DeVito")
words = input("Enter the name:")

def prevent_distractions(string, words):
    for item in string:
        if item in words:
            return "NO!"

    return "Safe Watching!"


print(prevent_distractions(string, words))


#Task_7
#https://edabit.com/challenge/Kh7Bm9X7Q4rYB8uT7

string = input("Enter the word:")
vowels = "aeuio"

def is_vowel_sandwich(string, vowels):
    if len(string) != 3:
        return False

    if string[0] not in vowels and string[2] not in vowels:
        if string[1] in vowels:
            return True

    return False

print(is_vowel_sandwich(string, vowels))

#Task_8
#https://edabit.com/challenge/yXekCk3qRWYR5AHif
input  = input("Enter the letter:")
s = "cheese casserole"

def vow_replace(input,  s):
    vowels = "aoiue"
    for x in vowels:
        if x in s:
            s = s.replace(x , input)
    return s


print(vow_replace(input,s))