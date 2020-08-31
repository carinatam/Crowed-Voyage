import time
import graphic_functions
def platform():
    graphic_functions.basic() #print graphic  
    print("What will you like to do?") #dialogue leading to choice
    print("\\Continue\\ fighting? or visit the \\travelling cart\\?")
balance=25
inventory=["coffee"]
#################
graphic_functions.basic()
mc=input("This is the MC. What is their name?: ") #name input
print("Welcome to CROWNED VOYAGE,", mc, "!")
time.sleep(2)
print("To start you off, here's 25 julles!")
time.sleep(2)
print("Balance=", balance)
time.sleep(2)
print()
graphic_functions.basic_mushu()
time.sleep(2)
print("???: Hello.")
time.sleep(2)
print(mc,": Who are you?")
time.sleep(2)
print("???: My name is Mushu and I own the travelling cart.") #intro/cut scene
time.sleep(2)
print(mc,": The travelling cart?")
time.sleep(2)
print("Mushu: Yes, the travelling cart. You will have many opportunities to buy from me after you finish off a mob.")
time.sleep(3)
print("Mushu: Since you seem new to this, here's a coffee, on the house! I hope to see you around!")
print("Inventory:", inventory)
time.sleep(3)
print()
graphic_functions.basic()
time.sleep(3)
print("Coffee will heal you 20 health, it costs 20 julles to buy one from Mushu, so save your money!")
time.sleep(3)
print("Words in slashes signal your input options! Make sure not to mispell any commands or your turn will end!")
time.sleep(3)
input("Are you ready to start your adventure?: ")
print("Great! Lets go!")

