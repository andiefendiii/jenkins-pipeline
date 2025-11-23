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
                    pip install -r /var/jenkins_home/workspace/API_Test/requirements.txt
                "
                '''
            }
        }

        stage('Run Tests With Allure') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    pytest /var/jenkins_home/workspace/API_Test/test_api.py \
                        -v --alluredir=/var/jenkins_home/workspace/API_Test/allure-results
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