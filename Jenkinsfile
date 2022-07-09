pipeline{
    agent any
    stages{
        stage('Clone')
        {
            steps{
                git branch: 'dev', url: 'https://github.com/Sanketkalode/books'
            }
        }

        stage('Docker Build'){
            steps{
                sh '''sudo docker build -t sanketkalode/bookapi web
                sudo docker tag sanketkalode/bookapi sanketkalode/bookapi:${BUILD_NUMBER}
                sudo docker tag sanketkalode/bookapi sanketkalode/bookapi:latest'''
            }
        }
        stage('Docker Push'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'password', usernameVariable: 'username')]) {
                    sh '''sudo docker login --username $username --password $password
                    sudo docker push sanketkalode/bookapi:${BUILD_NUMBER}
                    sudo docker push sanketkalode/bookapi:latest'''
                }
            }
        }
        stage('Deploy'){
            steps{
                sh'''
                    sudo ansible-playbook deploy.yml -u ubuntu
                '''
            }
        }
        stage('Clean Up'){
            steps{
                cleanWs()
            }
        }
    }
}
