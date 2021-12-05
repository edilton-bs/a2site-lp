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
    
    colunas = [mat1, "mat2", "mat3", "mat4", "mat5", "mat6", "mat7", "mat8", "mat9", "mat10"]
    
    pont = 0
    rank = []
    for i in range(0, len(materias)):
        
        soma = 0
        rank = []
        for col in colunas:
            x = tabela[(tabela[[col]] == materias[i][0])].count()
            soma += x
    
            pont = soma.sum()
            rank.append(pont)
    
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
     
    mat1 = materias[9][0]
    mat2 = materias[8][0]
    mat3 = materias[7][0]
    mat4 = materias[6][0]
    mat5 = materias[5][0]
    mat6 = materias[4][0]
    mat7 = materias[3][0]
    mat8 = materias[2][0]
    mat9 = materias[1][0]
    mat10 = materias[0][0]
    colunas = [mat1, "mat2", "mat3", "mat4", "mat5", "mat6", "mat7", "mat8", "mat9", "mat10"] 
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
        'rank10' : rank10,
        'materias' : colunas,
        'rank' : rank}
    
    # Render the HTML template index.html with the data in the context variable
    return render(request,'ebs_index.html', context=context)
