# Romanian translator glossary (English | Romanian)

Used by `scripts/translate_po.py --lang ro` (appended to the system prompt) and by human reviewers.
Sources: existing `locale/ro/LC_MESSAGES/*.po` and the Romanian UI catalogues of eyssen-owl
(`addons/{account,l10n_ro*,sale,purchase,stock,hr}/i18n/ro.po`). Where the old documentation
catalogue was inconsistent (e.g. "Sold trial", "Raport Taxa"), the UI wording wins: it is what the
user sees on screen and what `:guilabel:` / `:menuselection:` must match.

Rules: formal register ("dumneavoastră", imperative plural/polite: "Faceți clic", "Selectați");
comma-below diacritics only (ș ț, never ş ţ); keep `:guilabel:`/`:menuselection:` labels equal to the
UI strings below.

## UI: navigation and apps
Apps | Aplicații
Accounting | Contabilitate
Invoicing | Facturare
Sales | Vânzări
Purchase | Achiziție (menu); Achiziții (app name in text)
Inventory | Stoc (UI menu); Inventar (only when the UI says so)
Manufacturing | Producție
Point of Sale | Punct de vânzare
Website | Site web
Employees | Angajați
Time Off | Concediu
Recruitment | Recrutare
Expenses | Cheltuieli
Dashboard | Tablou de bord
Configuration | Configurare
Settings | Setări
Reporting | Raportare
Operations | Operațiuni
Products | Produse
Customers | Clienți
Vendors | Furnizori
Orders | Comenzi
Contacts | Contacte
Companies | Companii
Activities | Activități
Messages | Mesaje
Notes | Note
Tags | Etichete
Users | Utilizatori
Filters | Filtre
Group By | Grupează după
Favorites | Favorite
Search | Căutare

## UI: buttons and statuses
Create | Creează
Save | Salvează
Discard | Renunță
Archive | Arhivează
Delete | Șterge
Confirm | Confirmă
Validate | Validează
Send | Trimite
Print | Tipărește
Reset to Draft | Resetează la ciornă
Register Payment | Înregistrează plata
Draft | Ciornă
Posted | Postat
Cancelled | Anulat
Unposted | Nepostat
Unreconciled | Nereconciliat
Active | Activ
Status | Stare
Type | Tip

## Invoicing and documents
Invoice | Factură
Customer Invoices | Facturi clienți
Vendor Bills | Facturi furnizor
Bill | Factură (furnizor)
Credit Note | Notă de credit
Customer Credit Note | Notă de credit client
Vendor Credit Note | Notă de credit furnizor
Refund | Retur
Debit Note | Notă de debit
Proforma | Proformă
Quotation | Ofertă
Request for Quotation | Cerere de ofertă
Sales Order | Comandă de vânzare
Purchase Order | Comandă de achiziție
Delivery Slip / Delivery Note | Aviz de livrare
Waybill / Dispatch note | Aviz de însoțire
Receipt (stock) | Recepție
Receipt (cash) | Chitanță
Down Payment | Plată în avans
Payment Terms | Termene de plată
Early Payment Discount | Reducere pentru plată anticipată
Invoice Date | Data facturii
Due Date | Data scadenței
Payment Date | Data plății
Accounting Date | Dată contabilă
Untaxed Amount | Valoare fără taxe
Tax Included / Excluded | Taxe incluse / Fără taxe
Amount Due | Sumă de plată
Unit Price | Preț unitar
Discount | Reducere
Subtotal | Subtotal
Pricelist | Listă de prețuri
Salesperson | Agent de vânzări
Sales Team | Echipă de vânzări
Incoterms | Incotermuri
E-Invoicing / Electronic invoice | E-facturare / Factură electronică

## Accounting
Journal | Jurnal
Journals | Jurnale
Journal Entry | Notă contabilă (Înregistrare de jurnal)
Journal Entries | Înregistrări în jurnal
Journal Items | Înregistrări contabile
Sales Journal | Jurnal de vânzări
Purchase Journal | Jurnal de cumpărări
Miscellaneous Operations | Operațiuni diverse
General Journal (Romanian statutory) | Registru jurnal
Account | Cont
Chart of Accounts | Plan de conturi
Bank Accounts | Conturi bancare
Bank Statement | Extras bancar
Bank and Cash | Bancă și numerar
Reconciliation / Reconcile | Reconciliere / Reconciliază
Debit | Debit
Credit | Credit
Balance | Sold
Opening Balance | Sold inițial
Closing | Sold final
Trial Balance | Balanța de verificare (balanță)
General Ledger | Cartea mare
Partner Ledger | Registru partener
Account statement / Account card | Fișa contului
Balance Sheet | Bilanț
Profit and Loss | Cont de profit și pierdere
Financial Statements | Situații financiare
Aged Receivable | Creanțe pe vechime
Aged Payable | Datorii pe vechime
Receivable | Creanță (cont: De încasat)
Payable | Datorie (cont: De plată)
Equity | Capital propriu
Income | Venituri
Expense | Cheltuială
Current Assets | Active curente
Fixed Assets | Active fixe
Depreciation | Amortizare
Deferred Revenue | Venit amânat
Deferred Expense | Cheltuială amânată
Fiscal Year | An fiscal
Fiscal Country | Țară fiscală
Lock Date | Dată de blocare
Analytic account | Cont analitic
Budgets | Bugete
Cash Rounding | Rotunjire numerar
Cash Basis | Baza de numerar
Adjustments | Ajustări
Reserve | Rezervă
Currency | Monedă
Exchange rate | Curs valutar
Company | Companie

