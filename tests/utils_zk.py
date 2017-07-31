import os
from asyncio.test_utils import TestCase

from zk_observer.utils.zk import get_zk, get_nodes_by_path


class TestZk(TestCase):

    def test_get_nodes_by_path(self):
        get_zk().delete('/animals', recursive=True)

        animal_path = '/animals'
        bears_path = os.path.join(animal_path, 'bears')
        kinds = ['black', 'brown', 'white']

        for kind in kinds:
            get_zk().create(os.path.join(bears_path, kind), makepath=True)

        animals_nodes = get_nodes_by_path(animal_path)

        self.assertDictEqual({
            'parent': animal_path,
            'path': bears_path,
            'children_count': len(kinds),
            'created': animals_nodes[0]['created'],
            'last_modified': animals_nodes[0]['last_modified'],
        }, animals_nodes[0])

        bears_nodes = get_nodes_by_path(bears_path)
        for kind in kinds:
            bear_node = bears_nodes.pop(0)

            self.assertDictEqual({
                'parent': bears_path,
                'path': os.path.join(bears_path, kind),
                'children_count': 0,
                'created': bear_node['created'],
                'last_modified': bear_node['last_modified'],
            }, bear_node)
