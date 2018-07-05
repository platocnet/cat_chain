import hashlib as hash
import datetime as dt
from flask import Flask
from flask import request

# import flask as Flask

class CatBlock(object):
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha256 = hash.sha256()
        sha256.update((str(self.index) +
                      str(self.timestamp) +
                      str(self.data) +
                      str(self.prev_hash)).encode("utf-8"))
        return sha256.hexdigest()


def next_block(last_block):
    index = last_block.index + 1
    timestamp = dt.datetime.now()
    data = "kevin" + str(index)
    hash = last_block.hash
    return CatBlock(index, timestamp, data, hash)


if __name__ == "__main__":
    app = Flask(__name__)

    this_nodes_transactions = []

    @app.route("/txion", methods=["POST"])
    def transaction():
        if request.method == "POST":
            new_txion = request.get_json()
            this_nodes_transactions.append(new_txion)

            print("new transaction")
            print("from: {}".format(new_txion["from"]))
            print("to: {}".format(new_txion["to"]))
            print("amount: {}\n".format(new_txion["amount"]))

            return "transaction submission successful\n"

    app.run()

    # last_block = CatBlock(0, dt.datetime.now(), "first block", 0)
    # block_chain = [last_block]
    #
    # num_block = 20
    #
    # for i in range(num_block):
    #     block_to_add = next_block(last_block)
    #     block_chain.append(block_to_add)
    #     last_block = block_to_add
    #
    #     print("Block #-{} has been added to the blockchain!".format(block_to_add.index))
    #     print("Hash: {}\n".format(block_to_add.hash))
