#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yosaipy2.web.registry.abcs import WebRegistry


class FlaskWebRegistry(WebRegistry):
    def __init__(self, request):
        super(FlaskWebRegistry, self).__init__(request)

    def resource_params(self):
        """
        Obtains the resource-specific parameters of the HTTP request, returning
        a dict that will be used to bind parameter values to dynamic permissions.
        :rtype: dict
        """
        pass

    def raise_forbidden(self, msg=None):
        """
        This method is called to raise HTTP Error Code 403 (Forbidden).
        """
        pass

    def raise_unauthorized(self, msg=None):
        """
        This method is called to raise HTTP Error Code 401 (Unauthorized).
        """
        pass

    def _get_cookie(self, cookie_name, secret):
        pass

    def _set_cookie(self, response, cookie_name, cookie_val):
        pass

    def _delete_cookie(self, response, cookie_name):
        pass

    def register_response_callback(self):
        pass