##########################COMBAT CODE##########################
import random #every time this game is played, a new health is randomized for each mob within a range
graphic_functions.danger()
time.sleep(1)
graphic_functions.bunny_mob() #mob level 1
mch=100 #main character health: 100
mh=random.randint(40,60) #lvl 1 mob health is randomized between 40 and 60
mcdamage=random.randint(20,30) #the main character's damage is randomized between 20 and 30
mobdamage=random.randint(3,8) #the lvl 1 mob damage is randomized between 3 and 8
print("Health: ",mch) #print mc health
time.sleep(1)
print("Health of mob: ",mh) #print mob health
time.sleep(1)
choice=input("Will you \\attack\\ or \\heal\\?: ") #input choice (must be spelled properly!! or else your turn will be skipped!!!!!)
choice=choice.lower() #lowercase all characters to fit conditions
while((mch>0) and (mh>0)): #while both MC and mob are still alive
    for i in range(1,4): #this range counts up to 3; 3 is the critical hit code
        if(i<3): #if i is 1 or 2, run regular code (not critical hit code)
            if(choice=="attack"): #if they entered attack
                mh=mh-mcdamage #subtract the randomized MC damage from the mob health
                if(mh>0): #if mob health is greater than 0 after attack
                    graphic_functions.attack_bunny_mob() #print attack graphic
                    print("Health of mob: ",mh) #print health of mob after attack
                    time.sleep(1)
                elif(mh<=0): #if mob health is less than or equal to 0 after attack
                    graphic_functions.attack_bunny_mob() #print attack graphic
                    print("Health of mob: 0") #print health as 0 (no negative numbers will be printed)
                    time.sleep(1)
                    break
            elif(choice=="heal"): #if they entered heal
                check=inventory.count("coffee") #check inventory (list) for coffee
                if(check>0): #if there is one or more coffee, MC gains 20 health
                    graphic_functions.coffee_heal() #print graphic
                    print("You're in luck! You have", check, "coffee!") #dialogue
                    time.sleep(1)
                    mch=mch+20 #add 20 health to existing health
                    inventory.remove("coffee") #remove used coffee from inventory
                    time.sleep(1)
                    print("You used 1 coffee!")
                    time.sleep(1)
                    print("Your health is now: ", mch) #print new MC health
                    time.sleep(1)
                elif(check==0): #if there is no coffee in inventory list
                    print("Oh no! You don't have any coffee! Better buy some from Mushu later!") #dialogue
                    time.sleep(1)
        elif((i==3) and (mh>0)):# if i is equal to 3 and MC's health is above 0, run critical hit code
            if(choice=="attack"): #if they entered attack
                print("Critical hit!")
                time.sleep(1)
                mcdamage_alt=(mcdamage*2) #critical hit damage is double the already established damage
                mh=mh-mcdamage_alt #subtract alternate damage (critcal hit damage) from mob health
                if(mh>0): #if mob health is greater than 0 after attack
                    graphic_functions.attack_bunny_mob() #print attack graphic
                    print("Health of mob: ",mh) #print health of mob after attack
                    time.sleep(1)
                elif(mh<=0): #if mob health is less than or equal to 0 after attack
                    graphic_functions.attack_bunny_mob() #print attack graphic
                    print("Health of mob: 0") #print health as 0 (no negative numbers will be printed)
                    time.sleep(1)
                i=0 #reset loop (after critical hit, regualar hit will happen twice)
                break
            elif(choice=="heal"): #if they entered heal when i equals three, nothing changes from when i equals 1 or 2 (no bonus health or critcal hit)
                check=inventory.count("coffee") #check inventory (list) for coffee
                if(check>0): #if there is one or more coffee, MC gains 20 health
                    graphic_functions.coffee_heal() #print graphic
                    print("You're in luck! You have", check, "coffee!") #dialogue
                    time.sleep(1)
                    mch=mch+20 #add 20 health to existing health
                    inventory.remove("coffee") #remove used coffee from inventory
                    time.sleep(1)
                    print("You used 1 coffee!")
                    time.sleep(1)
                    print("Your health is now: ", mch) #print new MC health
                    time.sleep(1)
                elif(check==0): #if there is no coffee in inventory list
                    print("Oh no! You don't have any coffee! Better buy some from Mushu later!") #dialogue
                    time.sleep(1)
                i=0 #reset loop (after critical hit, regualar hit will happen twice)
        if(mh>0): #if the mob's health is above 0, they're capable of attack
            graphic_functions.bunny_attack() #print graphic
            print("The mob attacked!")
            time.sleep(1)
            mch=mch-mobdamage #subtract mob damage from MC damage
            if(mch<=0): #if MC health is less than or equal to 0
                mch=0 #set health to 0, gets rid of negatives
                print("Health: 0") #print health at 0
                time.sleep(1)
                break #leave while loop
            elif(mch>0): #if MC health is above 0
                print("Health: ",mch) #print health
                time.sleep(1)
                choice=input("Will you \\attack\\ or \\heal\\?: ") #reset choice, goes back into while loop to attack again
                choice=choice.lower() #lowercase all characters to fit conditions
                mcdamage=random.randint(20,30) #the main character's damage is re-randomized between 20 and 30
                mobdamage=random.randint(3,8) #the lvl 1 mob damage is re-randomized between 3 and 8
    if(mch<=0): #MC health is 0 (dead)
        graphic_functions.dead_man() #print graphic
        exit() #game is over, exit program
    elif(mh<=0): #if mob health is 0 (dead)
        graphic_functions.dead_bunny_mob() #print graphic
        time.sleep(1)
        loot_variable=random.randint(3,12) #give MC a randomized amount of julles for beating the mob
        print("Here is", loot_variable, "julles for defeating the monster!")
        time.sleep(1)
        balance=balance+loot_variable #add to balance
        print("Balance: ",balance) #print new balance

