from web3 import Web3
from json import loads
from var import contract_keys
import requests
from bs4 import BeautifulSoup
import lxml
from fake_useragent import UserAgent

web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth_goerli'))

weth_contract_abi = loads(contract_keys["weth_abi"])
weth_contract_address = Web3.to_checksum_address(contract_keys["weth_token"])
weth_contract = web3.eth.contract(
    address=weth_contract_address, abi=weth_contract_abi)
uni_contract_abi = loads(contract_keys["uni_abi"])
uni_contract_address = Web3.to_checksum_address(contract_keys["uni_token"])
uni_contract = web3.eth.contract(
    address=uni_contract_address, abi=uni_contract_abi)


def checker(address):
    rpc = "https://rpc.ankr.com/eth_goerli"
    web3 = Web3(Web3.HTTPProvider(rpc))
    check_sum = web3.to_checksum_address(address)
    balance_eth = web3.eth.get_balance(check_sum)
    get_currency(web3.from_wei(balance_eth, "ether"), "ethereum")

    balance_weth = weth_contract.functions.balanceOf(check_sum).call()
    get_currency(web3.from_wei(balance_weth, "ether"), "weth")

    balance_uni = uni_contract.functions.balanceOf(check_sum).call()
    get_currency(web3.from_wei(balance_uni, "ether"), "uniswap")


def get_currency(amount, token):
    url = f"https://coinmarketcap.com/currencies/{token}/"  # uniswap/#weth/
    headers = {"User-Agent": UserAgent(browsers=['edge', 'chrome']).random}
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    current = soup.find("div", {"class": "sc-aef7b723-0 dDQUel priceSection"}
                        ).find("span").text.replace("$", "").replace(",", "")
    print(f"{token}: ${current}")
    print(f'balance: {amount} (${float(current)*float(amount)})')
    print("----------------------------------------------")


if __name__ == '__main__':
    wallet_address = input('Input wallet address  -  ')
    checker(wallet_address)
