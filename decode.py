import base58

byte_array = base58.b58decode('2mHyE1uzXFYBEAozEdCKLkbxi1tN8ta19SrwThpEwkxRANWgW6ByukY5yR1CSrbVEWoPpM4dLYJB17EnLoKmVKZc')
json_string = "[" + ",".join(map(lambda b: str(b), byte_array)) + "]"
print(json_string)
