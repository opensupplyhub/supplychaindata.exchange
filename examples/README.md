# **SC-DEX Examples and Use Cases**

This page provides examples of how to implement extensions to the SC-DEX core schema for various use cases. These examples demonstrate the flexibility of SC-DEX to handle specific supply chain challenges and industries.

---

## **How to Contribute or Submit an Extension**

We welcome contributions from both technical and non-technical partners interested in expanding the SC-DEX schema to support new use cases. Extensions allow you to add custom fields while maintaining compatibility with the core structure.

To propose a new extension:

1. **Use the Extension Proposal Template**  
   Submit your idea directly through our [GitHub Issue Template for Extensions](https://github.com/opensupplyhub/supplychaindata.exchange/issues/new?template=sc-dex-extension-proposal-template.md).

2. **Include These Details**  
   The template will guide you to provide:
   - A short description of the extension and its purpose.
   - The relevant entity (location, organization, or affiliation) it extends.
   - A list of new fields, their types, and any expected formats.
   - How this extension aligns with a specific use case or implementation.

3. **Get Feedback and Collaborate**  
   Once submitted, the SC-DEX community can review, discuss, and help refine the proposal in the comments thread.

For implementation details and examples, visit the [Extensions Implementation Guide](https://github.com/opensupplyhub/supplychaindata.exchange/wiki/7.-Implementation-Tutorials#implementing-extensions).

If you have questions or want to explore ideas before submitting, join our [Slack Community](https://join.slack.com/t/supplychainexchange/shared_invite/zt-2h2f0zvhe-J9ksFAHHtmYCs_I2_Nlr0g).

---

To learn more about the core schema and other use cases, visit our [Core Schema page](../schema/schema.md) and [Extensions page](../wiki/Extensions-for-Use-Cases).
These examples show how SC-DEX can be extended for specific use cases.

---

## **Example Use Case: Responsible Recruiting**

This extension tracks data around recruitment fees and the employment process:

- **Recruitment Fee**: Amount charged to the worker.
- **Employer Coverage**: Portion of the fee covered by the employer.
- **Timeline**: Dates of initial contact, contract signing, and first paycheck.

(Data and source url are for example purposes only)

```json
{
  "organization-guid": "523e4567-e89b-12d3-a456-426614174555",
  "recruitment-fee-usd": 200,
  "employer-coverage-usd": 150,
  "initial-contact-date": "2024-01-15",
  "contract-signing-date": "2024-02-01",
  "first-paycheck-date": "2024-03-01",
  "source-organization": "Fair Hiring Network",
  "source-url": "https://fairhiring.example.org/report/123/org-id/357U8H5Gh"
}
```

---

## **Example Use Case: Sea Level Rise Risk**

This extension layers geographic data on top of the core schema to assess supply chain risk from rising sea levels:

- **Region**: Affected supply chain region.
- **Timing**: Projected date when the location will be underwater.
- **Impact**: Percentage of locations affected year by year.

(Data and source url are for example purposes only)

```json
{
  "location-guid": "623e4567-e89b-12d3-a456-426614174666",
  "region": "Coastal Factory Zone",
  "projected-underwater-date": "2030-12-31",
  "yearly-impact": [
    { "year": 2025, "percentage-affected": 5 },
    { "year": 2026, "percentage-affected": 10 },
    { "year": 2027, "percentage-affected": 15 }
  ],
  "source-organization": "Climate Risk Watch",
  "source-url": "https://climateriskwatch.example.org/factories/zoneA/20250323"
}
```
