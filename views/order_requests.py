import sqlite3
# import json
from models import Order, Jewelry, Metal, Size, Style
# from .metal_requests import get_single_metal
# from .size_requests import get_single_size
# from .style_requests import get_single_style
# from .jewelry_requests import get_single_jewelry

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
    """Using SQL database to get all orders with expansion"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.jewelry_id,
            o.timestamp,
            m.metal metal_metal,
            m.price metal_price,
            z.carets size_carets,
            z.price size_price,
            s.style style_style,
            s.price style_price,
            j.type jewelry_type,
            j.multiplier jewelry_multiplier            
        FROM "Order" o
        JOIN Metal m
            ON m.id = o.metal_id
        JOIN Size z
            ON z.id = o.size_id
        JOIN Style s
            ON s.id = o.style_id
        JOIN Jewelry j
            ON j.id = o.jewelry_id
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            order = Order(row['id'], row['metal_id'],
            row['size_id'], row['style_id'],row['jewelry_id'], row['timestamp'], )

            metal = Metal(row['id'], row['metal_metal'], row['metal_price'], )
            order.metal = metal.__dict__

            size = Size(row['id'], row['size_carets'],
            row['size_price'])
            order.size = size.__dict__

            style = Style(row['id'], row['style_style'],
            row['style_price'])
            order.style = style.__dict__

            jewelry = Jewelry(row['id'], row['jewelry_type'],
            row['jewelry_multiplier'])
            order.jewelry = jewelry.__dict__

            orders.append(order.__dict__)

    return orders

def get_single_order(id):
    """New single order request for SQL"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.jewelry_id,
            o.timestamp
        FROM "Order" o
        WHERE o.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        order = Order(data['id'], data['metal_id'], data['size_id'], data['style_id'],data['jewelry_id'], data['timestamp'], )

        return order.__dict__

def create_order(new_order):
    """Add to SQL database"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO "Order"
            ( metal_id, size_id, style_id, jewelry_id, timestamp )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_order['metal_id'], new_order['size_id'],
            new_order['style_id'], new_order['jewelry_id'],
            new_order['timestamp'], ))

        id = db_cursor.lastrowid
        new_order['id'] = id

    return new_order

def delete_order(id):
    """Delete from SQL"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM "Order"
        WHERE id = ?
        """, (id, ))

def update_order(id, new_order):
    """UPDATE in SQL"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE "Order"
            SET
                metal_id = ?,
                size_id = ?,
                style_id = ?,
                jewelry_id = ?,
                timestamp = ?
        WHERE id = ?
        """, (new_order['metal_id'], new_order['size_id'],
            new_order['style_id'], new_order['jewelry_id'],
            new_order['timestamp'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

# def get_all_orders():
#     """Using SQL database to get all orders with expansion"""
#     with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         SELECT
#             o.id,
#             o.metal_id,
#             o.size_id,
#             o.style_id,
#             o.jewelry_id,
#             o.timestamp
#          FROM "Order" o
#         """)

#         orders = []

#         dataset = db_cursor.fetchall()

#         for row in dataset:

#             order = Order(row['id'], row['metal_id'],
#             row['size_id'], row['style_id'],row['jewelry_id'], row['timestamp'], )

#             orders.append(order.__dict__)

#     return orders

# # Function with a single parameter
# def get_single_order(id):
#     """To get single order."""
#     # Variable to hold the found order, if it exists
#     requested_order = None

#     # Iterate the ORDERS list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for order in ORDERS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if order["id"] == id:
#             requested_order = order.copy()
#             matching_metal = get_single_metal(requested_order["metalId"])
#             requested_order.pop("metalId")
#             requested_order["metal"] = matching_metal
#             matching_size = get_single_size(requested_order["sizeId"])
#             requested_order["size"] = matching_size
#             requested_order.pop("sizeId")
#             matching_style = get_single_style(requested_order["styleId"])
#             requested_order["style"] = matching_style
#             requested_order.pop("styleId")
#             matching_jewelry = get_single_jewelry(requested_order["jewelryId"])
#             requested_order["jewelry"] = matching_jewelry
#             requested_order.pop("jewelryId")
#     return requested_order

# def create_order(order):
#     """Creates a new order"""
#     max_id = ORDERS[-1]["id"]
#     new_id = max_id + 1
#     order["id"] = new_id
#     ORDERS.append(order)
#     return order


# def delete_order(id):
#     """To Delete Customer."""
#     order_index = -1
#     for index, order in enumerate(ORDERS):
#         if order["id"] == id:
#             order_index = index
#     if order_index >= 0:
#         ORDERS.pop(order_index)

# def update_order(id, new_order):
#     "Edit order."
#     for index, order in enumerate(ORDERS):
#         if order["id"] == id:
#             ORDERS[index] = new_order
#             break
