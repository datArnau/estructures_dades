#!/usr/bin/env python
# coding: utf-8

# # Exercicis Tasca 2

# ## Exercici 1

# In[ ]:


T1 = ['Gener', 'Febrer', 'Març']
T2 = ['Abril', 'Maig', 'Juny']
T3 = ['Juliol', 'Agost', 'Setembre']
T4 = ['Octubre', 'Novembre', 'Desembre']


# In[3]:


Trimestres = [T1, T2, T3, T4]


# ## Exercici 2

# ### El segon mes del primer trimestre

# In[6]:


print(Trimestres[0][1])


# ### Els mesos del primer trimestre

# In[7]:


print(Trimestres[0])


# ### Setembre i octubre

# In[16]:


print(Trimestres[2][2] + ' i ' + Trimestres[3][0])


# ## Exercici 3

# In[17]:


llista = [3, 1, 5, 7, 2, 9, 4, 8, 13, 15, 11]


# ### Quants números hi ha?

# In[20]:


len(llista)


# ### Quantes vegades apareix el número 3

# In[22]:


print(llista.count(3))


# ### Quantes vegades apareixen els nombres 3 i 4?

# In[26]:


print('El 3 apareix ' + str(llista.count(3)) + ' vegada, i el 4 apareix ' + str(llista.count(4)) + ' vegada.')


# ### Quin és el número més gran?

# In[27]:


max(llista)


# ### Quins són els 3 números més petits?

# In[32]:


llista.sort()
print("els tres numeros més petits son", llista[0],', ', llista[1],' i ', llista[2])


# ### Quin és el rang d’aquesta llista?

# In[37]:


print(max(llista)-min(llista))


# ## Exercici 4

# In[38]:


compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }


# ### Afegeix alguna fruita més

# In[39]:


compra["Mandarines"] = {"Qty" : 7, "€": 0.54}


# In[40]:


### Quant han costat les peres en total?


# In[66]:


print(compra.get("Peres").get("€") * compra.get("Peres").get("Qty"), '€')


# In[58]:


### Quantes fruites hem comprat en total?


# In[67]:


print(compra.get("Pomes").get("Qty") + compra.get("Peres").get("Qty") + compra.get("Mandarines").get("Qty") , 'fruites comprades')


# In[ ]:


### Quina és la fruita més cara?


# In[68]:


llistaFruites = [compra.get("Pomes").get("€"), compra.get("Peres").get("€"), compra.get("Mandarines").get("€")]


# In[69]:


max(llistaFruites)


# In[ ]:




