import tkinter as tk
from tkinter import ttk
import supabase

# Configurar a conexão com o Supabase
supabase_url = 'https://wejguaikdgdzufdlgtbe.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Indlamd1YWlrZGdkenVmZGxndGJlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxMzk5MzcsImV4cCI6MjAxMDcxNTkzN30.ULwFJjt9upbxgTtl3uqvUeXEiGe-jRaKNj6Eo5Byps0'
supabase_client = supabase.Client(supabase_url, supabase_key)

# Função para inserir ou atualizar dados na tabela "custos"
def atualizar_custos():
    producao = producao_entry.get()
    material = material_entry.get()
    salario = salario_entry.get()
    
    data = supabase_client.table("custos").update({"producao": producao, "materia": material, "salario":salario}).eq("id", 1).execute()

    # Limpar os campos de entrada após a inserção ou atualização
    producao_entry.delete(0, tk.END)
    material_entry.delete(0, tk.END)
    salario_entry.delete(0, tk.END)


def inserir_cotacao():
    dolar = cotacao_entry.get()
    euro = euro_entry.get()
    ibovespa = ibovespa_entry.get()

    data = supabase_client.table("dolar").insert({"cotacao":dolar, "euro": euro, "ibovespa": ibovespa}).execute()


    cotacao_entry.delete(0, tk.END)
    euro_entry.delete(0, tk.END)
    ibovespa_entry.delete(0, tk.END)

def inserir_lucro():
    mes = mes_entry.get()
    lucro = lucro_entry.get()

    data = supabase_client.table("lucros").insert({"mes":mes, "lucro": lucro}).execute()


    cotacao_entry.delete(0, tk.END)
    euro_entry.delete(0, tk.END)
    ibovespa_entry.delete(0, tk.END)

# Criar a janela principal
root = tk.Tk()
root.title('Sistema de Custos')

# Etiquetas e campos de entrada para inserção/atualização de dados
producao_label = tk.Label(root, text='Produção:')
producao_label.pack()
producao_entry = tk.Entry(root)
producao_entry.pack(padx = 100, pady = 10)

material_label = tk.Label(root, text='Material:')
material_label.pack()
material_entry = tk.Entry(root)
material_entry.pack()

salario_label = tk.Label(root, text='Salário:')
salario_label.pack()
salario_entry = tk.Entry(root)
salario_entry.pack()

# Botão para inserir/atualizar dados na tabela "custos"
inserir_atualizar_button = tk.Button(root, text='Atualizar Dados', command=atualizar_custos)
inserir_atualizar_button.pack()


# Adicionar uma linha separadora horizontal--------------------------------------------------------------
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=10, pady=10)

# Continuar a adicionar outros widgets após a linha separadora
cotacao_label = tk.Label(root, text='Dolar:')
cotacao_label.pack()
cotacao_entry = tk.Entry(root)
cotacao_entry.pack()

euro_label = tk.Label(root, text='Euro:')
euro_label.pack()
euro_entry = tk.Entry(root)
euro_entry.pack()

ibovespa_label = tk.Label(root, text='Ibovespa:')
ibovespa_label.pack()
ibovespa_entry = tk.Entry(root)
ibovespa_entry.pack()

inserir_cotacao_button = tk.Button(root, text='Inserir Dados', command=inserir_cotacao)
inserir_cotacao_button.pack()

# Adicionar uma linha separadora horizontal--------------------------------------------------------------
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=10, pady=10)

mes_label = tk.Label(root, text='Mês:')
mes_label.pack()
mes_entry = tk.Entry(root)
mes_entry.pack()

lucro_label = tk.Label(root, text='Lucro:')
lucro_label.pack()
lucro_entry = tk.Entry(root)
lucro_entry.pack()

inserir_lucro_button = tk.Button(root, text='Inserir Lucro', command=inserir_lucro)
inserir_lucro_button.pack()

root.mainloop()
