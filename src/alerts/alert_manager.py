"""
alert_manager.py
----------------
Manages alerts and notifications.
"""

import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum

from src.utils.logger import get_logger

logger = get_logger(__name__)


class AlertSeverity(str, Enum):
    """Alert severity levels."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class AlertType(str, Enum):
    """Alert types."""
    DELAY_ALERT = "delay_alert"
    STAFF_ALERT = "staff_alert"
    QUEUE_ALERT = "queue_alert"
    BAGGAGE_ALERT = "baggage_alert"
    REVENUE_ALERT = "revenue_alert"
    ANOMALY_ALERT = "anomaly_alert"


class AlertManager:
    """Manages alert generation and delivery."""
    
    def __init__(self):
        """Initialize alert manager."""
        self.active_alerts = {}
    
    def create_alert(self,
                    alert_type: AlertType,
                    severity: AlertSeverity,
                    message: str,
                    metadata: Dict = None) -> Dict:
        """Create a new alert.
        
        Args:
            alert_type: Type of alert
            severity: Alert severity
            message: Alert message
            metadata: Additional metadata
            
        Returns:
            Alert dictionary
        """
        alert = {
            'id': len(self.active_alerts),
            'type': alert_type.value,
            'severity': severity.value,
            'message': message,
            'metadata': metadata or {},
            'created_at': datetime.utcnow(),
            'is_resolved': False
        }
        
        self.active_alerts[alert['id']] = alert
        logger.info(f"Alert created: {alert_type.value} - {message}")
        
        return alert
    
    def check_delay_alert(self, delay_minutes: float, threshold: float = 45) -> Optional[Dict]:
        """Check if delay exceeds threshold."""
        if delay_minutes > threshold:
            return self.create_alert(
                AlertType.DELAY_ALERT,
                AlertSeverity.HIGH if delay_minutes > 60 else AlertSeverity.MEDIUM,
                f"Flight delay of {delay_minutes} minutes",
                {'delay_minutes': delay_minutes}
            )
        return None
    
    def check_staff_alert(self, utilization_rate: float, threshold: float = 1.05) -> Optional[Dict]:
        """Check if staff utilization is too high."""
        if utilization_rate > threshold:
            return self.create_alert(
                AlertType.STAFF_ALERT,
                AlertSeverity.CRITICAL if utilization_rate > 1.15 else AlertSeverity.HIGH,
                f"Staff utilization at {utilization_rate*100:.1f}%",
                {'utilization_rate': utilization_rate}
            )
        return None
    
    def resolve_alert(self, alert_id: int) -> bool:
        """Resolve an alert."""
        if alert_id in self.active_alerts:
            self.active_alerts[alert_id]['is_resolved'] = True
            logger.info(f"Alert {alert_id} resolved")
            return True
        return False
    
    def get_active_alerts(self, severity: AlertSeverity = None) -> List[Dict]:
        """Get all active alerts."""
        alerts = [a for a in self.active_alerts.values() if not a['is_resolved']]
        
        if severity:
            alerts = [a for a in alerts if a['severity'] == severity.value]
        
        return alerts
