docker_prompt_template ="""
Assume you are a Dockerfile expert. Generate a Dockerfile based on the specific information provided by the user.
I want base image of Dockerfile to be {base_image} and I want to install {run_options} using apt-get.
I want my working directory to be {workdir} and I want to copy {copy} from my project files to {workdir}.
I want to expose port {expose_port} and we have these extra requirements needs to be installed: {extras}.
Make sure the Dockerfile is optimized and follows best practices. Don't include any explanations, just provide the dockerfile content. If you think something is missing, add it but don't add too much.
We don't work with requirements.text, we use pyproject.toml for dependency management. Keep the CMD instruction as provided: {cmd}.
"""

def render_dockerfile(base_image, run_options, workdir, copy, expose_port, cmd, extras):
    return docker_prompt_template.format(base_image=base_image, run_options=", ".join(run_options) if run_options else "no additional packages",
                                         workdir=workdir, copy=copy, cmd=cmd if cmd else "Don't add CMD step", expose_port=expose_port, extras=extras if extras else "no extra commands")