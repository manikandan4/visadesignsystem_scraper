# Visa Design System Documentation Generator for LLMs

## About the Project

This project contains a set of Python scripts to process the Visa Design System's component library data (in JSON format). It generates structured Markdown documentation and a comprehensive summary file. The primary goal is to create a knowledge base that can be fed to a Large Language Model (LLM) to assist in generating web pages and components that adhere to the Visa Design System.

## Project Workflow

1.  **Scraping Data:**
    *   `visadesignsystem_scraper.py`: This script scrapes the Visa Design System website to gather component data, which is then saved in JSON format.

2.  **Processing JSON to Markdown:**
    *   `process_json_to_markdown.py`: This script takes the raw JSON data, parses it, and creates individual Markdown files for each component, hook, and utility. These files are saved in the `output/components/` directory.

3.  **Generating the LLM-Friendly Summary:**
    *   `generate_summary.py`: This script reads all the individual Markdown files and compiles them into a single, comprehensive summary file named `output/visa_design_system_summary.md`. This summary is structured to be easily understood by LLMs.

## Directory Structure

-   `input/`: Contains the raw or pretty-printed JSON data from the design system.
-   `output/`: Contains all the generated documentation.
    -   `components/`: Holds the individual Markdown file for each component.
    -   `visa_design_system_summary.md`: The final, aggregated summary file to be used as context for an LLM.
-   `prompts/`: Contains sample prompts for interacting with an LLM using the generated summary.
-   `*.py`: The Python scripts that drive the documentation generation workflow.
-   `requirements.txt`: A list of Python packages required to run the scripts.

## How to Use

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Scraper:**
    To get the latest component data from the Visa Design System.
    ```bash
    python visadesignsystem_scraper.py
    ```

3.  **Process JSON to Markdown:**
    To generate individual documentation files for each component.
    ```bash
    python process_json_to_markdown.py
    ```

4.  **Generate the Final Summary:**
    To create the aggregated summary for the LLM.
    ```bash
    python generate_summary.py
    ```

5.  **Use the Summary with an LLM:**
    You can now use the `output/visa_design_system_summary.md` file as a knowledge base or context for a Large Language Model to generate designs, components, or web pages based on the Visa Design System.
