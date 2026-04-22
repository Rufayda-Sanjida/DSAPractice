#dictionary!!!

user_info = {
    "name": "Alice",
    "age": 25,
    "is_member": True
}

#immutable keys: name, age, is_member 

# 1. retreiving values based on keys:
print(user_info["age"]) #O(1)

# 2. seeing if a key exists?
if "name" in user_info:
    print("Key exists!")

# 3. add a key
user_info["key"] = "value"

# 4. iterate
for key in user_info:
    print(key, user_info[key])

