# 🐔 Chicken Disease Classification

An end-to-end deep learning project that classifies Chicken disease from fecal images.

## 📌 Overview

This project uses Convolutional Neural Networks to identify chicken diseases from fecal samples, helping in early detection and prevention of disease spread in poultry farms.

## 🛠️ Tech Stack

- Python 3.8
- TensorFlow/PyTorch
- DVC (Data Version Control)
- Docker
- AWS (EC2, ECR)
- GitHub Actions (CI/CD)

## ⚙️ Workflow

1. Update configuration files (`config.yaml`, `secrets.yaml`, `params.yaml`)
2. Update entity classes
3. Configure component managers
4. Update pipeline components
5. Update main execution script
6. Update DVC pipeline

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Conda
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/kabyik-kayal/Chicken-Disease-Classification.git
cd Chicken-Disease-Classification

# Create and activate your environment

#### If using Conda
conda create -n cnncls python=3.8 -y
conda activate cnncls

#### If using venv
python -m venv venv
# Activate virtual environment
## On Windows
venv\Scripts\activate
## On Linux or MacOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 🔄 CI/CD Pipeline with AWS

This project includes a complete CI/CD pipeline using GitHub Actions and AWS:

1. Build Docker image
2. Push image to AWS ECR
3. Deploy on AWS EC2 instance
4. Automated testing and deployment

### AWS Setup Requirements

- IAM user with ECR and EC2 access
- ECR repository for Docker images
- EC2 instance (Ubuntu) with Docker installed
- GitHub repository secrets configuration

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

    # with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws


    # Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2 

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
    
    - Save the URI: 

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:
    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

## 6. Configure EC2 as self-hosted runner:

    github > project-repo > setting > actions > runner > new self hosted runner > choose os > then run command one by one

## 7. Setup github secrets:

    AWS_ACCESS_KEY_ID =

    AWS_SECRET_ACCESS_KEY =

    AWS_REGION = 

    AWS_ECR_LOGIN_URI = 

    ECR_REPOSITORY_NAME = 


## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

- Original repository inspiration: [End-to-End-Chicken-Disease-Classification](https://github.com/entbappy/End-to-End-Chicken-Disease-Classification-using-Fecal-Image.git)