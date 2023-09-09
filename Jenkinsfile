pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        script {
          properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
        }
        git 'https://github.com/VictorLins/DevOpsProject.git'
      }
    }
    stage('Start APIs ') {
      when {
        expression {
          currentBuild.resultIsBetterOrEqualTo('SUCCESS')
        }
      }
      steps {
        script {
          if (checkOs() == 'Windows') {
            def scriptOutput1 = bat(
              script: 'start /min C:\\Users\\victo\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe rest_app.py',
              returnStatus: true
            )

            def scriptOutput2 = bat(
              script: 'start /min C:\\Users\\victo\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe web_app.py',
              returnStatus: true
            )

            if (scriptOutput1 != 0 || scriptOutput2 != 0) {
              currentBuild.result = 'FAILURE'
            }
          }
        }
      }
    }

    stage('Backend Test ') {
      when {
        expression {
          currentBuild.resultIsBetterOrEqualTo('SUCCESS')
        }
      }
      steps {
        script {

          def scriptOutput = bat(
            script: 'C:\\Users\\victo\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe backend_testing.py',
            returnStatus: true
          )
          if (scriptOutput != 0) {
            currentBuild.result = 'FAILURE'
          }
        }
      }
    }

    stage('Frontend Test ') {
      when {
        expression {
          currentBuild.resultIsBetterOrEqualTo('SUCCESS')
        }
      }
      steps {
        script {
          def scriptOutput = bat(
            script: 'C:\\Users\\victo\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe frontend_testing.py',
            returnStatus: true
          )
          if (scriptOutput != 0) {
            currentBuild.result = 'FAILURE'
          }
        }
      }
    }

    stage('Combined Test ') {
      when {
        expression {
          currentBuild.resultIsBetterOrEqualTo('SUCCESS')
        }
      }
      steps {
        script {
          def scriptOutput = bat(
            script: 'C:\\Users\\victo\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe combined_testing.py',
            returnStatus: true
          )
          if (scriptOutput != 0) {
            currentBuild.result = 'FAILURE'
          }
        }
      }
    }

    stage('Clean Environment ') {
      steps {
        script {
          if (checkOs() == 'Windows') {
            bat 'C:\\Users\\victo\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe clean_environment.py'
          } else {
            print("Not Windows")
          }
        }
      }
    }
  }
}

def checkOs() {
  if (isUnix()) {
    def uname = sh script: 'uname', returnStdout: true
    if (uname.startsWith("Darwin")) {
      return "Macos"
    } else {
      return "Linux"
    }
  } else {
    return "Windows"
  }
}
