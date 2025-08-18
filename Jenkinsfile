pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        PYTHON = ".\\venv\\Scripts\\python.exe"
        PIP = ".\\venv\\Scripts\\pip.exe"
    }

    options {
        skipStagesAfterUnstable()
        preserveStashes(buildCount: 5)
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat "${PYTHON} -m pip install --upgrade pip"
                bat "${PIP} install -r requisites.txt"
//                 bat 'appium'
//                 sleep time: 10, unit: 'SECONDS' // Wait for Appium to start
            }
        }

        stage('Run Tests') {
            steps {
                bat "${PYTHON} -m pytest -s --maxfail=2 --disable-warnings --alluredir=allure-results --html=reports/report.html --self-contained-html"
//                 bat "${PYTHON} testrunner.py"
            }
        }
    }

    post {
        always {
            echo '🔁 Pipeline completed.'

            // ✅ Archive both reports
            archiveArtifacts artifacts: 'reports/*.html, allure-results/**', allowEmptyArchive: true

            // ✅ Publish HTML Report
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'HTML_Report'
            ])

            // ✅ Publish Allure Report
            allure([
                includeProperties: false,
                jdk: '',
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-results']]
            ])

            // ✅ Send Email Notification
            emailext (
                subject: "Test Report: ${currentBuild.fullDisplayName}",
                body: """
                    <p><b>Build Status:</b> ${currentBuild.currentResult}</p>
                    <p><b>Project:</b> Python Automation</p>
                    <p><b>Allure Report:</b> <a href="${BUILD_URL}allure">View Allure</a></p>
                    <p><b>HTML Report:</b> <a href="${BUILD_URL}HTML_Report">View HTML</a></p>
                """,
                mimeType: 'text/html',
                to: 'san.sathish.com@gmail.com'
            )
        }

        success {
            echo '✅ Build succeeded!'
        }

        failure {
            echo '❌ Build failed!'
        }

        cleanup {
//             bat 'taskkill /F /IM node.exe' // Stop Appium
            bat 'rmdir /s /q venv'         // Clean venv
        }
    }
}
