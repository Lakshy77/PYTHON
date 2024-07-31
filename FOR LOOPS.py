'''friends = ["Jim","Karen","Kevin"]
for letter in "Giraffe Academy":
    print(letter)
for friend in friends:
    print(friend)
for index in range(10):
    print(index)
#EXPONENT FUNCTIOn
def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result
print(raise_to_power(2,3))
#2D LISTS AND NESTED LOOPS
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][0])
for row in number_grid:
    for col in row:
        print(col)'''
#TRANSLATOR
'''def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))
try:
    10/0
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("err")'''

