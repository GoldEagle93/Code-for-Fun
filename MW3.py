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