platform() #refer to platform above
x=0 #makes sure that you do not enter travelling cart if you entered continue
basic_choice=input("What is your decision?: ") #input 
basic_choice=basic_choice.lower() #lowercase to fit conditions
while(True): #while something was entered (will always happen)
    for tc in range(1,3): #tc counts how many times youve entered the traveling cart
        if(basic_choice=="travelling cart"): #if they enter the traveliing cart 
            graphic_functions.travelling_cart() #print graphic 
            #############################TRAVELING CART#################################
            if(tc==1): #if its their first time visiting 
                input("Mushu: Welcome to the travelling cart! How was your last battle?: ")
                print("Mushu: Thats great! Would you like to buy some coffee? It costs 20 julles")
            if(tc==2): #if its the second time visting 
                print("Mushu: Oh? Back again so soon?") #new dialogue 
                time.sleep(2)
                print("Mushu: More coffee? It's 20 julles!")
            time.sleep(2)
            print("Your inventory is:", inventory) #print inventory
            time.sleep(2)
            print("Your balance is: ", balance) #pring balance 
            time.sleep(2)
            store_choice=input("\\Yes\\ or \\No\\?: ") #store input (yes or no to coffee)
            store_choice=store_choice.lower() #lowercase to fit conditions 
            while(True): #while something was entered (will always happen)
                if((store_choice!="no") and (store_choice!="yes")): #if the input was mispelled 
                    store_choice=input("Mushu: I didn't quite get that. Can you say that again?: ") #option to re-input
                elif(store_choice=="yes"): #if yes (to coffee)
                    if(balance>=20): #if balance is greater than 20
                        balance=balance-20 #subtract 20 from balance
                        print("You have purchased 1 coffee")
                        time.sleep(1)
                        inventory.append("coffee") #add coffee to inventory 
                        print("Inventory:",inventory)
                        time.sleep(1)
                        print("Your balance is now: ", balance) #print new balance 
                        time.sleep(1)
                    else: #if balance is less than 20
                        print("Oh no! you dont have enough julles! Go fight some mobs to gain more.")
                        time.sleep(1)
                    x=1 #you have entered the shop, x now equals one
                    break #leave this while loop
                elif(store_choice=="no"): #if no
                    print("Mushu: No? That's okay. I won't take it personally.")
                    x=1 #you have entered the shop, x now equals one
                    time.sleep(1)
                    break #leave this while loop
            if(tc==1): #cut scene dialogue, only if first time going in travelling cart
                print(mc, ": Mushu? May I ask what you do outside of running the shop?")
                time.sleep(2)
                print("Mushu: Oh not much, I'm just working on a potion that makes the user 10000 times stronger.")
                time.sleep(3)
                print(mc,": ...")
                time.sleep(1)
            print("Mushu: Anyways, thanks for visiting the store! I hope to see you soon!") #goodbye dialogue
            if(tc==2): #if this is the second time in the travelling cart
                tc==1 #reset to one, if you enter travelling cart again, i will equal 2
            time.sleep(1)
        elif((basic_choice!="continue") and (basic_choice!="travelling cart")): #if something was mispelled in basic choice  
            basic_choice=input("I didn't quite get that. Can you say that again?: ") #re-input
            break #leave this while loop
        if(x!=0): #if they did not enter the travelling cart (entered continue)
            platform() #re-run platform (see above)
            x=0 #reset x to 0
            basic_choice=input("What is your decision?: ") #input 
            basic_choice=basic_choice.lower() #lower to fit conditions
        if(basic_choice=="continue"): #if continue
            print("Okay! Let's hope you don't run into any more mobs!")
            break #leave this while loop
    if(basic_choice=="continue"):
        break #leave final while loop
