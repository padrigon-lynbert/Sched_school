'''
it was a <adjective> summer day. <noun> and I are excited to go camping at <place>.
It was my first time going there. I packed my favorite <type of clothing>.
It is <adjective> and <adjective> Perfect for camping! On the road we went on 
our <adjective>, <adjective> van. I could smell <food> being cooked. It smelled <adjective>.
I [past tense verb] in the bed. I heard my mom scream, "Get off the bed" I [past tense verb] outside.
I saw [noun]. It was [noun]. Over the next few days I got to [ver] [verb] and [verb].
My camping trip was [adjective]
'''
import os

lst = list()
prompt = ["Adjective", "Place",
          "Type of Clothing",
          "adjective", "Adjective",
          "Adjective", "Adjective", "Food", "Adjective",
          "Past tense verb", "Past tense verb",
          "noun", "noun", "verb", "verb", "verb",
          "Adjective"]

[lst.append(input(f"{n}: ")) for n in prompt]

os.system('cls')

print(f"it was a {lst[0]} summer day. {lst[1]} and I are excited to go camping at {lst[2]}.\n\
It was my first time going there. I packed my favorite {lst[3]}.\n\
It is {lst[4]} and {lst[5]} Perfect for camping! On the road we went on\n\
our {lst[6]}, {lst[7]} van. I could smell {lst[8]} being cooked. It smelled {lst[9]}.\n\
I {lst[10]} in the bed. I heard my mom scream, \"Get off the bed\" I {lst[11]} outside.\n\
I saw {lst[12]}. It was {lst[13]}. Over the next few days I got to {lst[14]}, {lst[15]} and {lst[16]}.\n\
My camping trip was {lst[16]}.")
