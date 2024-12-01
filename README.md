# Web Crawl Refusal Regular Expressions

This repository contains a collection of meticulously crafted regular expressions (REs) designed for identifying server-side refusal patterns in web crawling datasets. These patterns enable researchers to detect and categorize access blocks, denial messages, and challenges encountered during automated web measurements.

## Overview

The `regular_expressions.py` file is a complementary piece of code to a research paper presented at the [Passive and Active Measurement (PAM) Conference 2025](https://udesa.edu.ar/pam25). While the paper focuses on analyzing server-side blocks and refusal behaviors in web crawling, this repository provides the regular expressions that were developed and refined as part of the research. These expressions serve as tools for identifying and categorizing refusal messages in web crawling data.

### Structure of `regular_expressions.py`

The file is structured as a list of dictionaries, where each dictionary represents a specific refusal scenario. The structure of each dictionary is as follows:

- **`full_msg`**: A sample full message that the server might return. This serves as the context or example text used to build and validate the regex.
- **`regex`**: The regular expression designed to match the refusal message.
- **`type`**: The category of refusal (e.g., `block`, `challenge`, `require_js`).
- **`who`**: The entity being blocked or challenged (e.g., `ip`, `request`, `you`).
- **`why`**: The reason for the refusal (e.g., `security/malicious`, `geoblock`, `excessive/suspicious`).
- **`tag`**: Tags indicating specific platforms, tools, or services involved in the refusal (e.g., `cloudflare`, `modsecurity`, `wordfence`).

#### Example Entry

```python
{
    "full_msg": "Access denied | Cloudflare. Sorry, you have been blocked. This website is using a security service to protect itself from online attacks.",
    "regex": "^.{20,250}us(ing|es) a security service (to|for) protect(ion)? (itself from|against) online attacks",
    "type": "block",
    "who": "you",
    "why": "security/malicious",
    "tag": "cloudflare"
}
```

### How to Use

1. **Integration**:
   - The REs can be integrated into data processing pipelines to classify refusal messages in web crawling datasets.
   - Import the `refusal_regex_set` from `regular_expressions.py` into your Python script.

2. **Regex Matching**:
   - Use the Python `re` library to apply regex patterns to web page content.
   - Example:
     ```python
     import re
     from regular_expressions import refusal_regex_set

     page_content = "Access denied | Cloudflare ..."
     for refusal in refusal_regex_set:
         if re.match(refusal["regex"], page_content):
             print(f"Matched: {refusal['type']} - {refusal['why']}")
     ```

3. **Customization**:
   - Add new patterns to the `refusal_regex_set` by appending dictionaries with the same structure.

### Contributions

Contributions are welcome! If you would like to contribute new patterns or improve existing ones:
- Fork the repository and create a pull request.
- Ensure new REs are validated with test data.
- Add metadata fields (`type`, `who`, `why`, `tag`) for consistency.

### Applications

- **Web Crawling**: Detect and analyze refusal messages to improve crawling strategies.
- **Web Security**: Understand server-side blocking behaviors and improve bot detection mechanisms.

### Conference Context

The regular expressions in this repository were developed as part of a research paper presented at the [Passive and Active Measurement (PAM) Conference 2025](https://udesa.edu.ar/pam25). 

### License

This project is licensed under the MIT License.



