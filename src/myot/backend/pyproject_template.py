pyproject_prompt_template = """Assume you are a pyproject.toml expert. Generate a pyproject.toml file based on the specific information provided by the user. This pyproject will be a uv package based manager.
I want my project to be named {project_name} and also provide {description} as provided and I want to use Python {python_version}. 
I want to include the following dependencies: {dependencies}, if there are no dependencies specified, keep the list empty. 
Also add the hatchling part in the pyproject and include the {project_name} at packages parameter also. Don't include any extra explanations or something, just give me pyproject.toml code only.
Take an example of below pyproject.toml.
[project]
name = "{project_name}"
version = "0.1.0"
description = "{description}"
readme = "README.md"
requires-python = ">={python_version}"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/{project_name}"]

""" 

def render_pyproject(project_name, python_version, description, dependencies):
    return pyproject_prompt_template.format(project_name=project_name, python_version=python_version, description=description if description else "A short description about your project", dependencies=", ".join([dep.strip() for dep in dependencies.split(",")]) if dependencies else "no dependencies")