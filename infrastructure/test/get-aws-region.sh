#!/bin/bash


# The name of the AWS profile to use
AWS_PROFILE="${1:-dev}"  # Use 'dev' if no argument is given

# Check if AWS_REGION is set and not empty
if [ -n "$AWS_REGION" ]; then
  echo "{\"region\":\"$AWS_REGION\"}"
else
  # Try to retrieve the region from AWS CLI configuration
  REGION=$(aws configure get region --profile "$AWS_PROFILE")
  if [ -n "$REGION" ]; then
    echo "{\"region\":\"$REGION\"}"
  else
    echo "Region not found" >&2
    exit 1
  fi
fi
