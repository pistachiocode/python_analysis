#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 23:44:52 2018

@author: rocio
"""

import pandas as pd

# Load dataset

df = pd.read_csv("./resources/CAERS_ASCII_2004_2017Q2.tsv", sep="\t")


df_products = df[['PRI_Reported Brand/Product Name', 
                  'PRI_FDA Industry Code', 
                  'PRI_FDA Industry Name']]

# Rename columns
df_products.columns = ['productname', 'categorycode', 'categoryname']
df_products = df_products.drop_duplicates()

# Correcting category 2 label
df_products.loc[df_products['categorycode']==2, ['categoryname']] = 'Whole Grain/Milled Grain Prod/Starch'

# Removin REDACTED products
df_products = df_products[df_products.productname != 'REDACTED']

df_products.to_csv('./resources/DC01_products.txt',sep="\t")
