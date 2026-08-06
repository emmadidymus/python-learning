def names():
    yield "Ross"
    yield "Cate"
    yield "Roman"

gen = names()
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen)) This will raise a StopIteration exception because there are no more values to yield

