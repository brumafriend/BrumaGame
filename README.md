# BrumaGame
A game
Made with python3, also it's a "console game" AKA all text.


How the game works:  
You have an army and a population, which number 5000 and 25000 respectively. Your population does not include soldiers. The aim is to conquer all of the 5 of the other countries there are right now: UK, USA, France, Germany and Russia.

You can lose in two ways. Firstly, if your population & army is so small that you can't win any war or explore to find more soldiers. Secondly, and most importantly, through **tension**:

Tension starts at 10%.  
Winning a war decreases tension.  
Losing a war increases tension.  
If tension is > 50% there is a chance there may be a civil war which can defeat you or severely damage your army and population numbers.

The mechanics:

**Conscription**: Conscription can allow you to add to an army's numbers by recruiting civilians. Your army can only get to 10,000 members through conscription and for each 1000 people conscripted, **tension** rises by 10%.

**Exploring**: You need 400 civs and 100 soldiers to explore. Exploring can result in gaining civilians and soldiers, this also decreases tension. It can also result in disaster - making you lose the people sent out and causing an increase in tension of 20%.

**War**: The most important aspect of the game is war. Waging war against another country is simple; winning is not. Your chance to win is (x/y)*50 with x being your troops and y being the enemy's. So, if you have equal numbers then there's a 50% chance you win. Upon winning, tension is decreased and you gain troops. You can't attack the same country twice. Upon losing, tension increases and you lose half of your troops. You can try to attack the country again at a later date.

**Money**: Money can be used to purchase soldiers. In a desperate situation? Buy your way out of it! You start with $50,000. Winning wars earns you money, losing wars loses you money. Money can also be earned by exploring.

**Parades**: Country tension too high? Have some fun! A parade costs $10,000 but it will reset your tension to zero percent, giving you a second chance at retaining authority! A parade does not come without risk. There is a 5% chance that the parade will end in disaster, causing a 51% increase in tension (meaning a civil war is possible) and costing you an extra $10,000!

**Tax:** (as of 20/11/2017) Low on money? Tax people. Not surprisingly, taxation isn't popular and, whilst raising funds for war, will also result in a huge increase in tension. Taxation should only really be used in emergencies or if you have a very low level of tension. For each person taxed, you gain $1. The tension increase per tax is: (n)*0.00092 with _n_ being the number of people taxed.
