#!/bin/bash
# Regenerate the Python SDK from the Fiber AI OpenAPI spec
# Usage: ./scripts/generate.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "🔄 Downloading latest OpenAPI spec..."
curl -s https://api.fiber.ai/openapi.json -o "$PROJECT_DIR/openapi.json"

echo "🗑️  Clearing old generated code..."
rm -rf "$PROJECT_DIR/src/fiberai/api" "$PROJECT_DIR/src/fiberai/models" \
       "$PROJECT_DIR/src/fiberai/client.py" "$PROJECT_DIR/src/fiberai/errors.py" \
       "$PROJECT_DIR/src/fiberai/types.py" "$PROJECT_DIR/src/fiberai/__init__.py"

echo "⚙️  Generating Python SDK..."
openapi-python-client generate \
  --path "$PROJECT_DIR/openapi.json" \
  --config "$PROJECT_DIR/config.yaml" \
  --meta none \
  --output-path "$PROJECT_DIR/src/fiberai" \
  --overwrite

echo "✅ SDK generated successfully!"
echo ""
echo "📦 Generated structure:"
find "$PROJECT_DIR/src/fiberai" -type f -name "*.py" | head -20
echo "..."
echo "Total Python files: $(find "$PROJECT_DIR/src/fiberai" -type f -name "*.py" | wc -l)"
