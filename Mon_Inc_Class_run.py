from Mon_Inc_Class_define import *

# Let's create some monsters!

Monster_1 = Monsters('James P. \'Sully\' Sullivan', 2, 'blue', ['scaring', 'playfulness', 'good friend'], 75)
Monster_2 = Monsters('Mike Wazowski', 1, 'yellowy/green', ['helpful', 'funny', 'good assistant'], 20)
Monster_3 = Monsters('Randall Boggs', 2, 'purple', ['camouflage', 'wicked schemes', 'slimy little thing'], -5)
Monster_4 = Monsters('Roz', 2, 'slug green', ['always watching', 'administration work', 'looking ugly'], -100)
Monster_5 = Monsters('Celia Mae', 1, 'purple', ['being a schmoopsie-poo', 'receptionist skills', 'has nice hair always'], 30)
Monster_6 = Monsters('Henry J. Waternoose', 5, 'grey', ['being the real baddie all along', 'lots of legs, good for moving places', 'keeping secrets'], 15)

print(Monster_4.name, 'is so scary!!!')
print(Monster_4.scare(100))

print('{} has {} eyes!'.format(Monster_2.name, Monster_2.eyes))
print(Monster_2.look_weird(99))

print('{} has {} fur...'.format(Monster_3.name, Monster_3.fur))
print(Monster_3.make_scream(70))

print('{} has {} cuteness points'.format(Monster_1.name, Monster_1.cuteness))
print(Monster_1.cuddle(500))

print('{} has skills: {}'.format(Monster_5.name, Monster_5.skill_list))
print(Monster_5.make_laugh(90))
