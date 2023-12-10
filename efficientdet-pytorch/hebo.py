import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import pandas as pd
import numpy as np
from hebo.design_space.design_space import DesignSpace
from hebo.optimizers.hebo import HEBO

import train


if __name__ == "__main__":
    N_TRAILS = 20

    space = DesignSpace().parse(
        [{'name': 'lr', 'type': 'num', 'lb': 1e-3, 'ub': 1e-1},
         {'name': 'model', 'type': 'cat', 'categories' : ['auto', 'sqrt', 'log2']}
        ])
    opt = HEBO(space, rand_sample=2)
    for i in range(N_TRAILS):
        rec = opt.suggest(n_suggestions=1)
        print(rec)
        acc = train.main_hpo(rec)
        opt.observe(rec, np.array(acc))
        print('After %d iterations, best obj is %.2f' % (i, opt.y.min()))
