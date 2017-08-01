import os

import six

from zk_observer.utils.zk import get_zk

NODES = {
    'animals': {'bears': ['white', 'black', 'brown']},
    'trees': {'conifers': ['pine', 'larch', 'spruce', 'fir-tree']},
    'flowers': {'red': ['rose'], 'yellow': ['tulip']},
}


def insert_demo_data():
    for section, kinds in six.iteritems(NODES):
        for kind, names in six.iteritems(kinds):
            for name in names:
                get_zk().create(os.path.join(section, kind, name), makepath=True)

insert_demo_data()
