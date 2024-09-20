from mitmproxy import http
from mitmproxy.connection import Server
from mitmproxy.net.server_spec import ServerSpec

class LogHeaders:
    def request(self, flow: http.HTTPFlow) -> None:
        print(flow.request.headers)

addons = [
    LogHeaders()
]
