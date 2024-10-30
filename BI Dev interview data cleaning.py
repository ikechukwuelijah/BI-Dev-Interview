#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries I need to do task
import pandas as pd
import numpy as np
import os


# In[2]:


# check work directory
os.getcwd()


# In[5]:


# read dataframe, identify sheet_names and view data
staffs = pd.read_excel("stafflist.xlsx",sheet_name = ["Employee List","Ref list"])


# In[8]:


# merge Employee List and Ref list sheet
staffs = pd.concat(pd.read_excel("stafflist.xlsx",sheet_name=None))
staffs


# In[36]:


# drop unwanted columns. Now have parent field, subgroup and subcode left joined to employee List table
staffs.drop(columns=['Occ Code & Grade','Job role','Area of work','Grade'], inplace=True)


# In[47]:


# check for null. mismatch caused alot of null. Will transform on Power BI to avoid missing important data for analysis
staffs.isnull().sum()


# In[58]:


# check for duplicate values. 413 duplicates. Will clean up using power query
staffs.duplicated().sum()


# In[73]:


# remove duplicates
staffs.drop_duplicates(inplace=True)


# In[74]:


# check for duplicate values. 413 duplicates. Will clean up using power query
staffs.duplicated().sum()


# In[75]:


staffs


# In[76]:


# export file in csv format
staffs.to_csv('Enriched_Employee_List.csv', index=False)

