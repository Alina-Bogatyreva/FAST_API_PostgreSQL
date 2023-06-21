from db import DBClientPerson
from db.session import Session

session = Session()
client = DBClientPerson(session)
mikhail = client.add_person("Mikhail", "I", False)
maria = client.add_person("Maria", "Dolgorukova", True, mikhail.id)
pelagiya = client.add_person("Pelagiya", "", False)
anna = client.add_person("Anna", "", False)
marfa = client.add_person("Marfa", "", False)
alexis = client.add_person("Alexis", "", False)
mariaMiloslavskaya = client.add_person("Maria", "Miloslavskaya", True, alexis.id)
сatherine = client.add_person("Catherine", "", False)
feodosia = client.add_person("Feodosia", "", False)
fedor = client.add_person("Fedor", "III", False)
marfaApraksina = client.add_person("Maria", "Apraksina", True, fedor.id)
ivan = client.add_person("Ivan", "V", False)
sofia = client.add_person("Sofia", "", False)
praskovia = client.add_person("Praskovia", "", True, ivan.id)
peter = client.add_person("Peter", "I", False)
feodosiaIvanovna = client.add_person("Feodosia", "", False)
natalya = client.add_person("Natalya", "III", False)
сatherineWife = client.add_person("Catherine", "", True, peter.id)
alexander = client.add_person("Alexander", "V", False)
pavel = client.add_person("Pavel", "", False)

client.update_person(mikhail.id, kids_ids=[pelagiya.id, anna.id, marfa.id, alexis.id])
client.update_person(maria.id, kids_ids=[pelagiya.id, anna.id, marfa.id, alexis.id])
client.update_person(mariaMiloslavskaya.id, kids_ids=[сatherine.id, feodosia.id, fedor.id])
client.update_person(alexis.id, kids_ids=[сatherine.id, feodosia.id, fedor.id])
client.update_person(fedor.id, kids_ids=[ivan.id, sofia.id])
client.update_person(marfaApraksina.id, kids_ids=[ivan.id, sofia.id])
client.update_person(ivan.id, kids_ids=[peter.id, feodosiaIvanovna.id, natalya.id])
client.update_person(praskovia.id, kids_ids=[peter.id, feodosiaIvanovna.id, natalya.id])
client.update_person(peter.id, kids_ids=[alexander.id, pavel.id])
client.update_person(сatherineWife.id, kids_ids=[alexander.id, pavel.id])





"""
                                       Mikhail I  +  Maria Dolgorukova
                  1.Pelagiya  2.Anna  3.Marfa  4.Alexis + Maria Miloslavskaya
                                        1.Catherine  2.Feodosia  3.Feodor III+Marfa Apraksina
                                                                      1.Ivan V+Praskovia Saltykova  2.Sofia
                                                                    1.Peter I+Catherine  2.Feodosia   3.Natalya
                                                                1.Alexander  2.Pavel
"""