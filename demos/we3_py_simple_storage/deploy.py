from solcx import compile_standard
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

#compile our solidity
compile_sol = compile_standard(
    {
    "language": "Solidity",
    "sources":{"SimpleStprage.sol": {"content": simple_storage_file}},
    "setting": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", ""]
            }
        }
    }
    }
)