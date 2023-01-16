import requests

'''
API_TOKEN = ""
with open("api_token.txt") as f:
    API_TOKEN = f.read()

print(API_TOKEN.strip())

API_URL = "https://api-inference.huggingface.co/models/ai4bharat/indicwav2vec_v1_bengali"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

output = query("output.wav")

'''


from transformers import AutoProcessor, AutoModelForCTC, pipeline

processor = AutoProcessor.from_pretrained("ai4bharat/indicwav2vec_v1_bengali")

model = AutoModelForCTC.from_pretrained("ai4bharat/indicwav2vec_v1_bengali")

pipe = pipeline(model="ai4bharat/indicwav2vec_v1_bengali")

bangla = pipe("https://github.com/prisar/electro/raw/main/py/bangla.wav")
print(bangla)
