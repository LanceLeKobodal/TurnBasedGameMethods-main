from Entity_Class import *
from Attack_Class import *

"""entityStats should be given in the order of :
    Strength, Dexterity, Vigor, Endurance, Intelligence, Mind, Faith all being
    given as integers"""

susie = Monster("Susie", [16,14,15,12,8,11,7], "Croc", [getWater()])
kittenKatten = Monster("Kitten Katten", [14,10,13,12,10,15,15], "Cat", [getElec(),getWater()])
sadie = Monster("Sadie", [8,10,15,9,8,13,20], "Human", [getPlant(),getLife()])
babyDraken = Monster("Baby Draken", [7,8,9,8,18,19,6], "Dragon", [getFire()])
liamNouvue = Monster("Liam Nouvue", [8,8,8,8,8,8,8], "Human", [getNeut()])
mossPuppy = Monster("Moss Puppy", [12,14,10,16,8,10,9], "Elemental", [getPlant()])
magmaSlug = Monster("Magma Slug", [9,2,11,6,11,10,12], "Elemental", [getFire()])
demBiggles = Monster("Dem Biggles", [15,17,14,16,10,14,13], "Sage", [getNeut()])
leChonk = Monster("Le Chonk", [14,17,11,14,12,16,16], "Pig", [getNeut()])
xquic = Monster("Xquic The All Mighty", [10,20,74,15,15,11,11], "Cat", [getNeut()])
grundleStumper = Monster("Grundle Stumper", [16,16,15,16,12,16,14], "Human", [getNeut()])
marnmer = Monster("Marnmer", [4,20,14,12,15,10,2], "Catfish", [getEarth(), getElec()])

team1 = [susie, kittenKatten, sadie, babyDraken]
team2 = [mossPuppy, xquic, magmaSlug, marnmer]

sadie.addAttack(vineWhip)
sadie.addAttack(waterBolt)
sadie.addAttack(milkDrink)

xquic.addAttack(slashAttack)

susie.addAttack(waterBolt)
susie.addAttack(slashAttack)
susie.addAttack(ram)

kittenKatten.addAttack(waterBolt)
kittenKatten.addAttack(elecBolt)
kittenKatten.addAttack(slashAttack)

babyDraken.addAttack(fireBolt)
babyDraken.addAttack(slashAttack)
babyDraken.addAttack(ram)


