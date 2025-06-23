import os
import json

# Define input and output paths
INPUT_JSON = "input/pretty_printed.json"
OUTPUT_DIR = "output/components"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_json():
    """
    Parse the JSON file and generate structured Markdown files.
    """
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Parse the `body` key if it exists
    body = data.get("body")
    if body:
        try:
            # Process the body content
            body_data = body if isinstance(body, dict) else json.loads(body)

            # Extract library information
            library_info = body_data.get("library", {})
            generate_library_markdown(library_info)

            # Extract property sections
            property_sections = body_data.get("propertySections", [])
            generate_property_sections_markdown(property_sections)

            # Extract components
            components = body_data.get("components", [])
            for component in components:
                component_name = component.get("name", "unknown_component")
                generate_markdown(component_name, component)

        except json.JSONDecodeError as e:
            print(f"Failed to parse 'body': {e}")
    else:
        print("No 'body' key found in the JSON file.")

def generate_library_markdown(library_info):
    """
    Generate a Markdown file for library information.
    """
    filename = os.path.join(OUTPUT_DIR, "library_info.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Library Information\n\n")
        name = library_info.get("name", "Unknown Library")
        version = library_info.get("version", "Unknown Version")
        f.write(f"- **Name**: {name}\n")
        f.write(f"- **Version**: {version}\n")
    print(f"✅ Library information saved to {filename}")

def generate_property_sections_markdown(property_sections):
    """
    Generate a Markdown file for property sections.
    """
    filename = os.path.join(OUTPUT_DIR, "property_sections.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Property Sections\n\n")
        for section in property_sections:
            name = section.get("name", "Unknown Section")
            description = section.get("description", "No description available.")
            selector = section.get("selector", "No selector available.")
            f.write(f"## {name}\n")
            f.write(f"- **Description**: {description}\n")
            f.write(f"- **Selector**: {selector}\n\n")
    print(f"✅ Property sections saved to {filename}")

def generate_markdown(component_name, component_data):
    """
    Generate a Markdown file for a single component.
    """
    filename = os.path.join(OUTPUT_DIR, f"{component_name}.md")
    with open(filename, "w", encoding="utf-8") as f:
        # Write component name as the title
        f.write(f"# {component_name}\n\n")

        # Add metadata
        version = component_data.get("version", "Unknown Version")
        description = component_data.get("description", "No description available.")
        category = component_data.get("category", "Unknown Category")
        f.write("## Metadata\n")
        f.write(f"- **Version**: {version}\n")
        f.write(f"- **Description**: {description}\n")
        f.write(f"- **Category**: {category}\n\n")

        # Add example sections
        example_sections = component_data.get("exampleSections", [])
        if example_sections:
            f.write("## Example Sections\n")
            for section in example_sections:
                name = section.get("name", "Unknown Section")
                description = section.get("description", "No description available.")
                order = section.get("order", "Unknown Order")
                f.write(f"{order}. **{name}**\n")
                f.write(f"   - Description: {description}\n")
            f.write("\n")

        # Add examples
        examples = component_data.get("examples", [])
        if examples:
            f.write("## Examples\n")
            for example in examples:
                name = example.get("name", "Unnamed Example")
                description = example.get("description", "No description available.")
                section = example.get("section", "Unknown Section")
                url = example.get("url", "No URL available.")
                tags = ", ".join(example.get("tags", []))
                snippet = example.get("snippets", {}).get("tsx", "No example available.")

                f.write(f"### {name}\n")
                f.write(f"- **Section**: {section}\n")
                f.write(f"- **URL**: {url}\n")
                f.write(f"- **Tags**: {tags}\n")
                f.write(f"```tsx\n{snippet}\n```\n\n")

        # Add property sections
        property_sections = component_data.get("propertySections", [])
        if property_sections:
            f.write("## Property Sections\n")
            for section in property_sections:
                name = section.get("name", "Unknown Section")
                selector = section.get("selector", "No selector available.")
                description = section.get("description", "No description available.")
                f.write(f"### {name}\n")
                f.write(f"- **Selector**: {selector}\n")
                f.write(f"- **Description**: {description}\n\n")

        # Add properties
        properties = component_data.get("properties", [])
        if properties:
            f.write("## Properties\n")
            for prop in properties:
                name = prop.get("name", "Unknown Property")
                section = prop.get("section", "Unknown Section")
                data = prop.get("data", {})
                prop_type = data.get("type", "Unknown Type")
                default = data.get("default", "No default value.")
                required = data.get("required", "Unknown")
                description = data.get("description", "No description available.")

                f.write(f"### {name}\n")
                f.write(f"- **Section**: {section}\n")
                f.write(f"- **Type**: {prop_type}\n")
                f.write(f"- **Default**: {default}\n")
                f.write(f"- **Required**: {required}\n")
                f.write(f"- **Description**: {description}\n\n")

    print(f"✅ Markdown generated for {component_name}: {filename}")

def generate_additional_markdown(key, value):
    """
    Generate a Markdown file for additional top-level keys in the JSON.
    """
    filename = os.path.join(OUTPUT_DIR, f"{key}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {key.capitalize()}\n\n")
        f.write(json.dumps(value, indent=4))
    print(f"✅ Additional content saved to {filename}")

if __name__ == "__main__":
    process_json()
