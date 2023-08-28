pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/VictorLins/DevOpsSandBox.git'
            }
        }
        stage('run python') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'C:\\Users\\victo\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe First.py'
                    } else {
                        bat 'C:\\Users\\victo\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe First.py'
                    }
                }
            }
        }
    }
}

def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}
