# 🐔 Chicken Disease Classification

An end-to-end deep learning project that classifies chicken diseases from fecal images.

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

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

- Original repository inspiration: [End-to-End-Chicken-Disease-Classification](https://github.com/entbappy/End-to-End-Chicken-Disease-Classification-using-Fecal-Image.git)
