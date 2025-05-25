# Deployment Guide

This guide covers various deployment options for the Survey Data Filtering Dashboard.

## Table of Contents

1. [Local Deployment](#local-deployment)
2. [Docker Deployment](#docker-deployment)
3. [Cloud Deployment](#cloud-deployment)
4. [Production Considerations](#production-considerations)
5. [Monitoring and Logging](#monitoring-and-logging)
6. [Troubleshooting](#troubleshooting)

## Local Deployment

### Prerequisites

- Python 3.8 or higher
- Git
- 4GB RAM minimum (8GB recommended)

### Quick Start

```bash
# Clone repository
git clone https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety.git
cd Filtrowanie-danych-z-ankiety

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Set up pre-commit hooks
pre-commit install

# Run tests
pytest

# Code quality checks
black .
flake8 .
mypy app.py
```

## Docker Deployment

### Single Container

```bash
# Build image
docker build -t survey-data-filter:latest .

# Run container
docker run -p 8501:8501 survey-data-filter:latest
```

### Docker Compose

```bash
# Basic deployment
docker-compose up -d

# With caching (Redis)
docker-compose --profile with-cache up -d

# With database (PostgreSQL)
docker-compose --profile with-database up -d

# Full stack
docker-compose --profile with-cache --profile with-database up -d
```

### Environment Variables

Create `.env` file from `.env.example`:

```bash
cp .env.example .env
# Edit .env with your configuration
```

## Cloud Deployment

### Streamlit Cloud

1. **Fork the repository** on GitHub
2. **Connect to Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Deploy from your forked repository
3. **Configure secrets** in Streamlit Cloud dashboard

### Heroku

```bash
# Install Heroku CLI
# Create Procfile
echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### AWS ECS

1. **Build and push Docker image**:
```bash
# Build for AWS
docker build -t survey-data-filter:aws .

# Tag for ECR
docker tag survey-data-filter:aws your-account.dkr.ecr.region.amazonaws.com/survey-data-filter:latest

# Push to ECR
docker push your-account.dkr.ecr.region.amazonaws.com/survey-data-filter:latest
```

2. **Create ECS task definition**
3. **Set up load balancer and security groups**
4. **Deploy service**

### Google Cloud Run

```bash
# Build and deploy
gcloud run deploy survey-data-filter \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Azure Container Instances

```bash
# Create resource group
az group create --name survey-rg --location eastus

# Deploy container
az container create \
  --resource-group survey-rg \
  --name survey-data-filter \
  --image your-registry/survey-data-filter:latest \
  --dns-name-label survey-filter \
  --ports 8501
```

## Production Considerations

### Security

1. **Environment Variables**:
   - Never commit secrets to version control
   - Use environment-specific configuration files
   - Implement proper secret management

2. **Network Security**:
   - Use HTTPS in production
   - Implement proper firewall rules
   - Consider VPN for internal tools

3. **Authentication**:
   - Implement user authentication if needed
   - Use OAuth providers for enterprise deployment
   - Set up role-based access control

### Performance

1. **Resource Allocation**:
   - CPU: 2+ cores recommended
   - Memory: 4GB minimum, 8GB for large datasets
   - Storage: SSD recommended for better I/O

2. **Caching**:
   - Enable Streamlit caching for data loading
   - Use Redis for session caching
   - Implement CDN for static assets

3. **Load Balancing**:
   - Use multiple instances for high availability
   - Implement health checks
   - Set up auto-scaling policies

### Data Management

1. **File Storage**:
   - Use cloud storage for large datasets
   - Implement file upload limits
   - Set up automated backups

2. **Database Integration**:
   - Consider PostgreSQL for persistent data
   - Implement connection pooling
   - Set up read replicas for scaling

## Monitoring and Logging

### Application Monitoring

```python
# Add to app.py for monitoring
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Monitor page loads
@st.cache_data
def log_page_load():
    logger.info(f"Page loaded at {datetime.now()}")
    return time.time()
```

### Health Checks

```python
# Health check endpoint
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "2.0.0"
    }
```

### Docker Health Checks

```dockerfile
# Already included in Dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1
```

## Troubleshooting

### Common Issues

1. **Port Already in Use**:
```bash
# Find process using port 8501
netstat -tulpn | grep 8501
# Kill process
kill -9 <PID>
```

2. **Memory Issues**:
```bash
# Check memory usage
docker stats
# Increase memory limit
docker run -m 4g survey-data-filter:latest
```

3. **Permission Errors**:
```bash
# Fix file permissions
chmod +x app.py
# Fix Docker permissions
sudo usermod -aG docker $USER
```

### Logs and Debugging

```bash
# Docker logs
docker logs survey-data-filter

# Follow logs
docker logs -f survey-data-filter

# Debug mode
streamlit run app.py --logger.level=debug
```

### Performance Issues

1. **Large Data Files**:
   - Implement data streaming
   - Use data sampling for preview
   - Optimize pandas operations

2. **Slow Charts**:
   - Limit data points in visualizations
   - Use aggregated data for large datasets
   - Implement progressive loading

### Support

- **Documentation**: Check [User Guide](docs/USER_GUIDE.md)
- **Issues**: [GitHub Issues](https://github.com/AlanSteinbarth/Filtrowanie-danych-z-ankiety/issues)
- **Contact**: alan.steinbarth@gmail.com

---

*Last updated: May 26, 2025*
*Version: 2.0.0*
