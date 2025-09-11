import os 
import requests
import json


from transformers import pipeline
import torch


def extract_entities_and_relations(abstract_text):
    prompt = f"""
    SYSTEM: You are an expert biomedical researcher specializing in neurodegenerative diseases. Your task is to extract entities and relationships from the provided scientific abstract with high precision.

    The entity types are: [Gene, Protein, Pathway, Drug, Disease, Biomarker, Patient_Cohort, Mutation, Cell_Type, Environmental_Factor].
    The relationship types are: [UPREGULATES, DOWNREGULATES, INHIBITS, ACTIVATES, INCREASES_RISK_OF, DECREASES_RISK_OF, IS_BIOMARKER_FOR, TREATS, AGGRAVATES].

    Format the output as a single, valid JSON object with "entities" (a list of objects with "name" and "type") and "relationships" (a list of objects with "source", "target", and "type").

    Abstract:
    ---
    {abstract_text}
    ---
    JSON Output:
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
            "temprature":0.1,
            "response_format":{"type":"json_object"}
        }

        outputs = pipe(
            response,
            max_new_tokens=1000,
        )
        response_text = outputs.json()['choices'][0]['message']['content']
        return json.loads(response_text)
    except Exception as e:
        print(f"JSON parsing failed: {e}")
        return None