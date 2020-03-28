import json
f = open("./counties.txt")
lines = f.readlines()
split = list(map(lambda x: x.splitlines()[0].split("\t"), lines))
labels = split[0]
county_list = split[1:]

fips_map = {}
for i in county_list:
    state, fips, _, county,_,_,_,_,lat,long= i
    fips_map[int(fips)] = {"state":state,"name":county,"lat":float(lat),"long":float(long)}

with open('fips_map_minify.json', 'w') as outfile:
    json.dump(fips_map, outfile)