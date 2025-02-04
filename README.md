**AWS-Based Document Management System (DMS) - Architecture**

### AWS Services Used
S3 - Store uploaded and extracted text files  
DynamoDB - Store metadata (title, sections, timestamps)  
Lambda - Automate text extraction and formatting  
API Gateway - Provide REST APIs for document retrieval  
Cognito - Secure user authentication  

### Low-Level Design (LLD)
1. **User Uploads a PDF to S3**  
   - The frontend uploads a document via an API.  
   - S3 triggers **Lambda** on file upload.

2. **Lambda Extracts and Formats Text**  
   - Reads PDF using `pdfplumber` .  
   - Maintains section hierarchy and saves formatted text in **S3**.

3. **DynamoDB Stores Metadata**  
   - Stores document title, section headers, and timestamps for **quick lookups**.

4. **API Gateway Exposes REST APIs**  
   - Provides endpoints for:  
     - Fetching document lists.  
     - Retrieving formatted text from **S3**.  
     - Accessing metadata from **DynamoDB**.

5. **Cognito Handles Authentication**  
   - Ensures only **authorized users** can access documents.

6. **Frontend Displays Documents**  
   - Fetches metadata and text via API.  
   - Presents a structured **hierarchical view** of extracted text.

### Key Benefits
✅ **Scalable** – Handles increasing documents efficiently.  
✅ **Secure** – Only authenticated users can access files.  
✅ **Cost-Effective** – Serverless AWS components optimize cost.  
✅ **Automated Processing** – Real-time extraction on upload.  



