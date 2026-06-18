pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/prasanna220103/Algerian-Forest-Fire-Prediction.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t forestfire .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop forestfire || true
                docker rm forestfire || true

                docker run -d \
                --name forestfire \
                -p 8081:5000 \
                forestfire
                '''
            }
        }
    }
}
