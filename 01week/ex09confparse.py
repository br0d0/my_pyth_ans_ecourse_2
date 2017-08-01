#!/usr/bin/env python
'''
Use the ciscoconfparse library to find the crypto maps that are using pfs group2 in cisco_ipsec.txt
'''

from ciscoconfparse import CiscoConfParse

from pprint import pprint

def main():
    cisco_file = "cisco_ipsec.txt"
    cisco_cfg = CiscoConfParse( cisco_file )

    crypto_maps = cisco_cfg.find_objects_w_child( parentspec=r'crypto map CRYPTO', childspec=r'set pfs group2' )

    print "Crypto maps using PFS group2: "
    for cmap in crypto_maps:
	print "  {0}".format( cmap.text )
    print


if __name__ == "__main__":
    main()
