import networkx as nx
import matplotlib.pyplot as plt
import requests

r = requests.get('https://eti-server.herokuapp.com/')

response = r.json()
print(response)



#G = nx.read_edgelist(r, create_using=nx.Graph(), nodetype=int)
G = nx.Graph()
G.add_edge(response[0]['sourceFile'], response[0]['importedFunction'])
G.add_edge(response[0]['importedFunction'], response[0]['importedFileSoure'])

G.add_edge(response[1]['sourceFile'], response[1]['importedFunction'])
G.add_edge(response[1]['importedFunction'], response[1]['importedFileSoure'])

G.add_edge(response[2]['sourceFile'], response[2]['importedFile'])
G.add_edge(response[2]['importedFile'], response[2]['importedFileSoure'])

G.add_edge(response[3]['sourceFile'], response[3]['importedFile'])
G.add_edge(response[3]['importedFile'], response[3]['iportedPackage'])



# for i in range(len(response)):
#    #  G.add_edge(response[i]['sourceFile'], response[i]['importedFileSoure'])
#
#     if hasattr(response[i], 'importedFileSoure'):
#         G.add_edge(response[i]['sourceFile'], response[i]['importedFileSoure'])
#     else:
#         G.add_edge(response[i]['sourceFile'], response[i]['iportedPackage'])

#print(i)

#G.add_edge(response[3]['sourceFile'], response[3]['importedFile']
#G.add_edge(response[3]['sourceFile'], response[3]['iportedPackage'])

nx.draw(G, with_labels = True)


print(nx.info(G))

# nx.draw(G)

plt.show()
