# Traction Load Testing Setup

This repo sets up a distributed Locust load-testing system with:
- EC2 master + workers
- Mac-hosted Grafana + Prometheus dashboards

---

## 🏗 Folder Structure

| Folder               | Purpose                                     |
|----------------------|-------------------------------------------|
| `docker/`            | Compose files for master + workers         |
| `prometheus/`        | Prometheus scrape config                   |
| `grafana-dashboards/`| Prebuilt Grafana dashboard JSON            |
| `src/`              | Locust load test scripts                   |
| `compose.monitor.yml`| Mac-local Prometheus + Grafana setup       |

---

## 🚀 Setup Steps

### 1️⃣ On EC2 Master

```bash
cd docker
docker compose -f compose.master.yml up -d



traction-load-testing/
├── docker/
│   ├── compose.master.yml
│   └── compose.worker.yml
├── prometheus/
│   └── prometheus.yml
├── grafana-dashboards/
│   └── traction-dashboard.json
├── src/
│   └── load_test.py
├── compose.monitor.yml
├── .gitignore
└── README.md
# traction-load-testing
