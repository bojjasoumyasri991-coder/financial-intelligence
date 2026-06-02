from celery import Celery
from celery.schedules import crontab

# ==========================================
# CREATE CELERY APP
# ==========================================

app = Celery(
    "financial_intelligence_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# ==========================================
# TIMEZONE
# ==========================================

app.conf.timezone = "Asia/Kolkata"

# ==========================================
# IMPORT FUNCTIONS
# ==========================================

from scripts.etl_pipeline import run_etl_pipeline
from scripts.health_score_generator import score_all_companies
from scripts.pros_cons_generator import generate_pros_cons
from scripts.anomaly_detection_job import detect_anomalies
from scripts.trend_analysis_job import detect_trends

# ==========================================
# TASKS
# ==========================================

@app.task
def etl_task():
    print("Running ETL Pipeline...")
    run_etl_pipeline()
    return "ETL Completed"


@app.task
def health_score_task():
    print("Calculating Health Scores...")
    score_all_companies()
    return "Health Scores Completed"


@app.task
def pros_cons_task():
    print("Generating Pros & Cons...")
    generate_pros_cons()
    return "Pros & Cons Completed"


@app.task
def anomaly_detection_task():
    print("Running Anomaly Detection...")
    detect_anomalies()
    return "Anomaly Detection Completed"


@app.task
def trend_analysis_task():
    print("Running Trend Analysis...")
    detect_trends()
    return "Trend Analysis Completed"

# ==========================================
# CELERY BEAT SCHEDULE
# ==========================================

app.conf.beat_schedule = {

    "run-etl-every-day": {
        "task": "tasks.etl_task",
        "schedule": crontab(hour=1, minute=0),
    },

    "generate-health-scores": {
        "task": "tasks.health_score_task",
        "schedule": crontab(hour=2, minute=0),
    },

    "generate-pros-cons": {
        "task": "tasks.pros_cons_task",
        "schedule": crontab(hour=3, minute=0),
    },

    "detect-anomalies": {
        "task": "tasks.anomaly_detection_task",
        "schedule": crontab(hour=4, minute=0),
    },

    "trend-analysis": {
        "task": "tasks.trend_analysis_task",
        "schedule": crontab(hour=5, minute=0),
    },
}

# ==========================================
# TEST REDIS CONNECTION
# ==========================================

if __name__ == "__main__":
    print("Celery Tasks Loaded Successfully")