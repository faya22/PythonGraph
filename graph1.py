import networkx as nx
import matplotlib.pyplot as plt
import requests

r = requests.get('https://eti-server.herokuapp.com/')

response = r.json()
print(response)




G = nx.DiGraph()

G.add_edge(response[0]['sourceFile'], response[0]['importedFunction'], weight=1, title='ab')
G.add_edge(response[0]['importedFunction'], response[0]['importedFileSoure'], weight=1)

G.add_edge(response[1]['sourceFile'], response[1]['importedFunction'], weight=1)
G.add_edge(response[1]['importedFunction'], response[1]['importedFileSoure'], weight=1)

G.add_edge(response[2]['sourceFile'], response[2]['importedFile'], weight=1)
G.add_edge(response[2]['importedFile'], response[2]['importedFileSoure'], weight=1)

G.add_edge(response[3]['sourceFile'], response[3]['importedFile'], weight=1)
G.add_edge(response[3]['importedFile'], response[3]['iportedPackage'], weight=1)

pos = nx.circular_layout(G)


edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_nodes(G, pos, node_color='pink', node_size=500,)

title = nx.get_node_attributes(G, 'title')

nx.draw_networkx_edges(G, pos, edge_color='blue', arrows=True)

nx.draw_networkx_labels(G, pos)

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("OUTPUT")
plt.axis('off')
plt.show()