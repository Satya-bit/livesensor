**APS Failure Detection in Truck Braking Systems**

->Problem Statement
Advanced Pneumatic Systems (APS) are crucial in truck braking systems, and their failure can lead to significant safety risks and operational downtime. Regular inspections of these systems are expensive and time-consuming for truck owners. The objective of this project was to develop a data-driven solution to reduce inspection costs by 20% while maintaining high recall to ensure safety and minimize false negatives.

->Objective
To build a full-stack data science solution capable of detecting APS failures accurately, leveraging machine learning models and deploying the solution for real-world use.

->Dataset Description
The dataset contained 170 sensor-related features and approximately 36,000 rows of data.
It exhibited significant class imbalance, with failure cases being relatively rare compared to non-failure cases.
The dataset included missing values and outliers that required extensive preprocessing for optimal model performance.

->Approach
1. Data Preprocessing
Outlier Removal: Analyzed and removed outliers that could skew model predictions.
Missing Value Handling: Experimented with multiple techniques (KNN imputer, constant imputer, median, mean) to impute missing values and selected the method that provided the best recall.
Data Balancing: Used SMOTETomek to address class imbalance and create a balanced dataset, improving model training for rare failure cases.

2. Model Development
Model Selection: Chose LightGBM for its efficiency and high performance on tabular data.
Hyperparameter Optimization: Leveraged Optuna to fine-tune model hyperparameters, achieving an optimal recall of 0.93 and accuracy of 98%.
Evaluation: Focused on maximizing recall to minimize false negatives, as detecting failures was critical for safety.

3. Full-Stack Pipeline Development
Built a complete end-to-end pipeline covering:
Data Ingestion: Automated loading of raw data form MongoDB.
Data Validation: Used ks_2samp to compare distributions and ensure data consistency.
Data Transformation: Scaled and transformed features for model compatibility.
Model Training and Evaluation: Trained the model and evaluated its performance using confusion matrix metrics.
Model Pusher: Automated the process of pushing the trained and validated model to the deployment environment, ensuring seamless integration with the production system.

4. Deployment
Database Management: Used MongoDB to store processed data and model metadata.
API Development: Implemented FastAPI for serving the model, allowing real-time predictions.
Cloud Deployment: Deployed the solution on AWS using:
GitHub Actions for CI/CD.
Amazon ECR for containerized applications.
Amazon S3 for storage of model artifacts.
Amazon EC2 for hosting the application.
Technologies Used
Data Preprocessing: Pandas, NumPy, Scikit-learn
Machine Learning: LightGBM, SMOTETomek, Optuna
API Development: FastAPI
Database: MongoDB
Deployment: AWS (GitHub Actions, ECR, S3, EC2)

->Results
Achieved a recall of 0.93 and accuracy of 96%, significantly reducing inspection costs by 40%.
Delivered a scalable, production-ready solution with seamless deployment and real-time inference capabilities.
This project highlights the integration of advanced machine learning techniques and full-stack development to solve real-world problems efficiently.
