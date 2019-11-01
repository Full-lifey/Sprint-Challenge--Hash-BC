#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Loop through tickets, making hash table of route
    for ticket in tickets:

        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # print(hash_table_retrieve(hashtable, 'NONE'))

    key = 'NONE'
    index = 0
    # Loop through hash table until dest == 'NONE'
    # starting with hashtable['NONE']
    while hash_table_retrieve(hashtable, key) != 'NONE':
        print(hash_table_retrieve(hashtable, key))
        # push destination to answer arr
        route[index] = hash_table_retrieve(hashtable, key)
        print('route', route)
        # Set source to dest
        index += 1
        key = hash_table_retrieve(hashtable, key)
    else:
        route[index] = hash_table_retrieve(hashtable, key)
    return route
