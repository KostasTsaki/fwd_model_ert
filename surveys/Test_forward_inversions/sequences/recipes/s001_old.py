import os.path

seq_name = os.path.basename(__file__)[:-3]
bh0 = 'F10.txt'
bh1 = 'F11.txt'
inf = 'inf.txt'
cabling = 'cabling_s001.txt'

seq_recipes = {seq_name:
                   {'seq_parts': [
                       # ______________________
                       # 1 panel
                       # ______________________
                       {'seq_func': 'create_AM_BN',
                        'func_params': {'electrode_strings': {0: bh0, 1: bh1}, 'reciprocals': (0,)}},
                       {'seq_func': 'create_AM_BN',
                        'func_params': {'electrode_strings': {1: bh0, 0: bh1}, 'reciprocals': (0,)}},

                       {'seq_func': 'create_AB_MN',
                        'func_params': {'electrode_strings': {0: bh0, 1: bh1}, 'reciprocals': (0,)}},
                       {'seq_func': 'create_AB_MN',
                        'func_params': {'electrode_strings': {1: bh0, 0: bh1}, 'reciprocals': (0,)}},

                       {'seq_func': 'create_M_BN',
                        'func_params': {'electrode_strings': {0: bh0, 1: bh1, 'inf': inf}}},
                       {'seq_func': 'create_M_BN',
                        'func_params': {'electrode_strings': {1: bh0, 0: bh1, 'inf': inf}}},

                         # ________________
                         # single boreholes
                         # ________________
                         {'seq_func': 'create_AMNB',
                          'func_params': {'electrode_strings': {0: bh1}, 'reciprocals': (0, 4), 'e_sp': range(1,2,1), 'n_sp': range(1,2,1)}},
                         {'seq_func': 'create_ABMN',
                          'func_params': {'electrode_strings': {0: bh1}, 'reciprocals': (0, 4), 'e_sp': range(1,2,1), 'n_sp': range(1,2,1)}},
                         {'seq_func': 'create_AMNB',
                          'func_params': {'electrode_strings': {0: bh0}, 'reciprocals': (0, 4), 'e_sp': range(1,2,1), 'n_sp': range(1,2,1)}},
                         {'seq_func': 'create_ABMN',
                          'func_params': {'electrode_strings': {0: bh0}, 'reciprocals': (0, 4), 'e_sp': range(1,2,1), 'n_sp': range(1,2,1)}}
                        ],
                       'cabling': cabling, 'optimize': True, 'func_params': {}},
               }
