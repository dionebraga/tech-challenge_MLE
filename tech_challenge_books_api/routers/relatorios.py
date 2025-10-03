from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..infra.database import get_db
from ..models.livro_model import Livro
import pandas as pd
import plotly.express as px
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/api/v1/relatorios", tags=["📊 Estatísticas"])


# 🔹 Função utilitária para converter consulta em DataFrame
def get_livros_df(db: Session):
    livros = db.query(Livro).all()
    if not livros:
        return pd.DataFrame(columns=["id", "titulo", "descricao", "preco", "categoria_id"])
    return pd.DataFrame([{
        "id": l.id,
        "titulo": l.titulo,
        "descricao": l.descricao,
        "preco": l.preco,
        "categoria_id": l.categoria_id
    } for l in livros])


# 🍕 Pizza - distribuição
@router.get("/pizza", response_class=HTMLResponse, summary="Distribuição de livros por categoria 🍕")
def grafico_pizza(db: Session = Depends(get_db)):
    df = get_livros_df(db)
    if df.empty:
        return HTMLResponse("<h3>Sem dados</h3>")
    fig = px.pie(df, names="categoria_id", title="📚 Distribuição de Livros por Categoria")
    return HTMLResponse(fig.to_html(full_html=False))


# 📊 Barras - preço médio
@router.get("/barras", response_class=HTMLResponse, summary="Preço médio por categoria 📊")
def grafico_barras(db: Session = Depends(get_db)):
    df = get_livros_df(db)
    if df.empty:
        return HTMLResponse("<h3>Sem dados</h3>")
    df_group = df.groupby("categoria_id")["preco"].mean().reset_index()
    fig = px.bar(df_group, x="categoria_id", y="preco", title="💰 Preço Médio dos Livros por Categoria")
    return HTMLResponse(fig.to_html(full_html=False))


# 📦 Histograma de preços
@router.get("/histograma", response_class=HTMLResponse, summary="Distribuição de preços 📦")
def grafico_histograma(db: Session = Depends(get_db)):
    df = get_livros_df(db)
    if df.empty:
        return HTMLResponse("<h3>Sem dados</h3>")
    fig = px.histogram(df, x="preco", nbins=10, title="📦 Distribuição de Preços dos Livros")
    return HTMLResponse(fig.to_html(full_html=False))


# 📊 Dashboard unificado (todos gráficos na mesma página)
@router.get("/dashboard", response_class=HTMLResponse, summary="Dashboard com todos os gráficos 📊")
def dashboard(db: Session = Depends(get_db)):
    df = get_livros_df(db)
    if df.empty:
        return HTMLResponse("<h3>Sem dados</h3>")

    # Gráficos
    fig_pizza = px.pie(df, names="categoria_id", title="📚 Distribuição de Livros por Categoria")
    df_group = df.groupby("categoria_id")["preco"].mean().reset_index()
    fig_barras = px.bar(df_group, x="categoria_id", y="preco", title="💰 Preço Médio por Categoria")
    fig_hist = px.histogram(df, x="preco", nbins=10, title="📦 Distribuição de Preços")

    # Juntar tudo em um HTML só
    html = """
    <h1>📊 Dashboard de Livros</h1>
    <div style='margin-bottom:50px;'>""" + fig_pizza.to_html(full_html=False) + """</div>
    <div style='margin-bottom:50px;'>""" + fig_barras.to_html(full_html=False) + """</div>
    <div style='margin-bottom:50px;'>""" + fig_hist.to_html(full_html=False) + """</div>
    """

    return HTMLResponse(html)
