x = [1, 2, 3, 4, 5]

import pickle

with open("num_list.pkl", "wb") as a:
    pickle.dump(x, a)


import pickle

num = []

with open("num_list.pkl", "rb") as a:
    num = pickle.load(a)

print(num)
