from functools import reduce
import hashlib as hl
from collections import OrderedDict
import json
from util.hash_util import hash_string_256, hash_block
import pickle

MINING_REWARD = 10

#initializing blochain list
genesis_block = {
        'previous_hash': '', 
        'index': 0, 
        'transactions': [],
        'proof': 100
    }
blockchain = []
open_transactions = []
owner = 'Mangesh'
participants = {'Mangesh'}

def load_data():
    global blockchain
    global open_transactions
    global participants

    try:
        with open('blockchain.txt', mode='r') as f:
            file_content = f.readlines()
            blockchain = json.loads(file_content[0][:-1])
            updated_blockchain = []
            for block in blockchain:
                updated_block = {
                    'previous_hash': block['previous_hash'],
                    'index': block['index'],
                    'proof': block['proof'],
                    'transactions': [OrderedDict(
                        [('sender',tx['sender']),
                        ('recipient',tx['recipient']), 
                        ('amount',tx['amount'])]) 
                        for tx in block['transactions']]
                }
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transactions = json.loads(file_content[1][:-1])
            updated_transactions = []
            for tx in open_transactions:
                updated_transaction = OrderedDict(
                        [('sender',tx['sender']),
                        ('recipient',tx['recipient']), 
                        ('amount',tx['amount'])])
                updated_transactions.append(updated_transaction)
            open_transactions = updated_transactions
            participants = set(json.loads(file_content[2]))
        # with open('blockchain.p', mode='rb') as f:
        #     file_content = pickle.loads(f.read())
        #     global blockchain
        #     global open_transactions
        #     global participants
        #     blockchain = file_content['chain']
        #     open_transactions = file_content['ot']
        #     participants = file_content['participants']
    except (IOError, IndexError):
        genesis_block = {
            'previous_hash': '', 
            'index': 0, 
            'transactions': [],
            'proof': 100
        }
        blockchain = [genesis_block]
        open_transactions = []
        participants = {'Mangesh'}
        print('File not found!')
    finally:
        print('cleanup!')

load_data()

def save_data():
    try:
        with open('blockchain.txt', mode='w') as f:
            # f.write(str(blockchain))
            # f.write('\n')
            # f.write(str(open_transactions))
            f.write(json.dumps(blockchain))
            f.write('\n')
            f.write(json.dumps(open_transactions))
            f.write('\n')
            f.write(json.dumps(list(participants)))
        # with open('blockchain.p', mode='wb') as f:
        #     dict_save_date = {
        #         'chain': blockchain,
        #         'ot': open_transactions,
        #         'participants': participants
        #     }
        #     f.write(pickle.dumps(dict_save_date))
    except IOError:
        print('saving failed!')


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    #guess_hash = hl.sha256(guess).hexdigest()
    guess_hash = hash_string_256(guess)
    #print(guess_hash)
    return guess_hash[0:2] == '00'

def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof

def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    # print('#### s 1')
    # print('tx_sender === ', tx_sender)
    # print('#### e 1')
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    # print('#### s 2')
    # print('open_tx_sender === ', open_tx_sender)
    # print('#### e 2')
    if len(open_tx_sender) > 0:
        tx_sender.append(open_tx_sender)
    # print('#### s 3')
    # print('tx_sender === ', tx_sender)
    # print('#### e 3')
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + (sum(tx_amt) if len(tx_amt)>0 else tx_sum + 0), tx_sender, 0)
    # amount_sent = 0
    # for tx in tx_sender:
    #     if len(tx) > 0:
    #         amount_sent += sum(tx)
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + (sum(tx_amt) if len(tx_amt)>0 else tx_sum + 0), tx_recipient, 0)
    # amount_received = 0
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         amount_received += tx[0]
    # print('amount_received == ',amount_received)
    # print('amount_sent == ',amount_sent)
    return amount_received - amount_sent

def get_last_blockchain_value():
    """ retuns the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transacation(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']

# this functions accepts two arguments
# one required one (transaction_amount) and one optional one (last_transaction)
# the optional one is is optional because it has a default value => [1]

def add_transaction(recipient, sender=owner, amount=1.0):
    """append a new value as well as the last blockchain value to the blockchain
    Arguments:
        :sender: the sender of the coins
        :recipient: the recipient of the coins
        :amount: the amount of coins sent with the transactions (default = 1.0)
    """
    # transaction = {
    #     'sender': sender, 
    #     'recipient': recipient, 
    #     'amount': amount
    # }
    transaction = OrderedDict(
        [('sender',sender), 
         ('recipient',recipient), 
         ('amount',amount)])
    if verify_transacation(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
        return True
    return False

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    # reward_transaction = {
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MINING_REWARD
    # }
    reward_transaction = OrderedDict([('sender','MINING'), ('recipient',owner), ('amount',MINING_REWARD)])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain), 
        'transactions': copied_transactions,
        'proof': proof
    }
    blockchain.append(block)
    # print('--' * 2)
    # print(blockchain)
    # print('--' * 2)
    return True

def get_transaction_value():
    """ returns the input of the user (a new transaction amount) as a float"""
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    #output the blockchain list to the console
    for block in blockchain:
        print('Outputing block')
        print(block)
    print('-' * 20)

def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            print('previous hash is invalid')
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of work is invalid')
            return False
    return True

def verify_transactions():
    # is_valid = True
    # for tx in open_transactions:
    #     if verify_transacation(tx):
    #         is_valid = True
    #     else:
    #         is_valid = False
    # return is_valid
    return all([verify_transacation(tx) for tx in open_transactions])

waiting_for_input = True

while waiting_for_input:
    print('Please choose option')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction')
        else:
            print('Transaction failed')
        # print('--' * 5, ' Open Transactions ', '--' * 5)
        # print(open_transactions)
        # print('--' * 5, ' Open Transactions ', '--' * 5)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
            save_data()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
                blockchain[0] = {
                    'previous_hash': '', 
                    'index': 0, 
                    'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100}]
                }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid')
    if not verify_chain():
        print('Invalid blockchain!')
        print_blockchain_elements()
        break
    print('Balance of {}: {:6.2f}'.format('Mangesh', get_balance('Mangesh')))
else:
    print('User left!')
print('Done!')