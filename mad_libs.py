story_1 = "It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I told them that they have to (Verb) first. I've decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) !"
story_2 = "This weekend I am going camping with ( Proper Noun (Person's Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!"
story_3 = "Dear (Proper Noun (Person's Name) ), I am writing to you from a (Adjective) castle in an enchanted forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!"

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
    body2 = input('Input another part of the body: ')
    noun4 = input('Input a noun again(food): ')
    adjective3 = input('Input adjective (feeling): ')
    silly_w = input('Input a silly word: ')

    story = story_1.replace('(Number)', number).replace('(Measure of time)', 
            time).replace('(Mode of Transportation)', vehicle).replace('(Adjective)',
            adjective).replace('(Adjective2)',adjective2).replace('(Noun)',noun).replace('(Color)', 
            color).replace('(Part of the Body )', body).replace('(Verb)', verb).replace('(Number2)',
            number2).replace('(Noun2)', noun2).replace('(Noun3)', noun3).replace("( Part of the Body 2)", 
            body2).replace('(Noun4)', noun4).replace('( Adjective3)', adjective3).replace('(Silly Word )', silly_w)

elif int(template) == 2:
    name= input("Input Proper Noun (Person's Name): ")
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

    story = story_2.replace("( Proper Noun (Person's Name))", name).replace('(Noun)', 
            noun).replace('(Adjective (Feeling))', adjective).replace("(Verb)",verb).replace("(Adjective (Feeling) 2)", 
            adjective2).replace("(Animal)",animal).replace("(Verb2)",verb2).replace("(Color)",color).replace("( Verb (ending in ing) )",
            verb_ing).replace("(Adverb (ending in ly))",adverb).replace("(Number)",number).replace("(Measure of Time)",time).replace("(Silly Word)",s_word).replace("(Noun2)",noun2)

elif int(template) == 3:
    name = input("Input Proper Noun (Person's Name): ")
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

    story = story_3.replace("(Proper Noun (Person's Name) )", name).replace("(Adjective)",adjective).replace("(Color)",color).replace("(Animal)",animal).replace("(Place)",place).replace("(Adjective2)",
            adjective2).replace("(Magical Creature (Plural))",creature).replace("(Adjective3)",adjective3).replace("(Magical Creature (Plural)2)",creature2).replace("( Room in a House)",room).replace("(Noun)",
            noun).replace("(Noun2)",noun2).replace("(Noun(Plural)3)",noun3).replace("(Adjective4)",adjective4).replace("( Noun (Plural)4)",noun4).replace("(Number)",number).replace("( Measure of time)",
            time).replace("(Verb (ending in ing))",verb_ing).replace("(Adjective5)",adjective5).replace("(Noun5)",noun5)

else: 
    story = 'Invalid, start over and enter an integer 1, 2 or 3'

print(story)
