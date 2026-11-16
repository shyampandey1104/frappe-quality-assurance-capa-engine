import unittest
from quality_capa.engine import FrappeQualityAssuranceEngine, InspectionParameter

class TestQualityAssurance(unittest.TestCase):
    def test_inspection_acceptance(self):
        engine = FrappeQualityAssuranceEngine()
        params = [
            InspectionParameter("Diameter (mm)", target_value=25.0, min_acceptable_value=24.8, max_acceptable_value=25.2, reading_value=25.05),
            InspectionParameter("Hardness (HRC)", target_value=45.0, min_acceptable_value=42.0, max_acceptable_value=48.0, reading_value=44.0)
        ]
        res = engine.evaluate_inspection("QC-001", "SHAFT-25MM", "BATCH-99", params)
        self.assertEqual(res.overall_status, "ACCEPTED")
        self.assertEqual(len(res.failed_parameters), 0)

    def test_inspection_rejection_triggers_failure(self):
        engine = FrappeQualityAssuranceEngine()
        params = [
            InspectionParameter("Purity (%)", target_value=99.5, min_acceptable_value=99.0, max_acceptable_value=100.0, reading_value=97.5) # Failed
        ]
        res = engine.evaluate_inspection("QC-002", "CHEM-SOLVENT", "BATCH-102", params)
        self.assertEqual(res.overall_status, "REJECTED")
        self.assertEqual(len(res.failed_parameters), 1)

if __name__ == "__main__":
    unittest.main()
