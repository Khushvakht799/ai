from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_path = r"C:\Users\usuario\Documents\1111\DeepSeak_models\deepseek-coder-1.3b-base.Q3_K_S.gguf"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
