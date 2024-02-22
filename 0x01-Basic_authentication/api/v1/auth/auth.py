#!/usr/bin/env python3
from typing import List, TypeVar
from flask import request

class Auth:
    """
    Auth class for handling authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of paths that are excluded from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request (flask.Request, optional): The request object. Defaults to None.

        Returns:
            str: The authorization header value.
        """
        return None

    def current_user(self, request=None) -> TypeVar:
        """
        Retrieves the current user from the request.

        Args:
            request (flask.Request, optional): The request object. Defaults to None.

        Returns:
            TypeVar: The current user object.
        """
        User = TypeVar('User')
        return None
