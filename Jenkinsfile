pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                script {
                    sh 'git clone https://github.com/ravivemula123799/Jenkines.git'
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project'
            }
        }
    }
}
