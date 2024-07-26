```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "<arn-from-lambda-role>"   
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<bucket-name>/*"   
        }
    ]
}

```

`Change the arn from lambda role for Principal`

`Remember to change the bucket name` 