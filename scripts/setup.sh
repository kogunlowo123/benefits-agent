#!/bin/bash
set -euo pipefail
echo "Setting up Benefits Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
