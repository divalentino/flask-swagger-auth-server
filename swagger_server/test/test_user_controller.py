# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.new_password import NewPassword  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_reset_password_put(self):
        """Test case for reset_password_put

        Reset a user password
        """
        body = NewPassword()
        response = self.client.open(
            '/api/v3/reset_password',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_token_get(self):
        """Test case for token_get

        Retrieve a Bearer token
        """
        response = self.client.open(
            '/api/v3/token',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
