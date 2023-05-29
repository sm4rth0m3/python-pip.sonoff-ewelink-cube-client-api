"""
Helper functions for examples.
"""

import os
import base64


def encode_ip_to_hash(ip_or_host: str) -> str:
    """
    Encode IP address or hostname to a hash.

    Args:
        ip_or_host (str): IP address or hostname.

    Returns:
        str: Encoded hash.
    """
    encoded_id = base64.b64encode(ip_or_host.encode()).decode()
    return encoded_id[:8]

def save_access_token(host_address: str, access_token: str) -> None:
    """
    Save access token to a file.

    Args:
        host_address (str): Host address.
        access_token (str): Access token.
    """
    home_dir = os.path.expanduser("~")
    host_hash = encode_ip_to_hash(host_address)
    file_path = os.path.join(home_dir, f".ewelink_cube_{host_hash}_access_token")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(access_token)

def load_access_token(host_address: str) -> str:
    """
    Load access token from a file.

    Args:
        host_address (str): Host address.

    Returns:
        str or None: Loaded access token or None if not found.
    """
    home_dir = os.path.expanduser("~")
    host_hash = encode_ip_to_hash(host_address)
    file_path = os.path.join(home_dir, f".ewelink_cube_{host_hash}_access_token")

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            access_token = file.read()

        if access_token.strip() == "":
            access_token = None
    else:
        access_token = None

    return access_token
