from struct import *

packed_data = pack('iif',4,6,7.89)

print(packed_data)

print(calcsize('i'))
print(calcsize('f'))

unpacked_data = unpack('iif',packed_data)

print(unpack('iif',b'\x04\x00\x00\x00\x06\x00\x00\x00\xe1z\xfc@'))
print(unpacked_data)