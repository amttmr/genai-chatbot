import os

def get_prompt_template(template_name: str) -> str:
    templates_file = os.path.join(os.path.dirname(__file__), 'templates.txt')
    with open(templates_file, 'r') as f:
        for line in f:
            if line.startswith(f"{template_name}:"):
                return line[len(template_name) + 1:].strip()
    return ""  # Default empty if not found
