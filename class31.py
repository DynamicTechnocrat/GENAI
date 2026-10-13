from dotenv import load_dotenv
import os
from google import genai
from sklearn.metrics.pairwise import cosine_similarity
from google.genai import types
#pip install pypdf
from pypdf import PdfReader

pages = PdfReader("student2.pdf").pages
document = []
for page in pages:
    document.append(page.extract_text().replace("\n", ""))

load_dotenv() # load environment variables from .env file

myapikey = os.getenv("my_api_key") ### getting api key from .env file

client = genai.Client(api_key=myapikey) # create a client object to interact with the GenAI API


embedding_chunk = client.models.embed_content(
    model="gemini-embedding-001",
    contents = document)

doc1_embed = embedding_chunk.embeddings[0].values 
doc2_embed = embedding_chunk.embeddings[1].values

question = "who is jeff?"

question_embed = client.models.embed_content(
    model = "gemini-embedding-001",
    contents = question)
question_number_embed = question_embed.embeddings[0].values

print(cosine_similarity([question_number_embed] , [doc1_embed]))
print(cosine_similarity([question_number_embed] , [doc2_embed]))

consine_result = [cosine_similarity([question_number_embed] , [doc1_embed])[0][0],
                    cosine_similarity([question_number_embed] , [doc2_embed])[0][0]]

max_value = max(consine_result)

location_of_max_value = consine_result.index(max_value)

print("this is the location of max value " , location_of_max_value)


document_align = document[location_of_max_value]

prompt = f"use this docuemnt {document_align} to answer this question {question} in a supportive , encouraging and highly analytical manner"

#developing our ai
instruction = "you are achievers ai , your role is to assist in academic recovery and student records advisor you are supportive , ecounraging hihly analyitical "
configuration = types.GenerateContentConfig(system_instruction = instruction)

ai = client.chats.create(model = "gemini-3.5-flash-lite" , config = configuration)

response = ai.send_message(prompt)
print(response.text)

