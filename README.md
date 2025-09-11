# Synapse: AI-Powered Medical Research Assistant 🔬

Synapse is a web-based application designed to accelerate scientific discovery in complex medical fields like Parkinson's Disease. It leverages Large Language Models (LLMs) to analyze vast amounts of scientific literature, build a dynamic knowledge graph, and generate novel, testable hypotheses that can guide researchers toward potential breakthroughs.


-----

## Key Features

  * **Automated Literature Review:** Ingests and processes hundreds of research paper abstracts from PubMed based on a specific query.
  * **AI-Powered Information Extraction:** Uses a powerful LLM to read unstructured text and extract key medical concepts (genes, proteins, drugs) and their relationships.
  * **Dynamic Knowledge Graph:** Synthesizes the extracted information into an interconnected knowledge graph, providing a "big picture" view of the current research landscape.
  * **Novel Hypothesis Generation:** Analyzes the graph to find non-obvious, indirect connections between concepts and formulates them into new, clinically relevant hypotheses.
  * **"Trust Layer" for Verifiability:** A core feature that links every piece of data in the graph back to its source research paper (via PMID), ensuring transparency and accountability.
  * **Interactive Web Interface:** A simple and intuitive UI built with Streamlit that allows users to run queries, view the knowledge graph, and explore generated hypotheses.

-----

## Technical Architecture & Tech Stack

Synapse is built as a modular Python pipeline that integrates several powerful open-source libraries.

  * **Backend/Logic:** Python
  * **Web Interface:** Streamlit
  * **Data Sourcing:** Pymed (for PubMed API)
  * **AI Model Interaction:** Requests (for LLM API calls, e.g., to Groq)
  * **Knowledge Graph:** NetworkX
  * **Visualization:** Matplotlib

-----

## Setup and Installation

Follow these steps to get a local instance of Synapse running.

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/synapse.git
    cd synapse
    ```

2.  **Install Dependencies:**
    Make sure you have Python 3.8+ installed. Then, install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

    *(Note: You will need to create a `requirements.txt` file containing streamlit, pymed, requests, networkx, and matplotlib).*

3.  **Set Up API Key:**
    This project requires an API key from an LLM provider like [Groq](https://console.groq.com/).

      * Open the `extractor.py` and `hypothesizer.py` files.
      * Replace the placeholder `"YOUR_GROQ_API_KEY_HERE"` with your actual API key.

-----

## How to Use

1.  **Run the Streamlit App:**
    Open your terminal in the project's root directory and run the following command:

    ```bash
    streamlit run app.py
    ```

2.  **Use the Application:**

      * Your browser will open a new tab with the Synapse interface.
      * Enter a research topic into the PubMed query box in the sidebar.
      * Adjust the number of papers to analyze.
      * Click the "Begin Synthesis" button to start the process.
      * Explore the generated knowledge graph and the novel hypotheses.

-----

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
