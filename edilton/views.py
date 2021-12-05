from django.shortcuts import render
import numpy as np
import pandas as pd
import sqlite3

# Create your views here.
def index(request):
    """View function for home page of site."""
    
    #calculus for context
    # Create your connection.
    cnx = sqlite3.connect('db.sqlite3')
    users = pd.read_sql_query("SELECT * FROM website_usuario", cnx)
    comb= pd.read_sql_query("SELECT * FROM website_comb_materias", cnx)
    tb = pd.concat([users, comb], axis=1)
    tabela = tb[['idade', "mat1", "mat2", "mat3", "mat4", "mat5", "mat6", "mat7", "mat8", "mat9", "mat10"]]
    tabela[(tabela['idade'] >= 18)]
    
    mats = pd.read_sql_query("SELECT * FROM website_materias", cnx)[["name"]]
    materias = mats.values.tolist()
    
    colunas = ['mat1', "mat2", "mat3", "mat4", "mat5", "mat6", "mat7", "mat8", "mat9", "mat10"]
    
    pont = 0
    rank = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(materias)):
        
        soma = 0
        
        for col in colunas:
            x = tabela[(tabela[[col]] == materias[i][0])].count()
            soma += x
    
            pont = soma.sum()
            rank[i] = pont
            
    df = pd.DataFrame(materias, rank)
    df = df.sort_index()
    rank = sorted(rank)
    
    rank1 = rank[9]
    rank2 = rank[8]
    rank3 = rank[7]
    rank4 = rank[6]
    rank5 = rank[5]
    rank6 = rank[4]
    rank7 = rank[3]
    rank8 = rank[2]
    rank9 = rank[1]
    rank10 = rank[0]
     
    mat1 = df[0].iloc[9]
    mat2 = df[0].iloc[8]
    mat3 = df[0].iloc[7]
    mat4 = df[0].iloc[6]
    mat5 = df[0].iloc[5]
    mat6 = df[0].iloc[4]
    mat7 = df[0].iloc[3]
    mat8 = df[0].iloc[2]
    mat9 = df[0].iloc[1]
    mat10 = df[0].iloc[0]
    
    context = {
        'mat1' : mat1,
        'mat2' : mat2,
       'mat3' : mat3,
       'mat4' : mat4,
       'mat5' : mat5,
      ' mat6' : mat6,
       'mat7' : mat7,
       'mat8' : mat8,
       'mat9' : mat9,
       'mat10': mat10,
        'rank1' : rank1,
        'rank2' : rank2,
        'rank3' : rank3,
        'rank4' : rank4,
        'rank5' : rank5,
        'rank6' : rank6,
        'rank7' : rank7,
        'rank8' : rank8,
        'rank9' : rank9,
        'rank10' : rank10}
    
    # Render the HTML template index.html with the data in the context variable
    return render(request,'ebs_index.html', context=context)
