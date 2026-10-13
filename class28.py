### rag retreieval augumentation generation >>

### document  >>> covert number  >>> store 
#### questio >>>  covert number >>> consine similarity
#### document >>>  embedding vector >>>  store in a database >>>  similiarity search >>> retrieve
moeel = "gemini-embedding-2"
text1 = "i am  boy"
text2 = "i am girl"
text3 = "hello philip join"




import numpy as np 

def consine_similarity(a , b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(consine_similarity([0,1,3] , [4,5,6]))
