import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from loadtime import LoadTime

model_path = "togethercomputer/RedPajama-INCITE-Chat-3B-v1"

model = LoadTime(name=model_path,
                 hf=True,
                 fn=lambda: AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16))()


tokenizer = AutoTokenizer.from_pretrained(model_path) # important: load tokenizer after loading model
