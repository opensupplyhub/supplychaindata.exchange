
> [!NOTE]
> The Core Specification is still work in progress. Feedback is welcome!

# **SC-DEX Core Schema Documentation**

The SC-DEX core schema is designed to facilitate structured, machine-readable supply chain data. It is based on key entities: **Locations**, **Organizations**, and **Affiliations**, which define relationships between locations and organizations. This document outlines the core schema structure, along with detailed specifications for each entity.

---

## **Schema Components Overview**

The following table outlines the key components of the SC-DEX schema:

| **Component**       | **Description**                                                                                                                                                      |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Locations**       | Represents physical locations in the supply chain, such as factories, warehouses, farms, etc.                                                                         |
| **Organizations**   | Represents entities (e.g., companies, suppliers) involved in the supply chain.                                                                                        |
| **Affiliations**    | Describes the relationships between locations and organizations (e.g., "is supplier of", "is owned by").                                                              |

---

## **Locations**

### **Locations** represent physical places, such as factories, warehouses, farms, etc.

The Location component of the SC DEX core schema is meant to identify where a supply chains location is physically, and the name, coordinates and/or address properties are optional fields with the intention that this information is already captured within the location-identifiers property. This is meant to build the SCDEX data ecosystem on top of existing supply chain data standards and map the relationships between already established reporting formats, as well as allow for linking different types of geospatial data, for example a point location of a factory (os-id or gln) with a region (field-id). A list of accepted and recommented location-identifiers is in progress.

Optional fields are helpful for cross referencing or appending data attributes onto accepted location-identifiers, but the critical information is already covered by the location-id. 

### **Location Fields Table**

| **Field**          | **Description**                                    | **Required/Optional** |
|--------------------|----------------------------------------------------|-----------------------|
| `guid`             | Unique identifier for the location data            | Required              |
| `location-type`    | Type of location (e.g., factory, warehouse, farm)  | Required              |
| `location-identifier` | One of the accepted location-identifiers is required. (i.e. Open Supply Hub’s unique location identifier (OSID), Varda Agriculture’s Global Field ID for boundaries, etc.)| Required  |
| `language`      | Language code in ISO 639-1 or ISO 639-2 format (e.g., 'en' for English, 'fr' for French).         | Optional             |
| `coordinates`      | Latitude and longitude of the location in ISO 6709         | Optional             |
| `name`         | Name of the location, if available. | Optional             |
| `address`      | the address of the location in ISO 20022 | Optional             |
| `country`      | the country of the location in ISO 3166 ALpha-2 or Alpha-3 | Optional             |
| `sector` | The sector of activities conducted at the location (textiles, raw materials, agricultural, etc)   | Optional|
| `processing-types` | Processing activities conducted at the location    | Optional              |
| `products`         | Products produced at the location                  | Optional              |

> [!NOTE]
> A more complete location-identifier list is in progress and will be published in Q4 of 2024. Please submit to this list by emailing shuya@opensupplyhub.org or through [this form submission](https://docs.google.com/forms/d/e/1FAIpQLSf5iJlmyyYj1QY2tH6IUmVTZL4samFfFglrHXyIh6BDKDc-Qg/viewform?usp=sf_link).

---

## **Organizations**

### **Organizations** represent companies or entities involved in the supply chain.

The Organization component of the SCDEX core schema is meant to identify the relationship of the organization to the location, and the name is an optional field, with the similar intention as the Location schema's location-identifier. A list of accepted and recommended organization-identifiers is in progress.

### **Organization Fields Table**

| **Field**            | **Description**                                 | **Required/Optional** |
|----------------------|-------------------------------------------------|-----------------------|
| `guid`               | Unique identifier for the organization          | Required              |
| `organization-type`  | Type of organization (e.g., supplier, retailer) | Required              |
| `language`      | Language code in ISO 639-1 or ISO 639-2 format (e.g., 'en' for English, 'fr' for French).         | Optional             |
| `name`         | Name of the organization. | Optional             |
| `address`      | the address of the organization in ISO 20022 | Optional             |
| `organizational-identifier`  | One of the accepted organizational-identifiers is required. (i.e., Legal Entity Identifier's LEI or GS1's GLN, etc.)  | Required |

> [!NOTE]
> A more complete organizational-identifier list is in progress and will be published in Q4 of 2024. Please submit to this list by emailing shuya@opensupplyhub.org or through [this form submission](https://docs.google.com/forms/d/e/1FAIpQLSf5iJlmyyYj1QY2tH6IUmVTZL4samFfFglrHXyIh6BDKDc-Qg/viewform?usp=sf_link).

---

## **Affiliations**

Affiliations describe the relationships between **Locations** and **Organizations**. This is a key aspect of the SC-DEX schema, as it allows for the mapping of supply chain relationships, such as "is supplier of" or "is owned by." Affiliations define how entities interact in a supply chain context.

### **Affiliation Fields Table**

| **Field**            | **Description**                                 | **Required/Optional** |
|----------------------|-------------------------------------------------|-----------------------|
| `from-guid`          | Unique identifier for the source entity         | Required              |
| `to-guid`            | Unique identifier for the target entity         | Required              |
| `affiliation-type`   | Type of relationship between the entities       | Required              |

### **Affiliation Types**

Affiliations can represent various types of relationships, including but not limited to:

- **is supplier of**: Indicates that a location or organization supplies goods or services to another.
- **is owned by**: Indicates ownership relationships between entities.
- **provides services for**: Indicates that one entity provides services to another.

## **Examples of Relationship Types from Wikirate**

Wikirate provides an additional set of relationship types that can be referenced for supply chain transparency. These relationships can include:

- **is supplier of**
- **is owned by**
- **is subsidiary of**
- **provides services for**

For more relationship types and examples, refer to the [Wikirate Relationship Types page](https://wikirate.org/Relationship).

> [!NOTE]
> A more complete relationships type list is in progress and will be published in Q4 of 2024. Please submit to this list by emailing shuya@opensupplyhub.org or through [this form submission](https://docs.google.com/forms/d/e/1FAIpQLSf5iJlmyyYj1QY2tH6IUmVTZL4samFfFglrHXyIh6BDKDc-Qg/viewform?usp=sf_link).

