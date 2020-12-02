import os.path


def recipe(seq_name='sXXX', cabling='cabling_day_X.txt', bh0='FXX.txt', bh1='FYY.txt', bh2='FZZ.txt', inf='inf.txt'):

    seq_recipe = \
        {seq_name:
            {'seq_parts':
             [{'seq_func': 'create_AM_BN', 'func_params': {'electrode_strings': {0: bh0, 1: bh1}, 'reciprocals': (0,)}},
              {'seq_func': 'create_AM_BN', 'func_params': {'electrode_strings': {1: bh0, 0: bh1}, 'reciprocals': (0,)}},
              {'seq_func': 'create_AM_BN', 'func_params': {'electrode_strings': {0: bh1, 1: bh2}, 'reciprocals': (0,)}},
              {'seq_func': 'create_AM_BN', 'func_params': {'electrode_strings': {1: bh1, 0: bh2}, 'reciprocals': (0,)}},
              {'seq_func': 'create_AB_MN', 'func_params': {'electrode_strings': {0: bh0, 1: bh1}, 'reciprocals': (0,)}},
              {'seq_func': 'create_AB_MN', 'func_params': {'electrode_strings': {1: bh0, 0: bh1}, 'reciprocals': (0,)}},
              {'seq_func': 'create_AB_MN', 'func_params': {'electrode_strings': {0: bh1, 1: bh2}, 'reciprocals': (0,)}},
              {'seq_func': 'create_AB_MN', 'func_params': {'electrode_strings': {1: bh1, 0: bh2}, 'reciprocals': (0,)}},
              {'seq_func': 'create_M_BN', 'func_params': {'electrode_strings': {0: bh0, 1: bh1, 'inf': inf}}},
              {'seq_func': 'create_M_BN', 'func_params': {'electrode_strings': {1: bh0, 0: bh1, 'inf': inf}}},
              {'seq_func': 'create_M_BN', 'func_params': {'electrode_strings': {0: bh1, 1: bh2, 'inf': inf}}},
              {'seq_func': 'create_M_BN', 'func_params': {'electrode_strings': {1: bh1, 0: bh2, 'inf': inf}}},
              {'seq_func': 'create_AMNB', 'func_params': {'electrode_strings': {0: bh0}, 'reciprocals': (0, 4)}},
              {'seq_func': 'create_ABMN', 'func_params': {'electrode_strings': {0: bh0}, 'reciprocals': (0, 4)}},
              {'seq_func': 'create_AMNB', 'func_params': {'electrode_strings': {0: bh1}, 'reciprocals': (0, 4)}},
              {'seq_func': 'create_ABMN', 'func_params': {'electrode_strings': {0: bh1}, 'reciprocals': (0, 4)}},
              {'seq_func': 'create_AMNB', 'func_params': {'electrode_strings': {0: bh2}, 'reciprocals': (0, 4)}},
              {'seq_func': 'create_ABMN', 'func_params': {'electrode_strings': {0: bh2}, 'reciprocals': (0, 4)}}
              ],
                'cabling': cabling, 'optimize': True,
                'func_params': {},
                'recipe': os.path.splitext(os.path.basename(__file__)),
                'author': 'O. Kaufmann',
                'date': '20161023',
                'description': 'A sequence for acquisition of two panels (bh0,bh1) and (bh1,bh2) between three boreholes'
                               ' using AB_MN, AM_BN and M_BN arrays.'},
         }
    return seq_recipe
