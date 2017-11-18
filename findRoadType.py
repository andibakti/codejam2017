import xml.etree.ElementTree as ET
import datetime

#parsing the data file from opensourcemaps
print('parsing...')
print(datetime.datetime.now())

tree = ET.parse('new york city2.xml')

print('done parsing!')
print(datetime.datetime.now())

#setting the root tag
root = tree.getroot()

#creating another XML tree for output
treeroot = ET.Element("root")
treeroot2 = ET.Element('root')

#array of desirable outputs
params = ['highway', 'maxspeed', 'name', 'oneway', 'bicycle','lanes']

a=0

print('finding nodes...')
print(datetime.datetime.now())
for way in root.findall('way'):
    id = way.get('id')
    road = ET.SubElement(treeroot, "road")
    idtag = ET.SubElement(road, 'id')
    idtag.text = id
    #ET.SubElement(road, "param", "id=").text = id
    #print('id: ' + id)
    if (a >-1):
        a = a + 1
        for tag in way.findall('tag'):

            key = tag.get('k')
            if(params.__contains__(key)):
               value = tag.get('v')
               keytag = ET.SubElement(road, key)
               keytag.text = value
    else:
        break


    children = len(road.getchildren())
    if(children==1):
        treeroot.remove(road)
        '''
        road = ET.SubElement(treeroot2, 'road')
        idtag = ET.SubElement(road, 'id')
        idtag.text = id
        
        '''


treeout = ET.ElementTree(treeroot)
treeout.write("out7.xml")

treeout2 = ET.ElementTree(treeroot2)
#treeout2.write("missinginfo.xml")

print('done!')
print(datetime.datetime.now())