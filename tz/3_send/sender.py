from web3 import Web3
import time
from var import contract_keys
from json import loads


def transfer(current_address, private_key, destination_address, amount):
    rpc = "https://rpc.ankr.com/eth_goerli"
    web3 = Web3(Web3.HTTPProvider(rpc))
    gas_price = int(web3.eth.gas_price * 1.1)
    current_address = Web3.to_checksum_address(current_address)
    receiver = Web3.to_checksum_address(receiver)
    nonce = web3.eth.get_transaction_count(current_address)

    tx = {
        'nonce': nonce,
        'chainId': 5,
        'to': receiver,
        'value': amount,
        'gas': 100000,
        'gasPrice': gas_price
    }

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("https://goerli.etherscan.io/tx/" + web3.to_hex(tx_hash))
    print('Waiting for receipt')
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print('complete')


def transfer_erc(current_address, private_key, destination_address, amount, token):
    rpc = "https://rpc.ankr.com/eth_goerli"
    web3 = Web3(Web3.HTTPProvider(rpc))
    gas_price = web3.eth.gas_price
    current_address = Web3.to_checksum_address(current_address)
    receiver = Web3.to_checksum_address(destination_address)
    nonce = web3.eth.get_transaction_count(current_address)
    if token == "WETH":
        contract_abi = loads(contract_keys["weth_abi"])
        contract_address = Web3.to_checksum_address(
            contract_keys["weth_token"])
    elif token == "UNI":
        contract_abi = loads(contract_keys["uni_abi"])
        contract_address = Web3.to_checksum_address(contract_keys["uni_token"])
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    tx = {
        'from': current_address,
        'nonce': web3.eth.get_transaction_count(current_address),
        'gasPrice': gas_price * 10,
        'gas': 500000
    }
    transaction = contract.functions.transfer(
        receiver, Web3.to_wei(amount, 'ether')).build_transaction(tx)
    signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("https://goerli.etherscan.io/tx/" + web3.to_hex(tx_hash))
    print('Waiting for receipt')
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print('complete')


if __name__ == '__main__':
    current_address = input('Input wallet address:  ')
    private_key = input('Input your private key:  ')
    receiver = input('Input destination address:  ')
    amount = float(input('Input amount to send: '))
    token = input(
        'Which token you want to transfer (input number) \n1 - ETH \n2 - WETH \n3 - UNI\n\n')
    match token:
        case '1':
            transfer(current_address, private_key, receiver, amount)
        case '2':
            transfer_erc(current_address, private_key,
                         receiver, amount, 'WETH')
        case '3':
            transfer_erc(current_address, private_key,
                         receiver, amount, 'UNI')
        case _:
            print('you inputed invalid value...')
