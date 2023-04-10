ORDERS = [
    {
        "id": 1,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3,
        "jewelryId": 2,
        "timestamp": 1614659931693
    }
    ]

def get_all_orders():
    """Get all orders."""
    return ORDERS

# Function with a single parameter
def get_single_order(id):
    """To get single order."""
    # Variable to hold the found order, if it exists
    requested_order = None

    # Iterate the ORDERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    """Creates a new order"""
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order

def delete_order(id):
    """To Delete Customer."""
    order_index = -1
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    "Edit order."
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break
