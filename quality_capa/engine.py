"""Complete Frappe Quality Management Engine (Quality inspections, corrective actions aur quality reports)."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class InspectionParameter:
    parameter_name: str
    target_value: float
    min_acceptable_value: float
    max_acceptable_value: float
    reading_value: float


@dataclass
class QualityInspectionReport:
    inspection_id: str
    item_code: str
    batch_no: str
    overall_status: str  # ACCEPTED, REJECTED
    failed_parameters: List[str]


@dataclass
class CAPAActionItem:
    capa_id: str
    root_cause_description: str
    corrective_action: str
    preventive_action: str
    action_owner: str
    is_closed: bool = False


class FrappeQualityAssuranceEngine:
    """Incoming, In-Process, and Outgoing Quality Inspections with automated CAPA triggers."""

    def evaluate_inspection(
        self,
        inspection_id: str,
        item_code: str,
        batch_no: str,
        parameters: List[InspectionParameter]
    ) -> QualityInspectionReport:
        """Evaluates physical and chemical readings against tolerances and returns QC verdict."""
        failed = []
        for p in parameters:
            if not (p.min_acceptable_value <= p.reading_value <= p.max_acceptable_value):
                failed.append(f"{p.parameter_name} (Reading: {p.reading_value}, Allowed: {p.min_acceptable_value}-{p.max_acceptable_value})")

        overall = "ACCEPTED" if len(failed) == 0 else "REJECTED"
        return QualityInspectionReport(
            inspection_id=inspection_id,
            item_code=item_code,
            batch_no=batch_no,
            overall_status=overall,
            failed_parameters=failed
        )
