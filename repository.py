DATABASE = {
"jewelry": [
        { "id": 1, "type": "Ring", "multiplier": 1 },
        { "id": 2, "type": "Necklace", "multiplier": 2 },
        { "id": 3, "type": "Earring", "multiplier": 4 }
    ],
"metals": [
    { "id": 1, "metal": "Sterling Silver", "price": 400.42 },
    { "id": 2, "metal": "14K Gold", "price": 736.4 },
    { "id": 3, "metal": "24K Gold", "price": 1258.9 },
    { "id": 4, "metal": "Platinum", "price": 795.45 },
    { "id": 5, "metal": "Palladium", "price": 1241.0 }
    ],
"sizes":[
    { "id": 1, "carets": 0.5, "price": 405 },
    { "id": 2, "carets": 0.75, "price": 782 },
    { "id": 3, "carets": 1, "price": 1470 },
    { "id": 4, "carets": 1.5, "price": 1997 },
    { "id": 5, "carets": 2, "price": 3638 }
    ],
"styles": [
    { "id": 1, "style": "Classic", "price": 500 },
    { "id": 2, "style": "Modern", "price": 710 },
    { "id": 3, "style": "Vintage", "price": 965 }
],
"orders": [
    {
        "id": 1,
        "metal_id": 3,
        "size_id": 2,
        "style_id": 3,
        "jewelry_id": 2,
        "timestamp": 1614659931693
    }
]
}

def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource]

def retrieve(resource, id, query_params):
    """For GET requests to a single resource"""
    requested_resource = None
    for object in DATABASE[resource]:
        if object["id"] == id:
            requested_resource = object
    if resource == "orders":
        requested_order = requested_resource.copy()

        matching_metal = retrieve("metals",requested_order["metal_id"], query_params)
        if "expand=metal" in query_params:
            requested_order["metal"] = matching_metal
            requested_order.pop("metal_id")

        matching_size = retrieve("sizes", requested_order["size_id"], query_params)
        if "expand=size" in query_params:
            requested_order["size"] = matching_size
            requested_order.pop("size_id")

        matching_style = retrieve("styles", requested_order["style_id"], query_params)
        if "expand=style" in query_params:
            requested_order["style"] = matching_style
            requested_order.pop("style_id")

        matching_jewelry = retrieve("jewelry", requested_order["jewelry_id"], query_params)
        if "expand=jewelry" in query_params:
            requested_order["jewelry"] = matching_jewelry
            requested_order.pop("jewelry_id")

        requested_order["price"] = matching_metal["price"] + matching_size["price"] + matching_style["price"] * matching_jewelry["multiplier"]
        return requested_order
    return requested_resource

def create(resource, post_body):
    """For POST requests to a collection"""
    max_id = DATABASE[resource][-1]["id"]
    new_id = max_id + 1
    post_body["id"] = new_id
    DATABASE[resource].append(post_body)
    return post_body

# Not currently being invoked; would delete in professional setting
def delete(resource, id):
    """For DELETE requests to a single resource"""
    resource_index = -1
    for index, item in enumerate(DATABASE[resource]):
        if item["id"] == id:
            resource_index = index
    if resource_index >= 0:
        DATABASE[resource].pop(resource_index)

def update(resource, id, post_body):
    """For PUT requests to a single resource"""
    for index, item in enumerate(DATABASE[resource]):
        if item["id"] == id:
            DATABASE[resource][index] = post_body
            break
