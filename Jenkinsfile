pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                withAWS(credentials: 'aws-creds', region: 'us-east-2') {
                sh 'python3 bucket.py'
              }
           }
        }
    }
}

