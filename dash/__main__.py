"""CLI entry point: python -m dash"""

import utils.net
import utils.clients
import utils.http_session
import utils.transport
import utils.session
from dash.agent import dash

if __name__ == "__main__":
    dash.cli_app(stream=True)
