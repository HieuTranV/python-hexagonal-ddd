from contextvars import ContextVar

# Define a context variable for the trace ID
trace_id_var: ContextVar[str] = ContextVar("trace_id", default="N/A")

def set_trace_id(trace_id: str):
    """
    Set the trace ID in the context.
    """
    trace_id_var.set(trace_id)

def get_trace_id() -> str:
    """
    Get the trace ID from the context.
    """
    return trace_id_var.get()