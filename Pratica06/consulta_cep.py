import requests

def consultar_cep(cep):
    cep = cep.replace("-", "").replace(" ", "")
    
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        
        if 'erro' not in dados:
            return dados
    
    return None

while True:
    cep = input("Digite o CEP (ou 'sair' para sair): ")
    
    if cep.lower() == 'sair':
        break
    
    resultado = consultar_cep(cep)
    
    if resultado:
        print(f"\n✅ Endereço encontrado:")
        print(f"Logradouro: {resultado['logradouro']}")
        print(f"Bairro: {resultado['bairro']}")
        print(f"Cidade: {resultado['localidade']}")
        print(f"Estado: {resultado['uf']}")
        print()
    else:
        print("❌ CEP não encontrado!")
        print()

