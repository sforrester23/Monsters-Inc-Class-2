# Let's define a class of monsters!

class Monsters():

# Define some characteristics

    def __init__(self, name, number_eyes, fur_colour, skills, cuteness_level):
        self.name = name
        self.eyes = number_eyes
        self.fur = fur_colour
        self.skill_list = skills
        self.cuteness = cuteness_level

# Define some behaviours

    def scare(selfs, scariness):
        return 'BOOOOOO! ' + 'Score {}'.format(scariness)

    def look_weird(self, weirdness):
        return 'WHOAAAA... ' + 'Score {}'.format(weirdness)

    def make_scream(self, loudness):
        return 'AAAAHHHHHHHH! ' + 'Score {}'.format(loudness)

    def cuddle(self, warmth):
        return 'AWWWWWW :) :) <3 ' + 'Score {}'.format(warmth)

    def make_laugh(self, funniness):
        return 'AHAHAHAHAAH LOL! :L :L :L ' + 'Score {}'.format(funniness)


