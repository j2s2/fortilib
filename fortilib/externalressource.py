import ipaddress

from fortilib.base import FortigateNamedObject

class FortigateExternalRessource(FortigateNamedObject):
    """Fortigate object for ip mask \
        extends :class:`fortilib.address.FortigateAddress` with a subnet.

    :ivar subnet: Adress subnet e.g. "10.10.10.1/255.255.255.255"
    """

    def __init__(self):
        super().__init__()
        self.type: string = None

    def populate(self, object_data: dict):
        super().populate(object_data)
        self.type = object_data.get("type")

    def render(self) -> dict:
        """Generate dict with all object arguments for fortigate api call.

        :example:
            .. code-block:: json

                {
                    "name": "Test_ressource",
                    "type": "address",
                    "comments": "Test comment",
                }
        """
        return {
            "name": self.name,
            "type": self.type,
            "comment": self.comment,
        }

