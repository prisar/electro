from transformers import AutoTokenizer, AutoModel

bnbert_tokenizer = AutoTokenizer.from_pretrained("sagorsarker/bangla-bert-base")
text = "আমি বাংলায় গান গাই।"
tokens = bnbert_tokenizer.tokenize(text)
print(tokens)
# ['আমি', 'বাংলা', '##য', 'গান', 'গাই', '।']