## Taxes (TVA)
VAT | TVA
Tax | Taxă
Taxes | Taxe
Tax Group | Grup taxă
Tax Grids | Grile fiscale
Tax Exigibility | Exigibilitate taxă
Tax Report | Raport fiscal (Raport TVA for VAT)
Tax Return | Declarație fiscală
VAT Return (D300) | Decont de TVA
Fiscal Position | Poziție fiscală
Fiscal Localization | Localizare fiscală
Fiscal Information | Informații fiscale
Tax ID | Cod de identificare fiscală (CIF/CUI)
Deductible VAT | TVA deductibilă
Collected VAT | TVA colectată
Non-deductible VAT | TVA nedeductibilă
VAT on collection (cash basis) | TVA la încasare
Reverse charge | Taxare inversă
VAT payment | Plata TVA
VAT rate | Cota TVA
Non-taxable | Neimpozabil
Exempt from VAT | Scutit de TVA
Intra-community | Intracomunitar
Declaration | Declarație
Informative declaration | Declarație informativă
Rectifying declaration | Declarație rectificativă
Recapitulative statement (D390) | Declarație recapitulativă
Intrastat | Intrastat
Withholding tax | Impozit reținut la sursă

## Inventory
Warehouse | Depozit
Locations | Locații
Routes | Rute
Transfers | Transferuri
Receipts | Recepții
Delivery | Livrare
Immediate Transfer | Transfer imediat
Backorder | Comandă restantă
Reordering Rules | Reguli de reaprovizionare
Replenishment | Reaprovizionare
Putaway Rules | Reguli de depozitare
Lots/Serial Numbers | Loturi/Numere seriale
Lot | Lot
Package | Pachet
Scrap | Rebut
Unit of Measure | Unitate de măsură
Quantity | Cantitate
Product Category | Categorie produs
Variants | Variante
Attributes | Atribute
Inventory Valuation | Evaluare stoc
Barcode | Cod de bare
Bill of Materials | Listă de materiale
Work Orders | Comenzi de lucru

## HR
Employee | Angajat
Department | Departament
Job Position | Funcție (UI: Poziții job)
Contract | Contract
Payslip | Fluturaș de salariu
Payroll | Salarizare
Attendances | Prezențe
Allocations | Alocări
Expense Report | Raport de cheltuieli
Work Entries | Pontaje

## Generic UI wording
Name | Nume
Description | Descriere
Reference | Referință
Date | Dată
Price | Preț
Total | Total
Partner | Partener
Customer / Vendor | Client / Furnizor
Dashboard | Tablou de bord
Credit Card | Card de credit
Payment Provider | Furnizor de plăți
Miscellaneous | Diverse
Cash | Numerar
Website visitor | Vizitator al site-ului

## Keep in English / do not translate
Odoo, eYssen, eYssen Cloud, Odoo.sh, PostgreSQL, Python, JavaScript, XML, CSV, JSON, API, URL, SQL
ANAF, SPV (Spațiul Privat Virtual), e-Factura, e-Transport, e-TVA, SAF-T, DUK, DUKIntegrator, OPANAF, RO e-Factura
D300, D390, D394, D406, D101, D100 (declaration codes), CIUS-RO, UBL, XSD, XAdES
CUI, CIF, CNP, IBAN, SWIFT/BIC, SEPA, VIES, EORI, NIF
BNR (Banca Națională a României) when used as a data source name
Technical identifiers: module / model / field / group technical names (`l10n_ro_*`, `account.move`,
  `res.partner`), code, XML ids, file paths, URLs, shell commands, config keys
Product/brand names: Stripe, PayPal, Adyen, Google, Microsoft, Azure, WhatsApp, Peppol, Mollie, ...
Terms that only make sense in English (field values quoted from code, technical menu paths in developer
  mode, log messages)
Abbreviations kept as-is: B2B, B2C, KPI, CRM, ERP, POS, SKU, EDI, OCR, PDF, SMTP, DNS, SSL

## Style notes
- "Click" -> "Faceți clic pe"; "Go to" -> "Accesați"; "Navigate to" -> "Navigați la"; "Select" -> "Selectați"
- "Enable" -> "Activați"; "Disable" -> "Dezactivați"; "Set up" -> "Configurați"
- Use "factură" (not "invoice") and "TVA" (not "VAT") in running Romanian text; keep "e-Factura" untranslated.
- Quotes: use plain "..." unless the source already uses typographic quotes.
- Never output cedilla forms (ş ţ Ş Ţ); always ș ț Ș Ț, and ă â î.
