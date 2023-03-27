echo "Remove extra files"
sudo find . -type d -name __pycache__ -exec rm -r {} \+
sudo find . -type d -name .venv -exec rm -r {} \+        