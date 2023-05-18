from web3 import Web3
import json
import time
from var import contract_keys

web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth_goerli'))

uniswap_contract_abi = json.loads(contract_keys["uniswap_contract_abi"])
uniswap_contract_address = Web3.to_checksum_address(
    contract_keys["uniswap_router_address"])
uniswap_contract = web3.eth.contract(
    address=uniswap_contract_address, abi=uniswap_contract_abi)


# contracts used in path, eth->weth->uni and uni->weth->eth
weth_contract_abi = json.loads(contract_keys["weth_abi"])
weth_contract_address = Web3.to_checksum_address(contract_keys["weth_token"])
weth_contract = web3.eth.contract(
    address=weth_contract_address, abi=weth_contract_abi)
uni_contract_abi = json.loads(contract_keys["uni_abi"])
uni_contract_address = Web3.to_checksum_address(contract_keys["uni_token"])
uni_contract = web3.eth.contract(
    address=uni_contract_address, abi=uni_contract_abi)


def buy_uni_for_eth(eth_out: int, receiver: str):
    path = [Web3.to_checksum_address(
        contract_keys["weth_token"]), Web3.to_checksum_address(contract_keys["uni_token"])]
    amountOutMin = 0
    to = receiver
    gas_price = web3.eth.gas_price
    # added 20 minutes from when the transaction was sent
    deadline = web3.eth.get_block("latest")["timestamp"] + (60 * 20)
    txn = uniswap_contract.functions.swapExactETHForTokens(amountOutMin=amountOutMin, path=path, to=to, deadline=deadline).build_transaction({
        'nonce': web3.eth.get_transaction_count(receiver),
        'value': web3.to_wei(eth_out, 'ether'),
        'gas': 500000,
        'gasPrice': gas_price})
    signed_tx = web3.eth.account.sign_transaction(txn, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    print("Swap ETH => UNI: https://goerli.etherscan.io/tx/" +
          Web3.to_hex(tx_hash) + "\nwaiting")
    try:
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print("buy successful")
        print("Swap ETH => UNI: https://goerli.etherscan.io/tx/" + Web3.to_hex(tx_hash))
    except Exception:
        time.sleep(30)
        pass
    
    
    


def approve(amount: int, contract, receiver: str):
    gas_price = web3.eth.gas_price
    spender = Web3.to_checksum_address(contract_keys["uniswap_router_address"])
    nonce = web3.eth.get_transaction_count(receiver)
    max_amount = web3.to_wei(amount, 'ether')
    approve = contract.functions.approve(spender, max_amount).build_transaction({
        'gasPrice': gas_price,
        'from': receiver,
        'nonce': nonce})
    signed_tx = web3.eth.account.sign_transaction(approve, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(
        f"The approve transaction has been sent! Txn Hash: https://goerli.etherscan.io/tx/{tx_hash.hex()}")
    print(f'Waiting for the approve')
    try:
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Approve passed, back to swap')
        time.sleep(10)
    except Exception:
        time.sleep(30)
        pass
    
    


def sell_uni_for_eth(uni_out: int, receiver: str):
    approve(amount=uni_out, contract=uni_contract, receiver=receiver)
    amountIn = web3.to_wei(uni_out, 'ether')
    amountOutMin = 0
    path = [Web3.to_checksum_address(
        contract_keys["uni_token"]), Web3.to_checksum_address(contract_keys["weth_token"])]
    to = receiver
    gas_price = web3.eth.gas_price
    deadline = web3.eth.get_block("latest")["timestamp"] + (60 * 20)
    txn = uniswap_contract.functions.swapExactTokensForETH(amountIn=amountIn, amountOutMin=amountOutMin, path=path, to=to, deadline=deadline).build_transaction({
        'nonce': web3.eth.get_transaction_count(receiver),
        'gas': 500000,
        'gasPrice': gas_price})

    signed_tx = web3.eth.account.sign_transaction(txn, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Swap UNI => ETH: https://goerli.etherscan.io/tx/" +
          Web3.to_hex(tx_hash) + "\nwaiting")
    try:
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print("sell successful")
    except Exception:
        time.sleep(30)
        pass


def uni_to_weth(uni_out: int, receiver: str):
    approve(amount=uni_out, contract=uni_contract, receiver=receiver)
    amountIn = web3.to_wei(uni_out, 'ether')
    amountOutMin = 0
    path = [Web3.to_checksum_address(
        contract_keys["uni_token"]), Web3.to_checksum_address(contract_keys["weth_token"])]
    to = receiver
    gas_price = web3.eth.gas_price
    deadline = web3.eth.get_block("latest")["timestamp"] + (60 * 20)
    txn = uniswap_contract.functions.swapExactTokensForTokens(amountIn=amountIn, amountOutMin=amountOutMin, path=path, to=to, deadline=deadline).build_transaction({
        'nonce': web3.eth.get_transaction_count(receiver),
        'gas': 500000,
        'gasPrice': gas_price,
        'from': receiver})

    signed_tx = web3.eth.account.sign_transaction(txn, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Swap UNI => WETH: https://goerli.etherscan.io/tx/" +
          Web3.to_hex(tx_hash) + "\nwaiting")
    try:
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print("sell successful")
    except Exception:
        time.sleep(30)
        pass


def weth_to_eth(weth_out: int, receiver: str):
    txn = weth_contract.functions.withdraw(web3.to_wei(weth_out, "ether")).build_transaction({
        'gas': 5000000,
        'nonce': web3.eth.get_transaction_count(Web3.to_checksum_address(receiver))})

    signed_tx = web3.eth.account.sign_transaction(txn, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Swap WETH => ETH: https://goerli.etherscan.io/tx/" +
          Web3.to_hex(tx_hash) + "\nwaiting")
    try:
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print("sell successful")
    except Exception:
        time.sleep(30)
        pass

if __name__ == "__main__":
    receiver = input('Input wallet address:  ')
    private_key = input('Input your private key:  ')
    buy_uni_for_eth(eth_out=0.1, receiver=receiver)
    sell_uni_for_eth(uni_out=5, receiver=receiver)
    uni_to_weth(uni_out=5, receiver=receiver)
    weth_to_eth(weth_out=0.1, receiver=receiver)
