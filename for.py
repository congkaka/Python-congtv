d = {
    'a': 1,
    'b': 2,
    'c': 3
}

# for key in d.values():
#     print(key)

for item in d.items():
    key, value = item
    # print(item)
    print(f"{key}={value}")
