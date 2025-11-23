// pipeline {
//     agent any

//     stages {
//         stage('Setup Python Env') {
//             steps {
//                 sh '''
//                 python3 -m venv env
//                 . env/bin/activate
//                 pip install -r requirement.txt
//                 '''
//             }
//         }

//         stage('Run API Tests') {
//             steps {
//                 sh '''
//                 . env/bin/activate
//                 pytest --maxfail=1 --disable-warnings -q
//                 '''
//             }
//         }
//     }

//     post {
//         always {
//             archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
//         }
//     }
// }

pipeline {
    agent any
    
    stages {
        stage('Copy Test Files') {
            steps {
                sh '''docker exec python-runner mkdir -p /app
                    docker cp . python-runner:/app/
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'docker exec python-runner pip install -r requirement.txt'
            }
        }

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