import streamlit as st
from myot.backend.dockerfile_template import render_dockerfile
from myot.backend.pyproject_template import render_pyproject
from myot.backend.mappings import list_of_base_images, versions
from myot.backend import llm_call

st.set_page_config(page_title="Minify", page_icon="🔥", menu_items={"About":"https://linkedin.com/in/harishgehlot"}, layout="wide")

def main():
    st.title("Minified: Your Project Template Generator 🔥")
    st.image('assets/banner.png')
    project_name = st.sidebar.text_input(label="What will be your project name ?", placeholder="classifier_project")
    project_placement = st.sidebar.selectbox(label=f"Where do you want to add your {project_name}.", options=[f"Inside src (like src/{project_name}).", f"At root (like {project_name})."])
    if project_name and project_placement:
        st.sidebar.success(f"Project '{project_name}' created successfully!")
        template_type = st.sidebar.selectbox(label="Select the type of template you want to create", options=["Dockerfile", "pyproject"])
        if template_type == "Dockerfile":
            st.subheader("Dockerfile Template Generator")
            with st.form(key="dockerfile_info"):
                row1 = st.columns(2)
                option = row1[0].selectbox(label="Do you want to use python or uv as base image?",options=["python", "uv"])
                base_image_list = list_of_base_images.get(option, [])
                base_image = row1[1].selectbox(label="Select the base image for your Dockerfile",
                 options=base_image_list)
                run_options = st.multiselect(label="Select OS oriented update/install options", options=["build-essential", "git", "curl"])
                row3 = st.columns(2)
                workdir = row3[0].text_input(label="Enter your Working Directory", placeholder="/app, /src ...")
                workdir = workdir if workdir else "/app"
                copy = row3[1].selectbox(label="What you want to copy from your project files?", options=["Everything (.)", "Only src"])
                expose_port = st.number_input(label="Which port do you want to expose?", min_value=1, max_value=65535, value=8000, step=1)
                cmd = st.text_area(label="What command you want to run to start your application?", placeholder="python main.py, uvicorn main:app --host")
                extras = st.text_area(label="Any extra commands you want to add?", placeholder="Want to install extras using RUN command. You can add your thoughts.")
                submit = st.form_submit_button(label="Generate Dockerfile")
                if submit:
                    prompt = render_dockerfile(base_image, run_options, workdir, copy, expose_port, cmd, extras)
                    response = llm_call.execute(prompt)
                    st.code(response["content"], language="dockerfile")
                    
        elif template_type == "pyproject":
            st.header("pyproject.toml Template Generator")
            with st.form(key="pyproject_info"):
                st.info("I am fetching project name from sidebar.")
                python_version = st.selectbox(label="Select the Python version you want to use", options=versions)
                description = st.text_input(label="Provide a short description of your project", placeholder="A short description about your project")
                dependencies = st.text_area(label="Add your required dependencies", placeholder="fastapi, pandas ..")
                submit = st.form_submit_button(label="Generate pyproject.toml")
                if submit:
                    prompt = render_pyproject(project_name, python_version, description, dependencies, project_placement)
                    response = llm_call.execute(prompt)
                    st.code(response["content"], language="toml") 
    else:
        st.sidebar.info("Please enter a project name and click 'Create Project'.")

if __name__ == "__main__":
    main()