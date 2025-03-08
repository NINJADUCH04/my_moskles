from transformers import pipeline 
import torch 
classifier = pipeline ("sentiment-analysis")

def analyze (user_input):

    result = classifier (user_input)
    return result
