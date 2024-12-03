****APS Failure Detection in Truck Braking Systems****

![image](https://github.com/user-attachments/assets/9d19872f-8f93-4ed8-97bc-6949f1b2a096)

**->Problem Statement**

Advanced Pneumatic Systems (APS) are crucial in truck braking systems, and their failure can lead to significant safety risks and operational downtime. Regular inspections of these systems are expensive and time-consuming for truck owners. The objective of this project was to develop a data-driven solution to reduce inspection costs by 20% while maintaining high recall to ensure safety and minimize false negatives.

**->Objective**
To build a full-stack data science solution capable of detecting APS failures accurately, leveraging machine learning models and deploying the solution for real-world use.

**->Dataset Description**
The dataset contained 175 sensor-related features and approximately 36,100 rows of data.
It exhibited significant class imbalance, with failure cases being relatively rare compared to non-failure cases.
The dataset included missing values and outliers that required extensive preprocessing for optimal model performance.

**->Approach**
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

![image](https://github.com/user-attachments/assets/07282edd-4a3d-463d-9e04-e6c6205cb722)

API Development: Implemented FastAPI for serving the model, allowing real-time predictions.

![image](https://github.com/user-attachments/assets/b4484d33-e8f6-4f05-85ea-cbd9551d8272)

Cloud Deployment: Deployed the solution on AWS using:

GitHub Actions for CI/CD.

![image](https://github.com/user-attachments/assets/b1c64dbe-1b46-4156-8551-284377d276ed)

Amazon ECR for containerized applications.

![image](https://github.com/user-attachments/assets/568fc0dd-bfcf-4511-b012-ed077e74f835)

Amazon S3 for storage of model artifacts.

![image](https://github.com/user-attachments/assets/2c6f2f91-a9d0-4015-8042-2f46cbeb6c0e)

Amazon EC2 for hosting the application.

![image](https://github.com/user-attachments/assets/e36bdb41-7d48-4997-8a31-c9b082ced8ce)

Technologies Used

Data Preprocessing: Pandas, NumPy, Scikit-learn

![image](https://github.com/user-attachments/assets/1ddb0704-38fa-434b-ad55-6a882eaa3d1a)
![image](https://github.com/user-attachments/assets/064fe0a1-019d-445a-95da-5afcc54be682)
![image](https://github.com/user-attachments/assets/1a3da765-c503-4d65-a7db-7ff967916396)


Machine Learning: LightGBM, SMOTETomek, Optuna

![image](https://github.com/user-attachments/assets/0c2a5dd5-e05f-493e-b9ea-1ec0c14d4910)

API Development: FastAPI

Database: MongoDB

Deployment: AWS (GitHub Actions, ECR, S3, EC2)

**->Results**
Achieved a recall of 0.93 and accuracy of 96%, significantly reducing inspection costs by 40%.

Delivered a scalable, production-ready solution with seamless deployment and real-time inference capabilities.
This project highlights the integration of advanced machine learning techniques and full-stack development to solve real-world problems efficiently.
