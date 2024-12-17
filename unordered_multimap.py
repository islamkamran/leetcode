from collections import defaultdict
unordered_multimap = defaultdict(list)
unordered_multimap['key'].append('v1')
unordered_multimap['key1'].append('v1')
unordered_multimap['key1'].append('v1')
unordered_multimap['key1'].append('v1')
unordered_multimap['key1'].append('v1')
print(unordered_multimap)
