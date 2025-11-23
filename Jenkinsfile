pipeline {
    agent any

    tools {
        allure 'allure'
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    pip install -r /var/jenkins_home/workspace/Jenkins-api/requirements.txt
                "
                '''
            }
        }

        stage('Run Tests With Allure') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    pytest /var/jenkins_home/workspace/Jenkins-api/test_api.py \
                        -v --alluredir=/var/jenkins_home/workspace/Jenkins-api/allure-results
                "
                '''
            }
        }

        // stage('Publish Allure Report') {
        //     steps {
        //         allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        //     }
        // }
    }
    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}