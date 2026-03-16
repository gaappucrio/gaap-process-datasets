import os
import requests
import zipfile
from tqdm import tqdm

DATASETS = {
    "1": {
        "id_nome": "3W_Dataset",
        "desc": "Eventos indesejáveis em poços de petróleo (Petrobras)",
        "url": "https://codeload.github.com/petrobras/3W/zip/refs/heads/main"
    },
    "2": {
        "id_nome": "Tennessee_Eastman",
        "desc": "O benchmark clássico de simulação de processos químicos",
        "url": "https://rserve.dataverse.harvard.edu/cgi-bin/zipdownload?b31-eb02b33c11fe"
    },
    "3": {
        "id_nome": "WAID_Dataset",
        "desc": "Base de dados focada em incidentes e integridade de poços (Petrobras)",
        "url": "https://codeload.github.com/petrobras/waid/zip/refs/heads/main"
    },
    "4": {
        "id_nome": "CWRU_Bearing",
        "desc": "Padrão ouro para análise de vibração em rolamentos",
        "url": "https://codeload.github.com/srigas/CWRU_Bearing_NumPy/zip/refs/heads/main"
    }
}

DATA_DIR = "data"

def download_and_extract(dataset_info):
    """Baixa um arquivo .zip e o descompacta na pasta data, se já não existir."""
    name = dataset_info["id_nome"]
    url = dataset_info["url"]
    
    dataset_path = os.path.join(DATA_DIR, name)
    zip_path = os.path.join(DATA_DIR, f"{name}.zip")

    # --- NOVA VERIFICAÇÃO AQUI ---
    # Verifica se a pasta existe E se não está vazia
    if os.path.exists(dataset_path) and os.listdir(dataset_path):
        print(f"\n[!] O dataset '{name}' já foi baixado e extraído em: {dataset_path}")
        print("Pulei o download para economizar tempo e banda.")
        return # Sai da função imediatamente
    # -----------------------------

    os.makedirs(dataset_path, exist_ok=True)
    print(f"\n[{name}] Iniciando o download...")
    
    try:
        # Faz o request com streaming
        response = requests.get(url, stream=True)
        response.raise_for_status() 
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(zip_path, 'wb') as file, tqdm(
            desc=name, total=total_size, unit='B', unit_scale=True, unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
                
        print(f"[{name}] Download concluído. Extraindo arquivos...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(dataset_path)
            
        print(f"[{name}] ✅ Sucesso! Salvo em: {dataset_path}")
        
    except zipfile.BadZipFile:
        print(f"❌ ERRO: O arquivo baixado para {name} não é um .zip válido. Verifique o link.")
    except Exception as e:
        print(f"❌ ERRO: Falha ao processar {name}. Detalhes: {e}")
    finally:
        if os.path.exists(zip_path):
            os.remove(zip_path)

def main():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    while True:
        print("\n==================================================")
        print("   GAAP Process Datasets - Gerenciador de Dados   ")
        print("==================================================")
        print("Escolha o dataset que deseja baixar:\n")
        
        for key, info in DATASETS.items():
            print(f"[{key}] {info['id_nome']} - ({info['desc']})")
            
        print("\n[0] Baixar TODOS os datasets")
        print("[S] Sair")
        print("==================================================")
        
        escolha = input("Digite o número da sua escolha: ").strip().upper()

        if escolha == 'S':
            print("Encerrando o gerenciador. Até mais!")
            break
        elif escolha == '0':
            print("\nIniciando o download de TODOS os datasets...")
            for info in DATASETS.values():
                download_and_extract(info)
            break
        elif escolha in DATASETS:
            download_and_extract(DATASETS[escolha])
            
            continuar = input("\nDeseja baixar outro dataset? (S/N): ").strip().upper()
            if continuar != 'S':
                print("Encerrando o gerenciador. Até mais!")
                break
        else:
            print("\n❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
