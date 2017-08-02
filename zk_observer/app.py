import json
import os
import pathlib
from datetime import datetime

from httptools import HttpParserInvalidURLError
from kazoo.exceptions import NoNodeError
from sanic import response, Sanic

from zk_observer.utils.file import get_index_page_content
from zk_observer.utils.zk import get_nodes_by_path, get_zk

app = Sanic(__name__)
app.static('/static', os.path.join(pathlib.Path(__file__).parent, 'static'))


@app.route('/nodes')
async def index(request):
    async def streaming_fn(response):
        if 'node' in request.raw_args:
            nodes = get_nodes_by_path(request.raw_args['node'])
            response.write(json.dumps(nodes))

    return response.stream(streaming_fn, content_type='application/json')


@app.route('/node_content')
def node_content(request):
    if 'node' not in request.raw_args:
        raise HttpParserInvalidURLError('GET parameter "node" is required')

    try:
        data, node = get_zk().get(request.raw_args['node'])
        return response.json(
            {
                'content': data,
                'created': str(datetime.fromtimestamp(node.created)),
                'last_modified': str(datetime.fromtimestamp(node.last_modified))
            }
        )
    except NoNodeError:
        return response.json({'error': 'Node was removed'})
    except Exception:
        return response.json({'error': 'Undefined error'})


@app.route('/')
def home(request):
    return response.html(get_index_page_content())
