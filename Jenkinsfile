pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from SCM
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Setup Python environment and install dependencies
                sh '''
                # Ensure Python and Pip are accessible
                export PATH=/usr/local/bin:$PATH
                echo "Checking Python installation..."
                which python || echo "Python is not installed"
                which pip || echo "Pip is not installed"

                # Ensure Pip is available
                python3 -m ensurepip --upgrade || echo "Ensurepip failed"

                # Install dependencies
                python3 -m pip install --upgrade pip
                python3 -m pip install -r requirements.txt
                '''
            }
        }
        stage('SonarQube Analysis') {
            steps {
                // Placeholder for SonarQube analysis steps
                echo 'Performing SonarQube analysis...'
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
