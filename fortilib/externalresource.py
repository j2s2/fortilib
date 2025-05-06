import ipaddress

from fortilib.base import FortigateNamedObject

class FortigateExternalResource(FortigateNamedObject):
    """Fortigate object for external resource \

    :ivar type: type of resource
    :ivar method: update method
    :ivar url: update URL for method "feed"
    """

    def __init__(self):
        super().__init__()
        self.type: string = None
        self.method = None
        self.url = None

    def __eq__(self, other):
        if isinstance(other, FortigateExternalRessource):
            return (
                self.name == other.name
                and self.type == other.type
                and self.method == other.method
                and self.url == other.url
            )
        return False

    def populate(self, object_data: dict):
        super().populate(object_data)
        self.type = object_data.get("type")
        self.method = object_data.get("update-method")
        self.url = object_data.get("resource",None)

    def render(self) -> dict:
        """Generate dict with all object arguments for fortigate api call.

        :example:
            .. code-block:: json

                {
                    "name": "Test_resource",
                    "type": "address",
                    "method": "feed",
                    "url": "http://a.b.c.d/xyz",
                    "comments": "Test comment",
                }
        """
        return {
            "name": self.name,
            "type": self.type,
            "method": self.method,
            "url": self.url,
            "comment": self.comment,
        }

