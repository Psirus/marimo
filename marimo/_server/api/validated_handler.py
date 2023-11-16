# Copyright 2023 Marimo. All rights reserved.
from __future__ import annotations

import tornado.web

from marimo._server import sessions


class ValidatedHandler(tornado.web.RequestHandler):
    def prepare(self) -> None:
        # Validate the server token -- don't allow connections from frontends
        # that weren't generated by this server
        sessions.check_server_token(self.request.headers)
