


# Build infrastructure 
## Architecture 
[Digram](./docs/architecture.md)

## AWS profiles configuration
you need to configure aws profile locally to run terraform configuration 

```shell 
vi ~/.aws/credentials
```

```shell 
[minisedric_dev]
aws_access_key_id = aws_access_key_id
aws_secret_access_key = aws_secret_access_key
region = preffered_region
```

to check if profiles is configured

```shell 
aws configure list-profiles           
```
## Python .env 

Add keys in file .env in root directory 
```
SECRET_KEY=test
ENV=test
```
for local  testing
```
AWS_ACCESS_KEY_ID=1
AWS_SECRET_ACCESS_KEY=1
AWS_DEFAULT_REGION=1 
S3_BUCKET_NAME=s3test
S3_BUCKET_URI=s3
```

## Commands to build infrastructure 
run in directory where env is
```shell
cd ./infrastructure/test
```

build 
```shell
terraform validate && terraform apply 
```
 
to destroy 
```shell
terraform destroy      
```


> [!TIP]
> Some of the resources with data may not be destroyed automatically (for example s3 with data)

# Testing 
## Build locally docker 

Check call 
```shell
curl -XPOST "http://localhost:9000" -d '{}'      
```

Docker run image 
```shell 
docker run --rm -p 9000:8080 URL/minisedric-lambda-api:latest      
```

Docker build 
```shell
docker build --platform linux/amd64 -t URL/minisedric-lambda-api:latest -f ./DockerfileLambda ./                               
```

## Locally run through poetry in virtualvenv

### Run
```shell
poetry run uvicorn main:app --reload --app-dir src
```

### Add dependencies

```shell
poetry add package_name
```
 

## Documentation 

Swagger is automatically on /docs page. 