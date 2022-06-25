pipeline{
    agent any
    stages{
        stage('Clone')
        {
            steps{
                git branch: 'dev', credentialsId: 'github_secret', url: 'https://github.com/Sanketkalode/books'
            }
        }

        // stage('Test'){
        //     steps{
        //         bat '''python -m virtualenv venv
        //         call venv/Scripts/activate.bat
        //         pip install -r web/requirements.txt
        //         python -m unittest discover -s web/test'''
        //     }
        // }

        stage('Docker Build'){
            steps{
                bat '''docker build -t sanketkalode/bookapi web
                docker tag sanketkalode/bookapi sanketkalode/bookapi:%BUILD_NUMBER%
                docker tag sanketkalode/bookapi sanketkalode/bookapi:latest'''
            }
        }
        stage('Docker Push'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'password', usernameVariable: 'username')]) {
                    bat '''docker login --username username --password password
                    docker push sanketkalode/bookapi:%BUILD_NUMBER%
                    docker push sanketkalode/bookapi:latest'''
                }
            }
        }
        stage('Clean Up'){
            steps{
                cleanWs()
            }
        }
    }
}
