import arxiv

def fetch_abstracts(query,max_results = 20):
    try:
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )
        abstracts = [result.summary.replace('\n',' ') for result in search.results()]
        print(f"Successfully fetched {len(abstracts)} abstracts")
        return abstracts
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == '__main__':
    test_query = "parkinson's disease"
    papers = fetch_abstracts(test_query,5)
    if papers:
        print("---First Abstract---")
        print(papers[0])