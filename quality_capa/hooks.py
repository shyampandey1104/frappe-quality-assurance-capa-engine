# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "quality_capa"
app_title = "Frappe Quality Assurance Capa Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Quality Assurance Capa Engine - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/quality_capa/css/quality_capa.bundle.css"
app_include_js = "/assets/quality_capa/js/quality_capa.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Quality Assurance Capa Engine Entry": {
        "validate": "quality_capa.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "quality_capa.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "quality_capa.tasks.hourly_sync"
    ],
    "daily": [
        "quality_capa.tasks.daily_reconciliation"
    ],
    "weekly": [
        "quality_capa.tasks.weekly_digest"
    ]
}
