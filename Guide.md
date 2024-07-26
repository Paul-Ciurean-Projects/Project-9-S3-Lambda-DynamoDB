# How To Build This Project

## Step 1: Create an S3 Bucket.

![S3-bucket](/images/create-s3.png)

## Step 2: Create DynamoDB table.

## !!! Make sure that the `Partition key` matches the first item in the `CSV` file. !!!

![create-db](/images/create-db.png)

### Keep the default for the rest of the settings.

## Step 3: Create a Policy and a Role for Lambda.

1. Create a policy with the JSON code I provided in the `/Usefull-files/JSON-for-Lambda-Role.txt`

![policy-for-lambda](/images/policy-for-lambda.png)

## Step 4: Create a Lambda Function.

![create-lambda](/images/create-lambda.png)

## Step 5: Create the code for Lambda.

![code-for-lambda](/images/code-for-lambda.png)

## Step 6: Edit the role for Lambda. Add the policy we created earlier.

### -> Configuration -> Permissions -> Click on the Role Name

![lambda-add-permissions](/images/lambda-add-permissions.png)

### Add the policy from above:

![permissions-for-lambda-role](/images/permissions-for-lambda-role.png)

## Step 7: Configure S3 to trigger Lambda.

1. Create S3 policy: -> Permissions

![s3-policy](/images/bucket-policy.png)

2. Create a trigger event: -> Properties -> Event Notifications

![create-event-1](/images/s3-event-1.png)

![create-event-2](/images/s3-event-2.png)

## You can check if the event was updated by going to the Lambda Function and refreshing the page.

![check-event](/images/check-s3-event.png)

## Time to test the project.

1. Upload a CSV file to S3. 

![upload-to-s3](/images/upload-to-s3.png)

### CSV example:

![csv-example](/images/csv-example.png)

2. Go to DynamoDB and click on the table -> Explore Table Items -> Run Scan

![run-scan](/images/run-scan.png)


## Hope you enjoyed it!

# THE END!