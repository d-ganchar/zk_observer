import json
import os
import pathlib

from sanic import response, Sanic

from zk_observer.utils.file import get_index_page_content
from zk_observer.utils.zk import get_nodes_by_path

app = Sanic(__name__)
app.static('/static', os.path.join(pathlib.Path(__file__).parent, 'static'))


@app.route('/nodes')
async def index(request):
    async def streaming_fn(response):
        if 'node' in request.raw_args:
            nodes = get_nodes_by_path(request.raw_args['node'])
            response.write(json.dumps(nodes))

    return response.stream(streaming_fn, content_type='application/json')


@app.route('/')
def home(request):
    return response.html(get_index_page_content())
