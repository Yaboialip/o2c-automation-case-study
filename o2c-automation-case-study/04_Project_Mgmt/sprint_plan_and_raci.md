# Sprint Plan, Project Plan and RACI

## Sprint plan (100 story points, 5 sprints of 2 weeks)
| Sprint | Goal | Stories | Points |
|---|---|---|---|
| 1 | Order entry with stock validation and secure access | US-01, US-02, US-03, US-16, T-01 | 23 + task |
| 2 | Controls and concurrency | US-15, US-04, US-05, US-06 | 23 |
| 3 | Fulfilment and automated invoicing | US-07, US-08, US-09 | 21 |
| 4 | Payments, replenishment and auditability | US-10, US-11, US-12, US-14, B-05 | 20 + B-05 |
| 5 | Returns, dashboard, UAT and release | US-13, US-17 (B-01, B-04 if capacity) | 13 plus UAT |

## 10-week project plan
| Week | Phase | Deliverables | Exit gate |
|---|---|---|---|
| 1 | Initiation | Problem statement, stakeholders, objectives, scope | Scope agreed |
| 2 | Analysis | AS-IS BPMN, business rules, FR list | BRD and FSD draft reviewed |
| 3 | Design | TO-BE BPMN, ERD, wireframes, stories, Jira board | Backlog ready |
| 4 to 8 | Build (5 sprints) | Odoo configuration, test execution per sprint | Sprint demos accepted |
| 9 | Test and UAT | System test, UAT, defect fixes, sign-off | UAT exit criteria met |
| 10 | Release and handover | Training guide, demo video, README, lessons learned | Portfolio published |

## RACI (R responsible, A accountable, C consulted, I informed)
| Activity | BA | Sponsor | Sales Mgr | Warehouse Spv | Finance Mgr | IT Admin |
|---|---|---|---|---|---|---|
| Requirements elicitation | R | A | C | C | C | I |
| BRD and FSD approval | R | A | C | C | C | C |
| Odoo configuration | R | I | C | C | C | A |
| Data migration | C | I | C | R | R | A |
| Test case design | R | I | C | C | C | I |
| UAT execution | C | I | R | R | R | I |
| UAT sign-off | C | A | R | R | R | I |
| Training | R | I | C | C | C | I |
| Go-live decision | C | A | R | R | R | C |

## Jira setup
Import `jira_import.csv` (map Summary, Issue Type, Priority, Story Points, Epic Link, Sprint, Labels, Description). Workflow: To Do, In Progress, In Test, Done. Take screenshots of the backlog, a sprint board and a burndown chart for the portfolio.
