import kfp


@kfp.dsl.component
def train():
    import logging
    logger = logging.getLogger()
    logger.info("Train")


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
