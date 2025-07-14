import pandas as pd
import sys
import os

# Verifica se pelo menos o caminho original foi fornecido
if len(sys.argv) < 2:
    print("Uso: python mudar_base.py caminho/do/arquivo.csv [novo_nome.csv]")
    sys.exit(1)

# Caminho do arquivo original
caminho_arquivo = sys.argv[1]

# Nome do novo arquivo (se fornecido)
if len(sys.argv) >= 3:
    novo_nome = sys.argv[2]
else:
    # Se não for fornecido, prefixa com "nova_"
    nome_original = os.path.basename(caminho_arquivo)
    novo_nome = f"{nome_original}"

# Tenta ler o arquivo original
try:
    df = pd.read_csv(caminho_arquivo)
except FileNotFoundError:
    print(f"Arquivo não encontrado: {caminho_arquivo}")
    sys.exit(1)
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
    sys.exit(1)

# Remove as linhas de índice 1 a 698 (linhas 2 até 699)
df_novo = df.drop(index=range(1, 699))

# Garante que a pasta 'data' existe
os.makedirs('data', exist_ok=True)

# Caminho completo do novo arquivo dentro da pasta 'data'
novo_caminho = os.path.join('data', novo_nome)

# Salva o novo arquivo
df_novo.to_csv(novo_caminho, index=False)

print(f"Novo arquivo salvo em: {novo_caminho}")