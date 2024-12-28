pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Ensure the correct Python path is set and Pip is available
                sh '''
                export PATH=/usr/local/bin:$PATH
                which python || echo "Python is not installed"
                which pip || echo "Pip is not installed"
                python3 -m ensurepip --upgrade || echo "Ensurepip failed"
                python3 -m pip install -r requirements.txt
                '''
            }
        }
        stage('SonarQube Analysis') {
            steps {
                echo 'Performing SonarQube analysis...'
                // Add SonarQube analysis steps here
            }
        }
    }

    post {
        always {
            echo 'This runs regardless of the result.'
        }
        failure {
            echo 'Pipeline failed'
        }
        success {
            echo 'Pipeline succeeded'
        }
    }
}
