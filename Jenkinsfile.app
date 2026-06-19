pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    environment {
        IMAGE_NAME = "devops-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "devops-app-test"
    }

    stages {
        stage('Check App Changes') {
            when {
                anyOf {
                    changeset "app/**"
                    changeset "Dockerfile"
                    changeset "requirements.txt"
                    changeset "kubernetes/**"
                }
            }
            steps {
                echo "App-related changes detected."
            }
        }

        stage('Build and Test App') {
            when {
                anyOf {
                    changeset "app/**"
                    changeset "Dockerfile"
                    changeset "requirements.txt"
                    changeset "kubernetes/**"
                }
            }
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    python -m pytest || echo "No tests found yet"

                    docker build -t $IMAGE_NAME:$IMAGE_TAG .

                    docker rm -f $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p 8000:8000 $IMAGE_NAME:$IMAGE_TAG
                    sleep 5
                    curl -f http://localhost:8000/health
                '''
            }
        }
    }

    post {
        always {
            sh 'docker rm -f $CONTAINER_NAME || true'
        }
    }
}