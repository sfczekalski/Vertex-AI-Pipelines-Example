import kfp
from kfp import dsl

IMAGE = "us-docker.pkg.dev/learning-terraform-428213/gcr.io/pipeline"


@dsl.container_component
def train():
    return dsl.ContainerSpec(image=IMAGE, command=["python"], args=["main.py"])


@kfp.dsl.pipeline(
    name="example_pipeline"
)
def pipeline():
    train()


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=pipeline,
        package_path="pipeline.yaml"
    )
