import mysql.connector
from os import system
import time

def clear():
	system("cls")

clear()
print("Connection à la db...")

try:
	db = mysql.connector.connect(
	  host = "localhost",
	  user = "root",
	  password = "",
	  database = "grabursubs"
	)
except:
	print("Une erreur s'est passé lors de la connexion à la db")

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS grabursubs (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), command VARCHAR(255), ppl_owner VARCHAR(255), ppl_client VARCHAR(255), price VARCHAR(255))")

print("Db connectée")
time.sleep(2)
clear()

def all_transaction():
	clear()
	cursor.execute("SELECT * FROM grabursubs")
	result = cursor.fetchall()

	for transactions in result:
		print(transactions)

	input()
	clear()
	menu()

def new_transaction():
	clear()
	sql = "INSERT INTO grabursubs (user, command, ppl_owner, ppl_client, price) VALUES (%s, %s, %s, %s, %s)"

	user_input = input("Discord du client (! MrCyci6#5054) >> ")
	command_input = input("Détail de la commande (insta = 1K) >> ")
	paypal_owner_input = input("Paypal du vendeur (@ccdiscord) >> ")
	paypal_client_input = input("Paypal du client (@pigeon) >> ")
	price_input = input("Prix du paiement (2€) >> ")
	value = (user_input, command_input, paypal_owner_input, paypal_client_input, price_input)

	cursor.execute(sql, value)
	db.commit()

	print("Transaction insérée avec succès")
	input()
	clear()
	menu()

def update_transaction():

	sql = "UPDATE grabursubs SET user = %s, command = %s, ppl_owner = %s, ppl_client = %s, price = %s WHERE id = %s"

	user_input = input("Discord du client (! MrCyci6#5054) >> ")
	command_input = input("Détail de la commande (insta = 1K) >> ")
	paypal_owner_input = input("Paypal du vendeur (@ccdiscord) >> ")
	paypal_client_input = input("Paypal du client (@pigeon) >> ")
	price_input = input("Prix du paiement (2€) >> ")
	id_input = input("ID de la transaction à modifier >>> ")
	value = (user_input, command_input, paypal_owner_input, paypal_client_input, price_input, id_input)

	cursor.execute(sql, value)
	db.commit()

	print("Transaction " + id_input + " mise à jour")
	input()
	clear()
	menu()

def delete_transaction():

	sql = "DELETE FROM grabursubs WHERE id = %s"

	id_input = input("ID de la transaction à supprimer >>> ")
	value = (id_input, )

	cursor.execute(sql, value)
	db.commit()

	print("Transaction " + id_input + " supprimée")
	input()
	clear()
	menu()

def menu():
	print("""

				 Gestion des commandes de GrabUrSubs
				    https://discord.gg/dZYVZFwUU8
				    
				      By ! MrCyci6#5054""")

	print("""

	1 - Insérer une nouvelle transaction
	2 - Lister toutes les transactions
	3 - Mettre à jour une transaction
	4 - Supprimer une transaction\n""")

	answer = input(">>>> ")

	if answer == "1":
		new_transaction()
	elif answer == "2":
		all_transaction()
	elif answer == "3":
		update_transaction()
	elif answer == "4":
		delete_transaction()
	else:
		exit()


clear()
menu()
