nbrkarva = int(input())
data = []

for i in range(nbrkarva):
    poids = int(input())
    age = int(input())
    cornes = int(input())
    hauteur = int(input())
    data.append((cornes*hauteur)+poids)

for j in range(nbrkarva):
    print(data[j])