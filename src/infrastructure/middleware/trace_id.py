import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from src.infrastructure.utils.context import set_trace_id

class TraceIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Generate a unique trace ID for the request
        if request.headers.get("X-Trace-ID"):
            trace_id = request.headers["X-Trace-ID"]
        else:
            trace_id = str(uuid.uuid4())
        set_trace_id(trace_id)  # Set trace ID in the context

        # Add trace ID to response headers
        response = await call_next(request)
        if "X-Trace-ID" not in response.headers or not uuid.UUID(response.headers["X-Trace-ID"], version=4):
            response.headers["X-Trace-ID"] = trace_id
        return response