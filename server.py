import hashlib

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

EMAIL = "25f1002516@ds.study.iitm.ac.in"

mcp = FastMCP(name="Exam Challenge Server")

@mcp.tool
def solve_challenge() -> str:
    """Return the required hash for the current exam challenge."""

    headers = get_http_headers()
    challenge = headers.get("x-exam-challenge")

    if not challenge:
        raise ValueError("Missing X-Exam-Challenge header")

    digest = hashlib.sha256(f"{challenge}:{EMAIL}".encode()).hexdigest()
    return digest[:16]

app = mcp.http_app(stateless_http=True)
