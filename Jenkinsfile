pipeline {
    agent any

    stages {
        stage('Setup Python Env') {
            steps {
                sh '''
                python3 -m venv env
                . env/bin/activate
                pip install -r requirement.txt
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                . env/bin/activate
                pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}