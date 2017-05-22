import time
from pvaccess import INT, DOUBLE, STRING, PvObject, PvaServer


def rotate_string(input):
    a = input[0]
    b = input[1:]
    return b + a


def rotate_array(input):
    a = input[0]
    b = input[1:]
    b.append(a)
    return b

# TODO: Can we use one PvaServer for all PVs?

# Create an INT
pv_int = PvObject({'value': INT})
pva_int_server = PvaServer('TEST:INT', pv_int)
pv_int['value'] = 0

# Create a DOUBLE
pv_dbl = PvObject({'value': DOUBLE})
pva_dbl_server = PvaServer('TEST:DBL', pv_dbl)
pv_dbl['value'] = 0.4567

# Create a STRING
pv_str = PvObject({'value': STRING})
pva_str_server = PvaServer('TEST:STR', pv_str)
pv_str['value'] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Create an INT ARRAY
pv_arr = PvObject({'value': [INT]})
pv_arr.setScalarArray([0, 1, 2, 3, 4, 5])
pva_str_server = PvaServer('TEST:ARRAY', pv_arr)

while True:
    pv_int['value'] += 1
    pv_dbl['value'] += 1
    pv_str['value'] = rotate_string(pv_str['value'])
    pv_arr.setScalarArray(rotate_array(pv_arr['value']))
    time.sleep(2)





