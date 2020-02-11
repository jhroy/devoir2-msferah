# coding : utf-8

import json
import csv 
import requests

fichier = "lobby.csv"
url = "http://jhroy.ca/uqam/lobby.json"

#s'afficher

entete = {
	"User-Agent":"Mayssa Ferah - 514/994-3629",
	"From":"mayssa.ferah@gmail.com"
}

req = requests.get(url,headers=entete)
#print(req)

lob = req.json()
# print(lob["registre"])
tout = lob["registre"] 
for comm in tout:
    # print(len(comm))
    # print(comm[0]["en_client_org_corp_nm"])
    # print(len(comm[1]))
    sujets = comm[1]
    infos = list("en_client_org_corp_nm","fr_client_org_corp_nm","client_org_corp_num","date_comm")
    for sujet in sujets:
        # print(sujet)
        if "limat" in sujet["objet"]:
            # print(sujet)
            list.append(comm[0]["en_client_org_corp_nm"])
            list.append(comm[0]["fr_client_org_corp_nm"])
            list.append(comm[0]["client_org_corp_num"])
            list.append(comm[0]["date_comm"])
            
            harry = open(fichier,"a")
            potter = csv.writer(harry)
            potter.writerow(infos)

    print(req)
            
            




 


