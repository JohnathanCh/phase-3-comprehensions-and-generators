#!/usr/bin/env python3
import ipdb

def return_evens(num_list):
    # ipdb.set_trace()
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    # ipdb.set_trace()
    return [f"{sentence}!" for sentence in sentence_list]
