pipeline {
    agent any
    stages {
        stage('Clone or Pull repository') {
            steps {
                script {
                    sh '''
                    #!/bin/bash
                    cd /home/ubuntu
                    if [ -d ".git" ]; then
                        echo "Repository exists, pulling latest changes from main branch..."
                        git checkout main
                        git pull origin main
                    else
                        echo "Repository does not exist, cloning main branch..."
                        git config --global --add safe.directory /home/ubuntu
                        git config --global init.defaultBranch main
                        git init
                        git remote add origin https://github.com/veronica2550/Gemini-Single-Chat.git
                        git pull origin main
                    fi
                    '''
                }
            }
        }
        stage('Install dependencies') {
            steps {
                script {
                    sh '''
                    #!/bin/bash
                    cd /home/ubuntu
                    echo "현재 작업 디렉토리: $(pwd)"
                    
                    # 가상환경이 활성화되어 있는지 확인
                    if [[ "$VIRTUAL_ENV" != "" ]]; then
                        echo "가상환경이 이미 활성화되어 있습니다."
                    else
                        echo "가상환경을 활성화합니다."
                        source ./.venv/bin/activate
                    fi
                    
                    # 의존성 설치
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Restart Flask App') {
            steps {
                script {
                    sh '''
                    cd /home/ubuntu
                    # 기존 Flask 앱 종료
                    pkill -f "python3 app.py" || true  # 기존 프로세스가 없으면 오류 방지
                    # Flask 앱 다시 시작
                    nohup python3 app.py > output.log 2>&1 &
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo '>>>>>>>>>>>>>Pipeline failed.<<<<<<<<<<<<<'
        }
    }
}
