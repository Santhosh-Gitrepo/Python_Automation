import os
import subprocess
import time
from datetime import datetime
import shutil

WEBPAGE_REPO_URL = "https://github.com/Santhosh-Gitrepo/santhu.github.io.git"
WEBPAGE_LOCAL_PATH = "webpage-repo"
REPORT_DIR = "reports_temp"  # Temporary folder for pytest report in automation repo
REPORT_FILE = "report.html"
REPORTS_FOLDER = os.path.join(WEBPAGE_LOCAL_PATH, "reports")
DASHBOARD_FILE = os.path.join(WEBPAGE_LOCAL_PATH, "ReportDashboard.html")


def clone_or_update_webpage_repo():
    if not os.path.exists(WEBPAGE_LOCAL_PATH):
        subprocess.run(["git", "clone", WEBPAGE_REPO_URL, WEBPAGE_LOCAL_PATH])
    else:
        subprocess.run(["git", "-C", WEBPAGE_LOCAL_PATH, "pull"])


def save_report():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest_folder = os.path.join(REPORTS_FOLDER, timestamp)
    os.makedirs(dest_folder, exist_ok=True)
    shutil.copy(os.path.join(REPORT_DIR, REPORT_FILE), os.path.join(dest_folder, "report.html"))
    # print(f"Report saved in {dest_folder}")
    return timestamp, os.path.join(dest_folder, "report.html")


