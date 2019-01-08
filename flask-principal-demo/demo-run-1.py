#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2019/1/8 2:22 PM
from functools import wraps

from flask import Flask, Response

app = Flask(__name__)

user_dict = {1: "johu", 2: "warmy", 3: "winndy"}
role_dict = {1: "admin", 2: "developer", 3: "owner"}
permissions_dict = {"add", "update", "delete", "get"}
user_role_dict = {1: {2, }}
user_permission_dict = {
    1: {"delete", },
    2: {"get", },
    3: {"get", "update"}
}
role_permission_dict = {
    1: {"add", "update", "delete", "get"},
    2: {"get", "update"},
    3: {"get", "update", "delete"}
}


def permission_check(permissions=None, logic="AND"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not check_permission(permissions, logic, 1):
                return Response("NO PERMISSION")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def check_permission(permissions, logic, user_id):
    if not permissions:
        return True
    if isinstance(permissions, str):
        permissions = {permissions, }
    user_permissions = user_permission_dict.get(user_id, set())
    user_role_ids = user_role_dict.get(user_id, set())
    user_role_permissions = set()
    for user_role_id in user_role_ids:
        role_permission = role_permission_dict.get(user_role_id, set())
        user_role_permissions = user_role_permissions.union(role_permission)
    user_all_permissions = user_permissions.union(user_role_permissions)
    if logic == "AND":
        return True if permissions.issubset(user_all_permissions) else False
    elif logic == "OR":
        return True if permissions.intersection(user_all_permissions) else False


@app.route('/admin')
@permission_check("get")
def do_admin_index():
    return Response('heihei')


@app.route('/articles')
def do_articles():
    return Response('Only if you are admin')


if __name__ == '__main__':
    app.run()
