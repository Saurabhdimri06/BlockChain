#import bitcoin
from bitcoin import *

#Generate Private Key
my_private_key = random_key()
print("Private Key: %s\n" %my_private_key)

#Generate Private Key
my_public_key = privtopub(my_private_key)
print("Public Key: %s\n" %my_public_key)
print

#Create a Bitcoin Address
my_bitcoin_address = pubtoaddr(my_public_key)
print("Bitcoin Address: %s\n" %my_bitcoin_address)
