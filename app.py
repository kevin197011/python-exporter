import prometheus_client
from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask
from metrics import Metrics

app = Flask(__name__)


@app.route("/metrics")
def metrics():
    REGISTRY = CollectorRegistry(auto_describe=False)
    gauge = Gauge(
        "devops_test_metrics",
        "test",
        ["project", "module"],
        registry=REGISTRY,
    )
    metrics_value = Metrics().values()
    gauge.labels(
        project="project_01",
        module="app01",
    ).set(metrics_value)

    return Response(prometheus_client.generate_latest(REGISTRY), mimetype="text/plain")


@app.route("/")
def index():
    return "<h1>Customized Exporter</h1><br> <a href='metrics'>Metrics</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9291, debug=True)
