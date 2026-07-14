# ✈️ Airport Operations AI

> Advanced AI-powered platform for real-time airport operations monitoring, predictive analytics, and intelligent resource optimization.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active%20Development-brightgreen)](#)

## 🚀 Features

✅ **Real-time Monitoring Dashboard** - Streamlit + Plotly interactive dashboards  
✅ **Advanced ML Models** - LSTM, Prophet, Ensemble methods for accurate forecasting  
✅ **Anomaly Detection** - Multiple algorithms (Isolation Forest, LOF, DBSCAN)  
✅ **Resource Optimization** - AI-powered staff & gate allocation  
✅ **RESTful API** - FastAPI endpoints for seamless integration  
✅ **Database Integration** - PostgreSQL + MongoDB support  
✅ **Automated Alerts** - Email notifications for critical events  
✅ **Model Explainability** - SHAP & LIME for interpretable predictions  
✅ **Docker Deployment** - Multi-container orchestration with docker-compose  
✅ **Real-time Processing** - Redis caching & async task queue  

## 📄 Project Structure

```
airport-operations-ai/
├── src/
│   ├── data/
│   │   ├── data_preprocessing.py
│   │   ├── data_loader.py
│   │   └── data_validator.py
│   ├── models/
│   │   ├── advanced_models.py       # LSTM, Prophet, Ensemble
│   │   ├── anomaly_detection.py     # Multiple algorithms
│   │   ├── optimization.py          # Resource allocation
│   │   └── explainability.py        # SHAP, LIME
│   ├── database/
│   │   ├── db_config.py
│   │   ├── models.py
│   │   └── migrations/
│   ├── api/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── forecasts.py
│   │   │   ├── anomalies.py
│   │   │   ├── optimization.py
│   │   │   └── health.py
│   │   └── schemas.py
│   ├── dashboard/
│   │   ├── app.py
│   │   ├── pages/
│   │   │   ├── 01_Overview.py
│   │   │   ├── 02_Forecasting.py
│   │   │   ├── 03_Anomalies.py
│   │   │   ├── 04_Optimization.py
│   │   │   ├── 05_Explainability.py
│   │   │   └── 06_Reports.py
│   │   └── utils/
│   ├── alerts/
│   │   ├── alert_manager.py
│   │   ├── email_service.py
│   │   └── notification_rules.py
│   ├── utils/
│   │   ├── logger.py
│   │   ├── config.py
│   │   ├── cache.py
│   │   └── helpers.py
│   └── main.py
├── tests/
│   ├── test_models.py
│   ├── test_api.py
│   └── test_anomaly_detection.py
├── docker/
│   ├── Dockerfile
│   ├── Dockerfile.api
│   ├── Dockerfile.dashboard
│   └── docker-compose.yml
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Model_Comparison.ipynb
│   └── 03_Advanced_Analysis.ipynb
├── scripts/
│   ├── init_db.py
│   ├── seed_data.py
│   └── model_training.py
├── config/
│   └── logging_config.yaml
├── .github/
│   └── workflows/
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/kavya07082-stack/airport-operations-ai.git
cd airport-operations-ai

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Start all services
docker-compose up -d

# Access services:
# Dashboard: http://localhost:8501
# API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Local Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python scripts/init_db.py

# Run dashboard
streamlit run src/dashboard/app.py

# In another terminal, run API
uvicorn src.api.main:app --reload --port 8000
```

## 📚 API Documentation

### Health Check
```bash
GET /api/health
```

### Forecasts
```bash
POST /api/forecasts
GET /api/forecasts/{days}
```

### Anomaly Detection
```bash
POST /api/anomalies
GET /api/anomalies/{days}
```

### Resource Optimization
```bash
POST /api/optimize/staff
POST /api/optimize/gates
```

## 📊 Dashboard Pages

1. **Overview** - Real-time KPIs and operational status
2. **Forecasting** - Interactive forecast visualization & model comparison
3. **Anomalies** - Detected issues and anomaly analysis
4. **Optimization** - Resource allocation recommendations
5. **Explainability** - Model feature importance and SHAP values
6. **Reports** - Automated report generation and export

## 📚 Database Schema

### PostgreSQL (Transactional Data)
- `flights` - Flight operations data
- `passengers` - Passenger information
- `staff_schedules` - Staff allocation
- `forecasts` - Stored predictions
- `alerts` - Alert history
- `model_metadata` - Model versions and metrics

### MongoDB (Time-series & Logs)
- `operational_logs` - Real-time operational events
- `anomaly_events` - Detected anomalies
- `user_interactions` - Dashboard user activity
- `model_predictions_archive` - Historical predictions

## ⚙️ Configuration

Edit `.env` file to configure:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/airport_ops
MONGO_URL=mongodb://localhost:27017/airport_ops
REDIS_URL=redis://localhost:6379/0

# API
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=False

# ML Configuration
ANOMALY_THRESHOLD=0.7
FORECAST_HORIZON=30

# Email Alerts
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

## 📊 Model Performance

| Model | MAPE | MAE | RMSE |
|-------|------|-----|------|
| Ensemble | 7.23% | 1,756.88 | 2,341.20 |
| LSTM | 7.65% | 1,890.33 | 2,456.78 |
| Random Forest | 8.44% | 2,096.42 | 2,675.01 |
| Prophet | 8.95% | 2,450.20 | 3,100.45 |
| XGBoost | 9.21% | 2,276.54 | 2,915.14 |
| SARIMA | 10.31% | 3,032.12 | 3,775.19 |

## 🚨 Alert Triggers

- On-time performance < 75%
- Delay duration > 45 minutes
- Staff utilization > 1.1x
- Baggage mishandling > 0.5%
- Queue wait time > 15 minutes

## 🖛️ Technologies Used

- **Frontend**: Streamlit, Plotly, Bootstrap
- **Backend**: FastAPI, Python
- **ML/AI**: TensorFlow, scikit-learn, XGBoost, Prophet, SHAP, LIME
- **Databases**: PostgreSQL, MongoDB
- **Caching**: Redis
- **Task Queue**: Celery, APScheduler
- **Containerization**: Docker, Docker Compose
- **Monitoring**: Logging, Sentry (optional)

## 👤 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋 Support & Contact

- **GitHub Issues**: [Report bugs or request features](https://github.com/kavya07082-stack/airport-operations-ai/issues)
- **Documentation**: [Wiki](https://github.com/kavya07082-stack/airport-operations-ai/wiki)
- **Author**: [@kavya07082-stack](https://github.com/kavya07082-stack)

## 📆 Changelog

### v2.0.0 (Latest)
- Complete rewrite with advanced ML models
- Multi-page Streamlit dashboard
- RESTful API with FastAPI
- Comprehensive alert system
- Docker containerization
- SHAP & LIME explainability

---

**Last Updated**: 2024-01-15  
**Status**: 🔵 Active Development
