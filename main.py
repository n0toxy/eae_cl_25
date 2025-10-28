def main():
    print("Hello from eae-cl-25!")

class MaClasse:
    def __init__(self, nom, age):
        self.nom = nom  # on stocke un attribut propre à chaque objet
        self.age = age  # on stocke un attribut propre à chaque objet
        self._parametretest = 1.2

    def parametretest(self):
        return self._parametretest
    
    def direbonjour(self):
        return f"Bonjour, je suis {self.nom} et j'ai {self.age*self.parametretest()} ans!"

    def direbonjoura(self,nom):
        return f"Bonjour {nom}, je suis {self.nom}"

if __name__ == "__main__":
    main()
    a = MaClasse("Alice",25)
    b = MaClasse("Bob",58)
    print(a.direbonjour())
    print(b.direbonjour())
    print(b.direbonjoura("chuck"))