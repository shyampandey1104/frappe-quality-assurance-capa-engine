# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "quality_capa"
app_title = "Frappe Quality Assurance Capa Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Quality Assurance Capa Engine for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/quality_capa/css/quality_capa.bundle.css"
app_include_js = "/assets/quality_capa/js/quality_capa.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "quality_capa.engine.on_document_submit",
        "on_cancel": "quality_capa.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "quality_capa.engine.daily_scheduled_sync"
    ]
}
