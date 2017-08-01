#!/usr/bin/env python
'''
Using ciscoconfparse find the crypto maps that are not using AES (based-on the
transform set name). Print these entries and their corresponding transform set
name.
'''

import re
from ciscoconfparse import CiscoConfParse

from pprint import pprint

def main():
    cisco_file = "cisco_ipsec.txt"
    cisco_cfg = CiscoConfParse( cisco_file )

    crypto_maps = cisco_cfg.find_objects_wo_child( parentspec=r'crypto map CRYPTO', childspec=r'AES' )

    print "Crypto maps not using AES: "
    for cmap in crypto_maps:
	for child in cmap.children:
	    if 'transform' in child.text:
		match = re.search(r"set transform-set (.*)$", child.text)
		encryption = match.group(1)
	print "  {0} >>> {1}".format(cmap.text.strip(), encryption)


if __name__ == "__main__":
    main()
