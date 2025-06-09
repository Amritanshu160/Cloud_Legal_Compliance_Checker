from flask import Flask, render_template, request

app = Flask(__name__)

checklist_items = {
    "Legal Considerations": [
        {"id": "ownership", "question": "Do you have legal ownership or rights to process the data?"},
        {"id": "consent", "question": "Have you obtained informed consent from data subjects?"},
        {"id": "compliance", "question": "Is the data handling compliant with relevant laws (e.g., GDPR, HIPAA)?"},
        {"id": "jurisdiction", "question": "Do you understand where the cloud provider stores data and applicable jurisdiction laws?"},
        {"id": "review_process", "question": "Has a legal or ethics board reviewed and approved the data use and upload plan?"}
    ],
    "Ethical Considerations": [
        {"id": "minimization", "question": "Have you minimized data collection to only what's necessary?"},
        {"id": "anonymization", "question": "Have you anonymized or pseudonymized sensitive data where possible?"},
        {"id": "transparency", "question": "Are users fully informed about how their data will be used, stored, and shared?"},
        {"id": "ethical_use", "question": "Will the data be used in ways that respect human rights and avoid bias or harm?"}
    ],
    "Security & Compliance": [
        {"id": "encryption", "question": "Is the data encrypted both in transit and at rest?"},
        {"id": "access_control", "question": "Do you have proper access control, role-based permissions, and logging in place?"},
        {"id": "third_party", "question": "Are all third-party vendors vetted and bound by data protection agreements?"},
        {"id": "data_retention", "question": "Is there a defined policy for data retention and secure disposal?"},
        {"id": "incident_response", "question": "Do you have an incident response plan in case of data breach or leakage?"}
    ]
}



@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    if request.method == "POST":
        results = {}
        for category, items in checklist_items.items():
            for item in items:
                response = request.form.get(item["id"])
                results[item["id"]] = response
        incomplete = {k: v for k, v in results.items() if v != "yes"}
        print(results)
        print(incomplete)
        return render_template("result.html", checklist=checklist_items, results=results, incomplete=incomplete)
    return render_template("index.html", checklist=checklist_items, results=results)

if __name__ == "__main__":
    app.run(debug=True)
