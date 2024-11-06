# **Full Examples**

This directory contains full examples of SC-DEX data structures, both valid and invalid.

The examples in these directories are also used by the backing test suite to validate the SC-DEX schema as it evolves over time, ensuring no regressions are introduced that would break existing data structures.

## **Valid Examples**

Examples within the `valid` directory are considered valid SC-DEX data structures and should pass the schema validation tests.

These examples are used to demonstrate how the SC-DEX schema can be used to represent real-world supply chain data in a standardized format.

## **Invalid Examples**

Examples within the `invalid` directory are considered invalid SC-DEX data structures and should fail with ValidationErrors in the test suite.

These examples are used to ensure that the SC-DEX schema is robust and can catch errors in data structures that do not conform to the standard.
