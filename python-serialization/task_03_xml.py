#!/usr/bin/python3


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, 'wb') as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        tree = ET.parse(f)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text
        return result

<?xml version='1.0' encoding='utf-8'?>
<data><name>John</name><age>28</age><city>New York</city></data>
