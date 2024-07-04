# Vertex-AI-Pipelines-Example

## Build pipeline Docker image

```bash
cd src
docker build -t us-docker.pkg.dev/learning-terraform-428213/gcr.io/pipeline --platform linux/amd64 .
docker push us-docker.pkg.dev/learning-terraform-428213/gcr.io/pipeline
```