"""
notification_rules.py
---------------------
Defines rules for when alerts should be triggered.
"""

from dataclasses import dataclass
from typing import Callable, Dict, Any
from enum import Enum

from src.utils.logger import get_logger

logger = get_logger(__name__)


class NotificationTrigger(str, Enum):
    """Notification trigger conditions."""
    THRESHOLD = "threshold"
    DEVIATION = "deviation"
    ANOMALY = "anomaly"
    CUSTOM = "custom"


@dataclass
class NotificationRule:
    """Defines a notification rule."""
    name: str
    trigger_type: NotificationTrigger
    metric: str
    condition: Callable[[Any], bool]
    severity: str
    message_template: str
    enabled: bool = True
    
    def check(self, value: Any) -> bool:
        """Check if rule condition is met."""
        try:
            return self.condition(value)
        except Exception as e:
            logger.error(f"Error checking rule {self.name}: {e}")
            return False
    
    def get_message(self, value: Any = None) -> str:
        """Get formatted message."""
        if value is not None:
            return self.message_template.format(value=value)
        return self.message_template


class NotificationRuleManager:
    """Manages notification rules."""
    
    def __init__(self):
        """Initialize rule manager."""
        self.rules: Dict[str, NotificationRule] = {}
        self._setup_default_rules()
    
    def _setup_default_rules(self):
        """Setup default notification rules."""
        # On-time performance alert
        self.add_rule(NotificationRule(
            name="low_on_time_performance",
            trigger_type=NotificationTrigger.THRESHOLD,
            metric="on_time_performance",
            condition=lambda x: x < 0.75,
            severity="high",
            message_template="On-time performance dropped to {value:.1%}"
        ))
        
        # High delays alert
        self.add_rule(NotificationRule(
            name="high_delays",
            trigger_type=NotificationTrigger.THRESHOLD,
            metric="avg_delay_minutes",
            condition=lambda x: x > 45,
            severity="high",
            message_template="Average delay increased to {value:.1f} minutes"
        ))
        
        # High staff utilization
        self.add_rule(NotificationRule(
            name="high_staff_utilization",
            trigger_type=NotificationTrigger.THRESHOLD,
            metric="resource_utilization_rate",
            condition=lambda x: x > 1.05,
            severity="critical",
            message_template="Staff utilization at {value:.1%}"
        ))
        
        # Queue time alert
        self.add_rule(NotificationRule(
            name="high_queue_time",
            trigger_type=NotificationTrigger.THRESHOLD,
            metric="avg_queue_minutes",
            condition=lambda x: x > 15,
            severity="medium",
            message_template="Queue wait time: {value:.1f} minutes"
        ))
        
        # Baggage mishandling
        self.add_rule(NotificationRule(
            name="high_baggage_mishandling",
            trigger_type=NotificationTrigger.THRESHOLD,
            metric="baggage_mishandling_rate",
            condition=lambda x: x > 0.005,
            severity="medium",
            message_template="Baggage mishandling rate: {value:.3%}"
        ))
    
    def add_rule(self, rule: NotificationRule):
        """Add a notification rule."""
        self.rules[rule.name] = rule
        logger.info(f"Rule added: {rule.name}")
    
    def remove_rule(self, rule_name: str) -> bool:
        """Remove a rule."""
        if rule_name in self.rules:
            del self.rules[rule_name]
            logger.info(f"Rule removed: {rule_name}")
            return True
        return False
    
    def check_rules(self, metrics: Dict[str, Any]) -> Dict[str, list]:
        """Check all rules against metrics."""
        triggered = {"critical": [], "high": [], "medium": [], "low": []}
        
        for rule in self.rules.values():
            if not rule.enabled:
                continue
            
            if rule.metric in metrics:
                value = metrics[rule.metric]
                if rule.check(value):
                    triggered[rule.severity].append({
                        'rule_name': rule.name,
                        'message': rule.get_message(value),
                        'metric': rule.metric,
                        'value': value
                    })
        
        return triggered
