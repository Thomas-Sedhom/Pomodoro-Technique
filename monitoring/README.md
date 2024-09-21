# Monitoring Logs with Grafana and Loki

![monitoring](https://github.com/user-attachments/assets/06b4ee18-da0e-42a2-a208-ed55d824af22)


This setup uses Docker Compose to run an application and monitor its logs using Grafana and Loki.

## Table of Contents

- [Monitoring Logs with Grafana and Loki](#monitoring-logs-with-grafana-and-loki)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
    - [Clone the Repository](#clone-the-repository)
    - [Run Docker Compose](#run-docker-compose)

## Prerequisites

- Docker
- Docker Compose

## Setup

### Clone the Repository

Clone the repository containing the `docker-compose.yaml` file.

### Run Docker Compose

Start the services using Docker Compose:

```sh
docker compose up
```

![img_18](https://github.com/user-attachments/assets/3f55f991-42e4-44ba-8d07-804735cbb036)

- then we can login in grafana `localhost:3000`
- open my application `localhost:8000`
- prometheus `localhost:9090`


**Stopping the Setup**
To stop the Docker Compose setup, run:
```bash
docker compose down
```
