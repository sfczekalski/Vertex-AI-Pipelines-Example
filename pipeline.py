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
    project_id: str,
    project_region: str,
    model: dsl.Output[dsl.Model]
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
            model.path,
            project_id,
            project_region
        ]
    )


@kfp.dsl.pipeline(
    name="example_pipeline"
)
def pipeline(project_id: str, project_region: str):
    prepare_data_task = prepare_data()
    prepare_data_outputs = prepare_data_task.outputs

    train_task = train(
        X_train_dataset=prepare_data_outputs["X_train_dataset"],
        y_train_dataset=prepare_data_outputs["y_train_dataset"],
        X_test_dataset=prepare_data_outputs["X_test_dataset"],
        y_test_dataset=prepare_data_outputs["y_test_dataset"],
        project_id=project_id,
        project_region=project_region
    )

    train_task.set_caching_options(enable_caching=False)


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=pipeline,
        package_path="pipeline.yaml"
    )
