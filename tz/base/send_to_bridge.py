from web3 import Web3


def transfer(current_address, private_key, destination_address, amount):
    rpc = "https://rpc.ankr.com/eth_goerli"
    web3 = Web3(Web3.HTTPProvider(rpc))
    gas_price = int(web3.eth.gas_price * 1.1)
    current_address = Web3.to_checksum_address(current_address)
    private_key = private_key
    destination_address = Web3.to_checksum_address(destination_address)

    balance = web3.eth.get_balance(current_address)
    nonce = web3.eth.get_transaction_count(current_address)

    tx = {
        'nonce': nonce,
        'chainId': 5,
        'to': destination_address,
        'value': amount,
        'gas': 100000,
        'gasPrice': gas_price
    }

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("https://goerli.etherscan.io/tx/" + web3.to_hex(tx_hash))
    print('waiting for receipt')
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print('complete')


def balance_base(current_address):
    rpc = "https://goerli.base.org"
    web3 = Web3(Web3.HTTPProvider(rpc))
    check_sum = web3.to_checksum_address(current_address)
    balance = web3.eth.get_balance(check_sum)
    print(f"Balance on base blockchain = {web3.from_wei(balance, 'ether')}")


if __name__ == '__main__':
    current_address = input('Input wallet address:  ')
    private_key = input('Input your private key:  ')
    destination_address = '0xe93c8cd0d409341205a592f8c4ac1a5fe5585cfa'
    amount = float(input('Input amount to send: '))

    transfer(current_address, private_key, destination_address, amount)
    check = input('Do you want to check base balance? \n y/n \n')
    balance_base(current_address) if check == 'y' else print('...')
