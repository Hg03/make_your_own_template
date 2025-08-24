structure = """
# Expected Directory Structure for {project_name}
{root_folder}
├── scripts.py
├ Dockerfile
├ pyproject.toml
├ .gitignore
├ README.md
"""

def render_structure(root_folder, project_name):
    return structure.format(root_folder=root_folder, project_name=project_name )