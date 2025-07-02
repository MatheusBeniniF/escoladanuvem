import requests

def consultar_cotacao(moeda):
    """Consulta a cotação de uma moeda em relação ao Real"""
    try:
        url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            codigo = f"{moeda}BRL"
            
            if codigo in data:
                cotacao = data[codigo]
                return cotacao
            else:
                return None
        else:
            return None
    except:
        return None

while True:
    moeda = input("Digite o código da moeda (USD, EUR, GBP, etc.) ou 'sair': ").upper().strip()
    
    if moeda == 'SAIR':
        print("Tchau!")
        break
    
    if len(moeda) != 3:
        print("❌ Digite um código de moeda válido (3 letras)")
        continue
    
    print(f"🔍 Consultando cotação de {moeda}...")
    
    cotacao = consultar_cotacao(moeda)
    
    if cotacao:
        print(f"\n💰 Cotação {moeda}/BRL:")
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Valor máximo: R$ {cotacao['high']}")
        print(f"Valor mínimo: R$ {cotacao['low']}")
        print(f"Última atualização: {cotacao['create_date']}")
        print()
    else:
        print(f"❌ Moeda {moeda} não encontrada ou erro na consulta.")
        print()
