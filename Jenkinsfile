pipeline {
    agent any

    environment {
        TERM = 'xterm'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Clean Environment') {
            steps {
                sh 'docker compose down --remove-orphans || true'
            }
        }

        stage('1. Ingest Data') {
            steps {
                echo 'Starting weather-db ingestion...'
                sh 'docker compose up --build weather-db'
            }
        }

        stage('2. Transform & Test Data') {
            steps {
                echo 'Running dbt transformations and custom tests...'
                sh 'docker compose run --rm weather_dbt dbt run'
                sh 'docker compose run --rm weather_dbt dbt test'
            }
        }

        stage('3. Deploy Dashboard') {
            steps {
                echo 'Deploying Streamlit dashboard...'
                sh 'docker compose up -d --build dashboards'
            }
        }
    }

    post {
        always {
            sh 'docker container prune -f'
        }
        failure {
            sh 'docker compose down'
        }
    }
}
