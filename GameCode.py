import random
import time
import os

def start():
    us = 1
    uk = 1
    fr = 1
    ge = 1
    ru = 1
    army = 500000000 
    population = 25000
    tension = 10
    xxx = 100
    while True:
        command = input("Type a command: ")
        if command == "!help":
            print("!army - view size of army")
            print("!population - view size of population")
            print("!war - go to war")
            print("!tension - view country's tension")
            print("!conscript - conscript people into the army")
            print("!explore - explore the world")

        elif command == "!explore":
            print("Are you sure you would like to explore the world?")
            print("You have the chance to find soldiers and people, but it could end in disaster.")
            print("1=yes/2=no")
            explore = int(input(""))
            if explore == 1:
                if population < 400 or army < 100:
                    print("Can not explore with this few people!")
                else:
                    print("Sending 500 people to explore...")
                    time.sleep(0.5)
                    print("Exploring...")
                    time.sleep(1)
                    if random.randint(0,100) < 60:
                        print('Success!')
                        if random.randint(0,100) < 75:
                            print('You have found 200 people and 100 soldiers!')
                            print("Following this success, your country's tension has decreased by 4 percent.")
                            army = army + 100
                            population = population + 200
                            tension = tension - 4
                            if tension < 0:
                                tension = 0
                            
                        else:
                            print("It's a miracle! You've stumbled across a group of 1000 soldiers!")
                            print("Follow this success, your country's tension has decreased by 15 percent.")
                            army = army + 1000
                            tension = tension - 15
                            if tension < 0:
                                tension = 0
                        
                    else:
                        print('It was a disaster!')
                        print('You have lost 400 civilians and 100 soldiers!')
                        print("Your country's tension has increased by 20%.")
                        army = army - 100
                        population = population - 400
                        tension = tension + 20
                
            if explore == 2:
                print("")

        elif command == "!conscript":
            print('How many people would you like to conscript?')
            print('(1000 people conscripted = tension increase of 10%)')
            con = int(input(""))
            if con > population:
                print("Can't conscript more people than live in your country.")
            elif con < 100:
                print("You must conscript more than 100 people.")
            elif con + army > 10000:
                print("You can only conscript up to 10000 troops!")
            else:
                army = army + con
                population = population - con
                tension = tension + (con/1000)
                print("You have conscripted %d people" % con)
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
            target = input("")
            if target == "1":
                if us == 1:
                    victory = ((army/10000)*50)
                    print("The USA has an army of 10,000 men. Your chance of winning is %d percent." % victory)
                    time.sleep(0.5)
                    print("Would you like to go to war with the USA?")
                    print("1=yes/2=no")
                    answer = int(input(""))
                    if answer == 1:
                        print("Your troops are travelling to America...")
                        time.sleep(1)
                        print("Your troops are fighting...")
                        time.sleep(1)
                        if random.randint(0,100) < victory:
                            us = 0
                            print('Success! Your troops defeated the opposition soldiers!')
                            print('You were also able to convert 2,000 enemy soldiers!')
                            army = army + 2000
                            print("As a result of your success, your country's tension has decreased by 5%.")
                            tension = tension - 5
                            if tension < 0:
                                tension = 0
                            else:
                                continue
                        else:
                            army = army/2
                            print('Failure! Your troops were defeated, %d men were killed.' % army)
                            print("As a result of your failure, your country's tension has increased by 6%")
                            tension = tension + 6
                else:
                    print("You have already conquered the USA!")
                         
            if target == "2":
                if uk == 1:
                    victory = ((army/7500)*50)
                    print("The UK has an army of 7,500 men. Your chance of winning is %d percent." % victory)
                    time.sleep(0.5)
                    print("Would you like to go to war with the UK?")
                    print("1=yes/2=no")
                    answer = int(input(""))
                    if answer == 1:
                        print("Your troops are travelling to the UK...")
                        time.sleep(1)
                        print("Your troops are fighting...")
                        time.sleep(1)
                        if random.randint(0,100) < victory:
                            uk = 0
                            print('Success! Your troops defeated the opposition soldiers!')
                            print('You were also able to convert 1,500 enemy soldiers!')
                            army = army + 1500
                            print("As a result of your success, your country's tension has decreased by 4%.")
                            tension = tension - 4
                            if tension < 0:
                                tension = 0
                            else:
                                continue
                        else:
                            army = army/2
                            print('Failure! Your troops were defeated, %d men were killed.' % army)
                            print("As a result of your failure, your country's tension has increased by 7%")
                            tension = tension + 7
                else:
                    print("You have already conquered the UK!")
                            
            if target == "3":
                victory = ((army/5000)*50)
                print("France has an army of 5,000 men. Your chance of winning is %d percent." % victory)
                time.sleep(0.5)
                print("Would you like to go to war with France?")
                print("1=yes/2=no")
                answer = int(input(""))
                if answer == 1:
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
                            print("As a result of your success, your country's tension has decreased by 3%.")
                            tension = tension - 3
                            if tension < 0:
                                tension = 0
                            else:
                                continue
                        else:
                            army = army/2
                            print('Failure! Your troops were defeated, %d men were killed.' % army)
                            print("As a result of your failure, your country's tension has increased by 8%")
                            tension = tension + 8
                else:
                    print("You have already conquered France!")
                    
            if target == "4":
                victory = ((army/4500)*50)
                print("Germany has an army of 4,500 men. Your chance of winning is %d percent." % victory)
                time.sleep(0.5)
                print("Would you like to go to war with Germany?")
                print("1=yes/2=no")
                answer = int(input(""))
                if answer == 1:
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
                            print("As a result of your success, your country's tension has decreased by 2%.")
                            tension = tension - 2
                            if tension < 0:
                                tension = 0
                            else:
                                continue
                        else:
                            army = army/2
                            print('Failure! Your troops were defeated, %d men were killed.' % army)
                            print("As a result of your failure, your country's tension has increased by 9%")
                            tension = tension + 9
                    else:
                        print("You have already conquered Germany!")
                    
            if target == "5":
                victory = ((army/50000)*50)
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
                            print("As a result of your success, your country's tension has decreased by 10%.")
                            tension = tension - 10
                            if tension < 0:
                                tension = 0
                            else:
                                continue
                        else:
                            army = army/1.5
                            print('Failure! Your troops were defeated, %d men were killed.' % army)
                            print("As a result of your failure, your country's tension has increased by 5%")
                            tension = tension + 5
                    else:
                        print("You have already conquered Russia!")
            
        elif command == "!tension":
            print("Your country's tension is %d percent" % tension)
            time.sleep(0.1)
            print("A country's tension goes up if a war is lost.")
            print("A country's tension goes down if a war is won.")
            print("If a country's tension is above 50%, a civil war may begin.")
            
        else:
            print("Incorrect command!")


        if tension > 50:
            time.sleep(1)
            print("Your tension is now above 50 percent! There is a chance of civil war.")
            if random.randint(0,100) < 40:
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
                    if random.randint(0,100) < 25:
                        print("Luckily, you have escaped with a tenth of your army and 400 civilians.")
                        uk = 1
                        us = 1
                        fr = 1
                        ru = 1
                        ge = 1
                        tension = 0
                        population = 400
                        army = army/10
                    else:
                        print("You have lost everything and everyone. You are captured and sentenced to death.")
                        print("Game over")
                        time.sleep(5)
                        print("New game:")
                        start()                
            else:
                time.sleep(3)
                print('There was no civil war. For now.')
                time.sleep(2)
                print("Your country's tension is now 35 percent.")
                tension = 35
                
        if ru + ge + uk + us + fr == 0:
            time.sleep(2)
            print("YOU HAVE WON, CONGRATULATIONS!")
            time.sleep(20)

country = input("Please enter the name of your country: ")
time.sleep(0.5)
os.system('cls')
print("Your country is called %s" % country)
print("")
time.sleep(0.5)
print("Type !help to see commands")
start()


   
