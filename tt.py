stage('Build') {
    steps {
        sh '''
        # Update PATH to include the Python and Scripts directories where pip is located
        export PATH=/usr/local/bin/python:/usr/local/bin:/Users/ariv/Downloads/sonar-scanner-6.2.1.4610-macosx-x64/bin:$PATH

        # Check Python version
        python3 --version || (echo "Python not found. Exiting." && exit 1)

        # Check pip3 version
        pip3 --version || (echo "Pip not found. Exiting." && exit 1)

        # Example: Install a Python package
        pip3 install requests
        '''
    }
}
