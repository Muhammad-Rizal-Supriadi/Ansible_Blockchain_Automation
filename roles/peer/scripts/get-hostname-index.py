
#!/usr/bin/python
import sys

hostnames = sys.argv[1]
inventoryHostname = sys.argv[2]
result = 0
for k, v in enumerate(hostnames.split(',')):
   if v == inventoryHostname:
      result = k + 1
      break
print(result, end='')
