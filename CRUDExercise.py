# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.



names = ['Christine', 'Alphonse', 'Arturo']


##	“Start with your program from Exercise 3-4. Add a print() 
# call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.”


	
# “You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, 
# informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.”







message1 = f"Hi {names[0].title()} lets go out to dinner some time."
message2 = f"Hi {names[1].title()} lets go out to dinner some time."
message3 = f"Hi {names[2].title()} lets go out to dinner some time."

print(message1, message2, message3)

popped_guest = names.pop()

print(popped_guest)

print(f"Sorry you cant make it {popped_guest}.")

names.append('Jim')

print(names)

for name in names:
	print(f"Hi {name.title()}, lets go out to dinner some time.")

for name in names:
	print(f"Hi {name.title()}, I've found a bigger table")

names.insert(0, "Kyle")
names.insert(1, "Jimothy")
names.insert(2, "Stephens")

print(names)

for name in names:
	print(f"Hi {name.title()}, lets go out to dinner some time.")


""" Start with your program from Exercise 3-6. Add a new line that prints a message saying that you 
can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, print a message to that person letting them know you’re 
sorry you can’t invite them to dinner.
Print a message to each of the two people still on your list, letting them know they’re still invited.
Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program."""

print("My apologies I can only invite two people for dinner :(")

popped_names = []

for i in range(3):
	popped_name = names.pop()
	popped_names.append(popped_name)
	print(f"I am sorry, {popped_name.title()}, I can't invite you to dinner.")

print(names)

for name in names:
	print(f"Hi, {name.title()}, you're still invited!")

print(names)

del names[0]
print(names)
del names[0]
print(names)
del names[0]

print(names)






	


