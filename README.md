# ReadMe for XSD Data Extraction and Formatting

## Author:
- Leon Doungala

## Date:
- March 20, 2023

## Place:
- Milan

---

### Project Description:

This Python code is developed to extract data from XML Schema Definition (XSD) files and convert it into structured data formats (CSV). The code consists of two main functions: one for extracting simple types and another for complex types from XSD files. Additionally, there is a formatting function for handling special formatting requirements, such as converting "[]" to None.

---

### Prerequisites:

Before using this code, ensure you have the following prerequisites:

- Python 3.x installed
- Required Python packages (`xmlschema`, `xml.etree.ElementTree`, and `pandas`) installed. You can install them using pip:

    ```bash
    pip install xmlschema pandas
    ```

---

### How to Use:

1. Import the necessary libraries:

    ```python
    from xmlschema import XMLSchema
    import xml.etree.ElementTree as ET
    import pandas as pd


- Use the extractor_SimpleType function to extract data from a Simple Type XSD file:

# Example for extracting simple types
    xsd_file = 'your_xsd_file.xsd'
    csv_outputName = 'output_simple_types.csv'
    df = extractor_SimpleType(xsd_file, csv_outputName)

- Use the extractor_complexType function to extract data from a Complex Type XSD file:

# Example for extracting complex types
    xsd_file = 'your_xsd_file.xsd'
    csv_outputName = 'output_complex_types.csv'
    df = extractor_complexType(xsd_file, csv_outputName)

- Use the FormatercomplexTtype function to format data by replacing "[]" with None in a CSV file:

# Example for formatting complex type data
    file_name = 'output_complex_types.csv'
    TBremove = '[]'
    formatted_df = FormatercomplexTtype(file_name, TBremove)

