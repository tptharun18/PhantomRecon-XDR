# PhantomRecon-XDR

> **Real-time Extended Detection & Response (XDR) platform** powered by Wazuh, OpenSearch, and custom ML-based threat detection — with multi-channel alerting and containerized deployment.

---

## 📐 System Architecture

PhantomRecon-XDR is built around a modular pipeline that connects monitored endpoints to a centralized SIEM for real-time detection, correlation, and response.

```
Endpoints → Endpoint Agent → Detection Engine → Threat Intelligence → Wazuh Manager
                                                                          ↓
                    Alerting Engine ← OpenSearch Cluster ← Wazuh Dashboard
```

### Core Components

| Component | Role |
|---|---|
| **Python Endpoint Agent** | Collects telemetry, system monitoring, log forwarding, secure communication |
| **Detection Engine** | Custom rules: Suspicious Processes, Reverse Shell, Port Scan, Brute Force, Malware Behavior |
| **Threat Intelligence** | AbuseIPDB API — IP reputation lookup, threat enrichment, malicious IP detection, confidence scoring |
| **Wazuh Manager** | Open-source SIEM — log ingestion, rule correlation, alert generation, active response |
| **OpenSearch Cluster** | Indexing, search, storage, aggregation |
| **Wazuh Dashboard** | Visualization, dashboards, threat hunting, reports |
| **Alerting Engine** | Desktop, Email, and Telegram alerts |

---

## 🔄 Endpoint Monitoring Flow

```
System Activity → Endpoint Agent → Event Normalization → Wazuh Manager
                                                              ↓
Alerts & Response ← Detection Engine ←────────────────────────
```

**System activity monitored:**
- Process Creation
- File Modification
- Registry Changes
- Network Connections

---

## 🧠 Detection Engine Workflow

1. **Log Ingestion** — Logs from endpoints and servers are received by Wazuh
2. **Rule Matching** — Logs are matched against custom detection rules
3. **Correlation & Analysis** — Events are correlated to identify suspicious or malicious activity
4. **Alert Generation** — If a rule is triggered, an alert is generated
5. **Response & Notification** — Alert is sent to dashboard and notification channels

---

## 🔔 Alerting Pipeline

```
Alert Triggered (Rule matched / Threat detected)
        ↓
Alert Enrichment (IP reputation, GeoIP, Threat Intel, MITRE tags)
        ↓
Alert Channels: Desktop | Email | Telegram
        ↓
Analyst / User — Receive alerts and take action
```

---

## 🏗️ Wazuh Integration Architecture

```
Wazuh Agent (Endpoint) ──┐
Wazuh Agent (Server)   ──┼──→ Wazuh Manager (Decode → Rule Engine → Correlate → Alert → Respond)
Other Sources (Syslog) ──┘              ↓                    ↓
                                 OpenSearch             Wazuh Dashboard
                              (Storage & Indexing)      (Visualization)
```

---

## 📁 Project Repository Structure

```
PhantomRecon-XDR/
├── endpoint-agent/        # Python endpoint monitoring agent
├── detections/            # Custom detection rules
├── alerts/                # Alerting modules (email/telegram/desktop)
├── ml-engine/             # ML-based anomaly detection
├── docker/
│   └── wazuh/             # Wazuh single-node setup
├── docs/
│   ├── architecture/      # Architecture diagrams
│   ├── detection-rules/   # Detection rule documentation
│   ├── installation/      # Installation guide
│   └── images/            # Screenshots & diagrams
├── config/                # Configuration files
├── dashboards/            # Dashboards & visualizations
├── logs/                  # Logs (gitignored)
├── tests/                 # Test scripts
├── .gitignore
├── LICENSE                # MIT License
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md           # Changelog
└── README.md              # Project documentation
```

---

## ✨ Key Capabilities

| Capability | Description |
|---|---|
| 🛡️ Real-time Threat Detection | Continuous monitoring of endpoints with instant rule-based detection |
| 🔍 Threat Intelligence Enrichment | Automatic IP reputation and MITRE ATT&CK tag enrichment on alerts |
| 📊 Centralized Logging & Monitoring | All events aggregated in OpenSearch with full-text search |
| 🔔 Multi-channel Alerting | Desktop, email, and Telegram notifications for analyst response |
| 🧠 ML-Powered Anomaly Detection | Behavioral baselines and statistical anomaly detection via ml-engine |
| ⚡ Active Response (Wazuh) | Automated response actions triggered by Wazuh rule matches |
| 🐳 Containerized Deployment | Docker-based single-node Wazuh setup for easy bootstrapping |

---

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- Python 3.8+
- Node.js (optional, for dashboard customization)

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/PhantomRecon-XDR.git
cd PhantomRecon-XDR
```

### 2. Start Wazuh Stack

```bash
cd docker/wazuh
docker-compose up -d
```

### 3. Deploy the Endpoint Agent

```bash
cd endpoint-agent
pip install -r requirements.txt
python agent.py --config ../config/agent.yaml
```

### 4. Configure Alerting

Edit `config/alerts.yaml` to set up your Email / Telegram credentials, then:

```bash
cd alerts
python alert_manager.py
```

---

## 📖 Documentation

- [Architecture Overview](docs/architecture/)
- [Detection Rules Guide](docs/detection-rules/)
- [Installation Guide](docs/installation/)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on code style, branch naming, and the PR process.

