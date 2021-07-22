# LST001
balances = Hash(default_value=0)
# LST002
metadata = Hash()
@construct
def seed():
    # LST001 - MINT SUPPLY to wallet that submits the contract
    balances[ctx.caller] = 696969
# LST002
    metadata['token_name'] = "LAMBden"
    metadata['token_symbol'] = "LAMB"
    metadata['operator'] = ctx.caller
    metadata['burn_address'] = '000000000000000000000000000000000000000000000000000000000000dead'
# LST002
@export
def change_metadata(key: str, value: Any):
    assert ctx.caller == metadata['operator'], 'Only operator can set metadata!'
    metadata[key] = value
# LST001
@export
def transfer(amount: float, to: str):
    assert amount > 0, 'Cannot send negative balances!'
    assert balances[ctx.caller] >= amount, 'Not enough coins to send!'
    balances[ctx.caller] -= amount
    balances[to] += (amount * 0.99)
    balances[metadata['burn_address']] += (amount * 0.01)
# LST001
@export
def approve(amount: float, to: str):
    assert amount > 0, 'Cannot send negative balances!'
    balances[ctx.caller, to] += amount
# LST001
@export
def transfer_from(amount: float, to: str, main_account: str):
    assert amount > 0, 'Cannot send negative balances!'
    assert balances[main_account, ctx.caller] >= amount, 'Not enough coins approved to send! You have {} and are trying to spend {}'\
        .format(balances[main_account, ctx.caller], amount)
    assert balances[main_account] >= amount, 'Not enough coins to send!'
    balances[main_account, ctx.caller] -= amount
    balances[main_account] -= amount
    balances[to] += (amount * 0.99)
    balances[metadata['burn_address']] += (amount * 0.01)
