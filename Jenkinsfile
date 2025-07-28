pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.\\venv\\Scripts\\python.exe -m pip install -r requisites.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\python.exe -m pytest -s --maxfail=2 --disable-warnings --alluredir=allure-results --html=reports\\report.html --self-contained-html'
            }
        }

        stage('Cleanup') {
            steps {
                bat 'rmdir /s /q venv'
            }
        }
    }

    post {
        success {
            echo '✅ Build succeeded!'
        }

        failure {
            echo '❌ Build failed!'
        }

        always {
            echo '🔁 Pipeline completed.'

            // HTML Report
            publishHTML(target: [
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Test Report',
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])

            // Allure Report
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }
}
