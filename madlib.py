story = '''
A strange magic starts when the new clock strikes midnight.

It has happened every night since the family had gotten the new clock.

Every night something new happens wheter it be all the old dishes gone or all 

the house keys are in the cars.
'''

magic = input("enter a Adj.")
midnight = input("enter a Adj.")
night = input("enter a Adj.")
old = input("enter a Adj.")
house = input("enter a Adj.")

story = story.replace ("magic",magic)
story = story.replace ("midnight",midnight)
story = story.replace ("night",night)
story = story.replace ("old",old)
story = story.replace ("house",house)
print (story)
