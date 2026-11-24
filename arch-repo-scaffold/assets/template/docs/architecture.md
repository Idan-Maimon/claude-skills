# {{TITLE_PREFIX}}{{PROJECT_NAME}}

<!--
  How to fill this document (delete this comment once read):
  - Start with section 1. Each requirement is a business operation (create, modify, upgrade,
    delete…), not a feature. Acceptance tests and procedures key off the R-IDs.
  - Every row has a stable ID. Never renumber; leave gaps when something is removed.
  - Decisions (section 5) give the reason, not just the choice. Constraints (section 3) are
    facts you cannot change; decisions are choices you made.
  - Example rows below are shown in comments; replace them with your own.
-->

## 1 :: Requirements

| ID | Requirement | Description |
|---|---|---|
| R1 | | |

<!-- Example:
| R1 | OCP cluster creation | The ability to orchestrate the end-to-end creation of clusters via zero-touch automation, leveraging pre-provisioned inventory |
-->

---

## 2 :: Quality Goals

| ID | Quality Category | Description |
|---|---|---|
| SC1 | | |

<!-- Example:
| SC1 | Operability | The solution can be understood, learned and used |
-->

### 2.1 :: Quality Scenarios

| ID | Quality Scenario | Description |
|---|---|---|
| SC1.1 | | |

<!-- Example:
| SC1.1 | Ease of Use | A tenant can create, modify and upgrade a cluster through a self-service interface without knowing how the platform places it. |
-->

---

## 3 :: Constraints

| ID | Constraint |
|---|---|
| C1 | |

<!-- Example:
| C1 | A single HostedCluster's NodePools cannot span multiple MCE Hubs |
-->

---

## 4 :: Quality Controls

<!-- One column per requirement (R1…), one row per quality scenario (SC…). Each cell lists the
     numbered controls that deliver that quality for that operation. Leave a cell empty when
     there is none yet: the gap is the point of the table. -->

|  | R1 | R2 |
|---|---|---|
| **SC1.1** | | |

---

## 5 :: Architectural Decisions

| ID | Decision | Reason |
|---|---|---|
| AD1 | | |

<!-- Example:
| AD16 | No CPU/Memory Overcommitment on the Hypervisor Layer | The hypervisor runs with dedicated 1:1 CPU and memory per VM. This eliminates double overcommitment when the tenant scheduler also overcommits. |
-->

---

## 6 :: Risks

| ID | Risk | Mitigation Process | Mitigation Status |
|---|---|---|---|
| R1 | | | |

<!-- Example:
| R2 | Seed cluster failure in a zone stops all control planes hosted on it. Existing workloads keep running. | Seed spans three racks; control-plane backups every hour | Partial |
-->

---

## 7 :: Deployment View

### 7.1 Static Deployment View

<!-- ![Deployment View](images/deployment-view.png) -->

### 7.2 Runtime Views

<!-- Link the procedures and animations that show the key runtime scenarios. -->

---

## 8 :: Context & Scope

<!-- One paragraph: what the system does and where its boundary is. -->

### 8.1 External Actors

| Actor | Interaction with the System |
|---|---|
| | |

### 8.2 External Systems

| System | Role |
|---|---|
| | |

### 8.3 Context Diagram

<!-- Diagram to be added -->

---

## 9 :: Naming Conventions

See [naming-convention.md](naming-convention.md) for the full rules. Summary:

| Object | Convention | Reason |
|---|---|---|
| | | |

---

## 12 :: Glossary

<!-- Group terms under ### headings by domain (Infrastructure, Platform, Orchestration…). -->

| Term | Definition |
|---|---|
| | |