########################### FISH MOB ######################################
graphic_functions.boat()
time.sleep(3)
print(mc,": A boat!")
time.sleep(2)
graphic_functions.mc_boat()
time.sleep(3)
graphic_functions.boat_danger()
time.sleep(3)
graphic_functions.fish_mob()
mh=random.randint(80,120)
mcdamage=random.randint(20,30)
mobdamage=random.randint(12,22)
print("Health: ",mch) #health of MC, carries over from last level
time.sleep(1)
print("Health of mob: ",mh) #health of mob
time.sleep(1)
choice=input("Will you \\attack\\ or \\heal\\?: ")
choice=choice.lower()
while((mch>0) and (mh>0)): #while mc health is above 0 and mh is above 0
    for i in range(1,4): #counts how many times you input choice, third time is critical hit
        if(i<3): #normal code (not critical hit)
            if(choice=="attack"): 
                mh=mh-mcdamage #subtract damage from mob health
                if(mh>0): #if mob is alive after attack
                    graphic_functions.attack_fish_mob_1()
                    time.sleep(0.5)
                    graphic_functions.attack_fish_mob_2()
                    time.sleep(0.5)
                    print("Health of mob: ",mh) #print health of mob
                    time.sleep(1)
                elif(mh<=0): #if mob is dead
                    graphic_functions.attack_fish_mob_1()
                    time.sleep(0.5)
                    graphic_functions.attack_fish_mob_2()
                    time.sleep(0.5)
                    mh=0 #set mob health to 0; gets rid of negatives
                    print("Health of mob: 0")
                    time.sleep(1)
                    break
            elif(choice=="heal"):#if input is heal
                check=inventory.count("coffee") #check inventory for coffee
                if(check>0): #if there is coffee in inventory
                    graphic_functions.boat_coffee_heal()
                    print("You're in luck! You have", check, "coffee!")
                    time.sleep(1)
                    mch=mch+20 #add 20 HP to existing health
                    inventory.remove("coffee") #remove one coffee from inventory
                    time.sleep(1)
                    print("You used 1 coffee!")
                    time.sleep(1)
                    print("Your health is now: ", mch)
                    time.sleep(1)
                elif(check==0): #if there is no coffee in inventory
                    print("Oh no! You don't have any coffee! Better buy some from Mushu later!")
                    time.sleep(1)
        elif((i==3) and (mh>0)):#if it is your third turn and the mob is still alive
            if(choice=="attack"): #if they enter attack its critical hit
                print("Critical hit!") #doesn't print
                time.sleep(1)
                mcdamage_alt=(mcdamage*2) #critical hit damage is normal damage times two
                mh=mh-mcdamage_alt #critical damage subtracted from mob health
                if(mh>0): #if mob is still alive
                    graphic_functions.attack_fish_mob_1()
                    time.sleep(0.5)
                    graphic_functions.attack_fish_mob_2()
                    time.sleep(0.5)
                    print("Health of mob: ",mh) #print mob health
                    time.sleep(1)
                elif(mh<=0): #if mob is dead
                    graphic_functions.attack_fish_mob_1()
                    time.sleep(0.5)
                    graphic_functions.attack_fish_mob_2()
                    time.sleep(0.5)
                    mh=0 #set mob health to 0; gets rid of negatives
                    print("Health of mob: 0") #print mob health
                    time.sleep(1)
                i=0 #set i (# of turns) to 0 to renew critical hit
            elif(choice=="heal"): #if third turn they enter heal; critical hit chance is lost
                check=inventory.count("coffee") #check inventory for coffee
                if(check>0): #if inventory has coffee
                    graphic_functions.boat_coffee_heal()
                    print("You're in luck! You have", check, "coffee!")
                    time.sleep(1)
                    mch=mch+20 #add 20 HP to existing MC health
                    inventory.remove("coffee") #remove one coffee from inventory
                    time.sleep(1)
                    print("You used 1 coffee!")
                    time.sleep(1)
                    print("Your health is now: ", mch) #print new health
                    time.sleep(1)
                elif(check==0): #if there is no coffee in inventory
                    print("Oh no! You don't have any coffee! Better buy some from Mushu later!") #no coffee dialogue appears
                    time.sleep(1)
                i=0 #set i (# of turns) to 0 to renew critical hit
        if(mh>0):#if mob is alive after you attack, mob attacks
            graphic_functions.fish_attack() 
            print("The mob attacked!")
            time.sleep(1)
            mch=mch-mobdamage #mob damage subtracted from mc health
            if(mch<=0): #if mc is dead after mob attacks
                mch=0 #set mc health to 0; gets rid of negatives
                print("Health: 0") #print health
                time.sleep(1)
                break #break out of while loop (you can no longer attack)
            elif(mch>0): #if mc is still alive after mob attack
                print("Health: ",mch)#print health
                time.sleep(1)
                choice=input("Will you \\attack\\ or \\heal\\?: ") #reset turn input
                choice=choice.lower() #lowercase everything to fit conditions
                mcdamage=random.randint(20,30) #randomize mc damage for the new turn
                mobdamage=random.randint(12,22) #randomize mob damage for the new turn
    if(mch<=0): #if mc is dead
        graphic_functions.dead_man_fish()
        exit() #exit program
    elif(mh<=0): #if mob is dead
        graphic_functions.dead_fish_mob()
        time.sleep(1)
        loot_variable=random.randint(18,25) #randomize Julles (money) drop for defeating the mob
        print("Here is", loot_variable, "julles for defeating the monster!")
        time.sleep(1)
        balance=balance+loot_variable #add Julles drop to balance
        print("Balance: ",balance) #print new balance

