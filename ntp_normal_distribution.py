import json
import math

json_data=open('ntp_plat_bill_value.json')
data = json.load(json_data)
total = len(data)
mu = 0
for value in data:
	mu = mu+value
mu = mu/total

use = 0
for x in data:
	v = x - mu
	v = math.pow(v,2)
	use = use + v
use = use/total
final = math.sqrt(use)
print final*0.44 + mu
# 25% 0.675
# 1/3 0.44
