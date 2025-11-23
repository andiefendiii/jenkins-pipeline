pipeline {
    agent any
    
    stages {

        stage('Run Tests') {
            steps {
                sh 'docker exec -w python-runner python -m pytest --maxfail=1 --disable-warnings -v'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}