platform() #refer to above
x=0 #makes sure that you do not enter travelling cart if you entered continue
tc=0 
basic_choice=input("What is your decision?: ") #continue or go to travelling cart
basic_choice=basic_choice.lower() #lowercase to fit conditions
while(True): #while something is inputted (always goes into while loop)
    for tc in range(1,3): #keep track of how many times you enter scene
        if(basic_choice=="travelling cart"): #if they enter travelling cart
            #############################TRAVELING CART #2 #################################
            if(tc==1): #first time visiting
                graphic_functions.travelling_cart()
                input("Mushu: Welcome to the travelling cart! How was your last battle?: ")
                print("Mushu: Thats great! Would you like to buy some coffee? It costs 20 julles")
                time.sleep(1)
                print("Your inventory is:", inventory)
                time.sleep(1)
                print("Your balance is: ", balance)
                time.sleep(1)
                store_choice=input("Yes or No?: ") #yes or no to buying coffee
                store_choice=store_choice.lower() #lowercase to fit conditions
                while(True): #while something is inputted (always goes into while loop)
                    if((store_choice!="no") and (store_choice!="yes")): #if they did not enter yes or no
                        store_choice=input("Mushu: I didn't quite get that. Can you say that again?: ") #prompt to re-input
                    elif(store_choice=="yes"): #if store choice is yes (coffee)
                        if(balance>=20): #if balance is bigger or equal to 20
                            balance=balance-20 #subtract coffee price from balance
                            print("You have purchased 1 coffee")
                            time.sleep(1)
                            inventory.append("coffee") #add coffee to inventory
                            print("Inventory:",inventory) #print inventory
                            time.sleep(1)
                            print("Your balance is now: ", balance) #print balance
                            time.sleep(1)
                        else: #if you don't have enough money
                            print("Oh no! you dont have enough julles! Go fight some mobs to gain more.") #no money dialogue
                            time.sleep(1)
                        x=1 #you entered travelling cart so x now equals 1   
                        break #break out of store choice while loop (coffee)
                    elif(store_choice=="no"): #if you say no to coffee
                        print("Mushu: No? That's okay. I won't take it personally.") #dialogue
                        x=1  #you entered travelling cart so x now equals 1
                        time.sleep(1)
                        break #break out of store choice while loop (coffee)
                print("Mushu: Anyways, thanks for visiting the store! I hope to see you soon!") #exit travelling cart
                time.sleep(1)
            elif(tc==2): #second time entering travelling cart
                graphic_functions.travelling_cart_night_1()
                time.sleep(5)
                graphic_functions.travelling_cart_night_2()
                time.sleep(2)
                print(mc,": Where did Mushu go?") #dialogue
                time.sleep(1)
                print(mc,": It's so dark...")
                break #break out of travelling cart while loop
        elif((basic_choice!="continue") and (basic_choice!="travelling cart")): #if they do not say continue or travelling cart, prompt to re-enter
            basic_choice=input("I didn't quite get that. Can you say that again?: ")
            break #break out of while loop
        elif(basic_choice=="continue"):
            print("Okay! Let's hope you don't run into any more mobs!") #dialogue
            break #break out of travelling cart loop
        platform() #refer to above
        x=0 #reset x (travelling cart visits) to 0
        basic_choice=input("What is your decision?: ")
        basic_choice=basic_choice.lower()
            
    if(tc>=2):
        break #break out of while loop
    if(basic_choice=="continue"):
        break #break out of while loop

