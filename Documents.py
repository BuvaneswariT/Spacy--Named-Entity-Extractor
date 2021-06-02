#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -U spacy')
get_ipython().system('python -m spacy download en')


# In[12]:


import spacy 
from spacy import displacy
import pandas as pd
#SpaCy 2.x brough significant speed and accuracy improvements
spacy.__version__


# In[6]:


get_ipython().system('python -m spacy download en_core_web_sm')


# In[13]:


nlp = spacy.load("en_core_web_sm")


# In[19]:


text = '''John bought a Toyota camry 2019 model in Toronto in January 2020 at a cost of $38000'''
doc = nlp(text)

entities = []
labels = []
position_start = []
position_end = []

for ent in doc.ents:
    entities.append(ent)
    labels.append(ent.label_)
    position_start.append(ent.start_char)
    position_end.append(ent.end_char)
    
df = pd.DataFrame({'Entities':entities,'Labels':labels,'Position_Start':position_start, 'Position_End':position_end})

df


# In[ ]:




