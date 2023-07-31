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

class AddCustomFieldSettingRequest(object):
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
        'custom_field': 'str',
        'is_important': 'bool',
        'insert_before': 'str',
        'insert_after': 'str'
    }

    attribute_map = {
        'custom_field': 'custom_field',
        'is_important': 'is_important',
        'insert_before': 'insert_before',
        'insert_after': 'insert_after'
    }

    def __init__(self, custom_field=None, is_important=None, insert_before=None, insert_after=None):  # noqa: E501
        """AddCustomFieldSettingRequest - a model defined in Swagger"""  # noqa: E501
        self._custom_field = None
        self._is_important = None
        self._insert_before = None
        self._insert_after = None
        self.discriminator = None
        self.custom_field = custom_field
        if is_important is not None:
            self.is_important = is_important
        if insert_before is not None:
            self.insert_before = insert_before
        if insert_after is not None:
            self.insert_after = insert_after

    @property
    def custom_field(self):
        """Gets the custom_field of this AddCustomFieldSettingRequest.  # noqa: E501

        The custom field to associate with this container.  # noqa: E501

        :return: The custom_field of this AddCustomFieldSettingRequest.  # noqa: E501
        :rtype: str
        """
        return self._custom_field

    @custom_field.setter
    def custom_field(self, custom_field):
        """Sets the custom_field of this AddCustomFieldSettingRequest.

        The custom field to associate with this container.  # noqa: E501

        :param custom_field: The custom_field of this AddCustomFieldSettingRequest.  # noqa: E501
        :type: str
        """
        if custom_field is None:
            raise ValueError("Invalid value for `custom_field`, must not be `None`")  # noqa: E501

        self._custom_field = custom_field

    @property
    def is_important(self):
        """Gets the is_important of this AddCustomFieldSettingRequest.  # noqa: E501

        Whether this field should be considered important to this container (for instance, to display in the list view of items in the container).  # noqa: E501

        :return: The is_important of this AddCustomFieldSettingRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_important

    @is_important.setter
    def is_important(self, is_important):
        """Sets the is_important of this AddCustomFieldSettingRequest.

        Whether this field should be considered important to this container (for instance, to display in the list view of items in the container).  # noqa: E501

        :param is_important: The is_important of this AddCustomFieldSettingRequest.  # noqa: E501
        :type: bool
        """

        self._is_important = is_important

    @property
    def insert_before(self):
        """Gets the insert_before of this AddCustomFieldSettingRequest.  # noqa: E501

        A gid of a Custom Field Setting on this container, before which the new Custom Field Setting will be added.  `insert_before` and `insert_after` parameters cannot both be specified.  # noqa: E501

        :return: The insert_before of this AddCustomFieldSettingRequest.  # noqa: E501
        :rtype: str
        """
        return self._insert_before

    @insert_before.setter
    def insert_before(self, insert_before):
        """Sets the insert_before of this AddCustomFieldSettingRequest.

        A gid of a Custom Field Setting on this container, before which the new Custom Field Setting will be added.  `insert_before` and `insert_after` parameters cannot both be specified.  # noqa: E501

        :param insert_before: The insert_before of this AddCustomFieldSettingRequest.  # noqa: E501
        :type: str
        """

        self._insert_before = insert_before

    @property
    def insert_after(self):
        """Gets the insert_after of this AddCustomFieldSettingRequest.  # noqa: E501

        A gid of a Custom Field Setting on this container, after which the new Custom Field Setting will be added.  `insert_before` and `insert_after` parameters cannot both be specified.  # noqa: E501

        :return: The insert_after of this AddCustomFieldSettingRequest.  # noqa: E501
        :rtype: str
        """
        return self._insert_after

    @insert_after.setter
    def insert_after(self, insert_after):
        """Sets the insert_after of this AddCustomFieldSettingRequest.

        A gid of a Custom Field Setting on this container, after which the new Custom Field Setting will be added.  `insert_before` and `insert_after` parameters cannot both be specified.  # noqa: E501

        :param insert_after: The insert_after of this AddCustomFieldSettingRequest.  # noqa: E501
        :type: str
        """

        self._insert_after = insert_after

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
        if issubclass(AddCustomFieldSettingRequest, dict):
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
        if not isinstance(other, AddCustomFieldSettingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
