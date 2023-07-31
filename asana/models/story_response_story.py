# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StoryResponseStory(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'gid': 'str',
        'resource_type': 'str',
        'created_at': 'datetime',
        'created_by': 'CustomFieldResponsePeopleValue',
        'resource_subtype': 'str',
        'text': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'created_at': 'created_at',
        'created_by': 'created_by',
        'resource_subtype': 'resource_subtype',
        'text': 'text'
    }

    def __init__(self, gid=None, resource_type=None, created_at=None, created_by=None, resource_subtype=None, text=None):  # noqa: E501
        """StoryResponseStory - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._created_at = None
        self._created_by = None
        self._resource_subtype = None
        self._text = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if resource_subtype is not None:
            self.resource_subtype = resource_subtype
        if text is not None:
            self.text = text

    @property
    def gid(self):
        """Gets the gid of this StoryResponseStory.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this StoryResponseStory.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this StoryResponseStory.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this StoryResponseStory.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this StoryResponseStory.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this StoryResponseStory.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this StoryResponseStory.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this StoryResponseStory.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def created_at(self):
        """Gets the created_at of this StoryResponseStory.  # noqa: E501

        The time at which this resource was created.  # noqa: E501

        :return: The created_at of this StoryResponseStory.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this StoryResponseStory.

        The time at which this resource was created.  # noqa: E501

        :param created_at: The created_at of this StoryResponseStory.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this StoryResponseStory.  # noqa: E501


        :return: The created_by of this StoryResponseStory.  # noqa: E501
        :rtype: CustomFieldResponsePeopleValue
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this StoryResponseStory.


        :param created_by: The created_by of this StoryResponseStory.  # noqa: E501
        :type: CustomFieldResponsePeopleValue
        """

        self._created_by = created_by

    @property
    def resource_subtype(self):
        """Gets the resource_subtype of this StoryResponseStory.  # noqa: E501

        The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.  # noqa: E501

        :return: The resource_subtype of this StoryResponseStory.  # noqa: E501
        :rtype: str
        """
        return self._resource_subtype

    @resource_subtype.setter
    def resource_subtype(self, resource_subtype):
        """Sets the resource_subtype of this StoryResponseStory.

        The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.  # noqa: E501

        :param resource_subtype: The resource_subtype of this StoryResponseStory.  # noqa: E501
        :type: str
        """

        self._resource_subtype = resource_subtype

    @property
    def text(self):
        """Gets the text of this StoryResponseStory.  # noqa: E501

        *Create-only*. Human-readable text for the story or comment. This will not include the name of the creator. *Note: This is not guaranteed to be stable for a given type of story. For example, text for a reassignment may not always say “assigned to …” as the text for a story can both be edited and change based on the language settings of the user making the request.* Use the `resource_subtype` property to discover the action that created the story.  # noqa: E501

        :return: The text of this StoryResponseStory.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this StoryResponseStory.

        *Create-only*. Human-readable text for the story or comment. This will not include the name of the creator. *Note: This is not guaranteed to be stable for a given type of story. For example, text for a reassignment may not always say “assigned to …” as the text for a story can both be edited and change based on the language settings of the user making the request.* Use the `resource_subtype` property to discover the action that created the story.  # noqa: E501

        :param text: The text of this StoryResponseStory.  # noqa: E501
        :type: str
        """

        self._text = text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StoryResponseStory, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StoryResponseStory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
