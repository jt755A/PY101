munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"


mess_with_demographics(munsters)

# the mess_with.. function modifies the nested function. As mappings
# are mutable, the original dict is modified.

# EDIT

# the object that is modified by the function is the munsters object.
# A reference to the dictionary is passed to the function, not a copy.