from transformers import pipeline 
import torch 
classifier = pipeline ("sentiment-analysis")

res = classifier ("I've been waiting for a HuggingFace course my whole")

print (res) 