def make_report(report_path):
    """Enhance the pytest HTML report with comprehensive dark theme for dashboard display."""
    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Enhanced dark CSS with comprehensive styling
    enhanced_dark_css = """
    <style>
        /* Global dark theme */
        * {
            box-sizing: border-box;
        }

        html, body {
            background-color: #000000 !important;
            color: #ffffff !important;
            font-family: 'Segoe UI', 'Arial', sans-serif !important;
            margin: 0 !important;
            padding: 0 !important;
            min-height: 100vh !important;
        }

        body {
            background: linear-gradient(135deg, #000000 0%, #1a1a1a 100%) !important;
        }

        /* Header and title styling */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5) !important;
        }

        h1 {
            background: linear-gradient(45deg, #ffd700, #ff6b35) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            font-size: 2.5rem !important;
            text-align: center !important;
            margin-bottom: 30px !important;
        }

        /* Container and layout */
        .container, .content {
            background-color: rgba(20, 20, 20, 0.95) !important;
            border-radius: 15px !important;
            padding: 20px !important;
            margin: 20px !important;
            box-shadow: 0 8px 32px rgba(0,0,0,0.6) !important;
            backdrop-filter: blur(10px) !important;
        }

        /* Table styling */
        table {
            background-color: rgba(30, 30, 30, 0.9) !important;
            color: #ffffff !important;
            border-collapse: collapse !important;
            width: 100% !important;
            border-radius: 10px !important;
            overflow: hidden !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
        }

        th {
            background: linear-gradient(135deg, #333333, #444444) !important;
            color: #ffd700 !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            padding: 15px 10px !important;
            border: 1px solid #555555 !important;
        }

        td {
            background-color: rgba(40, 40, 40, 0.8) !important;
            color: #ffffff !important;
            padding: 12px 10px !important;
            border: 1px solid #555555 !important;
            transition: background-color 0.3s ease !important;
        }

        tr:hover td {
            background-color: rgba(60, 60, 60, 0.9) !important;
        }

        tr:nth-child(even) td {
            background-color: rgba(35, 35, 35, 0.8) !important;
        }

        /* Test result status colors */
        .passed, .passed td {
            color: #00ff00 !important;
            font-weight: bold !important;
            text-shadow: 0 0 10px rgba(0, 255, 0, 0.3) !important;
        }

        .failed, .failed td {
            color: #ff4444 !important;
            font-weight: bold !important;
            text-shadow: 0 0 10px rgba(255, 68, 68, 0.3) !important;
        }

        .skipped, .skipped td {
            color: #ffaa00 !important;
            font-weight: bold !important;
            text-shadow: 0 0 10px rgba(255, 170, 0, 0.3) !important;
        }

        .error, .error td {
            color: #ff6b6b !important;
            font-weight: bold !important;
            text-shadow: 0 0 10px rgba(255, 107, 107, 0.3) !important;
        }

        /* Summary section */
        .summary, .header, .section, .results-table {
            background: linear-gradient(135deg, rgba(30,30,30,0.95), rgba(50,50,50,0.95)) !important;
            color: #ffffff !important;
            border-radius: 12px !important;
            padding: 20px !important;
            margin-bottom: 20px !important;
            border: 1px solid #444444 !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4) !important;
        }

        .summary-bar {
            background: linear-gradient(90deg, #1a1a1a, #333333) !important;
            color: #ffffff !important;
            padding: 15px !important;
            border-radius: 8px !important;
            border: 2px solid #555555 !important;
            margin: 10px 0 !important;
        }

        /* Links and buttons */
        a {
            color: #ffd700 !important;
            text-decoration: none !important;
            transition: color 0.3s ease !important;
        }

        a:hover {
            color: #ff6b35 !important;
            text-shadow: 0 0 8px rgba(255, 107, 53, 0.5) !important;
        }

        .expand, .collapse, .toggle-button, button {
            background: linear-gradient(135deg, #333333, #555555) !important;
            color: #ffd700 !important;
            border: 1px solid #666666 !important;
            border-radius: 6px !important;
            padding: 8px 12px !important;
            cursor: pointer !important;
            font-weight: bold !important;
            transition: all 0.3s ease !important;
        }

        .expand:hover, .collapse:hover, .toggle-button:hover, button:hover {
            background: linear-gradient(135deg, #555555, #777777) !important;
            color: #ffffff !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;
        }

        /* Code blocks and pre elements */
        pre, code {
            background-color: #111111 !important;
            color: #00ff00 !important;
            padding: 15px !important;
            border-radius: 8px !important;
            border: 1px solid #333333 !important;
            overflow-x: auto !important;
            font-family: 'Consolas', 'Monaco', monospace !important;
            box-shadow: inset 0 2px 10px rgba(0,0,0,0.5) !important;
        }

        /* Filter and search elements */
        .filter, .search, input[type="text"], select {
            background-color: #222222 !important;
            color: #ffffff !important;
            border: 1px solid #555555 !important;
            border-radius: 5px !important;
            padding: 8px 12px !important;
        }

        input[type="text"]:focus, select:focus {
            border-color: #ffd700 !important;
            outline: none !important;
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.3) !important;
        }

        /* Progress bars */
        .progress-bar {
            background-color: #333333 !important;
            border-radius: 10px !important;
            overflow: hidden !important;
            height: 20px !important;
        }

        .progress-fill {
            background: linear-gradient(90deg, #00ff00, #ffaa00, #ff4444) !important;
            height: 100% !important;
            transition: width 0.3s ease !important;
        }

        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 12px !important;
            height: 12px !important;
        }

        ::-webkit-scrollbar-track {
            background-color: #1a1a1a !important;
            border-radius: 6px !important;
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #333333, #555555) !important;
            border-radius: 6px !important;
            border: 2px solid #1a1a1a !important;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #555555, #777777) !important;
        }

        /* Additional enhancements */
        .test-case {
            margin: 10px 0 !important;
            padding: 15px !important;
            background-color: rgba(40, 40, 40, 0.8) !important;
            border-radius: 8px !important;
            border-left: 4px solid #ffd700 !important;
        }

        .timestamp {
            color: #cccccc !important;
            font-style: italic !important;
            font-size: 0.9em !important;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .container, .content {
                margin: 10px !important;
                padding: 15px !important;
            }

            table {
                font-size: 0.9rem !important;
            }

            th, td {
                padding: 8px 5px !important;
            }
        }
    </style>
    </head>
    """

    # Replace the original </head> with our enhanced CSS
    content = content.replace("</head>", enhanced_dark_css)

    # Add a subtle animation to the body
    body_enhancement = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Add subtle fade-in animation
            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.5s ease-in';
            setTimeout(() => {
                document.body.style.opacity = '1';
            }, 100);

            // Add hover effects to test rows
            const rows = document.querySelectorAll('tr');
            rows.forEach(row => {
                row.addEventListener('mouseenter', function() {
                    this.style.transform = 'scale(1.01)';
                    this.style.transition = 'transform 0.2s ease';
                });
                row.addEventListener('mouseleave', function() {
                    this.style.transform = 'scale(1)';
                });
            });
        });
    </script>
    </body>
    """

    # Add the script before </body>
    content = content.replace("</body>", body_enhancement)

    # Write the enhanced content back to the file
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(content)



def update_dashboard():
    if not os.path.exists(REPORTS_FOLDER):
        os.makedirs(REPORTS_FOLDER)

    report_folders = sorted(os.listdir(REPORTS_FOLDER))

    links_html = ""
    for folder in reversed(report_folders):  # latest first
        report_file = f"reports/{folder}/report.html"
        links_html += f'''
        <div class="report-card">
            <div class="report-date">{folder}</div>
            <a href="{report_file}" target="_blank">View Report</a>
        </div>
        '''

    # Enhanced full dashboard HTML with better styling
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Report Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', 'Arial', sans-serif;
            background: url('rpbg.png') no-repeat center center fixed;
            background-size: cover;
            color: #fff;
            min-height: 100vh;
            position: relative;
        }}

        body::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(0,0,0,0.8) 0%, rgba(20,20,20,0.9) 100%);
            z-index: -1;
        }}

        header {{
            text-align: center;
            padding: 30px 20px;
            background: linear-gradient(135deg, rgba(0,0,0,0.9), rgba(30,30,30,0.9));
            backdrop-filter: blur(15px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.5);
            border-bottom-left-radius: 25px;
            border-bottom-right-radius: 25px;
            margin-bottom: 30px;
        }}

        header h1 {{
            font-size: 3rem;
            background: linear-gradient(45deg, #ffd700, #ff6b35, #ffd700);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 3s ease-in-out infinite;
            letter-spacing: 2px;
            text-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }}

        @keyframes gradientShift {{
            0%, 100% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
        }}

        .subtitle {{
            color: #cccccc;
            font-size: 1.2rem;
            margin-top: 10px;
            font-weight: 300;
        }}

        .report-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            padding: 30px 20px;
            max-width: 1400px;
            margin: 0 auto;
        }}

        .report-card {{
            background: linear-gradient(135deg, rgba(20,20,20,0.9), rgba(40,40,40,0.9));
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.4);
            transition: all 0.3s ease;
            text-align: center;
            color: #fff;
            position: relative;
            overflow: hidden;
        }}

        .report-card::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255,215,0,0.1), transparent);
            transform: rotate(45deg);
            transition: all 0.5s ease;
            opacity: 0;
        }}

        .report-card:hover::before {{
            opacity: 1;
            transform: rotate(45deg) translate(10px, 10px);
        }}

        .report-card:hover {{
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 15px 40px rgba(0,0,0,0.6);
            border-color: rgba(255,215,0,0.3);
        }}

        .report-date {{
            color: #ffd700;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 15px;
            padding: 10px;
            background: rgba(0,0,0,0.3);
            border-radius: 10px;
            border: 1px solid rgba(255,215,0,0.2);
        }}

        .report-card a {{
            text-decoration: none;
            color: #ffffff;
            font-weight: bold;
            font-size: 1.2rem;
            display: inline-block;
            margin-top: 15px;
            padding: 12px 25px;
            background: linear-gradient(135deg, #333333, #555555);
            border-radius: 25px;
            border: 2px solid #666666;
            transition: all 0.3s ease;
            position: relative;
            z-index: 2;
        }}

        .report-card a:hover {{
            color: #ffd700;
            background: linear-gradient(135deg, #555555, #777777);
            border-color: #ffd700;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255,215,0,0.3);
        }}

        .stats-section {{
            background: linear-gradient(135deg, rgba(30,30,30,0.9), rgba(50,50,50,0.9));
            backdrop-filter: blur(10px);
            padding: 25px;
            margin: 30px 20px;
            border-radius: 20px;
            text-align: center;
            max-width: 1400px;
            margin-left: auto;
            margin-right: auto;
            border: 1px solid rgba(255,255,255,0.1);
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}

        .stat-item {{
            background: rgba(20,20,20,0.8);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid rgba(255,215,0,0.2);
        }}

        .stat-number {{
            font-size: 2rem;
            font-weight: bold;
            color: #ffd700;
        }}

        .stat-label {{
            color: #cccccc;
            margin-top: 5px;
        }}

        footer {{
            text-align: center;
            padding: 30px 20px;
            font-size: 0.9rem;
            color: #888;
            background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(20,20,20,0.8));
            margin-top: 50px;
            border-top: 1px solid rgba(255,255,255,0.1);
        }}

        .footer-content {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        /* Responsive design */
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 2rem;
            }}

            .report-container {{
                grid-template-columns: 1fr;
                padding: 20px 15px;
            }}

            .report-card {{
                padding: 20px;
            }}

            .stats-section {{
                margin: 20px 15px;
                padding: 20px;
            }}
        }}

        /* Loading animation */
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        .report-card {{
            animation: fadeInUp 0.6s ease-out forwards;
        }}

        .report-card:nth-child(even) {{
            animation-delay: 0.1s;
        }}

        .report-card:nth-child(odd) {{
            animation-delay: 0.2s;
        }}
    </style>
    </head>
    <body>
    <header>
        <h1>Automation Test Reports</h1>
        <div class="subtitle">Quality Assurance Dashboard</div>
    </header>

    <div class="stats-section">
        <h2>Dashboard Statistics</h2>
        <div class="stats-grid">
            <div class="stat-item">
                <div class="stat-number">{len(report_folders)}</div>
                <div class="stat-label">Total Reports</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Monitoring</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">100%</div>
                <div class="stat-label">Automated</div>
            </div>
        </div>
    </div>

    <div class="report-container">
        {links_html}
    </div>

    <footer>
        <div class="footer-content">
            <p>&copy; 2025 Santhosh R | Test Automation Dashboard</p>
            <p>Last updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            // Add smooth scrolling
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
                anchor.addEventListener('click', function (e) {{
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({{
                        behavior: 'smooth'
                    }});
                }});
            }});

            // Add loading effect
            const cards = document.querySelectorAll('.report-card');
            cards.forEach((card, index) => {{
                card.style.opacity = '0';
                card.style.transform = 'translateY(30px)';
                setTimeout(() => {{
                    card.style.transition = 'all 0.6s ease';
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }}, index * 100);
            }});
        }});
    </script>
    </body>
    </html>
    """

    with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)


def commit_and_push():
    subprocess.run(["git", "-C", WEBPAGE_LOCAL_PATH, "add", "."], stdout=subprocess.DEVNULL)
    subprocess.run(["git", "-C", WEBPAGE_LOCAL_PATH, "commit", "-m", "Add new test report"], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    subprocess.run(["git", "-C", WEBPAGE_LOCAL_PATH, "push"])


def generate_report():
    print("="*20+"Generating Test Reports!"+"="*20)
    clone_or_update_webpage_repo()
    timestamp, report_path = save_report()
    make_report(report_path)
    update_dashboard()
    commit_and_push()
    print("="*15+"Published Test Reports!"+"="*15)
    dashboard_url = "https://santhupage.netlify.app/reportdashboard"
    print(f"Check the reports in Dashboard after a minute: {dashboard_url}")
