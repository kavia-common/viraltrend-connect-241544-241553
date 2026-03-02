import json
import os

from src.api.main import app

# Get the OpenAPI schema
openapi_schema = app.openapi()

# Write to file (always relative to backend_api/ no matter current working directory)
this_dir = os.path.dirname(__file__)
backend_api_root = os.path.abspath(os.path.join(this_dir, "..", "..", ".."))
output_dir = os.path.join(backend_api_root, "interfaces")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "openapi.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(openapi_schema, f, indent=2)
