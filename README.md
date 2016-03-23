A utility that can be run locally on Cisco Nexus switches to display the top talker interfaces.

Upload to the bootflash:/scripts on the device and then run with the command:  source bwutil2.py

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

