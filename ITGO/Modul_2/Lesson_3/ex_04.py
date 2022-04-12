baz = int(input("Enter a number:"))
foo = int(input("Enter a number:"))

if baz < foo:
    temp = baz
    baz = (baz + foo) / 2
    foo = temp * baz

else:
    temp = foo
    foo = (foo + baz) / 2
    baz = temp * baz

print(baz, foo)
