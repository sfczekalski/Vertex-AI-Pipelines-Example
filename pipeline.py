import kfp
from kfp import dsl

IMAGE = "us-docker.pkg.dev/learning-terraform-428213/gcr.io/pipeline"


@dsl.container_component
def pass_name(name: dsl.OutputPath(str)):
    return dsl.ContainerSpec(
        image="alpine",
        command=[
            'sh', '-c', '''RESPONSE="Testing!"\
                            && echo $RESPONSE\
                            && mkdir -p $(dirname $0)\
                            && echo $RESPONSE > $0
                            '''
        ],
        args=[name]
    )


@dsl.container_component
def train(name: str):
    return dsl.ContainerSpec(image=IMAGE, command=["python"], args=["main.py", name])


@kfp.dsl.pipeline(
    name="example_pipeline"
)
def pipeline():
    name = pass_name().outputs["name"]
    train(name=name)


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=pipeline,
        package_path="pipeline.yaml"
    )
