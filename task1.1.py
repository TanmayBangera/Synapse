
from itertools import combinations as comb

result = []
Kevin = {"Halsey", "Taylor Swift", "Mitski","Joji","Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"}

Stuart = {"Kendrik Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeekend", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}

Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrik Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}

Edith = {"Metallica", "Billie Eilish", "TheWeekend", "Mitski", "NF", "Conan Gray", "Kendrik Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}


Dj = ['Kevin', 'Stuart', 'Bob', 'Edith']
DjObject = [Kevin, Stuart, Bob, Edith]

DjName = []
for name1, name2 in comb(Dj, 2): 
    DjName.append(f"{name1} and {name2}")


intersect = []
for item1, item2 in comb(DjObject, 2):
    value = ((len(item1.intersection(item2))/10)*100)
    intersect.append(value)


output = list(zip(DjName, intersect))
output = sorted(output, key=lambda x: x[1], reverse=True)
print(output)


# Output: 

#    [('Kevin and Bob', 40.0), 
#    ('Stuart and Bob', 40.0), 
#    ('Stuart and Edith', 40.0), 
#    ('Bob and Edith', 40.0), 
#    ('Kevin and Edith', 30.0), 
#    ('Kevin and Stuart', 10.0)]



