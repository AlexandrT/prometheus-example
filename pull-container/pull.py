from prometheus_client import start_http_server, Gauge
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY


g = Gauge('my_inprogress_requests', 'Description of gauge', ['type'])
start_http_server(8000)
while True:
    g.labels('all').set(12)
    g.labels('passed').set(10)
    g.labels('failed').set(2)
