from web3 import Web3


def transfer(current_address, private_key, contract_address, amount):
    rpc = "https://rpc.ankr.com/eth_goerli"
    web3 = Web3(Web3.HTTPProvider(rpc))
    current_address = Web3.to_checksum_address(current_address)
    contract_address = Web3.to_checksum_address(contract_address)

    # Deposit ETH ABI
    ABI = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"l1Token","type":"address"},{"indexed":true,"internalType":"address","name":"l2Token","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"DepositERC20","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"DepositETH","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"l1Token","type":"address"},{"indexed":true,"internalType":"address","name":"l2Token","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"FinalizeWithdrawERC20","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"FinalizeWithdrawETH","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"defaultERC20Gateway","type":"address"}],"name":"SetDefaultERC20Gateway","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":true,"internalType":"address","name":"gateway","type":"address"}],"name":"SetERC20Gateway","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"ethGateway","type":"address"}],"name":"SetETHGateway","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"ERC20Gateway","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"defaultERC20Gateway","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_gasLimit","type":"uint256"}],"name":"depositERC20","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_gasLimit","type":"uint256"}],"name":"depositERC20","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"uint256","name":"_gasLimit","type":"uint256"}],"name":"depositERC20AndCall","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_gasLimit","type":"uint256"}],"name":"depositETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_gasLimit","type":"uint256"}],"name":"depositETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"},{"internalType":"uint256","name":"_gasLimit","type":"uint256"}],"name":"depositETHAndCall","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"ethGateway","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"finalizeWithdrawERC20","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"finalizeWithdrawETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"getERC20Gateway","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Address","type":"address"}],"name":"getL2ERC20Address","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_ethGateway","type":"address"},{"internalType":"address","name":"_defaultERC20Gateway","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_defaultERC20Gateway","type":"address"}],"name":"setDefaultERC20Gateway","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_tokens","type":"address[]"},{"internalType":"address[]","name":"_gateways","type":"address[]"}],"name":"setERC20Gateway","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_ethGateway","type":"address"}],"name":"setETHGateway","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

    nonce = web3.eth.get_transaction_count(current_address)
    tx = {
        "value": web3.to_wei(amount, 'ether'),
        "nonce": nonce
    }

    contract = web3.eth.contract(address=contract_address, abi=ABI)
    txn = contract.functions.depositETH(
        current_address, web3.to_wei(amount, 'ether'), 0).build_transaction(tx)
    signed_tx = web3.eth.account.sign_transaction(txn, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("https://goerli.etherscan.io/tx/" + web3.to_hex(tx_hash))
    print('waiting for receipt')
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print('complete')


def balance_scroll(current_address):
    rpc = "https://alpha-rpc.scroll.io/l2"
    web3 = Web3(Web3.HTTPProvider(rpc))
    check_sum = web3.to_checksum_address(current_address)
    balance = web3.eth.get_balance(check_sum)
    print(f"Balance on scroll blockchain = {web3.from_wei(balance, 'ether')}")


if __name__ == '__main__':
    current_address = input('Input wallet address:  ')
    private_key = input('Input your private key:  ')
    contract_address = '0xe5e30e7c24e4dfcb281a682562e53154c15d3332'
    amount = float(input('Input amount to send: '))
    transfer(current_address, private_key, contract_address, amount)

    check = input('Do you want to check scroll balance? \n y/n \n')
    balance_scroll(current_address) if check == 'y' else print('...')
