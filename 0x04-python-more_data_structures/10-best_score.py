#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        studes = len(a_dictionary.values())
        if studes > 0:
            maxscore = max(a_dictionary.values())
            for key in a_dictionary.keys():
                if a_dictionary[key] == maxscore:
                    return key
    return None
