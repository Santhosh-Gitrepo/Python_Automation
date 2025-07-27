pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Santhosh-Gitrepo/Python_Automation.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\activate && pip install --upgrade pip'
                bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\activate && pytest --maxfail=2 --disable-warnings'
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
