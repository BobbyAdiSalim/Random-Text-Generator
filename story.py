"""Generating a random story.
"""

import random
from typing import TextIO


def generate_random_story(data_file: TextIO, context_size: int,
                          num_words: int) -> str:
    """Return a randomly generated story with num_words words based on a
    context of context_size words from the text in data_file.
    """
    # store a list of words from the story
    story = data_file.read().split()
    # context to words dictionary
    context_to_words = {}
    # builds the dictionary
    for i in range(len(story) - context_size):
        # index ofword after the context
        end = i + context_size
        context = tuple(story[i:end])
        # check if context is already in the dictionary
        if context in context_to_words:
            context_to_words[context].append(story[end])
        else:
            context_to_words[context] = [story[end]]
    # the dictionary is built now

    # makes a list of the words that will be returned, start it off with a
    # random context from the helper function
    stry_lst = list(get_random_context(context_to_words))
    # builds the random new story in a list
    # loop stops when length of stry_lst reaches num_words
    while len(stry_lst) < num_words:
        # new context = the last 'context_size' words
        n_context = tuple(stry_lst[-context_size:])
        # check if the new context is in the dictionary
        if n_context in context_to_words:
            stry_lst.append(random.choice(context_to_words[n_context]))
        else:
            stry_lst.extend(get_random_context(context_to_words))

    # converts the list to string
    n_stry = ''
    for word in stry_lst:
        n_stry += word + ' '
    return n_stry


# A helper function
def get_random_context(context_to_words: dict[tuple, list[str]]) -> tuple:
    """Return a random context (key) from context_to_words."""

    return random.choice(list(context_to_words.keys()))



filename = input('Enter a filename: ')
with open(filename) as training_file:
    print(generate_random_story(training_file, 10, 100))
pass
