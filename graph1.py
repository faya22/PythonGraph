import networkx as nx
import matplotlib.pyplot as plt
import requests

r = requests.get('https://eti-server.herokuapp.com/')

response = r.json()
print(response)


G = nx.Graph()
for i in range(len(response)):
    G.add_edge(response[i]['importedFileName'], response[i]['sourceFile'], weight=1)

# G.add_edge(response[0]['sourceFile'], response[0]['importedFileName'], weight=1)
# G.add_edge(response[1]['sourceFile'], response[1]['importedFileName'], weight=1)
# G.add_edge(response[2]['sourceFile'], response[2]['importedFileName'], weight=1)

pos = nx.circular_layout(G)


edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_nodes(G, pos, node_color='pink', node_size=500,)

nx.draw_networkx_edges(G, pos, edge_color='blue', arrows=True)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Historyjka 1")
plt.axis('off')
plt.show()

