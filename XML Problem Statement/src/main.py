import xml.etree.ElementTree as elementTree

sources = {}
target_list = []

data_flow_xml_tree = elementTree.parse('../resources/wf_src_idw_cntry_multi_def_cd.xml')
for folder in data_flow_xml_tree.findall('.//FOLDER'):
    # Incomplete logic due to time constraint
    #
    # for mapping in folder.findall('.//MAPPING'):
    #     for transformation in mapping.findall('.//TRANSFORMATION'):
    #
    for source in folder.findall('.//SOURCE'):
        sources[source.attrib['NAME']] = source.attrib['DBDNAME']
    for target in folder.findall('.//TARGET'):
        target_list.append(target.attrib['NAME'])

print("Source -> Target with no transformations")
for target in target_list:
    print(sources[target] + '->' + target)
