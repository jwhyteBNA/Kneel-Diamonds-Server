from .metal_requests import get_single_metal
from .size_requests import get_single_size
from .style_requests import get_single_style
from .jewelry_requests import get_single_jewelry

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
            requested_order = order.copy()
            matching_metal = get_single_metal(requested_order["metalId"])
            requested_order.pop("metalId")
            requested_order["metal"] = matching_metal
            matching_size = get_single_size(requested_order["sizeId"])
            requested_order["size"] = matching_size
            requested_order.pop("sizeId")
            matching_style = get_single_style(requested_order["styleId"])
            requested_order["style"] = matching_style
            requested_order.pop("styleId")
            matching_jewelry = get_single_jewelry(requested_order["jewelryId"])
            requested_order["jewelry"] = matching_jewelry
            requested_order.pop("jewelryId")
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
