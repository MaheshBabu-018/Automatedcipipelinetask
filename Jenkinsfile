pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo "Cloning repo..."
                git branch: 'main', url: 'https://github.com/MaheshBabu-018/Automatedcipipelinetask.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies..."
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."
                sh 'pytest --junitxml=reports/results.xml --maxfail=1 -q'
            }
            post {
                always {
                    junit 'reports/results.xml'
                }
            }
        }

        stage('Build & Package') {
            steps {
                echo "Packaging application..."
                sh 'mkdir -p build'
                sh 'zip -r build/artifact.zip src requirements.txt'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'build/artifact.zip', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Build success!"
        }
        failure {
            echo "Build failed!"
        }
    }
}
