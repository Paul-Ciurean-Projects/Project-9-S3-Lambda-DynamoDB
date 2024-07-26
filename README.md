# Automated CSV Data Processing Pipeline with AWS

![architecture](/images/P9.png)

### **Overview**

### This project involves the creation of an automated data processing pipeline using Amazon Web Services (AWS). The primary goal is to upload a CSV file to an S3 bucket, which triggers a Lambda function to process the file and update a DynamoDB table based on the contents of the CSV.

### **Components**

1. **Amazon S3 Bucket:** The S3 bucket serves as the storage location for the uploaded CSV files. Whenever a new file is uploaded, it triggers the Lambda function.

2. **AWS Lambda Function:** This function is the core of the data processing pipeline. It gets triggered by the S3 bucket event, reads the CSV file, processes its contents, and updates the corresponding DynamoDB table.

3. **Amazon DynamoDB:** This NoSQL database stores the processed data from the CSV file. The Lambda function parses the CSV data and inserts or updates records in the DynamoDB table accordingly.

### **Workflow**

1. **CSV Upload:** A user uploads a CSV file to the designated S3 bucket.

2. **S3 Event Trigger:** The upload event triggers the Lambda function.

3. **CSV Processing:** The Lambda function reads the CSV file, processes its contents, and updates the DynamoDB table.

4. **Database Update:** The DynamoDB table is updated with the data from the CSV file.

### **CSV Decoding Issue**

### During the development of this project, an issue was encountered with decoding the CSV files. Initially, the Lambda function faced difficulties in correctly reading the CSV content due to encoding problems. The CSV files contained a Byte Order Mark (BOM) at the beginning, which led to incorrect data parsing.

### To resolve this issue, the CSV decoding mechanism was modified to use `decode('utf-8-sig')`. This approach correctly handled the BOM, ensuring that the CSV files were read and processed accurately. Here is a brief explanation of the solution:

- **Problem:** Incorrect CSV file reading due to BOM, causing data parsing errors.
- **Solution:** Change the decoding method to `decode('utf-8-sig')` to correctly handle the BOM and read the CSV content accurately.

## **Use Case: Automated Inventory Management System**

### **Scenario**
### A retail company needs an efficient system to manage and update its inventory records. They receive regular CSV files from various suppliers, each containing information about stock levels, product details, and shipment updates. Manually updating the inventory database with these CSV files is time-consuming and prone to errors. An automated solution is required to streamline this process.

### **Solution**
### The company implements the automated CSV data processing pipeline using AWS services as described in the project. Here's how it works:

1. **CSV File Upload by Suppliers:** Suppliers upload CSV files containing inventory updates to a designated S3 bucket.
2. **Triggering Lambda Function:** The upload event in the S3 bucket triggers an AWS Lambda function.
3. **Processing CSV Data:** The Lambda function reads the uploaded CSV file, processes the inventory data, and updates the corresponding records in a DynamoDB table.
4. **Updating Inventory Records:** The DynamoDB table is updated with the latest stock levels, product details, and shipment information from the CSV file.

### **Benefits**
1. **Efficiency:** The automated process reduces the need for manual data entry, significantly speeding up the inventory update process.
2. **Accuracy:** By automating the data ingestion, the system minimizes human errors associated with manual updates.
3. **Scalability:** The solution can handle a high volume of CSV file uploads, making it suitable for large retail operations with multiple suppliers.
4. **Real-time Updates:** Inventory records are updated in near real-time as soon as new CSV files are uploaded, ensuring that the company's inventory data is always current.

## **Conclusion**

### This project successfully implements an automated pipeline for processing CSV files and updating a DynamoDB table using AWS services. The issue with CSV decoding was identified and resolved, ensuring robust and reliable data processing. This setup can be extended and customized further to meet specific business requirements, providing a scalable solution for automated data ingestion and processing.