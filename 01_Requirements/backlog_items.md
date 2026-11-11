# Backlog Items Closing Traceability Gaps

These items cover requirements that had no user story when the traceability matrix was built.

## T-01 Master data setup and migration (Task, Sprint 1)
Covers FR-MD-01 to FR-MD-05. Load 20 customers and 40 products from CSV, validate duplicates, create one customer price list.

## B-05 Stock adjustment with approval (Story, Must, Sprint 4)
**As a** Warehouse Admin, **I want to** adjust stock with a reason code and Supervisor approval **so that** corrections are controlled and traceable.
Covers FR-INV-05, BR-08.
```gherkin
Scenario: Adjustment requires a reason code
  Given I open the stock adjustment screen for "Gula 1kg"
  When I enter a quantity change without selecting a reason code
  Then the system rejects the adjustment with "Reason code is required"

Scenario: Adjustment above zero needs Supervisor approval
  Given I submit an adjustment of -5 units with reason "Damaged"
  Then the adjustment status is "Pending Approval" and On Hand does not change yet
  When the Warehouse Supervisor approves it
  Then On Hand decreases by 5 and a stock movement of type "Adjustment" is logged with both users

Scenario: Adjustment cannot make stock negative
  Given On Hand is 3 and Reserved is 0
  When I submit an adjustment of -5 units
  Then the system rejects it with "Adjustment would result in negative stock"
```

## B-01 Amend a confirmed order (Story, Should, Sprint 5 if capacity allows)
**As a** Sales Rep, **I want to** amend a confirmed order **so that** quantity changes are re-validated and logged.
Covers FR-ORD-09.
```gherkin
Scenario: Increase quantity within available stock
  Given a confirmed order line of 40 units and Available stock of 20
  When I amend the line to 55 units
  Then Reserved increases by 15, the amendment is logged, and the order stays "Confirmed"

Scenario: Increase quantity beyond available stock
  Given Available stock is 10
  When I amend the line from 40 to 60 units
  Then the amendment is blocked with "Insufficient stock. Available: 10" and the order is unchanged
```

## B-04 Cycle count and stock movement history (Story, Should, Sprint 5 if capacity allows)
**As a** Warehouse Supervisor, **I want** cycle counts and movement history **so that** I can find and explain stock variances.
Covers FR-INV-08, FR-INV-09.
```gherkin
Scenario: Cycle count shows variance
  Given system quantity 200 for "Gula 1kg"
  When I record a counted quantity of 195
  Then the variance shows -5 and an adjustment proposal is created

Scenario: Movement history is chronological
  When I open the movement history for a product
  Then I see reservations, releases, shipments, receipts and adjustments in time order with user and reference
```

## B-02 Order confirmation to customer (Story, Could, Deferred)
**As a** Sales Rep, **I want** an order confirmation sent to the customer **so that** they have written proof. Covers FR-ORD-10.

## B-03 Overdue payment reminders (Story, Could, Deferred)
**As a** Finance Staff, **I want** automatic reminders for overdue invoices **so that** I do not chase each manually. Covers FR-FIN-08.
