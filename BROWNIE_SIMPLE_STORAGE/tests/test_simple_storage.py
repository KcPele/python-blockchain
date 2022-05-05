from brownie import accounts, config, SimpleStorage

def test_deploy():
    #arrange
    account = accounts[0]
    #act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    #assert
    assert starting_value == expected

def test_updating_storage():
    #arrange
    account = accounts[0]
    #act
    simple_storage = SimpleStorage.deploy({"from": account})
    expected = 15
    updated_value = simple_storage.store(expected, {"from": account})
    #assert
    assert  expected == simple_storage.retrieve()