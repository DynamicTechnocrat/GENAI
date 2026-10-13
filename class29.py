from google import genai
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
myapikey = os.getenv("my_api_key")

client = genai.Client(api_key = myapikey)

chunk1 = """Nouns are words that name people, places, things, or ideas. They are the building blocks of sentences because they tell us who or what we are talking about. Nouns can be concrete, like "teacher," "river," or "phone," or abstract, like "freedom," "love," or "courage." They can also be common (general names such as "city") or proper (specific names such as "Lagos" or "Amina"). Most nouns change form to show number, so "book" becomes "books." In a sentence, a noun can act as the subject, the object, or the complement. For example, in "The dog chased the ball," both "dog" and "ball" are nouns."""

embedding_chunk1 = client.models.embed_content(
    model = "gemini-embedding-001" ,
    contents = chunk1
)

chunk1_number = embedding_chunk1.embeddings[0].values

question = "what is a noun"

embedding_question = client.models.embed_content(
    model = "gemini-embedding-001" ,
    contents = question)

question_number = embedding_question.embeddings[0].values

print("THIS IS FOR NOUN " , cosine_similarity([question_number] , [chunk1_number]))

chunk2 = """Pronouns are words that take the place of nouns. Their main purpose is to avoid repetition and make speech and writing smoother. Without pronouns, we would say, "Ada said Ada was tired because Ada had worked all day." With pronouns, we say, "Ada said she was tired because she had worked all day." There are several types: personal pronouns (I, you, he, she, it, we, they), possessive pronouns (mine, yours, hers, ours), reflexive pronouns (myself, themselves), demonstrative pronouns (this, that, these, those), and interrogative pronouns (who, what, which). A pronoun must agree with the noun it replaces in number, gender, and person."""

embedding_chunk2 = client.models.embed_content(
    model = "gemini-embedding-001" ,
    contents = chunk2)

chunk2_number = embedding_chunk2.embeddings[0].values

print("this is pronoun " , cosine_similarity([question_number] , [chunk2_number]))