pipeline {
    agent any

    environment {
        PYTHON_PATH = '/usr/local/bin/python:/Library/Frameworks/Python.framework/Versions/3.12/bin/python3'
        SONAR_SCANNER_PATH = '/Users/ariv/Downloads/sonar-scanner-6.2.1.4610-macosx-x64/bin'
        PATH = "${PYTHON_PATH}:${SONAR_SCANNER_PATH}:${PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

      steps {
    sh '''
    set PATH=%PYTHON_PATH%;%PATH%
    pip install -r requirements.txt
    '''
}


        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonar-token') // Accessing the SonarQube token stored in Jenkins credentials
            }
            steps {
                // Ensure that sonar-scanner is in the PATH
                sh '''
                export PATH=$SONAR_SCANNER_PATH:$PATH
                if ! command -v sonar-scanner &> /dev/null; then
                    echo "SonarQube scanner not found. Please install it."
                    exit 1
                fi
                export PATH=$PYTHON_PATH:$PATH
                sonar-scanner -Dsonar.projectKey=std \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://localhost:9000 \
                    -Dsonar.token=$SONAR_TOKEN
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            echo 'This runs regardless of the result.'
        }
    }
}
