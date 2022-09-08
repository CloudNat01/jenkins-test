pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                withAWS(region:'us-east-1',credentials:'creds') 
                sh 'python3 bucket.py'
            }
        }
    }
}
