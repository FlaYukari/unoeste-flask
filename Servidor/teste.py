from Modelo.Pet import Pet
from Persistencia.PetBD import PetBD

meuPet = Pet(0, "Simba", "Canina", "york", "preta", "01/01/2022", "000", "001")

petBD = PetBD()
petBD.incluir(meuPet)
print("O código gerado foi " + str(meuPet.codigo))