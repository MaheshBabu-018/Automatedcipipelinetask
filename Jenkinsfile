pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Cloning repo...'
                // ✅ Specify the correct branch name
                git branch: 'main', url: 'https://github.com/MaheshBabu-018/Automatedcipipelinetask.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // ✅ Add .local/bin to PATH so pytest is found
                sh 'export PATH=$PATH:/var/lib/jenkins/.local/bin && pytest --junitxml=reports/results.xml --maxfail=1 -q'
            }
            stage('Run Tests') {
    steps {
        echo 'Running tests...'
        sh '''
            export PATH=$PATH:/var/lib/jenkins/.local/bin
            export PYTHONPATH=$PYTHONPATH:$(pwd)/src
            pytest --junitxml=reports/results.xml --maxfail=1 -q
        '''
    }
}
        }

        stage('Build & Package') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                echo 'Building package...'
                sh 'mkdir -p build && zip -r build/artifact.zip .'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'build/*.zip', followSymlinks: false
            }
        }
    }

    post {
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}
