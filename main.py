union = lambda a,b: list(set([x for x in a+b]))
intersection = lambda a,b: [x for x in a if x in b]
set_diff = lambda u,a: [x for x in u if x not in a]
symmetric_diff = lambda a,b: set_diff(union(a,b), intersection(a,b))
cartesian_prod = lambda a,b: [(x,y) for x in a for y in b]
