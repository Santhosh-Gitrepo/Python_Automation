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
            }
        }

        stage('Run Tests') {
            steps {
                bat "${PYTHON} -m pytest -s --maxfail=2 --disable-warnings --alluredir=allure-results --html=reports/report.html --self-contained-html"
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'HTML Report'
                ])
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }

        stage('Archive Test Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html, allure-results/**', allowEmptyArchive: true
            }
        }

        stage('Cleanup Virtual Env') {
            steps {
                bat 'rmdir /s /q venv'
            }
        }
    }

    post {
        always {
            echo '🔁 Pipeline completed.'
        }
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}
