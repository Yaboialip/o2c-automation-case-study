# Odoo Configuration Notes (complete while you configure)

> Status: TEMPLATE. Fill in the real Odoo version, menu paths and findings from your own instance. Nothing here has been verified in a live Odoo yet.

- Odoo version / edition / hosting: ______
- Apps installed: Sales, Inventory, Purchase, Invoicing/Accounting

## Test data
5 demo products (Gula 1kg, Minyak Goreng 2L, Teh Celup 25s, Sabun Batang, Mie Instan Dus), 20 customers, 3 suppliers. Opening stock: Gula 200, Minyak Goreng 100, Teh Celup 60, Sabun Batang 0.
Users: sales.rep1, sales.mgr, wh.admin, wh.spv, fin.staff, purchasing.

## Fit-gap (verify each row)
| Requirement | Odoo feature | Fit level | Verified (Y/N) | Workaround / note |
|---|---|---|---|---|
| Customers, products, price lists (FR-MD) | Contacts, Products, Pricelists | Fit | | |
| Draft order, totals, tax (FR-ORD-01, 04) | Quotation to sales order | Fit | | |
| Available stock on order (FR-ORD-02) | Forecasted quantity on order line | Fit | | |
| Block overselling (FR-ORD-03, BR-01) | Availability warning; automation rule to block | Config or Custom | | Standard Odoo usually warns, not blocks |
| Reserve stock on confirmation (FR-INV-02) | Delivery order reservation | Fit | | |
| Approval above IDR 50M / 10% discount (FR-ORD-05) | Order approval setting or automation | Config or Custom | | Depends on edition |
| Credit limit (FR-ORD-06) | Customer credit limit warning | Config | | |
| Cancel and release stock (FR-ORD-08) | Cancel sales and delivery order | Fit | | |
| Pick list, delivery note (FR-SHP) | Delivery orders | Fit | | |
| Partial shipment and backorder (FR-SHP-03) | Backorder prompt | Fit | | |
| Invoice at shipment (FR-FIN-01) | Invoicing policy: delivered quantities | Fit | | |
| Email invoice (FR-FIN-02) | Send and print; outgoing mail server | Config | | |
| Due date from terms (FR-FIN-03) | Payment terms | Fit | | |
| Partial payments, overdue (FR-FIN-04) | Register payment; aged receivable | Fit | | |
| Locked invoices, credit notes (FR-FIN-05, 06) | Posted invoices locked; credit note | Fit | | |
| Low-stock alert (FR-INV-06) | Reordering rules | Config | | |
| Goods receipt (FR-INV-07) | Purchase receipts | Fit | | |
| Audit trail (FR-SEC-02) | Field tracking (chatter) | Config | | |
| Login lockout (FR-SEC-03) | Authentication settings | Config or Custom | | |

## Gaps found and workarounds
(Describe each gap, the workaround, and the impact on the requirement. Example: overselling block implemented as an automation rule on sales order confirmation.)

## Limitations and what would change in production
(Write after your dry run.)
