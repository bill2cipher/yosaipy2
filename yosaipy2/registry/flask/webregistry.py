#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yosaipy2.web.registry.abcs import WebRegistry
from flask import request
from typing import Callable, Dict, Any
from werkzeug.exceptions import Forbidden, Unauthorized


class FlaskWebRegistry(WebRegistry):
    def __init__(self, parser):
        # type: (Callable[[Any], Dict]) -> None
        super(FlaskWebRegistry, self).__init__(request)
        self._parser = parser

    def resource_params(self):
        # type: () -> Dict
        """
        Obtains the resource-specific parameters of the HTTP request, returning
        a dict that will be used to bind parameter values to dynamic permissions.
        """
        return self._parser(request)

    def raise_forbidden(self, msg=None):
        """
        This method is called to raise HTTP Error Code 403 (Forbidden).
        """
        raise Forbidden(description=msg)

    def raise_unauthorized(self, msg=None):
        """
        This method is called to raise HTTP Error Code 401 (Unauthorized).
        """
        raise Unauthorized(description=msg)

    def _get_cookie(self, cookie_name, secret):
        if cookie_name in request.cookies:
            return request.cookies[cookie_name]
        return None

    def _set_cookie(self, response, cookie_name, cookie_val):
        response.set_cookie(
            key=cookie_name,
            value=cookie_val,
            max_age=self.set_cookie_attributes.get('cookie_max_age', None),
            path=self.set_cookie_attributes.get('cookie_path', None),
            domain=self.set_cookie_attributes.get('cookie_domain', None),
            secure=self.set_cookie_attributes.get('cookie_secure', None),
            httponly=self.set_cookie_attributes.get('cookie_httponly', False)
        )

    def _delete_cookie(self, response, cookie_name):
        response.set_cookie('cookie_name', '', expires=0)

    def register_response_callback(self):
        pass
