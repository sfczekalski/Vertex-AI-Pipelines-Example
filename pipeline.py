import kfp
from kfp import dsl

IMAGE = "us-docker.pkg.dev/learning-terraform-428213/gcr.io/pipeline"


@dsl.component(packages_to_install=["pandas"])
def pass_data(dataset: dsl.Output[dsl.Dataset]):
    import pandas as pd

    df = pd.DataFrame.from_dict(
        {
            "letter": ["A", "B", "C", "D"],
            "number": [1, 2, 3, 4]
        }
    )

    df.to_csv(dataset.path)


@dsl.container_component
def train(dataset: dsl.Input[dsl.Dataset]):
    return dsl.ContainerSpec(image=IMAGE, command=["python"], args=["main.py", dataset.path])


@kfp.dsl.pipeline(
    name="example_pipeline"
)
def pipeline():
    dataset = pass_data().output
    train(dataset=dataset)


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=pipeline,
        package_path="pipeline.yaml"
    )
