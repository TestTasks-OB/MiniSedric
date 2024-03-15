

# Build infrastructure 

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


## Commands to build infrastructure 
build 
```shell
terraform validate && terraform apply                                                                                                                                                                                                            crudAPP miniforge3-4.10 at 09:29:08
```
 
destroy 
```shell
terraform destroy      
```


## Build locally 

Check call 
```shell
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'      
```

Docker run image 
```shell 
docker run --rm -p 9000:8080 URL/minisedric-lambda-api:latest      
```

Docker build 
```shell
docker build --platform linux/amd64 -t URL/minisedric-lambda-api:latest -f ./DockerfileLambda ./                               
```