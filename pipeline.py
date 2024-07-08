import kfp
from kfp import dsl

IMAGE = "us-docker.pkg.dev/learning-terraform-428213/gcr.io/pipeline"


@dsl.container_component
def prepare_data(
    X_train_dataset: dsl.Output[dsl.Dataset],
    y_train_dataset: dsl.Output[dsl.Dataset],
    X_test_dataset: dsl.Output[dsl.Dataset],
    y_test_dataset: dsl.Output[dsl.Dataset],
):
    return dsl.ContainerSpec(
        image=IMAGE,
        command=["python"],
        args=[
            "prepare_data.py",
            X_train_dataset.path,
            y_train_dataset.path,
            X_test_dataset.path,
            y_test_dataset.path,
        ]
    )


@dsl.container_component
def train(
    X_train_dataset: dsl.Input[dsl.Dataset],
    y_train_dataset: dsl.Input[dsl.Dataset],
    X_test_dataset: dsl.Input[dsl.Dataset],
    y_test_dataset: dsl.Input[dsl.Dataset],
):
    return dsl.ContainerSpec(
        image=IMAGE,
        command=["python"],
        args=[
            "train.py",
            X_train_dataset.path,
            y_train_dataset.path,
            X_test_dataset.path,
            y_test_dataset.path,
        ]
    )


@kfp.dsl.pipeline(
    name="example_pipeline"
)
def pipeline():
    outputs = prepare_data().outputs

    train(
        X_train_dataset=outputs["X_train_dataset"],
        y_train_dataset=outputs["y_train_dataset"],
        X_test_dataset=outputs["X_test_dataset"],
        y_test_dataset=outputs["y_test_dataset"],
    )


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=pipeline,
        package_path="pipeline.yaml"
    )