############################### MUSHU FIGHT ####################################
graphic_functions.mushu_alone() #graphics
time.sleep(2)
graphic_functions.mc_and_mushu()
time.sleep(2)
print(mc,": Mushu? Is that you?") #backstory dialogue
time.sleep(2)
print("Mushu: Hello,", mc)
time.sleep(2)
print(mc,": What are you doing here Mushu? I thought you were supposed to be tending your cart.")
time.sleep(3)
print("Mushu: I've been spying on you.")
time.sleep(3)
print(mc,": What? Why?")
time.sleep(3)
print("Mushu: You see, a long time ago, your father came to my village in search of the Legendary Golden Crown.")
time.sleep(3)
print("Mushu: He never found it, but he destroyed our village looking for it.")
time.sleep(3)
print(mc,": ...I never knew.")
time.sleep(2)
print("Mushu: Well, now I'm going to get my revenge!!")
time.sleep(2)
print("Mushu: HAHAHAHAAHAHAHAHAHAHAHAHAH!!!!!")
time.sleep(4)
graphic_functions.mushu_drinking()
print(mc,": Is that the potion you were working on?")
time.sleep(4)
graphic_functions.mushu_transformation_1()
time.sleep(4)
graphic_functions.mushu_transformation_2()
time.sleep(3)
graphic_functions.mushu_transformation_3()
time.sleep(2)
graphic_functions.mushu_transformation_4()
time.sleep(1)
graphic_functions.mushu_transformation_5()
time.sleep(1)
############################# BOSS FIGHT #######################################
mh=random.randint(100,140)  #randomize mob health
mcdamage=random.randint(30,45) #randomize mc damage
mobdamage=random.randint(20,35) #randomize mob damage
print("Health: ",mch) #health of mc carries over from last battle
time.sleep(1)
print("Health of mob: ",mh)
time.sleep(1)
choice=input("Will you \\attack\\ or \\heal\\?: ") #turn choice
choice=choice.lower() #lowercase to fit conditions
while((mch>0) and (mh>0)): #while mc and mob are alive
    for i in range(1,4): #keep track of # of turns for critical hit code
        if(i<3): #if turn is less than 3 (normal code, not critical hit)
            if(choice=="attack"): #if attack is chosen
                mh=mh-mcdamage #damage is subtracted from mob health
                if(mh<=0): #if mob is dead
                    graphic_functions.attack_mushu()
                    mh=0 #set mob health to 0, gets rid of negatives
                    print("Health of mob: 0")
                    time.sleep(1)
                elif(mh>0): #if mob is alive after attack
                    graphic_functions.attack_mushu()
                    print("Health of mob: ",mh) #print mob health
                    time.sleep(1)
            elif(choice=="heal"):#if they enter heal
                check=inventory.count("coffee") #check inventory for coffee
                if(check>0): #if they have coffee
                    graphic_functions.coffee_heal()
                    print("You're in luck! You have", check, "coffee!")
                    time.sleep(1)
                    mch=mch+20 #add 20 HP to existing health
                    inventory.remove("coffee") #remove coffee from inventory
                    time.sleep(1)
                    print("You used 1 coffee!")
                    time.sleep(1)
                    print("Your health is now: ", mch) #print new health
                    time.sleep(1)
                elif(check==0): #no coffee in inventory
                    print("Oh no! You don't have any coffee! You're screwed!") #dialogue
                    time.sleep(1)

                    
        elif((i==3) and (mh>0)):#3rd turn (critical hit) and mob is still alive
            if(choice=="attack"): #if attack is chosen
                print("Critical hit!")
                time.sleep(1)
                mcdamage_alt=(mcdamage*2) #damage is doubled
                mh=mh-mcdamage_alt #subtract critical hit damage from mob health
                if(mh<=0): #if mob is dead after attack
                    graphic_functions.attack_mushu()
                    mh=0 #set mob health to 0; gets rid of negatives
                    print("Health of mob: 0")
                    time.sleep(1)
                elif(mh>0): #if mob is still alive after attack
                    graphic_functions.attack_mushu()
                    print("Health of mob: ",mh) #print health
                    time.sleep(1)
                i=0 #resets critical hit count
            elif(choice=="heal"): #if they chose heal
                check=inventory.count("coffee") #check inventory for coffee
                if(check>0): #if there is coffee
                    graphic_functions.coffee_heal()
                    print("You're in luck! You have", check, "coffee!")
                    time.sleep(1)
                    mch=mch+20 #add 20 HP to existing health
                    inventory.remove("coffee") #remove coffee from inventory
                    time.sleep(1)
                    print("You used 1 coffee!")
                    time.sleep(1)
                    print("Your health is now: ", mch)
                    time.sleep(1)
                elif(check==0): #if no coffee
                    print("Oh no! You don't have any coffee! You're screwed!") #dialogue
                    time.sleep(1)
                i=0 #reset critical hit counter
        if(mh>0):#if mob is still alive after attack
            graphic_functions.mushu_attack() 
            print("The mob attacked!")
            time.sleep(1)
            mch=mch-mobdamage#mob damage is subtracted from mc health
            if(mch<=0): #if mc is dead after attack
                mch=0 #set mc health to 0; gets rid of negatives
                print("Health: 0")
                time.sleep(1)
                break #break out of combat while loop
            elif(mch>0): #if mc is still alive after attack
                print("Health: ",mch) #print health
                time.sleep(1)
                choice=input("Will you \\attack\\ or \\heal\\?: ") #reset turn
                choice=choice.lower() #lowercase to fit conditions
                mcdamage=random.randint(30,45) #randomize mc damage for new turn
                mobdamage=random.randint(20,35) #randomize mob damage for new turn
    if(mch<=0): #if mc is dead
        graphic_functions.final_defeat_1() #graphics
        time.sleep(2)
        graphic_functions.final_defeat_2()
        time.sleep(2)
        graphic_functions.final_defeat_3()
        time.sleep(2)
        graphic_functions.defeat_statement()
        time.sleep(2)
    elif(mh<=0): #if mob is dead
        graphic_functions.final_victory_1() #graphics
        time.sleep(2)
        graphic_functions.final_victory_2()
        time.sleep(2)
        graphic_functions.final_victory_3()
        time.sleep(2)
        graphic_functions.final_victory_4()
        time.sleep(2)
        graphic_functions.victory_statement()
        time.sleep(2)
        print("Mushu is dead!! Yay!!") #dialogue
        time.sleep(2)
        print("You beat the game!!!! Congratulations!!!")
        time.sleep(2)
        balance=balance+1000000434 #Mushu loot drop add to balance
        print("Here's 1000000434 julles for beating the game!!!")
        time.sleep(2)
        print("You can't spend them, the game is over, but you have a shiny new crown!")
        time.sleep(3)
        graphic_functions.end_screen()
        print("Thank you for playing!")

########### HOW TO WIN ###############
# do NOT heal during the last level, it's a waste of a turn, instead use your first coffee in the first level, then purchase another and use it in the second where the damage done to the MC is much smaller
# every third turn for the MC is a critical hit, where MC damage is doubled, so make sure to always attack the third time
# have fun!!!!
