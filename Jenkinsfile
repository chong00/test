pipeline {
	agent any
	stages {
        stage ('Setup') {
        	steps {
		 	    sh 'python3 app.py'
	   		}
		}

		stage ('test') {
			steps {
                sh 'python3 test.py'
				
			}
		}

	}


}
