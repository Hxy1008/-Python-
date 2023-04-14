import pickle

ls = ["123", "32134", "4325435", "645yyth", "afdlfdldd"]

bs = pickle.dumps(ls)
print(bs)
lst = pickle.loads(bs)
print(lst)