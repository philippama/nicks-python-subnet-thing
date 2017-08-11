# Nick's Python sub-net thing

Nick, to merge the sub-nets from all the files in the directory `./network/data/test`,
you can run the code in subnet.py (except the `if __name__ == '__main__':` bit at the end for the doctests)
to create the Subnets class then do the following:

```
>>> subnets = Subnets.build_from_directory('./network/data/test')
>>> subnets.merge()
```

then you will get a list of merged sub-nets.
