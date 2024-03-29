# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import asana
from asana.api.allocations_api import AllocationsApi  # noqa: E501
from asana.rest import ApiException


class TestAllocationsApi(unittest.TestCase):
    """AllocationsApi unit test stubs"""

    def setUp(self):
        self.api = AllocationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_allocation(self):
        """Test case for create_allocation

        Create an allocation  # noqa: E501
        """
        pass

    def test_delete_allocation(self):
        """Test case for delete_allocation

        Delete an allocation  # noqa: E501
        """
        pass

    def test_get_allocation(self):
        """Test case for get_allocation

        Get an allocation  # noqa: E501
        """
        pass

    def test_get_allocations(self):
        """Test case for get_allocations

        Get multiple allocations  # noqa: E501
        """
        pass

    def test_update_allocation(self):
        """Test case for update_allocation

        Update an allocation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
