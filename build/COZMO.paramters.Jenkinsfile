#!groovy

pipeline {
    agent { node ('temp') }
        // wait condition
        // Input paramter pro stage
    parameters {
        string(name: 'drive_straight_1', defaultValue: '0', description: 'positive value in mm to drive forward')
        string(name: 'turn_around_1', defaultValue: '0', description: 'positive or negative value in degrees')
    }
    stages {
        stage('drive_straight_1') {
            steps {
                // Webhook
                script {hook = registerWebhook()}
                echo "Waiting for POST to ${hook.getURL()}"

                // COZMO call
                echo "Driving distance of ${params.drive_straight_1} mm"
                httpRequest responseHandle: 'NONE', httpMode: 'GET', url: "http://localhost:5000/drive?dist=${params.drive_straight_1}&webhook=${hook.getURL()}"
                // Wait for webhook
                script {data = waitForWebhook hook}
                echo "Webhook called with data: ${data}"
            }
        }
        stage('turn_around_1') {
            steps {
                // Webhook
                script {hook = registerWebhook()}
                echo "Waiting for POST to ${hook.getURL()}"

                // COZMO call
                echo "Turning around for ${params.turn_around_1} degrees"
                httpRequest responseHandle: 'NONE', httpMode: 'GET', url: "http://localhost:5000/turn?angle=${params.turn_around_1}&webhook=${hook.getURL()}"

                // Wait for webhook
                script {data = waitForWebhook hook}
                echo "Webhook called with data: ${data}"
            }
        }
    }
    post {
        always {
            echo "I'm finished"
            // Webhook
            //script {hook = registerWebhook()}
            //echo "Waiting for POST to ${hook.getURL()}"

            //httpRequest responseHandle: 'NONE', httpMode: 'GET', url: "http://localhost:5000/speak?text=Ichbinfertig&webhook=${hook.getURL()}"

             httpRequest ignoreSslErrors: true, responseHandle: 'NONE', httpMode: 'GET', url: "http://localhost:5000/shutdown"
            // Wait for webhook
            //script {data = waitForWebhook hook}
            //echo "Webhook called with data: ${data}"
        }
    }
}