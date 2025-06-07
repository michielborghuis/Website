import numpy as np
from tsp_solver.greedy import solve_tsp
from scipy.spatial.distance import pdist, squareform
from geopy.geocoders import Nominatim
import time

start = time.time()

app = Nominatim(user_agent="RouteGenerator")
addresses = [
'Elsenerstraat 31 Rijssen',
'Plaagslagen 8 Rijssen',
'Aalscholver 40 Rijssen',
'Ooievaarstraat 23 Rijssen',
'Markeloseweg 11 Rijssen',
'Schoolstraat 30 Rijssen',
'Paardebloem 18 Rijssen',
'Nassaustraat 39 Rijssen',
'Mulder 22 Rijssen',
'Reigerstraat 52 Rijssen',
'Van Broekhuizenstraat 45 Rijssen',
'Dennenlaan 47 Rijssen',
'Molendijk noord 80 Rijssen',
'Veldovenstraat 13 Rijssen',
'De Stroekeld 116 Rijssen',
'Zuiderstraat 64 Rijssen',
'Petersweg 6 Markelo',
'Veldovenstraat 13 Rijssen',
'Potdijk 8b Markelo',
'Grotestraat 33 Markelo',
'Molenbelterweg 18 Holten',
'Dannenberg 53 Rijssen',
'Gracht 40 Rijssen',
'Esstraat 161a Rijssen'
    ]
url = 'www.google.nl/maps/dir/'


def house_number_start(l):
    for n, i in enumerate(l):
        if len(i) < 5:
            if i[0].isnumeric():
                return n


def url_piece(address_raw):
    l = address_raw['display_name'].split(', ')
    start = house_number_start(l)
    url_pieces = []
    url = ''

    [url_pieces.append(i) for i in l[start + 1].split(' ')]
    url_pieces.append(l[start])
    with open('plaatsnamen_cleaned.txt', 'r', encoding='utf-8') as f:
        plaatsnamen = f.read().splitlines()
    if l[start + 2] in plaatsnamen:
        url_pieces.append(l[start + 2])
    elif l[start + 3] in plaatsnamen:
        url_pieces.append(l[start + 3])
    elif l[start + 4] in plaatsnamen:
        url_pieces.append(l[start + 4])
    elif l[start + 5] in plaatsnamen:
        url_pieces.append(l[start + 5])

    for i in url_pieces:
        url += i + '+'
    return url[:-1] + '/'

addresses_raw = []
wrongs = []
for address in addresses:
    geocoded = app.geocode(address)
    if geocoded:
        addresses_raw.append(geocoded.raw)
    else:
        wrongs.append(address)

latlons = []
for raw in addresses_raw:
    latlons.append((float(raw['lat']), float(raw['lon'])))
long = time.time()
print(long-start)

matrix = squareform(pdist(np.array(latlons)))
matrix[:, 0] = 0


path = solve_tsp(matrix, endpoints=(0, len(addresses)-1))
for i in path:
    url += url_piece(addresses_raw[i])
print(url)

print(time.time()-long)
print(time.time()-start)
