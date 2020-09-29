"""
Several years ago I used to play Call of Duty Modern Warfare 3
on a local network with some friends. The games reads a .dspl file
in which each line defines three parameters:
1. Type of game,
2. Map,
3. Probability of that combination.

The game didn't do a good job at choosing lines randomly when all
the probabilities were equal. So I made this script which would
generate a new .dspl file with random combinations of maps and
game types for one game session. Every night we wanted to play
I got a new .dspl file from this script and the randomness was
guaranteed!
"""

import random

firstPart=[ 'mp_alpha',         'mp_bootleg',       'mp_bravo',         'mp_carbon',        'mp_dome',          'mp_exchange',
            'mp_hardhat',       'mp_interchange',   'mp_lambeth',       'mp_mogadishu',     'mp_paris',         'mp_plaza2',
            'mp_radar',         'mp_seatown',       'mp_underground',   'mp_village',       'mp_italy',         'mp_morningwood',
            'mp_overwatch',     'mp_park',          'mp_cement',        'mp_hillside_ss',   'mp_meteora',       'mp_qadeem',
            'mp_restrepo_ss',   'mp_burn_ss',       'mp_crosswalk_ss',  'mp_six_ss',        'mp_boardwalk',     'mp_moab',
            'mp_nola',          'mp_roughneck',     'mp_shipbreaker',   'mp_aground_ss',    'mp_courtyard_ss',  'mp_terminal_cls']

secondPart=['FFA_default', 'TDM_default','KC_default', 'SD_default', 'CTF_default', 'DZ_default', 'HQ_default', 'INF_default', 'OIC_default',
            'GG_default', 'SAB_default', 'TDEF_default', 'DOM_default', 'SD_default', 'SD_default', 'SD_default', 'CTF_default', 'HQ_default', 'SD_default', 'SD_default']

indices = random.sample(range(1, 36), 20)

open('tonight.dspl', 'w').close()
secI = 0
while secI <= 19:
    for i in indices:
        with open ("tonight.dspl","a") as file:
            file.write(firstPart[i]+','+secondPart[secI]+',500' + '\n')
        secI = secI + 1
print(
'-----------------------------------------------------------------'+ '\n'
'Generated (replaced) new MW3 multiplayer DSPL file: tonight.dspl'+ '\n'
'-----------------------------------------------------------------'+ '\n'
)
