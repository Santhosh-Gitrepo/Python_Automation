import os
import subprocess
import report_generator

REPORT_DIR = "reports_temp"  # Temporary folder for pytest report in automation repo
REPORT_FILE = "report.html"
PYTEST_CMD = ["pytest", f"--html={os.path.join(REPORT_DIR, REPORT_FILE)}", "--self-contained-html"]


def run_pytest():
    os.makedirs(REPORT_DIR, exist_ok=True)
    print("Running pytest and generating report...")
    subprocess.run(PYTEST_CMD)
    print("Pytest completed.")


run_pytest()
report_generator.generate_report()
