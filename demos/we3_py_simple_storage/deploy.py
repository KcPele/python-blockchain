# read more about the doc //pip install py-solc-x
# python3 -m venv env 
# source env/bin/activate
# pip3 install py-solc-x 
from solcx import compile_standard, install_solc
import json
from web3 import Web3

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

#compile our solidity
install_solc("0.6.0")


compile_sol = compile_standard(
    {
    "language": "Solidity",
    "sources":{"SimpleStprage.sol": {"content": simple_storage_file}},
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
            }
        },
    },

    },
    solc_version="0.6.0"
)
with open("compile_code.json", "w") as file:
    json.dump(compile_sol, file)

#deploying
# pip install web3

bytescode = compile_sol["contracts"]["SimpleStprage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compile_sol["contracts"]["SimpleStprage.sol"]["SimpleStorage"]["abi"]
print(abi)


w3 = Web3(Web3.HTTP)