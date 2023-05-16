l1 = [{
  "id": 1,
  "name": "A"
}, {
  "id": 2,
  "name": "B"
}, {
  "id": 3,
  "name": "C"
}, {
  "id": 4,
  "name": "D"
}, {
  "id": 5,
  "name": "E"
}, {
  "id": 6,
  "name": "F"
}, {
  "id": 7,
  "name": "G"
}]

d1 = zip(list(map(lambda v: v['id'], l1)), l1)
print(d1)

d = dict(d1)
print(d[4])
