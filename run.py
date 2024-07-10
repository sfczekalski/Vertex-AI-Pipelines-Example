import google.cloud.aiplatform as aip
import yaml

with open("config.yml") as f:
    config = yaml.safe_load(f)

PROJECT_ID = config["project_id"]
PROJECT_REGION = config["project_region"]

aip.init(
    project=PROJECT_ID,
    location=PROJECT_REGION,
)

job = aip.PipelineJob(
    display_name="example_model_training",
    template_path="pipeline.yaml",
    parameter_values={
        "project_id": PROJECT_ID,
        "project_region": PROJECT_REGION
    }
)

job.submit(experiment="example")
