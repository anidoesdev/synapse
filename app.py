import streamlit as st 
from data_miner import fetch_medical_data
from extractor import extract_entities_and_relations
from graph_builder import build_knowledge_graph,draw_graph_matplotlib
from hypothesizer import find_potential_connections, generate_hypothesis

st.set_page_config(layout="wide")
st.title("🔬 Synapse: Parkinson's Disease Research Assistant")

st.sidebar.header("Controls")
default_query = ('Parkinson\'s Disease')
query = st.sidebar.text_area("PubMed Query",default_query,height=100)
max_papers = st.sidebar.slider("Number of papers to analyze",5,50,10)
run_button = st.sidebar.button("Begin Synthesis")

if run_button:
    st.session_state.clear()
    with st.spinner(f"Fetching {max_papers} recent articles from PubMed..."):
        articles = []
        articles = fetch_medical_data(query,"anikajain1307@gmail.com",max_papers)
        st.session_state.articles = articles
    if not articles:
        st.error("Could not fetch articles. Check your query or network connection.")
    else:
        processed_articles = []
        progress_bar = st.progress(0, text="Analyzing abstracts...")
        for i, article in enumerate(articles):
            data = extract_entities_and_relations(article['abstract'])
            if data:
                processed_articles.append({'pmid':article['pmid'],'data':data})
            progress_bar.progress((i+1)/len(articles),text=f"Analyzing abstract {i+1}/{len(articles)}")
        st.session_state.processed_articles = processed_articles
        
        with st.spinner("Building and visualizing the knowledge graph..."):
            graph = build_knowledge_graph(processed_articles)
            st.session_state.graph = graph
            fig = draw_graph_matplotlib(graph)
            st.session_state.graph_fig = fig

if 'graph_fig' in st.session_state:
    st.subheader("Synthesized Knowledge Graph")
    st.pyplot(st.session_state.graph_fig,width="stretch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💡 Generated Hypotheses")
        with st.spinner("Generating novel hypotheses..."):
            connections = find_potential_connections(st.session_state.graph)
            if not connections:
                st.warning("No clear hidden connections found to generate hypotheses from.")
            else:
                for conn in connections:
                    hypothesis = generate_hypothesis(conn)
                    with st.expander(f"Hypothesis: Link between **{conn[0]}** and **{conn[1]}**"):
                        st.markdown(hypothesis)
    
    with col2:
        st.subheader("✅ Trust Layer: Source Verification")
        st.info("Click on a concept to see the research papers (PMIDs) that mention it.")
        
        if st.session_state.graph is not None and st.session_state.graph.nodes():
            sorted_nodes = sorted(st.session_state.graph.degree,key=lambda item: item[1],reverse=True)
            for node, degree in sorted_nodes[:10]:
                with st.expander(f"**{node}**(mentioned in {len(st.session_state.graph.nodes[node]['source'])}papers)"):
                    for pmid in st.session_state.graph.nodes[node]['sources']:
                        st.markdown(f"- [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)")
        
            