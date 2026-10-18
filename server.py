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

    text_to_hash = f"{challenge}:{EMAIL}"
    digest = hashlib.sha256(text_to_hash.encode("utf-8")).hexdigest()

    return digest[:16]

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000,
        path="/mcp",
        stateless_http=True,
        json_response=True,
    )
