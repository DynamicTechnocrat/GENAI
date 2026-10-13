from dotenv import load_dotenv
import os
from google import genai
from sklearn.metrics.pairwise import cosine_similarity
from google.genai import types


chunk1 = """Nouns are words that name people, places, things, or ideas. They are the building blocks of sentences because they tell us who or what we are talking about. Nouns can be concrete, like "teacher," "river," or "phone," or abstract, like "freedom," "love," or "courage." They can also be common (general names such as "city") or proper (specific names such as "Lagos" or "Amina"). Most nouns change form to show number, so "book" becomes "books." In a sentence, a noun can act as the subject, the object, or the complement. For example, in "The dog chased the ball," both "dog" and "ball" are nouns."""

chunk2 = """Pronouns are words that take the place of nouns. Their main purpose is to avoid repetition and make speech and writing smoother. Without pronouns, we would say, "Ada said Ada was tired because Ada had worked all day." With pronouns, we say, "Ada said she was tired because she had worked all day." There are several types: personal pronouns (I, you, he, she, it, we, they), possessive pronouns (mine, yours, hers, ours), reflexive pronouns (myself, themselves), demonstrative pronouns (this, that, these, those), and interrogative pronouns (who, what, which). A pronoun must agree with the noun it replaces in number, gender, and person."""

chunk3 = """Verbs are words that express actions, events, or states of being. They are essential to sentences because they tell us what the subject is doing or what is happening. Verbs can be action verbs (run, jump, write), linking verbs (am, is, are), or auxiliary verbs (have, do, will). They can also change form to indicate tense, mood, and voice. For example, "I run" (present tense) becomes "I ran" (past tense) and "I will run" (future tense). In a sentence, the verb usually follows the subject and may be followed by an object or complement."""


load_dotenv() # load environment variables from .env file

myapikey = os.getenv("my_api_key") ### getting api key from .env file

client = genai.Client(api_key=myapikey) # create a client object to interact with the GenAI API

embedding_chunks = client.models.embed_content(
    model="gemini-embedding-001",
    contents = [chunk1, chunk2, chunk3] # embedding multiple chunks of text at once
)

embedding_chunk1 = embedding_chunks.embeddings[0].values
embedding_chunk2 = embedding_chunks.embeddings[1].values
embedding_chunk3 = embedding_chunks.embeddings[2].values

question = "what is a verb"

embedding_question = client.models.embed_content(
    model = "gemini-embedding-001",
    contents = question)

question_number = embedding_question.embeddings[0].values

print("THIS IS FOR NOUN " , cosine_similarity([question_number] , [embedding_chunk1]))
print("this is pronoun " , cosine_similarity([question_number] , [embedding_chunk2]))
print("this is verb " , cosine_similarity([question_number] , [embedding_chunk3]))

#####

context = "Answer this user question which is : " + question  + " based on this : " + chunk3

instruction = "you are jeff ai our ai assistant"

configuration = types.GenerateContentConfig(system_instruction = instruction)

ai = client.chats.create(model = "gemini-3.5-flash-lite" , config = configuration)
response = ai.send_message(context)
print(response.text)












#