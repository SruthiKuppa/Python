#spilting a string

songLyric="""Once the flight had flown
With the wilt of the rose
I slept all alone
You still wouldn’t go
Let’s fast forward to three hundred takeout coffees later
I see your profile and your smile on unsuspecting waiters
You dream of my mouth before it called you a lying traitor
You search in every maiden’s bed for something greater

Baby, was it over
When she laid down on your couch?
Was it over when he unbuttoned my blouse?
“Come here,” I whispered in your ear
In your dream as you passed out, baby
Was it over then?

I’m not sure if I’m ready for this"""


#print(songLyric)
print("Song has: ",len(songLyric),"words")
print(songLyric.split())

word_count= {}

for word in songLyric.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1
print(word_count)

