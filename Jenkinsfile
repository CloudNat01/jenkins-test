pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                withAWS(credentials: 'sam-jenkins-demo-credentials', region: 'us-east-1') {
                sh 'python3 bucket.py'
              }
           }
        }
    }
}

