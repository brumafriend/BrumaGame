import random
import time
import os

def start():
    us = 1
    uk = 1
    fr = 1
    ge = 1
    ru = 1
    sp = 1
    army = 5000
    population = 25000
    tension = 10
    money = 50000
    pol = 1
    comm = 0
    lib = 0
    con = 0
    xxx = 100
    while True:
        command = input("Type a command: ")
        if command == "!help":
            print("")
            print("!army - view size of army")
            print("!population - view size of population")
            print("!money - view your country's treasury")
            print("!war - go to war")
            print("!tension - view country's tension")
            print("!conscript - conscript people into the army")
            print("!explore - explore the world")
            print("!buy - buy more soldiers")
            print("!parade - hold a parade")
            print("!tax - tax your population")
            print("!politics - give your country a political belief")
            print("")

        elif command == "!politics":
            print("")
            if pol == 1:
                print("Your country currently has no political belief.")
                time.sleep(0.2)
                print("You may change your political belief once, and only once.")
                time.sleep(0.2)
                print("What political belief would you like your party to adpot?")
                time.sleep(0.1)
                print("1 = Liberal - lower chance of civil war")
                print("2 = Conservative - lower tension increases")
                print("3 = Communist - army has higher chance to win wars")
                pchoice = input("")
                if pchoice == "1":
                    b = "Liberal"
                    lib = lib + 5
                    pol = 0
                    print("Your country is now liberal!")
                    time.sleep(0.2)
                    print("as a result, the chance of a civil war breaking out is 5% less.")
                    print("")
                elif pchoice == "2":
                    b = "Conservative"
                    con = con + 5
                    pol = 0
                    print("Your country is now conservative!")
                    time.sleep(0.2)
                    print("As a result of this, tension increase is lowered by 5%.")
                    print("")
                elif pchoice == "3":
                    b = "Communist"
                    comm = comm + 5
                    pol = 0
                    print("Your country is now communist!")
                    time.sleep(0.2)
                    print("As a result, your chance of winning any war is 5% higher than usual.")
                    print("")
            else:
                print("You country is currently %s." % b)        
            
        elif command == "!tax":
            print("Taxing your population can help raise funds for war, but also causes increased tension")
            time.sleep(0.5)
            print("For every person taxed, you gain $1 but tension will rise.")
            time.sleep(0.5)
            print("How many people would you like to tax?")
            print("1 = Your entire population")
            print("2 = Half of your population")
            tax = input("")
            if tax == "1":
                print("You have taxed your entire population.")
                time.sleep(0.1)
                wholemoney = population*0.15
                print("As a result, you have raised $%d." % wholemoney)
                money = money + wholemoney
                time.sleep(0.5)
                tensionincrease = (population)*0.00092
                print("However, tension has also increased by %d percent." % tensionincrease)
                tension = tension + tensionincrease - con
            elif tax == "2":
                print("You have taxed half of your population.")
                time.sleep(0.1)
                halfmoney = (population/2)*0.15
                print("As a result you have raised $%d." % halfmoney)
                money = money + halfmoney
                time.sleep(0.5)
                tensionincrease = (population/2)*0.00092
                print("However, tension has also increased by %d percent." % tensionincrease)
                tension = tension + tensionincrease - con
            else:
                print("Incorrect command!")

        elif command == "!parade":
            print("Would you like to hold a parade? It will cost $10,000.")
            print("It will also reset your country's tension to zero percent!")
            print("1=yes/2=no")
            parade = input("")
            if parade == "1":
                money = money - 10000
                if money < 0:
                    money = money + 10000
                    print("You do not have enough money to have a parade.")
                else:
                    time.sleep(0.1)
                    print("Preparing parade...")
                    time.sleep(0.5)
                    print("Carrying out parade...")
                    time.sleep(1)
                    if random.randint(0,100) < 90:
                        print("The parade was a success!")
                        time.sleep(0.5)
                        print("Your country's tension is now zero percent!")
                        tension = 0
                        time.sleep(0.5)
                        print("Following the parade, a visting group of 100 civilians have decided to live in %s!" % country)
                    else:
                        print("The parade was a disaster!")
                        time.sleep(0.5)
                        print("All the parade did was show off your frivolous spenging habits!")
                        time.sleep(1)
                        print("Tension in your country has risen by 51%! A civil war is possible!")
                        tension = tension + 51 - con
                        time.sleep(0.5)
                        print("Furthermore, the country of %s lies in ruins! You lose an additional $10,000." % country)                
                        money = money - 10000
                        if money < 0:
                            money = 0
                        else:
                            continue

            else:
                print("")

        elif command == "!buy":
            print("What would you like to buy?")
            time.sleep(0.5)
            print("1 = 100 soldiers for $500")
            print("2 = 1000 soldiers for $5,000")
            print("3 = 1500 soldiers for $7,000")
            print("4 = 2000 soldiers for $9,500")
            print("5 = 5000 soldiers for $20,000")
            buy = input("")
            if buy == "1":
                print("You have purchased 100 soldiers.")
                army = army + 100
                money = money - 500
                if money < 0:
                    print("No money. Could not purchase soldiers.")
                    money = money + 500
                    army = army - 100
            elif buy == "2":
                print("You have purchased 1000 soldiers.")
                army = army + 1000
                money = money - 5000
                if money < 0:
                    print("No money. Could not purchase soldiers.")
                    money = money + 5000
                    army = army - 1000
            elif buy == "3":
                print("You have purchased 1500 soldiers.")
                army = army + 1500
                money = money - 7000
                if money < 0:
                    print("No money. Could not purchase soldiers.")
                    money = money + 7000
                    army = army - 1500
            elif buy == "4":
                print("You have purchased 2000 soldiers.")
                army = army + 2000
                money = money - 9500
                if money < 0:
                    print("No money. Could not purchase soldiers.")
                    money = money + 9500
                    army = army - 2000
            elif buy == "5":
                print("You have purchased 5000 soldiers")
                army = army + 5000
                money = money - 20000
                if money < 0:
                    print("No money. Could not purchase soldiers.")
                    money = money + 20000
                    army = army - 5000
            else:
                print("Incorrect command!")

        elif command == "!money":
            print("Your country has $%d" % money)

        elif command == "!explore":
            print("Are you sure you would like to explore the world?")
            print("You have the chance to find soldiers and people, but it could end in disaster.")
            print("1=yes/2=no")
            explore = input("")
            if explore == "1":
                if population < 400 or army < 100:
                    print("Can not explore with this few people! Your population must be at least 400 your army must contain at least 100 soldiers.")
                else:
                    print("Sending 500 people to explore...")
                    time.sleep(0.5)
                    print("Exploring...")
                    time.sleep(1)
                    if random.randint(0,100) < 60:
                        print('Success!')
                        if random.randint(0,100) < 75:
                            print('You have found 200 people, 100 soldiers and $200!')
                            money = money + 200
                            print("Following this success, your country's tension has decreased by 2 percent.")
                            army = army + 100
                            population = population + 200
                            tension = tension - 2
                            if tension < 0:
                                tension = 0
                            
                        else:
                            print("It's a miracle! You've stumbled across a group of 1000 soldiers and $2,500!")
                            money = money + 2500
                            print("Follow this success, your country's tension has decreased by 15 percent.")
                            army = army + 1000
                            tension = tension - 15
                            if tension < 0:
                                tension = 0
                        
                    else:
                        print('It was a disaster!')
                        print('You have lost 400 civilians and 100 soldiers!')
                        print("You have also lost $500.")
                        print("Your country's tension has increased by 20%.")
                        money = money - 500
                        army = army - 100
                        population = population - 400
                        tension = tension + 20 - con
                
            if explore == "2":
                print("")

        elif command == "!conscript":
            print('How many people would you like to conscript?')
            print('(1000 people conscripted = tension increase of 10%)')
            try:
                cons = int(input(""))
            except ValueError:
                print("Incorrect command!")
                cons = 0
            if cons > population:
                print("Can't conscript more people than live in your country.")
            elif cons < 100 and con > 0:
                print("You must conscript more than 100 people.")
            elif cons + army > 10000:
                print("You can only conscript soldiers such that your army has 10000 troops!")
                time.sleep(0.5)
                cons = 10000 - army
                army = army + cons
                print("%d people have been conscripted." % cons)
                tension = tension + (cons/1000)
            else:
                army = army + cons
                population = population - cons
                tension = tension + (cons/1000)
                print("You have conscripted %d people" % cons)
                print("Your population is now %d" % population)
                print("Your tension is now %d percent" % tension)
            
        elif command == "!army":
            print("The size of your army is %d" % army)
            
        elif command == "!population":
            print("The population of your country is %d" % population)
            
        elif command == "!war":
            print("Which country would you like to go to war with?")
            time.sleep(0.1)
            print("1 = United States of America")
            print("2 = United Kingdom")
            print("3 = France")
            print("4 = Germany")
            print("5 = Russia")
            print("6 = Spain")
            target = input("")
            if target == "1":
                if us == 1:
                    victory = (army/(army + 10000)*100) + comm
                    print("The USA has an army of 10,000 men. Your chance of winning is %d percent." % victory)
                    time.sleep(0.5)
                    print("Would you like to go to war with the USA?")
                    print("1=yes/2=no")
                    answer = input("")
                    if answer == "1":
                        print("Your troops are travelling to America...")
                        time.sleep(1)
                        print("Your troops are fighting...")
                        time.sleep(1)
                        if random.randint(0,100) < victory:
                            us = 0
                            print('Success! Your troops defeated the opposition soldiers!')
                            print('You were also able to convert 2,000 enemy soldiers!')
                            army = army + 2000
                            print("Your net profit from the war was $5000.")
                            money = money + 5000
                            print("As a result of your success, your country's tension has decreased by 5%.")
                            tension = tension - 5
                            if tension < 0:
                                tension = 0
                            else:
                                continue
                        else:
                            army = army*0.69
                            print('Failure! Your troops were defeated, %d men escaped.' % army)
                            print("As a result of your failure, your country's tension has increased by 10%")
                            tension = tension + 10
                            time.sleep(1)
                            print("The defeat cost you $500")
                            money = money - 500
                    else:
                        print("")
                        
                else:
                    print("You have already conquered the USA!")
                         
            if target == "2":
                if uk == 1:
                    victory = (army/(army + 7500)*100) + comm
                    print("The UK has an army of 7,500 men. Your chance of winning is %d percent." % victory)
                    time.sleep(0.5)
                    print("Would you like to go to war with the UK?")
                    print("1=yes/2=no")
                    answer = input("")
                    if answer == "1":
                        print("Your troops are travelling to the UK...")
                        time.sleep(1)
                        print("Your troops are fighting...")
                        time.sleep(1)
                        if random.randint(0,100) < victory:
                            uk = 0
                            print('Success! Your troops defeated the opposition soldiers!')
                            print('You were also able to convert 1,500 enemy soldiers!')
                            army = army + 1500
                            print("Your net profit from the war was $4500.")
                            money = money + 4500
                            print("As a result of your success, your country's tension has decreased by 4%.")
                            tension = tension - 4
                            if tension < 0:
                                tension = 0
                            else:
                                continue
                        else:
                            army = army*0.6
                            print('Failure! Your troops were defeated, %d men escaped.' % army)
                            print("As a result of your failure, your country's tension has increased by 10%")
                            tension = tension + 10 - con
                            time.sleep(1)
                            print("The defeat cost you $500")
                            money = money - 500
                    
                    else:
                        print("")
                else:
                    print("You have already conquered the UK!")
            if target == "3":
                victory = (army/(army + 5000)*100) + comm
                print("France has an army of 5,000 men. Your chance of winning is %d percent." % victory)
                time.sleep(0.5)
                print("Would you like to go to war with France?")
                print("1=yes/2=no")
                answer = input("")
                if answer == "1":
                    if fr == 1:
                        print("Your troops are travelling to France...")
                        time.sleep(1)
                        print("Your troops are fighting...")
                        time.sleep(1)
                        if random.randint(0,100) < victory:
                            fr = 0
                            print('Success! Your troops defeated the opposition soldiers!')
                            print('You were also able to convert 1000 enemy soldiers!')
                            army = army + 1000
                            print("Your net profit from the war was $4000.")
                            money = money + 4000
                            print("As a result of your success, your country's tension has decreased by 3%.")
                            tension = tension - 3
                            if tension < 0:
                                tension = 0
                            else:
                                continue
                        else:
                            army = army*0.63
                            print('Failure! Your troops were defeated, %d men escaped.' % army)
                            print("As a result of your failure, your country's tension has increased by 12%")
                            tension = tension + 12 - con
                            time.sleep(1)
                            print("The defeat cost you $500")
                            money = money - 500
                    
                    else:
                        print("You have already conquered France!")
                else:
                    print("")
                    
            if target == "4":
                victory = (army/(army + 4500)*100) + comm
                print("Germany has an army of 4,500 men. Your chance of winning is %d percent." % victory)
                time.sleep(0.5)
                print("Would you like to go to war with Germany?")
                print("1=yes/2=no")
                answer = input("")
                if answer == "1":
                    if ge == 1:
                        print("Your troops are travelling to Germany...")
                        time.sleep(1)
                        print("Your troops are fighting...")
                        time.sleep(1)
                        if random.randint(0,100) < victory:
                            ge = 0
                            print('Success! Your troops defeated the opposition soldiers!')
                            print('You were also able to convert 750 enemy soldiers!')
                            army = army + 750
                            print("Your net profit from the war was $2000.")
                            money = money + 2000
                            print("As a result of your success, your country's tension has decreased by 2%.")
                            tension = tension - 2
                            if tension < 0:
                                tension = 0
                            else:
                                continue
                        else:
                            army = army*0.62
                            print('Failure! Your troops were defeated, %d men escaped.' % army)
                            print("As a result of your failure, your country's tension has increased by 14%")
                            tension = tension + 14 - con
                            time.sleep(1)
                            print("The defeat cost you $500")
                            money = money - 500
                    else:
                        print("You have already conquered Germany!")
               
                else:
                    print("")
                    
            if target == "5":
                if uk + ge + fr + us + sp == 5:
                    print("You must defeat at least one country before attacking Russia")
                else:
                    victory = (army/(army + 50000)*100) + comm
                    print("Russia has an army of 50000 men. Your chance of winning is %d percent." % victory)
                    time.sleep(0.5)
                    print("Would you like to go to war with Russia?")
                    print("1=yes/2=no")
                    answer = int(input(""))
                    if answer == 1:
                        if ru == 1:
                            print("Your troops are travelling to Russia...")
                            time.sleep(1)
                            print("Your troops are fighting...")
                            time.sleep(1)
                            if random.randint(0,100) < victory:
                                ru = 0
                                print('Success! Your troops defeated the opposition soldiers!')
                                print('You were also able to convert 7500 enemy soldiers!')
                                army = army + 7500
                                print("Your net profit from the war was $15000.")
                                money = money + 25000
                                print("As a result of your success, your country's tension has decreased by 15%.")
                                tension = tension - 15
                                if tension < 0:
                                    tension = 0
                                else:
                                    continue
                            else:
                                army = army*0.51
                                print('Failure! Your troops were defeated, %d men escaped.' % army)
                                print("As a result of your failure, your country's tension has increased by 15%")
                                tension = tension + 15 - con
                                time.sleep(1)
                                print("The defeat cost you $3500")
                                money = money - 3500
                        else:
                            print("You have already conquered Russia!")
                            
            if target == "6":
                victory = (army/(army + 8500)*100) + comm
                print("Spain has an army of 8500 men. Your chance of winning is %d percent." % victory)
                time.sleep(0.5)
                print("Would you like to go to war with Spain?")
                print("1=yes/2=no")
                answer = int(input(""))
                if answer == 1:
                    if sp == 1:
                        print("Your troops are travelling to Spain...")
                        time.sleep(1)
                        print("Your troops are fighting...")
                        time.sleep(1)
                        if random.randint(0,100) < victory:
                            sp = 0
                            print('Success! Your troops defeated the opposition soldiers!')
                            print('You were also able to convert 1750 enemy soldiers!')
                            army = army + 1750
                            print("Your net profit from the war was $15500.")
                            money = money + 11500
                            print("As a result of your success, your country's tension has decreased by 12%.")
                            tension = tension - 12
                            if tension < 0:
                                tension = 0
                            else:
                                continue
                        else:
                            army = army*0.61
                            print('Failure! Your troops were defeated, %d men escaped.' % army)
                            print("As a result of your failure, your country's tension has increased by 16%")
                            tension = tension + 16 - con
                            time.sleep(1)
                            print("The defeat cost you $2500")
                            money = money - 2500
                    else:
                        print("You have already conquered Spain!")                
             
            
        elif command == "!tension":
            print("Your country's tension is %d percent" % tension)
            time.sleep(0.1)
            print("A country's tension goes up if a war is lost.")
            print("A country's tension goes down if a war is won.")
            print("If a country's tension is above 50%, a civil war may begin.")
            
        else:
            print("Incorrect command!")

        if money < 0:
            time.sleep(1)
            print("You have no money!")
            money = 0

        if army < 100 or population < 0:
            print("You have lost all military influence")
            print("Your civilians have fled and your army has turned against you.")
            time.sleep(2)
            print("Game Over.")
            time.sleep(5)
            Return

        if tension < 0:
            tension = 0
            
        if tension > 20 and tension < 25:
            time.sleep(1.5)
            if random.randint(0,100) < 5:
                print("")
                print("A revolt has broken out amongst your population due to high tension")
                print("In putting down the revolt, you have lost 100 soldiers.")
                army -= 100
                population -= 10
                print("")
                
        if tension >= 25 and tension <= 50:
            time.sleep(1.5)
            if random.randint(0,100) < 10:
                print("")
                print("A revolt has broken out amongst your population due to high tension.")
                print("In putting down the revolt, you have lost 200 soldiers.")
                army -= 200
                population -=100
                print("")
        
        if tension > 50:
            time.sleep(1)
            print("Your tension is now above 50 percent! There is a chance of civil war.")
            if random.randint(0,100) < (40 - lib):
                time.sleep(2)
                print('Civil war! The country has turned against you!')
                if random.randint(0,100) < 60:
                    time.sleep(1)
                    print('The uprising has been put down. Sadly, half of your soldiers have died and 5000 civiliands have fled')
                    time.sleep(1)
                    print("Following the war, your country's tension is down to 10 percent.")
                    tension = 10
                    army = army/2
                    population = population - 5000
                else:
                    time.sleep(1)
                    print('The uprising could not be put down!')
                    time.sleep(0.2)
                    if random.randint(0,100) < 25:
                        print("Luckily, you managed to escape with a tenth of your army and 400 civilians.")
                        uk = 1
                        us = 1
                        fr = 1
                        ru = 1
                        ge = 1
                        sp = 1
                        tension = 0
                        population = 400
                        army = army/10
                    else:
                        print("You have lost everything and everyone. You are captured and sentenced to death.")
                        print("Game over.")
                        time.sleep(5)
                        print("New game:")
                        start()                
            else:
                time.sleep(3)
                print('There was no civil war. For now.')
                time.sleep(2)
                print("Your country's tension is now 35 percent.")
                tension = 35
                
        if ru + ge + uk + us + fr + sp == 0:
            time.sleep(1)
            print("As the dust of war settles, %s has come out on top." % country)
            time.sleep(0.2)
            print("You have captured all known enemy land and the rest of the world lives to fear your name.")
            time.sleep(2)
            print("YOU HAVE WON, CONGRATULATIONS!")
            time.sleep(5)
            Return

country = input("Please enter the name of your country: ")
time.sleep(0.5)

print("Your country is called %s" % country)
time.sleep(0.5)
print("")
print("Type !help to see commands")
start()
