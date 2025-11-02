pipeline {
    agent any // Specifies that the pipeline can run on any available agent

    stages {
        stage('Checkout / Build') {
            steps {
                //git clone
                sh '''git clone https://github.com/andiefendiii/jenkins-pipeline.git'''
            }
            steps {
                // cretae venv
                sh '''python -m venv env'''
            }
            steps {
                // activate venv
                sh '''env/Scripts/activate'''
            }
            steps {
                // install requirement
                sh '''pip install -r requirement.txt''' 
            }
        }
        stage('Test') {
            steps {
                //running script
                sh '''pytest test_user.py'''
            }
        }
        stage('Report') {
            steps {
                echo 'Misalnya ada reportnya disini'
                // command reportnya disini
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline successful!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}