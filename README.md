
# Metadata Service

A small metadata service similar to modern data governance platforms.

Supports:
- Dataset metadata management
- Dataset-to-dataset lineage tracking
- Cycle detection in lineage graph
- Search by dataset name
- Dockerized deployment

---

##Tech Stack

- FastAPI
- MySQL
- SQLAlchemy
- Docker & Docker Compose
- AWS EC2

---

## Architecture Overview

### Dataset Model
- Each dataset is uniquely identified using FQN (Fully Qualified Name).
- FQN is used as the primary key to guarantee uniqueness.

Example:
connection.database.schema.table

---

### Lineage Model
- Lineage is stored as a directed edge between datasets.
- Implemented using a separate `lineage` table.
- Supports upstream and downstream relationships.

---

### Cycle Detection
- Before creating lineage, a DFS (Depth-First Search) traversal is executed.
- If adding a relationship introduces a cycle, the request is rejected.
- Returns HTTP 400 with meaningful error message.

This ensures the lineage graph remains a valid Directed Acyclic Graph (DAG).

---

### Search
- Search endpoint supports searching datasets by name.
- Returns matching datasets and metadata.

---

# open this in chrome  to view the endpoints because i already deployed in the aws using EC2,docker,docker-compose

http://44.207.6.208:8000/docs

