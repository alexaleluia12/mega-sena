from src import randon_generator as rg

def test_pure_random():
    generator = rg.GeneratorPureRandom()
    ns = rg.SequenceNumber()

    created_numbers = ns.create(generator)

    assert len(created_numbers) == 6
    cp_numbers = created_numbers.copy()
    cp_numbers.sort()
    assert cp_numbers == created_numbers

def test_bf_low():
    generator = rg.GeneratorBFLow()
    ns = rg.SequenceNumber()

    created_numbers = ns.create(generator)

    assert len(created_numbers) == 6
    cp_numbers = created_numbers.copy()
    cp_numbers.sort()
    assert cp_numbers == created_numbers

def test_aa_low():
    generator = rg.GeneratorAALow()
    ns = rg.SequenceNumber()

    created_numbers = ns.create(generator)

    assert len(created_numbers) == 6
    cp_numbers = created_numbers.copy()
    cp_numbers.sort()
    assert cp_numbers == created_numbers