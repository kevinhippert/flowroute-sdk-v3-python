# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessaging.models.error_1

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class Error1(object):

    """Implementation of the 'Error1' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        status (int): TODO: type description here.
        detail (string): TODO: type description here.
        title (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id" : "id",
        "status" : "status",
        "detail" : "detail",
        "title" : "title"
    }

    def __init__(self,
                 id=None,
                 status=None,
                 detail=None,
                 title=None):
        """Constructor for the Error1 class"""

        # Initialize members of the class
        self.id = id
        self.status = status
        self.detail = detail
        self.title = title


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id")
        status = dictionary.get("status")
        detail = dictionary.get("detail")
        title = dictionary.get("title")

        # Return an object of this model
        return cls(id,
                   status,
                   detail,
                   title)


