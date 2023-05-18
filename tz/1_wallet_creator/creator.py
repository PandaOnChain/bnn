from bip_utils import Bip39WordsNum, Bip39MnemonicGenerator
from eth_account import Account
from web3.auto import w3

number_of_wallets_input = int(input("How many wallets you want to get: "))


def creator():
    w3.eth.account.enable_unaudited_hdwallet_features()
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
    private_key = Account.from_mnemonic(
        str(mnemonic), account_path="m/44'/60'/0'/0/0")._private_key.hex()
    address = Account.from_key(str(private_key)).address
    print(f'{address}  ---  {private_key}  \n {mnemonic} \n =======================')

    fileVar = open(f"{numberOfWalletsInput}_wallets.txt", "a")
    fileVar.write(address + ':' + private_key + ':' + str(mnemonic) + '\n')
    fileVar.close()


if __name__ == '__main__':
    for i in range(number_of_wallets_input):
        creator()
