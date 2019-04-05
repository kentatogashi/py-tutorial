#!/usr/bin/env python
import os
loads = os.getloadavg()
print('### Load avg ###')
print('Load avg 1 min %.2f' % loads[0])
print('Load avg 5 min %.2f' % loads[1])
print('Load avg 15 min %.2f' % loads[2])
print('')

import shutil
total, used, free = shutil.disk_usage('/')
print('### Disk usage ###')
print('Disk total %d GB' % (total // (2**30)))
print('Disk used %d GB' % (used // (2**30)))
print('Disk free %d GB' % (free // (2**30)))
print('')

from psutil import virtual_memory
mem = virtual_memory()
print('### Memory usage ###')
print('Mem total %d GB' % (mem.total // (2**30)))
print('Mem available %d GB' % (mem.available// (2**30)))
print(f'Mem percent {mem.percent} %')
print('')

from psutil import net_io_counters
print('### Network stastics ###')
nics = net_io_counters(pernic=True)
for nic in nics:
    print(f'NIC {nic}')
    print('Bytes sent %d MB' % (nics[nic].bytes_sent // (2**20)))
    print('Bytes recv %d MB' % (nics[nic].bytes_recv // (2**20)))
    print('Packets sent %d' % (nics[nic].packets_sent))
    print('Packets recv %d' % (nics[nic].packets_recv))
