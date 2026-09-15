# AWS Deployment Steps

> Record the actual commands and screenshots you use during deployment. Do not claim a step was completed until you actually perform it.

## 1. Create an EC2 instance
1. Open AWS Management Console.
2. Go to EC2.
3. Launch an Ubuntu Server instance.
4. Create/select a key pair and download the `.pem` file.
5. Configure the security group to allow SSH (port 22) and HTTP (port 80).
6. Launch the instance.

## 2. Connect to EC2
Use SSH from a terminal with the key pair provided by AWS.

## 3. Install required software
Update Ubuntu and install Python, pip, virtual environment support and Git.

## 4. Upload/clone the project
Clone the GitHub repository onto the EC2 instance.

## 5. Set up the Django environment
Create and activate a virtual environment and install packages from `requirements.txt`.

## 6. Initialize the database
Run Django migrations.

## 7. Test the application
Run the Django development server temporarily and verify the application through the EC2 public IP.

## 8. Production setup (if required by the instructor)
Configure Gunicorn and Nginx, then expose the application through HTTP port 80.

## 9. Documentation
Add screenshots of:
- EC2 instance
- Security group
- SSH connection
- Project files on EC2
- Successful Django page
- GitHub repository

Replace this document's generic wording with the exact commands/screenshots actually used.
