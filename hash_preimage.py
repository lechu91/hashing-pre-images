import hashlib
import os
import random
import string

def hash_preimage(target_string):
    if not all([x in '01' for x in target_string]):
        print("Input should be a string of bits")
        return

    # Collision finding code goes here

    k = len(target_string)
    mask = int(''.join(['0' for i in range(256 - k)] + ['1' for i in range(k)]), 2)
    letters = string.ascii_letters
    target_binary = int(target_string,2)

    while True:
        x = (''.join(random.choice(letters) for _ in range(random.randint(1, 10)))).encode('utf-8')
        hash_x = hashlib.sha256(x).hexdigest()
        comp_x = int(hash_x, 16) & mask
        if comp_x == target_binary:
            break
            
    nonce = x

    return nonce
