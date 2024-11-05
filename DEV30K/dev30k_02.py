import base64
import os
from stellar_sdk import Keypair
from stellar_sdk import Server, TransactionBuilder, Network
from stellar_sdk.exceptions import NotFoundError
from dotenv import load_dotenv, dotenv_values 


def sign_message(message, secret_key):
    keypair = Keypair.from_secret(secret_key)
    message_e = keypair.sign(message.encode())
    signed_message = base64.b64encode(message.encode())
    return signed_message.hex()

message = "DEV30K"
secret_key = "SAWYSQUOVW6H2GL6OXRP4UZRKCW56CIPAVZZUVFRDH7ZAQVICGN5YT2V"
destination_address = "GDBO5PI7NXTGX2RZBZHCBUK4LXQOLNVCQPD36WHHIP6D4TK66Y2HRV26"
signed_message = sign_message(message, secret_key)
print("Mensagem assinada:", signed_message)


server = Server("https://horizon.stellar.org")
def create_transaction(source_secret_key, destination_address, signed_message):
    source_keypair = Keypair.from_secret(source_secret_key)
    source_public_key = source_keypair.public_key

    try:
        source_account = server.load_account(source_public_key)
    except NotFoundError:
        raise Exception("Conta de origem não encontrada na rede Stellar")

    base_fee = server.fetch_base_fee()
    transaction = (
        TransactionBuilder(
            source_account=source_account,
            network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE,
            base_fee=base_fee,
        )
        .add_text_memo(signed_message)  # Adiciona a mensagem assinada como memo
        .append_manage_data_op(data_name="desafio", data_value=signed_message)
        .build()
    )

    transaction.sign(source_keypair)
    response = server.submit_transaction(transaction)
    return response


response = create_transaction(secret_key, destination_address, signed_message)
print("Transação enviada:", response)
