# SERVICE D'ANNUAIRE PARTAGE CLIENT/SERVEUR

from typing import NamedTuple


class User(NamedTuple):
    id: str
    mdp: str

id = input("Saisissez votre identifiant: \n")

mdp=input("Saisissez votre mot de passe: \n")

utilisateur = User(id,mdp)
data ="nom: {} / mdp: {} \n".format(utilisateur.id,utilisateur.mdp)


# opening a text file
auth = open("auth.txt", "r")
  
# setting flag and index to 0
flag = 0
index = 0
  
# Loop through the file line by line
for line in auth:  
    index += 1 
      
    # checking string is present in line or not
    if id in line:
        
      flag = 1
      break 
          
# checking condition for string found or not
if flag == 0: 
    auth = open("auth.txt","a+")
    auth.write(data)
    auth.close()
else: 
   print('String', id, 'Found In Line', index)
  
# closing text file    
auth.close() 


class Directory(NamedTuple):
    id : str
    
    class contact(NamedTuple):
        nom : str
        numero : str

    @staticmethod
    def aj_contact():
        directory = open("%s.txt"%id,"a+")
        nom = input("Saisissez le nom du contact: \n")
        numero=input("Saisissez son numero: \n")
        data ="nom: {} / numero: {} \n".format(nom,numero)
        directory.write(data)


annuaire = Directory(id)
annuaire.aj_contact()

