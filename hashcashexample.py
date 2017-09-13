import string
import random
import hashlib
import time
example_challenge = '9Kzs52jSfxGJ54Sfjz5gZ111s'

def generation(challenge = example_challenge, size = 25):
    answer = ''.join(random.choice(string.ascii_lowercase
                                   + string.ascii_uppercase
                                   + string.digits) for x in range(size))
    attempt = challenge + answer
    return attempt, answer

shaHash = hashlib.sha256()

def testAttempt():
    Found = False
    start = time.time()
    while Found == False:
        attempt, answer = generation()
        shaHash.update(attempt.encode('utf-8')) 
        solution = shaHash.hexdigest()
        if solution.startswith('00000'):
            timeTook = time.time() - start
            print (solution)
            print ('Time Took:',timeTook)
            Found = True

    print (answer) 
testAttempt()


