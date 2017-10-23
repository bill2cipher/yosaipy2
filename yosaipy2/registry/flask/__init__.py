#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Response, request, Flask, Request
from flask import g, session
from yosaipy2.web.registry.abcs import WebRegistry
from yosaipy2.web import WebYosai
from yosaipy2.registry.flask.webregistry import FlaskWebRegistry
from typing import Callable, Dict


def init_flask(app, yosai, parser):
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
            registry = FlaskWebRegistry(parser)
            session['yosai_webregistry'] = registry
        else:
            registry = session['yosai_webregistry']
        yosai_context = WebYosai.context(yosai, registry)
        g.yosai_context = yosai_context
        g.yosai_context.__enter__()

    def after_request(response):
        # type:(Response) -> Response
        response = registry_callback(response)
        g.yosai_context.__exit__()
        return response

    app.before_request(before_request)
    app.after_request(after_request)
