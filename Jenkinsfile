// ⚠️ LEGAL DISCLAIMER:
// This Jenkins pipeline is for **local testing and educational purposes only**.
// It must NOT be used for automated, scheduled, or large-scale downloading of content from Instagram.
// The tool only supports public URLs and is designed for individual personal archiving.
// Instagram™ and Meta Platforms, Inc. are not affiliated with this tool.
// You are responsible for complying with Instagram’s Terms of Use: https://help.instagram.com/581066165581870

pipeline {
    agent any

    parameters {
        string(name: 'URL', defaultValue: '', description: 'Enter a public Instagram Reel/Post URL to download manually.')
    }

    stages {
        stage('🧪 Setup Python environment') {
            steps {
                sh '''
                    echo "🔧 Creating virtual environment..."
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('🚀 Download video (manual trigger only)') {
            steps {
                sh '''
                    echo "🎯 Downloading from URL: $URL"
                    . venv/bin/activate
                    python3 main.py "$URL"
                '''
            }
        }

        stage('📂 Move to SMB folder') {
            steps {
                sh '''
                    echo "📦 Moving .mp4 files to /var/smb/"
                    find ./downloads -name "*.mp4" -exec mv {} /var/smb/ \\; || echo "⚠️ No .mp4 files found."

                    echo "📦 Moving .txt files to /var/smb/"
                    find ./downloads -name "*.txt" -exec mv {} /var/smb/ \\; || echo "⚠️ No .txt files found."
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully. Files moved to /var/smb/.'
        }
        failure {
            echo '❌ Pipeline failed. Check the logs and verify the URL.'
        }
        always {
            echo 'ℹ️ Pipeline finished.'
        }
    }
}