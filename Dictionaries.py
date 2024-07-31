'''monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "Octomber",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions["Nov"])
print(monthConversions["Mar"])
print(monthConversions.get("Dec"))'''
#WHILE LOOP
'''i=1
while i<=10:
    print(i)
    i=i+1
print("Done with Loop") '''
#BUILDING A GUESSING GAME
secret_word = "giraffe"
guess = ""
guess_count =0
guess_limit=3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
     if guess_count < guess_limit:
         guess=input("Enter guess: ")
         guess_count += 1
     else:
         out_of_guesses = True
if out_of_guesses :
    print("out of guesses, YOU LOSE!")
else:
    print("You win!")