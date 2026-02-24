# XDE-8Ball | (c) 2026 xde-dev
# Licensed under the MIT License.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
# See LICENSE file in repository for full legal text.

import sys
import random
import time
comand=input("wellcome user, type 8ball to play 8ball game or type custom to make custom 8 ball version and to quit type quit! note: all desigions are random and not related to reality!")
if comand == "8ball":
    print("The 8-Ball is consulting the void...")
    time.sleep(2)
    print(random.choice(["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]))
    input("\npress enter to exit...")
elif comand == "custom":
    a=input("type your type first thing to roll!")
    b=input("type your type second thing to roll!")
    c=input("type your type third thing to roll!")
    d=input("type your type 4th thing to roll!")
    e=input("type your type 5th thing to roll!")
    f=input("type your type 6th thing to roll!")
    j=input("type your type 7th thing to roll!")
    h=input("type your type 8th thing to roll!")
    print("The 8-Ball is consulting the void...")
    time.sleep(2)
    print(random.choice([a, b , c , d , e , f , j , h]))
    input("\npress enter to exit...")
elif comand == "quit":
    print("bye user!")
    sys.exit
else:
    print("no right comand detected, please retry")
    input("\npress enter to exit...")