import datetime
from hashids import Hashids

timestamp = int(datetime.datetime.now().strftime("%y%m%d%H%M%S"))

hs = Hashids()

hashFileName = hs.encode(timestamp)

print(hashFileName)