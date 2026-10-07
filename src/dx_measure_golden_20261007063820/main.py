"""dx-measure-golden-20261007063820: HTTP entry point."""

from fastapi import FastAPI
from pydantic import BaseModel

from dx_measure_golden_20261007063820 import __version__

app = FastAPI(title="dx-measure-golden-20261007063820", version=__version__)


class Health(BaseModel):
    status: str
    version: str


class Greeting(BaseModel):
    message: str


@app.get("/health")
def health() -> Health:
    """Liveness probe used by Docker HEALTHCHECK and the deploy platform."""
    return Health(status="ok", version=__version__)


@app.get("/hello")
def hello(name: str = "world") -> Greeting:
    """Return a greeting for ``name``."""
    return Greeting(message=f"Hello, {name}!")
