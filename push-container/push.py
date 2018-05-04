import time
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()
g = Gauge('monitoring_stats', 'Count of tests', registry=registry)
while True:
    g.set(62)
    push_to_gateway('pushgateway:9091', job='all', registry=registry)
    g.set(60)
    push_to_gateway('pushgateway:9091', job='passed', registry=registry)
    g.set(2)
    push_to_gateway('pushgateway:9091', job='failed', registry=registry)
    time.sleep(10)
