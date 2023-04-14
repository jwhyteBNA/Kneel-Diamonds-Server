JEWELRY = [
        { "id": 1, "type": "Ring", "multiplier": 1 },
        { "id": 2, "type": "Necklace", "multiplier": 2 },
        { "id": 3, "type": "Earring", "multiplier": 4 }
    ]

def get_all_jewelry():
    """Get all jewelry."""
    return JEWELRY

# Function with a single parameter
def get_single_jewelry(id):
    """To get single jewelry."""
    # Variable to hold the found order, if it exists
    requested_jewel = None

    # Iterate the ORDERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for jewel in JEWELRY:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if jewel["id"] == id:
            requested_jewel = jewel

    return requested_jewel
