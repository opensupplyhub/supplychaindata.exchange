## **Technical Schema Structure**

The SC-DEX schema can support different supply chain arrangements, including multiple locations, organizations, and their various affiliations to each other to represent data assets.

- The JSON Schema of the core SC-DEX can be found [here](./core-schema.json)
- The core schema description can be found [here](./schema.md)
- An SC-DEX Example can be found [here](../examples/full/valid/core-schema-example.json)

Below are three examples of entity-relationship diagrams showing how locations, organizations, and affiliations interact in various supply chain scenarios.

### **1. Simple Supply Chain (Single-Tier)**

![Simple Location-Organization Diagram](https://github.com/opensupplyhub/supplychaindata.exchange/blob/6783acbdaac7ad331121dee9927456d56c51a46b/website/locationorganizationsimple.png?raw=true)

In this example, a single location is affiliated with a single organization.

- **Locations**: Represent factories or warehouses.
- **Organizations**: Represent companies that own or manage the locations.
- **Affiliation**: Simple relationship such as "is owned by" or "is supplier of".

---

### **2. Multi-Tier Supply Chain**

This example demonstrates a more complex supply chain where multiple locations are affiliated with multiple organizations.

![Multi-Tier Diagram](https://github.com/opensupplyhub/supplychaindata.exchange/blob/28ce6f3635e311919e8583b00dfa4e9ddacba180/website/locationorganizationmulti.png)

- **Locations**: Different supply chain locations, like multiple factories.
- **Organizations**: Various organizations involved in the supply chain.
- **Affiliations**: Multiple affiliations like "is supplier of", "is owned by", etc.

---

### **3. Complex Affiliation**

In this case, an organization has different types of affiliations with various locations, showing how a single organization can manage multiple types of relationships.

![Complex Affiliation Diagram](https://github.com/opensupplyhub/supplychaindata.exchange/blob/e989167ca3370c900b093afce07f7707939dd75e/website/complexrelationshiporganization.png)

- **Locations**: Different locations related to the organization.
- **Organizations**: One organization with multiple types of affiliations.
- **Affiliations**: One location could be "owned by" the organization, while another might "supply" it.

---

These diagrams show different ways to structure supply chain relationships in SC-DEX, allowing flexibility depending on the complexity of the data. While these common use cases show a mixture of relationships between locations and organizations, we also anticipate the need to express just the relationships between organizations or just between locations, although the case of just locations is rare. That might look like this: 

### **4. Organizations Only**

In this example, multiple organizations are affiliated with each other, without locations attached to them.

![Organizations-Only Diagram](https://github.com/opensupplyhub/supplychaindata.exchange/blob/41df6fd9b8d7aca36edfbf0bf996941d197d4cb0/website/organizationsonly.png)

- **Organizations**: Represent companies that own or manage the locations.
- **Affiliation**: Simple relationship such as "is owned by" or "is supplier of".

This case might be helpful in the instance that there are organizations with frequently changing locations, or if it is an organization with no geo-spatial location (i.e. an entirely remote or virtual operation)

---

### **5. Locations Only**

In this example, multiple locations are affiliated with each other, without organizations attached to them.

![Locations-Only Diagram](https://github.com/opensupplyhub/supplychaindata.exchange/blob/e610ad87ff2933213b071f638df020fe4c35a174/website/locationonly.png)

- **Locations**: Different supply chain locations, like multiple factories.
- **Affiliation**: Simple relationship such as "is within" or "is supplier of".

This is a specific case, as each location is likely to have some kind of organizational identifier associated with it. This case would typically be used to express relationships within an industrial campus park, or perhaps a farm processing location within a field, but would still typically have an organization attached. 
