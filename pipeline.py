import kfp


@kfp.dsl.component
def train():
    print("Train")


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
