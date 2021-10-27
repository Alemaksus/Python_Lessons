def gen_with_return(start):
    value = start
    while True:
        if value > start + 1:
            return "Enough, I'm sick and tired of this."
        yield value
        value += 1


print(list(gen_with_return(10)))

g = gen_with_return(10)
print(next(g))
print(next(g))
print(next(g))
