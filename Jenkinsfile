pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/ravivemula123799/Jenkines.git'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 gopi.py'
            }
        }
    }
}
