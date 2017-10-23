#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Response, request, Flask, Request
from flask import g, session
from yosaipy2.web.registry.abcs import WebRegistry
from yosaipy2.web import WebYosai
from yosaipy2.registry.flask.webregistry import FlaskWebRegistry
from typing import Callable, Dict


def init_flask(app, yosai):
    # type: (Flask, WebYosai, Callable[[Request], Dict]) -> None

    def registry_callback(response):
        # type:(Response) -> Response
        if 'yosai_webregistry' not in session:
            return response
        else:
            registry = session['yosai_webregistry']  # type: WebRegistry
            registry.webregistry_callback(request, response)
            return response

    def before_request():
        if 'yosai_webregistry' not in session:
            registry = FlaskWebRegistry()
            session['yosai_webregistry'] = registry
        else:
            saved_registry = session['yosai_webregistry']
            if not isinstance(saved_registry, FlaskWebRegistry):
                registry = FlaskWebRegistry()
                registry.decode(saved_registry)
            else:
                registry = saved_registry
        yosai_context = WebYosai.context(yosai, registry)
        g.yosai_context = yosai_context
        g.yosai_context.__enter__()

    def after_request(response):
        # type:(Response) -> Response
        response = registry_callback(response)
        g.yosai_context.__exit__(None, None, None)
        return response

    app.before_request(before_request)
    app.after_request(after_request)
