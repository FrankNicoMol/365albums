import os
import re


def load_credentials(sh_path):
    """Parse export KEY="VALUE" lines from a shell script and set them in os.environ."""
    with open(sh_path, 'r') as f:
        for line in f:
            match = re.match(r'^export\s+(\w+)="([^"]*)"', line.strip())
            if match:
                os.environ[match.group(1)] = match.group(2)
