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

class UserBaseResponsePhoto(object):
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
        'image_21x21': 'str',
        'image_27x27': 'str',
        'image_36x36': 'str',
        'image_60x60': 'str',
        'image_128x128': 'str',
        'image_1024x1024': 'str'
    }

    attribute_map = {
        'image_21x21': 'image_21x21',
        'image_27x27': 'image_27x27',
        'image_36x36': 'image_36x36',
        'image_60x60': 'image_60x60',
        'image_128x128': 'image_128x128',
        'image_1024x1024': 'image_1024x1024'
    }

    def __init__(self, image_21x21=None, image_27x27=None, image_36x36=None, image_60x60=None, image_128x128=None, image_1024x1024=None):  # noqa: E501
        """UserBaseResponsePhoto - a model defined in Swagger"""  # noqa: E501
        self._image_21x21 = None
        self._image_27x27 = None
        self._image_36x36 = None
        self._image_60x60 = None
        self._image_128x128 = None
        self._image_1024x1024 = None
        self.discriminator = None
        if image_21x21 is not None:
            self.image_21x21 = image_21x21
        if image_27x27 is not None:
            self.image_27x27 = image_27x27
        if image_36x36 is not None:
            self.image_36x36 = image_36x36
        if image_60x60 is not None:
            self.image_60x60 = image_60x60
        if image_128x128 is not None:
            self.image_128x128 = image_128x128
        if image_1024x1024 is not None:
            self.image_1024x1024 = image_1024x1024

    @property
    def image_21x21(self):
        """Gets the image_21x21 of this UserBaseResponsePhoto.  # noqa: E501


        :return: The image_21x21 of this UserBaseResponsePhoto.  # noqa: E501
        :rtype: str
        """
        return self._image_21x21

    @image_21x21.setter
    def image_21x21(self, image_21x21):
        """Sets the image_21x21 of this UserBaseResponsePhoto.


        :param image_21x21: The image_21x21 of this UserBaseResponsePhoto.  # noqa: E501
        :type: str
        """

        self._image_21x21 = image_21x21

    @property
    def image_27x27(self):
        """Gets the image_27x27 of this UserBaseResponsePhoto.  # noqa: E501


        :return: The image_27x27 of this UserBaseResponsePhoto.  # noqa: E501
        :rtype: str
        """
        return self._image_27x27

    @image_27x27.setter
    def image_27x27(self, image_27x27):
        """Sets the image_27x27 of this UserBaseResponsePhoto.


        :param image_27x27: The image_27x27 of this UserBaseResponsePhoto.  # noqa: E501
        :type: str
        """

        self._image_27x27 = image_27x27

    @property
    def image_36x36(self):
        """Gets the image_36x36 of this UserBaseResponsePhoto.  # noqa: E501


        :return: The image_36x36 of this UserBaseResponsePhoto.  # noqa: E501
        :rtype: str
        """
        return self._image_36x36

    @image_36x36.setter
    def image_36x36(self, image_36x36):
        """Sets the image_36x36 of this UserBaseResponsePhoto.


        :param image_36x36: The image_36x36 of this UserBaseResponsePhoto.  # noqa: E501
        :type: str
        """

        self._image_36x36 = image_36x36

    @property
    def image_60x60(self):
        """Gets the image_60x60 of this UserBaseResponsePhoto.  # noqa: E501


        :return: The image_60x60 of this UserBaseResponsePhoto.  # noqa: E501
        :rtype: str
        """
        return self._image_60x60

    @image_60x60.setter
    def image_60x60(self, image_60x60):
        """Sets the image_60x60 of this UserBaseResponsePhoto.


        :param image_60x60: The image_60x60 of this UserBaseResponsePhoto.  # noqa: E501
        :type: str
        """

        self._image_60x60 = image_60x60

    @property
    def image_128x128(self):
        """Gets the image_128x128 of this UserBaseResponsePhoto.  # noqa: E501


        :return: The image_128x128 of this UserBaseResponsePhoto.  # noqa: E501
        :rtype: str
        """
        return self._image_128x128

    @image_128x128.setter
    def image_128x128(self, image_128x128):
        """Sets the image_128x128 of this UserBaseResponsePhoto.


        :param image_128x128: The image_128x128 of this UserBaseResponsePhoto.  # noqa: E501
        :type: str
        """

        self._image_128x128 = image_128x128

    @property
    def image_1024x1024(self):
        """Gets the image_1024x1024 of this UserBaseResponsePhoto.  # noqa: E501


        :return: The image_1024x1024 of this UserBaseResponsePhoto.  # noqa: E501
        :rtype: str
        """
        return self._image_1024x1024

    @image_1024x1024.setter
    def image_1024x1024(self, image_1024x1024):
        """Sets the image_1024x1024 of this UserBaseResponsePhoto.


        :param image_1024x1024: The image_1024x1024 of this UserBaseResponsePhoto.  # noqa: E501
        :type: str
        """

        self._image_1024x1024 = image_1024x1024

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
        if issubclass(UserBaseResponsePhoto, dict):
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
        if not isinstance(other, UserBaseResponsePhoto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
