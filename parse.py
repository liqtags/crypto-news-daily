from my_custom_package import parse_xml_file, dump_json_pretty

import xml.etree.ElementTree as ET

all_outlines = []
parse_xml_file_path_one = './pythonmodules/my_custom_package/RSSAggregatorforWeb3'
parse_xml_file_path_two = './pythonmodules/my_custom_package/CustomRSS'
parse_array = [parse_xml_file_path_one, parse_xml_file_path_two]

for path in parse_array:
    parse_file_name = path.split('/')[-1]
    print(parse_file_name)

    end_markdownfile_name = parse_file_name + '.md'
    parse_xml_file(path, all_outlines, end_markdownfile_name)
    dump_json_pretty(all_outlines, parse_file_name + '.json')

