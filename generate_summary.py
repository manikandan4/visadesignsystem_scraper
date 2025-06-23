
import os
import re

def generate_summary():
    components_dir = "output/components"
    output_file = "output/visa_design_system_summary_by_category.md"

    components_by_category = {}

    for filename in os.listdir(components_dir):
        if filename.endswith(".md") and filename not in ["library_info.md", "property_sections.md"]:
            filepath = os.path.join(components_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

                # Extract metadata
                category_match = re.search(r"- \*\*Category\*\*: (.*)", content)
                description_match = re.search(r"- \*\*Description\*\*: (.*)", content)
                # Extract first code snippet
                code_snippet_match = re.search(r"```tsx\n(.*?)```", content, re.DOTALL)

                if category_match and description_match:
                    category = category_match.group(1).strip()
                    description = description_match.group(1).strip()
                    component_name = filename.replace(".md", "")
                    code_snippet = code_snippet_match.group(1).strip() if code_snippet_match else ""

                    if category not in components_by_category:
                        components_by_category[category] = []

                    components_by_category[category].append({
                        "name": component_name,
                        "description": description,
                        "code_snippet": code_snippet
                    })

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Visa Design System Summary by Category\n\n")
        for category, components in sorted(components_by_category.items()):
            f.write(f"## {category.capitalize()}\n\n")
            for component in components:
                f.write(f"### {component['name']}\n\n")
                f.write(f"- **Description**: {component['description']}\n")
                f.write(f"- **Details**: [details](components/{component['name']}.md)\n\n")
                if component['code_snippet']:
                    f.write(f"**Example:**\n")
                    f.write(f"```tsx\n{component['code_snippet']}\n```\n\n")

    print(f"✅ Summary by category generated at {output_file}")

if __name__ == "__main__":
    generate_summary()
