pipeline {
    agent any

    environment {
        PYTHON_PATH = '/usr/local/bin/python'  // Path to Python on your macOS system
        SONAR_SCANNER_PATH = '/Users/ariv/Downloads/sonar-scanner-6.2.1.4610-macosx-x64/bin' // Path to SonarQube scanner
        PATH = "${PYTHON_PATH}:${SONAR_SCANNER_PATH}:${PATH}" // Add both to PATH globally
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Setting up the environment and installing dependencies...'
                sh '''
                if [ -f requirements.txt ]; then
                    pip3 install -r requirements.txt
                else
                    echo "requirements.txt not found. Skipping dependency installation."
                fi
                '''
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube') // Accessing the SonarQube token stored in Jenkins credentials
            }
            steps {
                echo 'Running SonarQube analysis...'
                sh '''
                if ! command -v sonar-scanner &> /dev/null
                then
                    echo "SonarQube scanner not found. Please install it."
                    exit 1
                fi

                # Run the SonarQube scanner with the token
                sonar-scanner \
                    -Dsonar.projectKey=std \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://localhost:9000 \
                    -Dsonar.token=$SONAR_TOKEN
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
        always {
            echo 'This runs regardless of the result.'
        }
    }
}
