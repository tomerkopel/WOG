pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/tomerkopel/WOG.git']]])
            }
        }
        stage('Build') {
            steps{
                sh 'docker build -t wog .'
            }
        }
        stage('Run') {
            steps{
                sh 'docker run --name wog -dp 8777:4000 wog'
            }
        }
        stage('Test') {
            steps{
                withPythonEnv('python3') {
                    sh 'pip install selenium'
                    sh 'python3 Tests/e2e.py'
                }
            }
        }
        stage('Finalize') {
            steps{
                    sh 'docker stop wog'
                    sh 'docker rm wog'
            }
        }
    }
}