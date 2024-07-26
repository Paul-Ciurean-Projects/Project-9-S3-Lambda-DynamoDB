```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:CreateLogGroup",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "dynamodb:PutItem"
            ],
            "Resource": [
                "arn:aws:s3:::<s3-bucket-name>/*", 
                "arn:aws:dynamodb:us-east-1:<account-number>:table/<table-name>" 
            ]
        }
    ]
}

```

`update the S3 bucket name`

`update the account number and table name`