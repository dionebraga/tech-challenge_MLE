import requests
import matplotlib.pyplot as plt

# URL da sua API rodando localmente
API_URL = "http://127.0.0.1:8000/api/v1/relatorios/categorias"

def gerar_grafico():
    response = requests.get(API_URL)
    if response.status_code != 200:
        print("❌ Erro ao buscar dados:", response.text)
        return

    data = response.json()

    categorias = [item["categoria"] for item in data]
    quantidades = [item["quantidade"] for item in data]

    # 📊 Gráfico de barras
    plt.figure(figsize=(8, 5))
    plt.bar(categorias, quantidades)
    plt.title("Distribuição de Livros por Categoria 📚")
    plt.xlabel("Categoria")
    plt.ylabel("Quantidade de Livros")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    gerar_grafico()
