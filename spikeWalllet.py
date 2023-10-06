from binance.spot import Spot
import config


client = Spot(config.API_KEY,config.API_SECRET_KEY)


# Define los detalles del retiro
coin = 'USDT'
address = 'TSxaaiVwsuUTMYvKwBU1Fxv135Axmabjy1'  # La dirección de la billetera a la que deseas enviar
amount = 10.0
name = 'Retiro prueba 1'
network = 'TRC20'  # Especifica que deseas usar la red TRC20


# Realiza el retiro
response = client.withdraw(
    coin = coin,
    amount = amount,
    address = address,
    name = name,
    network = network
)
print(response)