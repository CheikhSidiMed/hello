# player = {
#     "name": "Bilal",
#     "country": "Algeia",
#     "score": 86
# }
# print(player["name"])
contacts = {
    "zied": 50200201,
    "nour": 22100305,
    "omar": 95450500,
    "bilel": 55700107
}
print(contacts["zied"])
print(contacts.get("zied"))
print(contacts.get("sidi", "key not find"))
print(contacts.get("zied"))
contacts.update({'zied': 52300105})
print(contacts.get("zied"))
contacts["amal"] = 20102103
# contacts.setdefault("amal": 20102103)
contacts.pop("omar")
print(contacts.keys())
print(contacts.values())
print(dict(contacts.items()))
print(dict(sorted(contacts.items())))

# print(contacts.s())
contacts.clear()
print(contacts)