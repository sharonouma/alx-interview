#!/usr/bin/python3
"""
Module containing a function to find the minimum number of coins
required make up a given amount.
"""


def makeChange(coins, total):
    """
    Given a list of coin denominations and a total value to be paid,
    return the minimum number of coins required to make up that amount.
    """
    if total <= 0:
        return 0

    amountsArray = [float('inf')] * (total + 1)
    amountsArray[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            amountsArray[i] = min(amountsArray[i], amountsArray[i - coin] + 1)

    return amountsArray[total] if amountsArray[total] != float('inf') else -1
