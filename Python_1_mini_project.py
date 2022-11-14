# # for random pick up uncomment below: random library & template = random.randint(1,3); and comment: template with input function
# import random
# template = random.randint(1,3) !
if int(template) == 1:
    number = input('Input a number: ')
    time = input('Measure of time: ')
    vehicle = input('Mo

template = input('Type story number (a digit out of 1, 2 or 3): ')

if int(template) == 1:
    number = input('Input a number: ')
    time = input('Measure of time: ')
    vehicle = input('Mode of Transportation: ')
    adjective = input('Input adjective: ')
    adjective2 = input('Input adjective (feeling): ')
    noun = input('Input noun: ')
    color = input('Input a color: ')
    body = input('Input Part of the Body: ')
    verb = input('Input verb: ')
    number2 = input('Input a number again: ')
    noun2 = input('Input a noun again: ')
    noun3 = input('Input a noun again: ')
    body2 = input('input another part of the body: ')
    noun4 = input('Input a noun again(food): ')
    adjective3 = input('Input adjective (feeling): ')
    silly_w = input('Input a silly word: ')

    story=f'''
Story 1:
It was about {number} {time} ago when I arrived at the hospital in a {vehicle}. The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun}s here. 
There are nurses here who have {color} {body}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number2} {noun2}. 
Today I talked to a doctor and they were wearing a {noun3} on their {body2}. I heard that all doctors {verb} {noun4} every day for breakfast. 
The most {adjective3} thing about being in the hospital is the {silly_w} {noun} !
    '''

elif int(template) == 2:
    name= input('Input Proper Noun (Person’s Name): ')
    noun = input('Input noun: ')
    adjective = input('Input adjective (feeling): ')
    verb = input('Input verb: ')
    adjective2 = input('Input adjective (feeling): ')
    animal = input('Input an animal: ')
    verb2 = input('Input verb again: ')
    color = input('Input a color: ')
    verb_ing = input('Input a verb + ing: ')
    adverb = input('Input a adverb + ly: ')
    number = input('Input a number: ')
    time = input('Measure of time: ')
    s_word= input('Input a silly word: ')
    noun2 = input('Input a noun again: ')

    story = f'''
Story 2:
This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun}. I am so {adjective} to {verb} in a tent. 
I am {adjective2} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. 
I have heard that the {color} lake is great for {verb_ing}. Then we will {adverb} hike through the forest for {number} {time}. 
If I see a {color} {animal} while hiking, I am going to bring it home as a pet! 
At night we will tell {number} {s_word} stories and roast {noun2} around the campfire!!
'''

elif int(template) == 3:
    name = input('Input Proper Noun (Person’s Name): ')
    adjective = input('Input adjective: ')
    color = input('Input a color: ')
    animal = input('Input an animal: ')
    place = input('Input a place: ')
    adjective2 = input('Input adjective again: ')
    creature = input('Input Magical Creature (Plural): ')
    adjective3 = input('Input adjective again: ')
    creature2 = input('Input another Magical Creature (Plural): ')
    room = input('Input Room in a House: ')
    noun = input('Input noun: ')
    noun2 = input('Input a noun again: ')
    noun3 = input('Input a noun again(Plural): ')
    adjective4 = input('Input adjective again: ')
    noun4 = input('Input a noun again(Plural): ')
    number = input('Input a number: ')
    time = input('Measure of time: ')
    verb_ing = input('Input a verb + ing: ')
    adjective5 = input('Input adjective again: ')
    noun5 = input('Input a noun again(Plural): ')

    story=f'''
Story 3:
Dear {name}, I am writing to you from a {adjective} castle in an enchanted forest. 
I found myself here one day after going for a ride on a {color} {animal} in {place}. 
There are {adjective2} {creature} and {adjective3} {creature2} here! 
In the {room} there is a pool full of {noun}. 
I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. 
It feels as though I have lived here for {number} {time}. 
I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!!
'''

else:
    story = 'Invalid, start over and enter an integer 1, 2 or 3'

print(story)

