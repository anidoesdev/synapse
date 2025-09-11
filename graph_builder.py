# graph_builder.py
# in graph_builder.py

import networkx as nx
import matplotlib.pyplot as plt

def build_knowledge_graph(processed_articles):
    # This function is correct, no changes needed here.
    G = nx.DiGraph()
    for article in processed_articles:
        pmid = article['pmid']
        data = article['data']
        if not data or 'entities' not in data or 'relationships' not in data:
            continue

        for entity in data.get('entities', []):
            node_name = entity['name']
            if G.has_node(node_name):
                G.nodes[node_name]['sources'].add(pmid)
            else:
                G.add_node(node_name, type=entity['type'], sources={pmid})

        for rel in data.get('relationships', []):
            source, target = rel['source'], rel['target']
            if G.has_node(source) and G.has_node(target):
                if G.has_edge(source, target):
                    G.edges[source, target]['sources'].add(pmid)
                else:
                    G.add_edge(source, target, type=rel['type'], sources={pmid})
    return G


def draw_graph_matplotlib(G):
    """
    Draws the graph and returns the Matplotlib Figure object.
    """
    # 1. Create a figure and axes
    fig, ax = plt.subplots(figsize=(20, 20))

    pos = nx.spring_layout(G, k=0.5, iterations=50)
    
    # 2. Draw the graph on the specified axes
    nx.draw(ax=ax, G=G, pos=pos, with_labels=True, node_size=2500, node_color='lightblue', 
            font_size=10, arrowsize=20, edge_color='gray')
    
    edge_labels = nx.get_edge_attributes(G, 'type')
    nx.draw_networkx_edge_labels(ax=ax, G=G, pos=pos, edge_labels=edge_labels, font_color='red')
    
    # 3. Set the title on the axes
    ax.set_title("Parkinson's Research Knowledge Graph", size=20)
    
    # 4. Return the figure object
    return fig