#!usr/bin/env python
from __future__ import print_function
import operator

'''
This script calculates the aggregate input/output bandwidth
through the system by summing the 30 second and 5 minute bandwidth
values from all physical interfaces.  The aggregate bandwidths
are displayed,  as well as the interface name and description of
the 10 busiest interfaces in the system (top talkers).

Installation

Copy the script to bootflash:/scripts and then execute the following
command:

source bwutil2.py

You can also create a CLI alias:

conf t
cli alias name bwutil source bwutil2.py

Example output:

I02AVDCCOREZ1# bwutil

--- Aggregate System Bandwidth Utilization ---

--- 30 Second ---
 Input(bps):  508,379,416
Output(bps):  513,100,056


--- 5 Minute ---
 Input(bps): 504,135,528
Output(bps): 506,043,488


Input Top Talkers (30 second):

Interface       Description                                bps
----------------------------------------------------------------------
Ethernet6/3    Link to sw6504-id-2 - Ten1/4                109,582,104
Ethernet6/8    SW-6509-CORE-1 Te6/1                         87,631,688
Ethernet6/17   SW-6509-CORE-2 - G3/17                       73,778,208
Ethernet6/2    Link to sw6504-id-1 - Ten1/4                 61,251,824
Ethernet6/5    Link to sw6504-wd-2 - Ten1/4                 52,814,568
Ethernet6/4    Link to sw6504-wd-1 - Ten1/4                 38,212,528
Ethernet6/25   SW-6509-CORE-2 - G3/18                       33,373,720
Ethernet6/6    Link to sw6504-md-1 Ten1/4                   22,038,912
Ethernet6/7    Link to sw6504-md-2 Ten1/4                   19,764,864
Ethernet6/11   To I02AC65IPTDZ2 T1/5                         6,847,360


Output Top Talkers (30 second):

Interface       Description                                bps
----------------------------------------------------------------------
Ethernet6/5    Link to sw6504-wd-2 - Ten1/4                122,374,416
Ethernet6/8    SW-6509-CORE-1 Te6/1                        119,960,856
Ethernet6/4    Link to sw6504-wd-1 - Ten1/4                107,731,904
Ethernet6/6    Link to sw6504-md-1 Ten1/4                   73,053,664
Ethernet6/7    Link to sw6504-md-2 Ten1/4                   38,190,592
Ethernet6/2    Link to sw6504-id-1 - Ten1/4                 27,205,728
Ethernet6/3    Link to sw6504-id-2 - Ten1/4                 20,670,576
Ethernet6/10   To I02AC65IPTDZ1 T1/4                         1,692,136
Ethernet6/11   To I02AC65IPTDZ2 T1/5                         1,440,016
Ethernet2/21   I02AN77DISTZ1 - Eth2/21                         257,392
'''

load_int1_input = 0
load_int2_input = 0
load_int1_output = 0
load_int2_output = 0
input_talker_list = []
output_talker_list = []
int_list = []

print ('Gathering interface statistics, please wait...')
sh_int_status = clid('show int status | i connected')

# Get the interfaces to look at
for key in sh_int_status.keys():
    if 'interface/interface' in key:
        if 'Eth' in sh_int_status[key]:
            int_list.append(sh_int_status[key])

# Loop over interfaces, grab show interface output for each, and save the
# interface name, description, and rates to a list.  Note:  load-int1 = 30 second, load-int2 = 5 minute.
for iface in int_list:
    if 'Eth' in iface:
        output = clid('show interface {0}'.format(iface))
        intf = output['TABLE_interface/interface/1']
        if_load_int1_input = int(output['TABLE_interface/eth_inrate1_bits/1'])
        if_load_int2_input = int(output['TABLE_interface/eth_inrate2_bits/1'])
        if_load_int1_output = int(output['TABLE_interface/eth_outrate1_bits/1'])
        if_load_int2_output = int(output['TABLE_interface/eth_outrate2_bits/1'])
        if 'TABLE_interface/desc/1' in output:
            ifdesc = output['TABLE_interface/desc/1']
        else:
            ifdesc = '---'
        load_int1_input += if_load_int1_input
        load_int2_input += if_load_int2_input
        load_int1_output += if_load_int1_output
        load_int2_output += if_load_int2_output
        input_talker_list.append((intf, ifdesc, if_load_int1_input))
        output_talker_list.append((intf, ifdesc, if_load_int1_output))

# Sort the lists.  Since they are lists of tuples,  the operator.itemgetter() function as the sort key
# provides the ability to sort by the 3rd element of each tuple which is the interface bandwidth.
sorted_input_talkers = sorted(input_talker_list, key=operator.itemgetter(2), reverse=True)
sorted_output_talkers = sorted(output_talker_list, key=operator.itemgetter(2), reverse=True)

print ('\n--- Aggregate System Bandwidth Utilization ---\n')
print ('--- 30 Second ---')
print (' Input(bps):  {0}'.format(str("{:,}".format(load_int1_input))))
print ('Output(bps):  {0}'.format(str("{:,}".format(load_int1_output))))
print ('\n')
print ('--- 5 Minute ---')
print (' Input(bps): {0}'.format(str("{:,}".format(load_int2_input))))
print ('Output(bps): {0}'.format(str("{:,}".format(load_int2_output))))
print ('\n')
print ('Input Top Talkers (30 second):\n')
print ('Interface'.ljust(15), 'Description'.ljust(35), 'bps'.rjust(10))
print ('-'*70)
for i in range(0,10):
    print (sorted_input_talkers[i][0].ljust(15),end='')
    print (sorted_input_talkers[i][1].ljust(35),end='')
    print ('{:,}'.format(sorted_input_talkers[i][2]).rjust(20))
print ('\n')
print ('Output Top Talkers (30 second):\n')
print ('Interface'.ljust(15),'Description'.ljust(35),'bps'.rjust(10))
print ('-'*70)
for i in range(0,10):
    print (sorted_output_talkers[i][0].ljust(15),end='')
    print (sorted_output_talkers[i][1].ljust(35),end='')
    print ('{:,}'.format(sorted_output_talkers[i][2]).rjust(20))
print ('\n')
