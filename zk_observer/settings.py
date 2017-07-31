import os

ZK_HOST = os.getenv('ZK_HOST') or 'localhost:2181'
if os.getenv('ZK_ACL'):
    ZK_ACL = os.getenv('ZK_ACL').split(',')
else:
    ZK_ACL = []

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
