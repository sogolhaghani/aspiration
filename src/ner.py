from transformers import AutoTokenizer,AutoModelForTokenClassification
from transformers import pipeline
print('OK')

# tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
# print('OK')
# # sentences = [list of sentences]
# # inputs = tokenizer(sentences, padding="max_length", truncation=True)

model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
print('OK')


# nlp = pipeline("ner", model=model, tokenizer=tokenizer)
# example = "My name is Wolfgang and I live in Berlin"

# ner_results = nlp(example)
# print(ner_results)