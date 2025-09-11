import requests
import json
from itertools import combinations
from transformers import pipeline
import torch

def find_potential_connections(graph):
    connections = []
    for node in graph.nodes():
        neighbors = list(graph.successors(node)) + list(graph.predecessors(node))
        if len(neighbors) > 1:
            for neighbor1, neighbor2 in combinations(neighbors, 2):
                if not graph.has_edge(neighbor1, neighbor2) and not graph.has_edge(neighbor2,neighbor1):
                    connections.append((neighbor1,neighbor2,node))
    return connections[:5]

def generate_hypothesis(connection_tuple,api_key):
    node_A, node_C, common_node_B = connection_tuple
    prompt = f"""
    SYSTEM: You are an innovative clinical research strategist specializing in Parkinson's Disease. Your goal is to translate basic science findings into testable clinical hypotheses.

    My knowledge graph, synthesized from recent literature, has revealed two key findings that are not yet directly linked:
    1.  **Finding A:** There is a relationship between "{node_A}" and "{common_node_B}".
    2.  **Finding B:** There is a relationship between "{node_C}" and "{common_node_B}".

    Based on these findings, formulate a **novel and testable clinical hypothesis** directly linking "{node_A}" and "{node_C}". Your response must include three sections formatted with Markdown:
    1.  **### Hypothesis:** State the core hypothesis clearly.
    2.  **### Scientific Rationale:** Explain the biological reasoning supporting your hypothesis.
    3.  **### Experimental Validation:** Propose a specific, high-level experiment to test it.
    """
    try:
        model_id = "openai/gpt-oss-20b"

        pipe = pipeline(
            "text-generation",
            model=model_id,
            dtype=torch.bfloat16,
            device_map="auto",
        )
        response={
            "messages":[{"role":"user","content":prompt}],
            "temprature":0.7,
            "response_format":{"type":"json_object"}
        }
        output=pipe(
            response,
            max_new_tokens = 1000
        )
        return output.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating hypothesis: {e}"