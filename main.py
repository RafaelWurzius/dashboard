from flask import Flask, render_template
import pandas as pd
import plotly.express as px
from supabase import create_client
import os

app = Flask(__name__)

# Configurações do Supabase (substitua com suas próprias credenciais)
SUPABASE_URL = 'https://wejguaikdgdzufdlgtbe.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Indlamd1YWlrZGdkenVmZGxndGJlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxMzk5MzcsImV4cCI6MjAxMDcxNTkzN30.ULwFJjt9upbxgTtl3uqvUeXEiGe-jRaKNj6Eo5Byps0'

# Configuração do cliente Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Função para buscar dados do Supabase
def buscar_dados_supabase():

    # Busque os dados da tabela 'lucros'
    lucros_query = supabase.from_('lucros').select('*').order('id').execute()  # Ordene em ordem crescente
    # lucros_query = supabase.from_('lucros').select('*').execute()
    # lucros_data = lucros_query.get('data')
    lucros_data = lucros_query.data 

    # Busque os dados da tabela 'custos'
    custos_query = supabase.from_('custos').select('*').execute()
    # custos_data = custos_query.get('data')
    custos_data = custos_query.data

    # Busque a cotação do dólar da tabela 'dolar'
    # dolar_query = supabase.from_('dolar').select('*').limit(1).order('created_at', ascending=False).execute()
    # dolar_query = supabase.from_('dolar').select('*').limit(1).order('-created_at').execute()  # Use '-' para ordenar em ordem decrescente
    # dolar_data = dolar_query.get('data')
    # dolar_data = dolar_query.data

    dolar_query = supabase.from_('dolar').select('*').order('id').execute()  # Ordene em ordem crescente
    dolar_data = dolar_query.data  # Use .data para acessar os dados
    dolar_data.reverse()  # Inverta a ordem dos dados

    return lucros_data, custos_data, dolar_data

# Rota principal que exibe os gráficos e a cotação do dólar
@app.route('/')
def index():
    lucros_data, custos_data, dolar_data = buscar_dados_supabase()

    # Converta os dados em DataFrames do pandas
    custos_df = pd.DataFrame(custos_data)
    lucros_df = pd.DataFrame(lucros_data)
    dolar_df = pd.DataFrame(dolar_data)

    print('-------------------------')
    print("lucros_df: \n" , lucros_df)
    print('-------------------------')

    # Transforme o DataFrame para um formato apropriado para o gráfico de pizza
    df_melted = pd.melt(custos_df, id_vars=['id'], value_vars=['producao', 'materia', 'salario'], var_name='Custos', value_name='Valor')

    # Crie o gráfico de pizza
    custos_pie = px.pie(df_melted, names='Custos', values='Valor', title='Custos')

    # Crie um gráfico de pizza para os custos
    #custos_pie = px.pie(custos_df, names=custos_df.columns[1:], title='Custos')
# , values = custos_df.iloc[1]
    # Crie um gráfico de barras para os lucros
    
    # Renomeie a coluna 'mês' para 'Mês' (com a primeira letra maiúscula)
    # lucros_df.rename(columns={'mês': 'Mês'}, inplace=True)
    # print('-------------------------')
    # print(custos_df.head())
    # print('-------------------------')
    lucros_bar = px.bar(lucros_df, x='mes', y='lucro', title='Lucro Mensal')
    # Obtenha a cotação mais recente do dólar
    cotacao_dolar = dolar_df.iloc[0]['cotacao']
    euro = dolar_df.iloc[0]['euro']
    ibovespa = dolar_df.iloc[0]['ibovespa']

    return render_template('index.html', custos_pie=custos_pie.to_html(), lucros_bar=lucros_bar.to_html(), cotacao_dolar=cotacao_dolar, euro=euro, ibovespa=ibovespa)

if __name__ == '__main__':
    app.run(debug=True)