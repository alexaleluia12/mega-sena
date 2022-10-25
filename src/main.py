import randon_generator as rg

gen = rg.GeneratorPureRandom()
seq = rg.SequenceNumber()
s = seq.create(gen)
print(s)