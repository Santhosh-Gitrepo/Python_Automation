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
                bat '.\\venv\\Scripts\\python.exe -m pytest -s --maxfail=2 --disable-warnings'
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
        }
    }
}
