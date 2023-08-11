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

class TaskResponseArray(object):
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
        'data': 'list[TaskResponse]',
        'next_page': 'NextPage'
    }

    attribute_map = {
        'data': 'data',
        'next_page': 'next_page'
    }

    def __init__(self, data=None, next_page=None):  # noqa: E501
        """TaskResponseArray - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._next_page = None
        self.discriminator = None
        self.data = data
        if next_page is not None:
            self.next_page = next_page

    @property
    def data(self):
        """Gets the data of this TaskResponseArray.  # noqa: E501


        :return: The data of this TaskResponseArray.  # noqa: E501
        :rtype: list[TaskResponse]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TaskResponseArray.


        :param data: The data of this TaskResponseArray.  # noqa: E501
        :type: list[TaskResponse]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def next_page(self):
        """Gets the next_page of this TaskResponseArray.  # noqa: E501


        :return: The next_page of this TaskResponseArray.  # noqa: E501
        :rtype: NextPage
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this TaskResponseArray.


        :param next_page: The next_page of this TaskResponseArray.  # noqa: E501
        :type: NextPage
        """

        self._next_page = next_page

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
        if issubclass(TaskResponseArray, dict):
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
        if not isinstance(other, TaskResponseArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other