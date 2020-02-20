# Given a text file words.txt, print out the largest set of anagrams

"""
1. Understand:
    What is an anagram?
    - anagram: a word, phrase, or name formed by rearanging the letters 
    of an other, such as spar, formed from rasp

2. > we need to generate all anagram sets
    - should have the same number of each letter
    - ANAGRAMS should be equal to the original word when both are sorted
    - How do we want to handle case? (ignore case)
   > once all sets are generated, we need to find the largest set
    - utilize some sort of MAX function

3. Implement
"""

def anagrams(words):
    # generate random values for each character a-z
    # set a list of char values initialized to zero (26 list slots)
    # iterate over the len of the char list
        # set the chars at index to a random number

    # create a new dictionary and a signature
    # create an empty dictionary
    # create a integer signature and set it to zero
    
    # use random char values to calculate a value for each word
    # iterate over each word in the words list
        # set each word to lower case

        # iterate over each character in the word
            # find the ordinal value of the char and decrement it by 97
            # and set it to the label of index

            # check if the index is greater than zero and less than 26
                # set the signature to the caharacter at index
            
            # group words with the same value
            # check if the signature is not in anagrams:
                # append the word to the anagrams at signature
                # reset the signature to zero

    # get max entry in the dictionary
    # set max anagrams to the max of the anagram item at the zeroth index
    pass