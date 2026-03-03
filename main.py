from processing.preprocess import preprocess
from models.marketing_prediction import train_model
from models.anomaly_detection import detect_anomalies
from alerting.alert_engine import generate_alerts

print("🚀 Starting Bank Marketing AIOps Pipeline")

preprocess()
train_model()
detect_anomalies()
generate_alerts()

print("✅ Pipeline Completed Successfully")