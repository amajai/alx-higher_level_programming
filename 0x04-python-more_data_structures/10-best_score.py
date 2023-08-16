#!/usr/bin/python3
def best_score(a_dictionary):
    score_name = None
    if a_dictionary:
        score_num = 0
        for k, v in a_dictionary.items():
            if v > score_num:
                score_num = v
                score_name = k
    return score_name
