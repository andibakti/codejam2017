import xml.etree.ElementTree as ET
import datetime

tree = ET.parse('test.xml')

#setting the root tag
root = tree.getroot()

#creating another XML tree for output
treeroot = ET.Element("root")
treeroot2 = ET.Element('root')

#array of desirable outputs
params = ['service', 'footway', 'steps', 'pedestrian', 'path']


a = False

print('finding nodes')
for elem in tree.iter(tag='highway'):
    if not params.__contains__(elem.text):
    	a = True
'''
if(a==True):
	print('splash')
	for way in tree.iter(tag='road')
    	road = ET.SubElement(treeroot, "road")
        for tag in way.getchildren:

        	key = tag.tag
           	value = tag.attribute
           	keytag = ET.SubElement(road, key)
           	keytag.text = value
   
'''

treeout = ET.ElementTree(treeroot)
treeout.write("out-test.xml")