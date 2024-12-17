from pathlib import Path
from grpc_tools import protoc

# Get the current directory
current_dir = Path(__file__).parent
proto_path = current_dir / "proto"

# Generate Python code from proto file
protoc.main(
    [
        "grpc_tools.protoc",
        f"--proto_path={proto_path}",
        f"--python_out={proto_path}",
        f"--grpc_python_out={proto_path}",
        f"{proto_path}/glossary.proto",
    ]
)

# Fix imports in generated files
pb2_file = proto_path / "glossary_pb2_grpc.py"
content = pb2_file.read_text()
content = content.replace("import glossary_pb2", "from . import glossary_pb2")
pb2_file.write_text(content)
