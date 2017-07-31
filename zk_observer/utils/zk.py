import os
from datetime import datetime

from kazoo.client import KazooClient
from kazoo.exceptions import NoNodeError, NoAuthError

from zk_observer import settings
from zk_observer.settings import ZK_ACL

__zk = None


def get_zk() -> KazooClient:
    global __zk

    if not __zk:
        __zk = KazooClient(
            hosts=settings.ZK_HOST,
            auth_data=[('digest', item) for item in ZK_ACL]
        )

    if not __zk.connected:
        __zk.start(3)

    return __zk


def get_nodes_by_path(node_path: str) -> list:
    def exception_to_error(error: Exception, error_node: str) -> dict:
        message = 'Node %s. ' % error_node
        if isinstance(error, NoNodeError):
            message += 'Node does not exist'
        elif isinstance(error, NoAuthError):
            message += 'Authentication error'
        else:
            message += str(error)

        return {'error': message}

    nodes = []

    try:
        children = get_zk().get_children(node_path)
    except Exception as e:
        nodes.append(exception_to_error(e, node_path))

        return nodes

    for child in children:
        child_path = os.path.join(node_path, child)
        try:
            _, node = get_zk().get(child_path)
        except Exception as e:
            nodes.append(exception_to_error(e, child_path))
            continue

        nodes.append({
            'created': str(datetime.fromtimestamp(node.created)),
            'last_modified': str(datetime.fromtimestamp(node.last_modified)),
            'children_count': node.children_count,
            'path': child_path,
            'parent': node_path
        })

    return nodes
