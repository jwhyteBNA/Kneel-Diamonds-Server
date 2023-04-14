import json
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from repository import all, retrieve, create, update

method_mapper = {
    "jewelry": {
        "single": retrieve,
        "all": all
    },
    "metals": {
        "single": retrieve,
        "all": all
    },
    "sizes": {
        "single": retrieve,
        "all": all
    },
    "styles": {
        "single": retrieve,
        "all": all
    },
    "orders": {
        "single": retrieve,
        "all": all
    }
}

class HandleRequests(BaseHTTPRequestHandler):
    """GET, PUT, POST, DELETE requests to the server """

    def get_all_or_single(self, resource, id, query_params):
        """DRY method for all or single."""

        if id is not None:
            response = method_mapper[resource]["single"](resource,id, query_params)
            if response is not None:
                self._set_headers(200)
            else:
                self._set_headers(404)
                response = {"message": f"{resource} {id} does not exist."}
        else:
            self._set_headers(200)
            response = method_mapper[resource]["all"](resource)
        return response

    def do_GET(self):
        """Get all or single resource"""
        response = None
        (resource, id, query_params) = self.parse_url(self.path)
        response = self.get_all_or_single(resource, id, query_params)
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Create New Resource."""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id, query_params) = self.parse_url(self.path)

        if resource == "orders":
            required_fields = {
            "orders": ["metal_id", "size_id", "style_id", "jewelry_id"],
            }
            missing_fields = [
                field for field in required_fields[resource] if field not in post_body
            ]
            if not missing_fields:
                self._set_headers(201)
                new_resource = create(resource, post_body)
                self.wfile.write(json.dumps(new_resource).encode())
            else:
                self._set_headers(400)
                message = {"message": "".join(
                    [f"{field} is required" for field in missing_fields]
                )
                }
                self.wfile.write(json.dumps(message).encode())
        else:
            self._set_headers(400)
            message = {"message": "Resource cannot be created"}
            self.wfile.write(json.dumps(message).encode())

    def do_DELETE(self):
        """To Delete Items."""
        (resource, id, query_params) = self.parse_url(self.path)

        if resource:
            self._set_headers(405)
            delete_resource = { "message": f"User cannot delete {resource}." }
            self.wfile.write(json.dumps(delete_resource).encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id, query_params) = self.parse_url(self.path)
        if resource == "metals":
            self._set_headers(204)
            update(resource, id, post_body)
            self.wfile.write("".encode())
        else:
            self._set_headers(405)
            update_resource = { "message": "Update prohibited." }
            self.wfile.write(json.dumps(update_resource).encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # def parse_url(self, path):
    #     """parsing"""
    #     # Just like splitting a string in JavaScript. If the
    #     # path is "/metals/1", the resulting list will
    #     # have "" at index 0, "metals" at index 1, and "1"
    #     # at index 2.
    #     path_params = path.split("/")
    #     resource = path_params[1]
    #     id = None

    #     # Try to get the item at index 2
    #     try:
    #         # Convert the string "1" to the integer 1
    #         # This is the new parseInt()
    #         id = int(path_params[2])
    #     except IndexError:
    #         pass  # No route parameter exists: /metals
    #     except ValueError:
    #         pass  # Request had trailing slash: /metals/

    #     return (resource, id)  # This is a tuple

    # Replace existing function with this
    def parse_url(self, path):
        """Parsing updates"""
        url_components = urlparse(path)
        path_params = url_components.path.strip("/").split("/")
        query_params = url_components.query.split("&")
        resource = path_params[0]
        id = None

        try:
            id = int(path_params[1])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id, query_params)

#Starting point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
