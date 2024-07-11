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

experiment_model = aip.get_experiment_model(
    artifact_id="classifier20240710151625", project=PROJECT_ID, location=PROJECT_REGION
)

experiment_model.register_model(display_name="example_model")
