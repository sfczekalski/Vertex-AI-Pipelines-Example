import kfp
from kfp import dsl

IMAGE = "us-docker.pkg.dev/learning-terraform-428213/gcr.io/pipeline"


@dsl.component
def pass_name() -> str:
    return "test"


@dsl.container_component
def train(name: str):
    return dsl.ContainerSpec(image=IMAGE, command=["python"], args=["main.py", name])


@kfp.dsl.pipeline(
    name="example_pipeline"
)
def pipeline():
    name = pass_name().output
    train(name=name)


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=pipeline,
        package_path="pipeline.yaml"
    )
