pipeline {
    agent any

    stages {
        stage('Deploy Flask MySQL App') {
            steps {
                sh '''
                ssh khevi@app-lab "
                cd ~/flask-mysql-devops-app &&
                git pull &&
                docker-compose down &&
                docker-compose up -d --build
                "
                '''
            }
        }
    }
}