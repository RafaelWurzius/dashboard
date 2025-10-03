# 📊 Dashboard de Custos e Lucros com Flask + Tkinter + Supabase

Este projeto foi desenvolvido para demonstrar a integração entre **Python**, **Flask**, **Tkinter** e **Supabase** em um sistema simples de custos, lucros e indicadores econômicos.  

O sistema possui duas partes principais:

---

## 🖥️ 1. Dashboard (Flask + Plotly + Supabase)
- Interface web para visualização dos dados em **gráficos interativos**.
- Os dados são buscados em tempo real do **Supabase**.
- Mostra:
  - Gráfico de pizza dos custos (`produção`, `material`, `salário`)
  - Gráfico de barras com os **lucros mensais**
  - Cotação do **Dólar**, **Euro** e **Ibovespa**.

![Dashboard](/dashboard.png)

---

## ⚙️ 2. Painel Administrativo (Tkinter + Supabase)
- Interface gráfica desktop feita em **Tkinter**.
- Permite inserir e atualizar dados diretamente no **Supabase**.
- Funcionalidades:
  - Atualizar **custos**
  - Inserir cotações (**Dólar, Euro, Ibovespa**)
  - Inserir **lucros mensais**

---

## 🚀 Tecnologias Utilizadas
- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Supabase](https://supabase.com/)

---

## 📂 Estrutura
```
dashboard/
├── main.py                 # Flask app (dashboard web)
├── adm.py                # Painel administrativo (Tkinter)
├── templates/
    └── index.html          # Template Jinja2 usado pelo Flask SUPABASE_KEY
```
---

## ⚡ Como executar

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

pip install flask pandas plotly supabase

python main.py
```
Acesse em: http://127.0.0.1:5000

```
python admin.py
```
