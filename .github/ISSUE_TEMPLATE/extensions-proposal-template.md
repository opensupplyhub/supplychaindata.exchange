---
name: SC-DEX Extension Proposal Template
about: Propose a new SC-DEX use case through an extension
title: "[EXTENSION PROPOSAL] "
labels: extension
assignees: ''
---

# SC-DEX Extension Proposal Template

| Status        | (Proposed / Accepted / Implemented / Obsolete)       |
|:--------------|:-----------------------------------------------------|
| **Extension #** | [NNN](https://github.com/org/repo/pull/NNN) (update when applicable) |
| **Author(s)** | Your Name (email@example.com)                        |
| **Partner**   | Partner Organization Name (email@example.com)        |
| **Updated**   | YYYY-MM-DD                                           |
| **Obsoletes** | Any prior SC-DEX extension it replaces, if applicable |

---

## Objective

Describe specifically what this proposed extension adds as a use case to the core schema of the SC-DEX. The core schema represents foundational attributes like **Location** (geospatially), **Organization**, and **Relationship** (between locations, between organizations, between locations and organizations). This extension proposes to build upon the SC-DEX core schema by adding data that captures additional supply chain information beyond these core data attributes.

## Motivation

- **Problem Statement**: Describe the use case this extension aims to express with data. What supply chain scenarios, information, or metrics does this extension enable or enhance?
- **Stakeholders**: Identify the individuals or organizations and the ecosystems that may be impacted or benefit from this extension.

## Stakeholder Benefits

Outline how this extension will add a valuable use case for organizations and/or end-users, helping to extend the SC-DEX framework. 

*For example, an extension could add data attributes around recruiting fees and wages to facilitate calculating metrics for responsible recruiting.*

## Extension Design

This section defines the technical specifications of the extension, including key data attributes and any other requirements. Describe any new data attributes introduced in this extension and how they contribute to the targeted use case.

### **Example Use Case: Responsible Recruiting**

This extension tracks data around recruitment fees and the employment process:

- **Recruitment Fee**: Amount charged to the worker.
- **Employer Coverage**: Portion of the fee covered by the employer.
- **Timeline**: Dates of initial contact, contract signing, and first paycheck.

```json
"responsible-recruiting": {
                "recruitment-fee": 200,
                "employer-coverage": 150,
                "initial-contact-date": "2024-01-15",
                "contract-signing-date": "2024-02-01",
                "first-paycheck-date": "2024-03-01"
            }
```

### Alternatives Considered

Discuss any other SC-DEX extensions that are similar to this one, including their strengths and limitations. Explain why this proposed extension uniquely meets the intended use case.

## Technical Considerations

Describe relevant technical considerations for implementing this extension. Cover topics like performance (e.g., speed, memory usage), dependencies (e.g., integrations with standards or tools), and compatibility with SC-DEX and other extensions.

## Implementation Plan

Complete the following prompts to outline the implementation approach:

- **Milestones**:
  - Initial steps for designing this extension
  - Steps for validating the extension with stakeholders
  - Final steps for integrating into SC-DEX

- **Partner Organizations**: Identify partner organizations that may serve as data holders, collectors, or stewards for the data attributes relevant to this extension.

- **Next Steps**:
  - Reach out to partner organizations with a description of the use case and proposed extension.
  - Gather information about their API and/or data-sharing protocols.
  - Explore initial steps to co-create this extension within the SC-DEX ecosystem for exchanging supply chain data.

## Questions and Feedback

List any open questions or feedback you are seeking for this extension proposal.
