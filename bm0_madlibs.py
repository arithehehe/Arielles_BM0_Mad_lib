import random

story=random.randint(0,1)

print("Create your own story!")



print("input noun:")
noun=input()

print("input verb")
verb=input()

print("input adjective")
adjective=input()

if story==1:
	print(f'''
Once apon a time a {noun} whom was a mage decied to go on a long walk, 
on this walk they discovered a dragon which was {adjective}. 
This dragon looked as mighty as a shark and was as sttong as fifteen bears.
This mage knew this dragon was a large threat and slayed the dragon by {verb}
		''')
else:
	print(f'''
Before i go to bed i always {verb}, 
this action always makes me feel vary {adjective}.
I also always say goodnight to my {noun}
		''')