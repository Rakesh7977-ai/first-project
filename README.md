# first-project
This is my first Git Repository.
<br>
Author - Rakesh (first git repo)

# make devcontainer folder and files
mkdir -p .devcontainer

cat > .devcontainer/devcontainer.json <<'JSON'
{
  "name": "ollama-codespace",
  "image": "mcr.microsoft.com/vscode/devcontainers/base:ubuntu",
  "postCreateCommand": "bash .devcontainer/post-create.sh",
  "forwardPorts": [11434]
}
JSON

cat > .devcontainer/post-create.sh <<'BASH'
#!/usr/bin/env bash
set -e
apt-get update -y
apt-get install -y curl jq
echo "Installing ollama CLI..."
curl -fsSL https://ollama.com/install.sh | sh || { echo "Installer failed; run manually"; exit 0; }
echo "ollama installed"
BASH

cat > start-ollama.sh <<'BASH'
#!/usr/bin/env bash
set -e
mkdir -p /tmp/ollama
nohup ollama serve --listen 0.0.0.0:11434 > /tmp/ollama/ollama.log 2>&1 &
echo "Started ollama (logs: /tmp/ollama/ollama.log)"
BASH

cat > stop-ollama.sh <<'BASH'
#!/usr/bin/env bash
pkill -f "ollama serve" || true
echo "Stopped ollama (if running)"
BASH

chmod +x .devcontainer/post-create.sh start-ollama.sh stop-ollama.sh
echo "Files created. Commit them or keep for this Codespace."
