import random
# Demo of basic input in python
# name = input("Enter your name: ")
# print("Hello " + name)

# Demo of a program that computes for an area of a circle
# radius = float(input("Enter the radius: "))
# area = 3.14 * (radius**2)
# print("The area of the Circle is: " + str(area))

# Demo of a program that computes for a volume of a cylinder
# radius = float(input("Enter the Radius: "))
# height = float(input("Enter the Height: "))
# volume = 3.14 *(radius**2 * height)
# print("The Volume of the Cylinder: " + str(volume))

#Demo for array 
# fruits = ["apple", "banana", "cherry", "strawberry", "melon", "watermelon"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

#Demo for for Loop
# for x in fruits:
#     print(x)

# i = 0
# while i < 10:
#     print("Hello World")
#     print(i)
#     i = i + 1



#sample text-based game with simple conditional statement
#character attributes
character_health = 100
cht_dmg = 14
cht_crit = cht_dmg * 2
max_hp = 100
item = ""


name = input("Enter your name: ")
print("Hello " + name)

while character_health > 0:
    if character_health != 100 and item == "Fish":
        n = input("You have taken some damage to heal select [1 to heal/ 0 to ignore]")
        if n == "1" and character_health < max_hp:
            character_health += 10
            print("Your character's health is back to " + str(character_health))
        else :
             print("Your character's health is back to " + str(character_health))


    v = int(input("Choose 1 if you want to cross the river\nChoose 2 if you want to jump on the ravine\nChoose 3 to fight side monsster to gain exp and claim rewards \nChoose 4 if you want to fight monster in the dungeon \nInput: "))
   
    #Start of Journey
    if v == 1: 
        choice = input("If you want to go fishing select [1 for yes/ 0 for no]")
        if choice == "1":
            #Fishing minigame
            print("You have chosen Fishing! ")
            chance = random.randint(0,9)
            if chance > 4:
                item = "Fish"
                print("You have catch a Fish!")
            else:
                print("There is no fish to catch")

        elif choice == "0":
            print("You have crossed the river")


    elif v == 2:
        #damages the player
        print("You have jumped into the ravine")
        print("Your character has taken 10pt of damage")
        character_health = character_health - 10


    #practice mode
    elif v == 3:
        #lis of the monster in
        side_monster = ["minions","smurfs","zombie"]
        
        #minions
        minions_defeated = False
        minions_hp = 35
        minions_atk = 4
        minions_crit_damage = 8
        #smurfs
        smurfs_defeated = False
        smurfs_hp = 75
        smurfs_atk = 4
        smurfs_crit_damage = 8
        
        #zombies
        zombie_defeated = False
        zombie_hp = 100
        zombie_atk = 4
        zombie_crit_damage = 8
        #iterating the lisst of side monster
        for little_monster in side_monster:
            #if minions
            if little_monster == "minions":
                #battling the minions
                while character_health > 0:
                    #critical chance of minions
                     crit_chance = random.randint(0,75)
                     if crit_chance < 4:
                         print("Minions just got critical!")       
                         character_health = character_health - minions_crit_damage
                         print("Character health", str(character_health))
                     else:
                         #normal attack of minionns
                         print("Minions just attack me!")
                         character_health = character_health - minions_atk
                         print("Character health", str(character_health))
                    #if low  life
                     if character_health <= 20:
                         K = int(input("Your life is low do you want to continue or exit press 1 to exit, press 2 to continue"))
                         if K == 1:
                             print("Just exited the dungeon")
                             break

                     #attacking the minion
                     n = int(input("press [1] to attack"))
                     if n == 1:
                         #critical  chance for the character
                         if crit_chance < 5:
                             print("You just got critical")
                             minions_hp = minions_hp - cht_crit
                             print("Minions hp", str(minions_hp))
                         #normal attack of character
                         else:
                             print("You just attack Minions")
                             minions_hp = minions_hp - cht_dmg
                             print("Minions hp", str(minions_hp))
                         #defeated the monster and acquire an item
                         if minions_hp < 1:
                             minions_defeated = True
                             print("Minions defeated!")
                             item = "Minion's heart"
                             if item == "Minion's heart":
                                 print("You just acquired", item + " " + "additional 30 max_hp")
                                 max_hp = max_hp + 30
                             break
             #new monster                   
            elif little_monster == "smurfs" and minions_defeated == True:
                print("Another monster has arrive!")
                while character_health > 0:
                    #critical chance for smurf
                     crit_chance = random.randint(0,75)
                     if crit_chance < 6:
                         print("Smurfs just got critical!")       
                         character_health = character_health - smurfs_crit_damage
                         print("Character health", str(character_health))
                      #normal attack of smurfs   
                     else:
                         print("Smurfs just attack me!")
                         character_health = character_health - smurfs_atk
                         print("Character health", str(character_health))
                         
                    #if low life
                     if character_health <= 20:
                         e = int(input("Your life is low do you want to continue or exit press 1 exit, press 2 to continue"))
                         if e == 1:
                             print("Just exited the practice mode")
                             break
                        
                     #attacking the smurf
                     n = int(input("press [1] to attack"))
                     if n == 1:
                         #criit chance for the character
                         if crit_chance < 5:
                             print("You just got critical")
                             smurfs_hp = smurfs_hp - cht_crit
                             print("Smurfs hp", str(smurfs_hp))
                        #normal attack of the character
                         else:
                             print("You just attack Smurfs")
                             smurfs_hp = smurfs_hp - cht_dmg
                             print("Smurf hp", str(smurfs_hp))
                        #defeated the monstee and acquire and item
                         if smurfs_hp < 1:
                             smurfs_defeated = True
                             print("Smurf defeated!")
                             item = "Smurf's nails"
                             if item == "Smurf's nails":
                                 print("You just acquired", item + " " + "additional 10 attack damage")
                                 cht_dmg = cht_dmg + 10
                             break
            #third monster 
            elif little_monster == "zombie" and smurfs_defeated == True:
                print("another monster has arrive!")
                while character_health > 0:
                    #critical chance for the third monster
                     crit_chance = random.randint(0,75)
                     if crit_chance < 8:
                         print("Zombie just got critical!")       
                         character_health = character_health - zombie_crit_damage
                         print("Character health", str(character_health))
                         #normal attack of the monster
                     else:
                         print("Zombie just attack me!")
                         character_health = character_health - zombie_atk
                         print("Character health", str(character_health))
                         
                      #if low  life
                     if character_health <= 20:
                         l = int(input("Your life is low do you want to continue or exit press 1 exit, press 2 to continue"))
                         if l == 1:
                             print("Just exited the practice mode")
                             break
                      
                    #attacking the monster
                     n = int(input("press [1] to attack"))
                     if n == 1:
                         #critical chance for the character
                         if crit_chance < 5:
                             print("You just got critical")
                             zombie_hp = zombie_hp - cht_crit
                             print("zombie hp", str(zombie_hp))
                         #normal attack of the character    
                         else:
                             print("You just attack Zombie")
                             zombie_hp = zombie_hp - cht_dmg
                             print("Zombie", str(zombie_hp))
                         #defeated the monster and acquire the item
                         if zombie_hp < 1:
                             print("Zombie defeated!")
                             item = "Zombie's tooth"
                             if item == "Zombie's tooth":
                                 print("You just acquired", item + " " + "additional 20 attack damage")
                                 print("Exited the dungeon")
                                 cht_dmg = cht_dmg + 20
                             #exited the dungeon
                             break
                            
    #dungeon
    elif v == 4:
        #monsters
        red_dragon_defeated = False
        dragons = ["red dragon", "blue dragon"]
        
        #lvl1 dragon attributes
        lvl1_dungeon = dragons[0]
        lvl1_hp = 200
        lvl1_dead = False
        lvl1_atk = 15
        lvl1_crit = lvl1_atk * 2
        dr1low_health = False
        
        #lvl2 dragon attributes
        lvl2_dungeon = dragons[1]
        lvl2_hp = 400
        lvl2_atk = 30
        lvl2_crit = lvl2_atk * 2
        dr2low_health = False
        dungeon_cleared = False

        #entering the dungeon
        print("You have enter the dungeon")
        on_dungeon = True
        for dragon in  dragons:
            if dragon == "red dragon":
                while on_dungeon == True and character_health > 0:

                    if character_health <=250:
                        n = int(input("oh no your attributes is too low! Do you want to continue Press [1] to exit, Press [2] to continue"))
                        if n == 1:
                            print("Exited the dungeon")
                            break
                        
                    
                    crit_chance = random.randint(1,50)
                    #normal lvl1 dragon
                    if dr1low_health == False:
                    #criticcal chance for dragon
                        if crit_chance < 7:
                            character_health = character_health - lvl1_crit
                            print("red dragon got critical hit")
                            print("Character health is", str(character_health))
                        else:
                            print("Rawr!!! The dragon attack me")
                            character_health = character_health - lvl1_atk
                            print("Character health is", str(character_health))
                                
                    #attacking the dragon
                    atk = int(input("Press 1 to Attack: "))
                    if atk == 1 and character_health > 0:
                        #critical chance for the character
                        if crit_chance < 5:
                            lvl1_hp = lvl1_hp - cht_crit
                            print("You got critical")
                            print("Monster health is ", str(lvl1_hp))
                        else:
                            lvl1_hp = lvl1_hp - cht_dmg
                            print("Monster health is ", str(lvl1_hp))

                    #final form of the dragon1                            
                    if lvl1_hp <= 100 and lvl1_hp > 0:
                        dr1low_health = True
                        print("The red dragon evolved to it's final  form! additional attack +30 and more chancee to give critical damage!")
                        lvl_atk = lvl1_atk + 30
                        character_health = character_health - lvl1_atk
                        print("Character health is", str(character_health))
                        if crit_chance < 10:
                            character_health = character_health - lvl1_crit
                            print("red dragon got critical hit attack 2")
                        else:
                            print("Rawr!!! The dragon attack me")
                            character_health = character_health - lvl1_atk
                        
                        #lvl1 dragon is defeated and acquire the item
                    if lvl1_hp < 1:
                        red_dragon_defeated = True
                        print("Congratulations you defeated the Red Dragon!")
                        item = "Dragon Claw"
                        if item == "Dragon Claw":
                            print("You gain Dragon claw additional 100 attack damage and more chance to give critical damage ")
                            cht_dmg = cht_dmg + 100
                            if crit_chance < 15:
                                lvl1_hp = lvl1_hp - cht_crit
                                lvl2_hp = lvl2_hp - cht_crit
                        break
                    
            #new monster
            elif dragon == "blue dragon" and red_dragon_defeated == True:
                print("The final dragon has arrived!")
                while character_health > 0:
                    #warning
                    if character_health <=250:
                        q = int(input("oh no your attributes is too low! Do you want to continue Press 1 to exit, Press 2 to continue"))
                        if q == 1:
                            print("Exit the dungeon")
                        
                    crit_chance = random.randint(1,50)
                    #normal lvl2 dragon
                    if dr2low_health == False:
                    #criticcal chance for dragon2
                        if crit_chance < 7:
                            character_health = character_health - lvl2_crit
                            print("blue dragon got critical hit")
                            print("Character health is", str(character_health))
                        else:
                            print("Rawr!!! The dragon attack me")
                            character_health = character_health - lvl2_atk
                            print("Character health is", str(character_health))
                                
                    #attacking the dragon2
                    atk = int(input("Press 1 to Attack: "))
                    if atk == 1 and character_health > 0:
                        #critical chance for the character
                        if crit_chance < 5:
                            lvl2_hp = lvl2_hp - cht_crit
                            print("You got critical")
                            print("Monster health is ", str(lvl2_hp))
                        #normal attack of the charactter
                        else:
                            lvl2_hp = lvl2_hp - cht_dmg
                            print("Monster health is ", str(lvl2_hp))

                    #final form of the dragon2                            
                    if lvl2_hp <= 200 and lvl2_hp > 0:
                        dr2low_health = True
                        print("The Blue dragon evolved to it's final  form! additional attack +60 and more chancee to give critical damage!")
                        lvl2_atk = lvl2_atk + 60
                        character_health = character_health - lvl2_atk
                        print("Character health is", str(character_health))
                        if crit_chance < 10:
                            character_health = character_health - lvl2_crit
                            print("Blue dragon got critical hit attack 2")
                        else:
                            print("Rawr!!! The dragon attack me")
                            character_health = character_health - lvl2_atk
                        
                    #lvl2 dragon is defeated
                    if lvl2_hp < 1:
                        print("Congratulations you cleared the dungeon!")
                        item = "Dragon Skin"
                        if item == "Dragon Skin":
                            print("You gain Dragon skin additional 200 hp")
                            max_hp = max_hp + 200
                        print("You exited the dungeon")
                        breaK
    else:
        print("Invalid input")
    print("Your damage is ", cht_dmg)
    print("Your character's Health: " + str(character_health))

print("Your Character is dead!")
