import numpy as np

from mango.domain.domain_space import domain_space


def test_domain():
    params = {
        'a': (1, 2, 4),
        'b': np.random.randint(0, 1e6, size=50),
        'c': np.random.uniform(low=-100., high=100., size=(50,))
    }
    print(params)
    ds = domain_space(params, domain_size=100)
    samples = ds.get_domain()

    for sample in samples:
        for param in params.keys():
            assert (sample[param] in params[param])
