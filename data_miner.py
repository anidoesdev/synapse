from pymed import PubMed

def fetch_medical_data(query, email="your_email@example.com", max_papers=50):
    """
    Fetches abstracts and their PMIDs from PubMed in a robust way.
    
    Args:
        query (str): The search query for PubMed.
        email (str): Your email address for the PubMed API (as a courtesy).
        max_papers (int): The maximum number of papers to fetch.
        
    Returns:
        list: A list of dictionaries, each containing a 'pmid' and 'abstract'.
    """
    # 1. Input Validation: Check if the query is valid before making an API call.
    if not query or not isinstance(query, str):
        print("Error: A valid query string must be provided.")
        return []

    try:
        # 2. Reusability: Email is now an argument, not hardcoded.
        pubmed = PubMed(tool="Synapse", email=email)
        results = pubmed.query(query, max_results=max_papers)
        
        articles = []
        for article in results:
            if article.abstract and article.pubmed_id:
                # 3. Robustness: Use .strip() for safer cleaning of the PMID.
                articles.append({
                    'pmid': article.pubmed_id.strip(),
                    'abstract': article.abstract
                })
                
        print(f"Successfully fetched {len(articles)} articles.")
        return articles
    
    # 4. Specificity (Optional but good practice): Handle potential errors more gracefully.
    except Exception as e:
        print(f"An error occurred during the PubMed query: {e}")
        return []

