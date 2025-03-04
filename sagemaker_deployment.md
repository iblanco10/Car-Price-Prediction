# AWS SageMaker Deployment Status

## Successfully Completed Steps 
- Built and containerized the model using Docker.
- Pushed the container image to Amazon ECR (`car-price-predictor` in `us-east-2` region).
- Verified that the image exists in ECR.

## Challenge Encountered     
- SageMaker requires Docker Manifest V2 Schema 2 format, but the image was built in OCI format (`application/vnd.oci.image.index.v1+json`).
- This is a known issue with newer Docker clients.

## Solutions for Future Deployment  
- **Option 1:** Rebuild image with Docker BuildKit disabled:
  ```bash
  DOCKER_BUILDKIT=0 docker build -t car-price-predictor:sagemaker .

