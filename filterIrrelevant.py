#remove values with irrelevant information 
# such as data with only IDs and data with only names

import xml.etree.ElementTree as ET
import datetime
import json

tags = ['bicycle','highway', 'lanes', 'maxspeed', 'name', 'oneway']
params = ['service', 'footway', 'steps', 'pedestrian', 'path']


treeroot = ET.Element("root")


#parsing the data file from opensourcemaps
print('parsing...')
print(datetime.datetime.now())

tree = ET.parse('out-montreal.xml')

print('done parsing!')
print(datetime.datetime.now())

root = tree.getroot()



print('removing invalid inputs and IDs')
for road in root.findall('road'):
	if(len(road.getchildren()) < 3):
		root.remove(road)
		continue
	for tag in road:
		if(tag.tag == 'highway'):
			if(params.__contains__(tag.text)):
				root.remove(road)
		if(tag.tag == 'id'):
			road.remove(tag)

print(datetime.datetime.now())


print('creating dictionary')
streetDitc = dict()
for road in root.findall('road'):
    key = ""
    values = dict()
    for tag in road:
        if(tag.tag == 'name'):
            key = tag.text
        else:
            values[tag.tag] = tag.text
    streetDitc[key] = values


print(datetime.datetime.now())

print('adding missing params and removing unnecessary values')

for key in list(streetDitc):
    values = streetDitc[key]

    if(len(values)<3):
        del streetDitc[key]
        continue
    if(params.__contains__(values['highway'])):
        del streetDitc[key]
        continue

    for tag in tags:
        if(tag not in values):
            values[tag] = None
     
json = json.dumps(streetDitc)
f = open("streetDictionary.json", "w")
f.write(json)
f.close()

tree.write('test.xml')





