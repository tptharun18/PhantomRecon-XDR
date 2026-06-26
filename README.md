<div align="center">

# PhantomRecon-XDR

**AI-Powered Extended Detection & Response Platform**

Collect endpoint telemetry · Detect malicious behavior · Enrich with threat intelligence · Respond in real time

<br/>

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Wazuh](https://img.shields.io/badge/Wazuh-4.x-0055A5?style=flat-square)](https://wazuh.com)
[![OpenSearch](https://img.shields.io/badge/OpenSearch-2.x-005EB8?style=flat-square&logo=opensearch&logoColor=white)](https://opensearch.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-22C55E?style=flat-square)]()

</div>

---

## What is PhantomRecon-XDR?

PhantomRecon-XDR is a modular, open-source **Extended Detection & Response (XDR)** platform built for blue-team operations, security research, and hands-on learning.

It connects a Python-based endpoint agent to the **Wazuh SIEM**, enriches security events with external **threat intelligence**, and delivers alerts across multiple channels — all deployable via Docker in minutes.

> **Built for:** Security students, researchers, and blue-team practitioners who want a production-grade detection pipeline they can own, extend, and learn from.

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                      Monitored Endpoints                         │
│               Windows  ·  Linux  ·  Servers                      │
└──────────────────────────────┬───────────────────────────────────┘
                               │  Process Events · File Changes
                               │  Network Connections · System Logs
                               ▼
                    ┌──────────────────────┐
                    │    Endpoint Agent    │  Python · Secure Transport
                    │  (Telemetry Layer)   │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │   Detection Engine   │  Custom Rules
                    │  (Analysis Layer)    │  Behavioral Signatures
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │ Threat Intelligence  │  AbuseIPDB · MITRE
                    │  (Enrichment Layer)  │  IP Reputation · Scoring
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │   Wazuh Manager      │  Log Decoding
                    │     (SIEM Layer)     │  Rule Correlation
                    └──────┬───────┬───────┘  Active Response
                           │       │
             ┌─────────────▼─┐   ┌─▼────────────────────┐
             │  OpenSearch   │   │    Alerting Engine    │
             │   Cluster     │   │  Desktop · Email      │
             │  Index · Store│   │  Telegram             │
             └───────┬───────┘   └──────────────────────┘
                     │
             ┌───────▼───────┐
             │ Wazuh Dashboard│
             │ Visualization  │
             │ Threat Hunting │
             └───────────────┘
```

---

## Core Components

| Component | Role |
|---|---|
| **Endpoint Agent** | Collects process events, file changes, network connections, and system logs from Windows and Linux endpoints |
| **Detection Engine** | Applies custom Python detection modules for reverse shells, port scans, brute force, and malware behavior |
| **Threat Intelligence** | Enriches suspicious IPs via AbuseIPDB — reputation lookup, confidence scoring, MITRE ATT&CK tagging |
| **Wazuh Manager** | Decodes logs, runs rule correlation, generates alerts, and triggers active responses |
| **OpenSearch Cluster** | Indexes and stores all security events for search and analytics |
| **Wazuh Dashboard** | Provides real-time dashboards, threat hunting, and incident reports |
| **Alerting Engine** | Delivers multi-channel notifications — Desktop, Email, and Telegram |

---

## Detection Capabilities

| Detection Module | Description |
|---|---|
| 🔍 **Reverse Shell Detection** | Identifies outbound shell connections via process and network correlation |
| 🔎 **Port Scan Detection** | Detects sequential or distributed port scanning patterns |
| 🔐 **Brute Force Detection** | Flags repeated authentication failures against services |
| ⚠️ **Suspicious Process Detection** | Monitors for anomalous process trees and unusual parent-child relationships |
| 🦠 **Malware Behavior Detection** | Matches behavioral indicators including registry modifications and persistence mechanisms |
| 🌐 **IP Reputation Analysis** | Checks source IPs against AbuseIPDB with configurable confidence thresholds |
| 📊 **Statistical Anomaly Detection** | Baselines normal behavior and flags deviations *(ML engine — in progress)* |

---

## Feature Status

| Feature | Status |
|---|:---:|
| Endpoint Monitoring (Windows & Linux) | ✅ |
| Custom Detection Rules | ✅ |
| Wazuh SIEM Integration | ✅ |
| OpenSearch Logging & Indexing | ✅ |
| Threat Intelligence Enrichment (AbuseIPDB) | ✅ |
| Desktop Notifications | ✅ |
| Telegram Alerts | ✅ |
| Email Alerts | ✅ |
| Docker Deployment | ✅ |
| ML-Based Behavioral Detection | 🚧 In Progress |
| MITRE ATT&CK Mapping | 🚧 In Progress |
| Sigma Rule Support | 🗓️ Planned |
| Kubernetes Deployment | 🗓️ Planned |

---

## Repository Structure

```
PhantomRecon-XDR/
│
├── endpoint-agent/          # Python endpoint monitoring agent
├── detections/              # Custom detection rule modules
├── alerts/                  # Alerting (email / telegram / desktop)
├── ml-engine/               # ML-based anomaly detection (WIP)
│
├── docker/
│   └── wazuh/               # Wazuh single-node Docker setup
│
├── config/                  # Configuration files
├── dashboards/              # OpenSearch / Wazuh dashboard exports
│
├── docs/
│   ├── architecture/        # Architecture diagrams
│   ├── detection-rules/     # Rule documentation
│   ├── installation/        # Setup and deployment guides
│   └── images/              # Screenshots and diagrams
│
├── logs/                    # Runtime logs (gitignored)
├── tests/                   # Unit and integration tests
│
├── .gitignore
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
└── README.md
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent & Detection | Python 3.11 |
| SIEM | Wazuh 4.x |
| Search & Storage | OpenSearch 2.x |
| Containerization | Docker & Docker Compose |
| Threat Intelligence | AbuseIPDB API |
| Alerting | Telegram Bot API · SMTP · Desktop Notify |
| Supported OS | Windows · Linux |

---

## Quick Start

### Prerequisites

- Docker & Docker Compose
- Python 3.10+
- Git

### 1 · Clone

```bash
git clone https://github.com/tptharun18/PhantomRecon-XDR.git
cd PhantomRecon-XDR
```

### 2 · Start the Wazuh Stack

```bash
cd docker/wazuh
docker compose up -d
```

Wazuh Manager and OpenSearch will be available at `https://localhost` once healthy (allow ~2 minutes on first run).

### 3 · Configure

Copy and edit the example config:

```bash
cp config/example.yaml config/config.yaml
# Set your AbuseIPDB API key, Telegram token, and SMTP credentials
```

### 4 · Deploy the Endpoint Agent

```bash
cd endpoint-agent
pip install -r requirements.txt
python agent.py --config ../config/config.yaml
```

### 5 · Open the Dashboard

Navigate to `https://localhost` in your browser and log in with your Wazuh credentials to see live events and alerts.

---

## Roadmap

- [x] Endpoint Monitoring Agent
- [x] Custom Detection Rule Engine
- [x] Wazuh SIEM Integration
- [x] OpenSearch Integration
- [x] Threat Intelligence Enrichment
- [x] Multi-channel Alerting
- [ ] ML-Based Behavioral Detection
- [ ] MITRE ATT&CK Mapping
- [ ] Sigma Rule Compatibility
- [ ] Interactive Web Dashboard
- [ ] Kubernetes Deployment

---

## Documentation

| Guide | Link |
|---|---|
| Architecture Overview | [docs/architecture/](docs/architecture/) |
| Installation Guide | [docs/installation/](docs/installation/) |
| Detection Rules | [docs/detection-rules/](docs/detection-rules/) |
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Changelog | [CHANGELOG.md](CHANGELOG.md) |

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for branch naming conventions, code style guidelines, and the pull request process.

---

## License

Distributed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

Built by **TP Tharun** — Cybersecurity Student · Security Researcher · Blue Team Enthusiast

*If PhantomRecon-XDR is useful to you, consider giving it a ⭐ on GitHub.*

</div>
