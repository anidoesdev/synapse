import networkx as nx
import matplotlib.pyplot as plt

def build_knowledge_graph(list_of_extracted_data):
    G = nx.DiGraph()
    
    for data in list_of_extracted_data:
        if not data or 'entities' not in data or 'relationships' not in data:
            continue
        for entity in data['entities']:
            G.add_node(entity['name'],type=entity['type'])
        
        for rel in data['relationships']:
            if G.has_node(rel['source']) and G.has_node(rel['target']):
                G.add_edge(rel['source'],rel['target'],type=rel['type'])
    
    print(f"Built graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    return G
def draw_graph(G):
    plt.figure(figsize=(16,16))
    pos = nx.spring_layout(G, k=0.9)
    
    nx.draw_networkx_nodes(G, pos, node_size=2000,node_color='skyblue')
    nx.draw_networkx_edges(G,pos,edgelist=G.edges(),arrowstyle='->',arrowsize=20)
    nx.draw_networkx_labels(G,pos,font_size=10)
    
    edge_labels = nx.get_edge_attributes(G,'type')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_color='red')
    
    plt.title("Synapse Knowledge Graph")
    plt.axis('off')
    return plt