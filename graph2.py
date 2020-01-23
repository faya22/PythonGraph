import networkx as nx
import matplotlib.pyplot as plt
import requests

r = requests.get('https://eti-server.herokuapp.com/')

response = r.json()
print(response)


G = nx.DiGraph()

G.add_edge(str(response[0]['functionName']), response[0]['sourceFile'], weight=1)
G.add_edge(str(response[1]['functionName']), response[1]['sourceFile'], weight=1)
G.add_edge(str(response[2]['functionName']), response[1]['functionName'], weight=1)


pos = nx.spring_layout(G)

edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_nodes(G, pos, node_color='red', node_size=500,)

nx.draw_networkx_edges(G, pos, edge_color='purple', arrows=True)

nx.draw_networkx_labels(G, pos)

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Historyjka 2")
plt.axis('off')
plt.show()
