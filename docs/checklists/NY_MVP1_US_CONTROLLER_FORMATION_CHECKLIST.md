# NY MVP-1 US Controller Formation Checklist

Date: 2026-09-24

Status: PREPARATION_ONLY

Target hypothesis: US_CONTROLLER_US_MARKET

Preferred bootstrap jurisdiction hypothesis: WYOMING

This checklist does not constitute legal or tax advice and does not authorize P1.

## 1. Formation-provider quote review

Before authorizing a filing, obtain a written quote and identify:

- state filing fee;
- provider formation fee;
- first-year registered-agent fee;
- registered-agent renewal fee;
- EIN assistance fee, if any;
- address/mail service scope and recurring fee, if any;
- document/certification fees, if any;
- optional services and whether they are actually optional;
- cancellation/refund terms;
- expected recurring annual costs;
- support path to a named human contact.

Do not select an upsell because it appears in a checkout flow. Separate mandatory formation costs from optional convenience services.

## 2. Product Owner decisions before filing

The Product Owner must explicitly confirm, with provider/attorney guidance where needed:

- intended LLC legal name plus backup names;
- single-member or multi-member ownership;
- member-managed or manager-managed structure;
- owner/member identity;
- authorized signer;
- intended principal business address;
- registered-agent provider;
- entity intended to sign future LSP/customer agreements;
- entity intended to receive future service fees;
- whether EIN assistance is required;
- whether any US banking/payment account is needed before P1.

Do not infer any answer from the software architecture.

## 3. Data-minimization decisions

Before placing controller information in any project system:

- identify which formation facts are public by nature of the filing;
- identify which facts should stay outside the public GitHub repository;
- keep personal residential address out of the repository unless explicit publication is required and approved;
- keep tax identifiers, identification documents, signatures and banking data out of the repository;
- keep EIN and other tax-account details outside the repository unless a future controlled secret/document policy explicitly requires them.

## 4. Formation evidence to retain outside the public repo

Retain the authoritative documents supplied by the state/provider, such as applicable:

- accepted formation filing;
- state acceptance/confirmation;
- registered-agent engagement confirmation;
- operating agreement, if created;
- EIN confirmation, if obtained;
- invoices/receipts needed to establish actual formation and recurring cost;
- provider terms applicable to the purchased services.

The exact document names depend on the actual provider/state process. Do not invent missing documents.

## 5. Facts to bind after formation

Transfer only verified facts into the controlled Controller Fact Packet:

- exact legal name;
- entity type;
- formation jurisdiction;
- principal business address;
- privacy contact, if defined;
- relevant EU establishment/arrangement facts;
- EU live owner-PII access facts;
- agreement-signing entity;
- fee-receiving entity;
- US-only MVP1 market fact;
- EU targeting fact;
- EU monitoring fact.

## 6. Professional review before real P1

Obtain professional review appropriate to the actual facts for:

- federal tax/compliance obligations of the chosen ownership/entity structure;
- foreign-owned US entity filing obligations;
- Form 5472 / pro-forma Form 1120 applicability and process;
- then-current beneficial-ownership/reporting obligations;
- Wyoming recurring state obligations;
- New York nexus and any foreign-qualification implications for the planned activity;
- contractual role of the LSP/controller;
- privacy/consumer-protection constraints triggered by actual operations;
- cross-border access if any EU person/entity will access live owner PII.

## 7. Formation completion gate

Formation is not considered ready for controller binding until:

- the filing has been accepted;
- the legal name and jurisdiction are evidenced;
- the principal business address is known;
- signing/fee-receiving entity roles are known;
- EU-presence/access and market-scope facts are explicitly answered.

Until then HUMAN_DECIDE_AND_FORM_US_CONTROLLER_ENTITY_FOR_REAL_P1 remains the blocker.

All seven P1 gates remain NOT_GRANTED.
