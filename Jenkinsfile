pipeline {
    agent any

    stages {

        stage('Deploy Flask App') {
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

        stage('Deploy Nginx Config') {
            steps {
                sh '''
                scp nginx/flask-app.conf khevi@app-lab:/tmp/flask-app.conf

                ssh khevi@app-lab "
                sudo mv /tmp/flask-app.conf /etc/nginx/sites-available/flask-app &&
                sudo ln -sf /etc/nginx/sites-available/flask-app /etc/nginx/sites-enabled/flask-app &&
                sudo rm -f /etc/nginx/sites-enabled/default &&
                sudo nginx -t &&
                sudo systemctl restart nginx
                "
                '''
            }
        }

    }
}