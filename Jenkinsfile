pipeline {
    agent any

    stages {

        //  1. Checkout source code
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/JinsaJohnson/webapp-ci.git'
            }
        }

        //  2. Install dependencies in virtual environment
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        //  3. Run tests and generate JUnit XML report
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PYTHONPATH:$PWD
                mkdir -p reports
                pytest --junitxml=reports/results.xml --maxfail=1 -q
                '''
            }
        }

        //  4. Build zip artifact (excluding venv, git, cache)
        stage('Build Artifact') {
            steps {
                sh '''
                echo "Zipping project files into artifact.zip..."
                zip -r artifact.zip . -x "venv/*" "*.git*" "__pycache__/*"
                '''
            }
        }

        //  5. Archive artifact to Jenkins
        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'artifact.zip', allowEmptyArchive: false
            }
        }
    }

    //  6. Post actions for success/failure and test result publishing
    post {
        always {
            echo 'Build finished!'
            junit 'reports/results.xml'   // publishes test report automatically
        }

        success {
            echo ' Build Succeeded!'
        }

        failure {
            echo ' Build Failed!'
        }
    }
}
