# Start Here: What is ready and what you still do

## Ready in this folder
- README.md (case study page for GitHub; simulated KPI results filled in from the script run)
- 01: Requirements_Workbook.xlsx (46 FRs, 10 rules, 17 stories, backlog), backlog_items.md
- 02: BPMN AS-IS and TO-BE, ERD (SVG, PNG, DBML), wireframe link
- 03: Test_Management_Workbook.xlsx (62 test cases, RTM with coverage formulas, UAT, defect log, execution summary)
- 04: sprint plan, RACI, jira_import.csv
- 05: Odoo notes template, demo script
- 06: generate_data.py, 10,000-row simulated data set, KPI summary and charts

## You must still do (these cannot be produced for you)
1. Export the BRD/FSD document from Claude (open the doc, then export or download as PDF) and save it as `01_Requirements/BRD_FSD.pdf`. It also contains the user stories with Gherkin, section 15 (fit-gap) and section 21 (Odoo walkthrough).
2. Install Odoo, configure it, and fill `05_Solution/odoo_configuration_notes.md`.
3. Execute the test cases in the workbook, set statuses, and log real defects (DEF-001 to DEF-003 are illustrative).
4. Create the Jira board by importing jira_import.csv, then take screenshots.
5. Recreate the wireframes in Figma (optional but recommended) and update the link.
6. Record the demo video and add the link to the README.
7. Fill in README sections 7 (testing summary) and 8 (lessons learned) after execution.
8. Optional: load the CSV into Apache Superset and add a dashboard screenshot.

## Honesty rules
- The client, data and KPI results are simulated; keep the label in the README and in interviews.
- Do not claim test results you have not run.
