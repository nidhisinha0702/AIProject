import os
from pathlib import Path
from time import sleep
from dotenv import load_dotenv
from groq import Groq
import re
from time import sleep

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

JD="""
Responsibilities

 Design and implement scalable backend services, ensuring high availability, low latency, and reliability across multi-cloud environments.
 Drive end-to-end ownership of components, from requirement gathering through development, testing, deployment, and post-production quality assurance.
 Collaborate across disciplines—engineering, PM, and customer teams—to deliver features that simplify data access and governance for global customers.
 Embed security, compliance, and observability into every stage of development to uphold operational excellence and governed self-service.
 Innovate with AI-first development practices, leveraging modern tech stacks (C#, Service Fabric, Spark, Kusto) to accelerate quality and velocity.

Embody our culture and values

Qualifications

Required/Minimum Qualifications 

 Bachelor's degree in computer science, or related technical discipline AND 2+years technical engineering experience with design, building robust & scalable solutions in languages including, but not limited to, C, C++, C#, Java, JavaScript, or Python OR equivalent experience. 
Experience with cloud service development. 
Technical problem solving and debugging skills. 

Job Requirements: Other & Additional 

Ability to meet Microsoft, customer and/or government security screening requirements are required for this role. These requirements include, but are not limited to the following specialized security screenings: Microsoft Cloud Background Check:

This position will be required to pass the Microsoft Cloud background check upon hire/transfer and every two years thereafter.

Preferred/Additional Qualifications

Ability to meet Microsoft, customer and/or government security screening requirements are required for this role. These requirements include, but are not limited to the following specialized security screenings: Microsoft Cloud Background Check:

This position will be required to pass the Microsoft Cloud background check upon hire/transfer and every two years thereafter.

"""
RESUME="""
Nidhi Kumari
Location: Bangaluru, KA |Phone: +91-9776511372 |Email: nsinha7295@gmail.com
GitHub: https://www.github.com/nidhisinha0702/ Portfolio: https://nidhisinha0702.github.io/Portfolio/ 
LinkedIn: https://www.linkedin.com/in/itsnidhikumari 
Summary
•	Software Engineer with over 5 years of experience building scalable applications in the banking and finance sector.
•	Demonstrated expertise in Software Development Lifecycle, Object Oriented Programming, System Design, Design Patterns, Software Engineering principles and Agile methodologies.
•	Proficient in implementing microservices architecture, RESTful APIs, distributed systems, Test-Driven Development, CI/CD pipelines using Jenkins, and skilled in database development.
•	Actively upskilling with a strong interest in emerging technologies and languages like React, Artificial Intelligence, etc.
Education
University of Cincinnati, OH, USA								                           Jan 2024-May 2025
Master of Science, Information Technology						                                           Major GPA: 4.0
Biju Patnaik University of Technology								           Jun 2013-May 2017	
Bachelor of Technology, Information Technology							           Major GPA: 3.67

Skills: Java, Multithreading, Spring Boot, Hibernate, Microservices, Kafka, MongoDB, MySQL, Oracle, REST APIs.
Tools and Platforms: AWS (ECS, S3, Lambda), Jenkins, Docker, Kubernetes, Git, Jira, Confluence, Perforce, JUnit, Mockito.
Relevant Coursework: Data Structures, Algorithms, Machine Learning, Python, React, JavaScript, Cloud (AWS, GCP).
Professional Experience
Nagarro, KA, India										             Oct 2025-Present
Associate Staff Engineer
•	Worked as a Java Backend Developer delivering scalable, enterprise-grade solutions for BFSI clients.
•	Designed and developed high-performance RESTful APIs using Java and Spring Boot, supporting critical business workflows and improving system scalability.
•	Built and enhanced microservices-based components, ensuring loose coupling, fault tolerance, and high availability.
•	Collaborated with global cross-functional teams in Agile environments to deliver high-quality features within sprint timelines.
Proximate Technologies, OH, USA									            Jul 2025- Aug 2025
Software Developer Intern - Training
•	Gained hand-on experience in java programming, spring boot, and hibernate for database connectivity.
•	Implemented small scale projects to strengthen knowledge of OOP, collections, and exception handling.
•	Learned to design and test RESTful web services using spring boot. Practiced writing Junit tests to improve code quality.
•	Collaborated in team activities, using git/GitHub for version control and code sharing.
Master of Science, University of Cincinnati, USA							            Jan 2024-May 2025
•	Pursued MS degree in Information Technology, coursework included -Machine Learning, React, React Native, projects, and research.
•	Completed core coursework, capstone project, and research.
•	Developed a fashion recommendation system using EfficientNet-B0 and TensorFlow, achieving 89.86% accuracy on a dataset of over 44,000 images. Applied image classification and data preprocessing techniques.
•	Created a jaywalker detection system using VGG16 and TensorFlow, trained on 691 images and achieved 49% accuracy. Implemented computer vision features using Python.
MS Admission Prep, USA 										           Feb 2023-Dec 2023
•	Dedicated time to exam preparation, application process, and securing university admission.
•	Prepared for entrance exams (GRE/TOEFL), researched universities, wrote SOPs, managed applications.
Accolite Digital, KA, India										           Jan 2023-Jan 2023
Senior Software Engineer
•	Developed and optimized Rest APIs.
•	Conducted technical interviews for potential hires.
Capco, KA, India										          	          Sep 2021-Dec 2022
Senior Software Engineer
•	Designed and developed high-performance PDF generation APIs leveraging RESTful services, JDBC, and proprietary tools, automating report creation for client accounts and generating 10,000+ PDFs/month with minimal latency.
•	Built and deployed 12+ RESTful CRUD APIs for new business features, empowering 5,000+ users to efficiently manage investment and market data across multiple systems.
•	Integrated proprietary market data APIs to implement Overruling/Underruling logic, improving portfolio accuracy and enabling a 30% increase in investment analysis precision.
•	Implemented unit and integration testing using JUnit and Mockito, achieving > 90% code coverage, reducing defects pre-production by 40% and strengthening the overall system reliability.
•	Collaborated with global cross-functional teams to deliver Agile sprint deliverables on time and supported production deployments ensuring business continuity and regulatory compliance.
•	Contributed to API documentation, code reviews, and design discussions, ensuring adherence to architectural standards and performance benchmarks.
Envestnet Yodlee, KA, India									            Sep 2019-Sep 2021
Software Engineer
•	Developed and optimized RESTful APIs using Java, Spring Boot, and Hibernate (JPA) to process large-scale financial data, boosting system throughput by 30%.
•	Enhanced multi-account transaction aggregation with AJAX and optimized SQL queries, improving data accuracy and processing time by 15%.
•	Refactored legacy code and resolved high-priority production bugs, reducing API latency by 25% and system issues by 35%.
•	Maintained strong data consistency using ACID-compliant SQL databases and contributed to ongoing feature enhancements in collaboration with cross-functional teams.
•	Partnered with product owners and QA engineers in Agile sprints to deliver new feature enhancements and critical bug fixes, reducing system issues by 35%.
•	Mentored junior developers, conducted knowledge-sharing sessions, and created architectural and onboarding documentation, achieving 100% onboarding success rate for new hires.
Associate Software Engineer									            Sep 2018-Sep 2019
•	Designed and implemented a unified login system using multithreading and the singleton design pattern, improving authentication time by 40% and reducing infrastructure cost through optimized thread utilization.
•	Integrated SMS-based multi-factor authentication (MFA) to strengthen application security, reducing unauthorized access by 30%.
•	Developed scalable, reusable screen-scraper crawlers and data ingestion APIs to support millions of financial users, significantly enhancing data availability and business intelligence.
•	Supported cross-functional collaboration across QA and DevOps teams to ensure seamless integration and deployment of backend services.

"""
def ask_llm(system_prompt, user_prompt):
    sys_msg={
        "role":"system",
        "content":system_prompt
    }
    user_msg={
        "role":"user",
        "content":user_prompt
    }
    messages=[sys_msg, user_msg]
    response=client.chat.completions.create(model=model, messages=messages)
    answer=response.choices[0].message.content
    return answer

def step1_res_extract():
    system_prompt="""
    you are a professional HR assistant. Extract the skills from the candidates resume provided. Only return the skills no other information. Do not invent any skills by yourself
    """

    user_prompt=f"""
    Extract the skills from this resume
    {RESUME}
    """
    return ask_llm(system_prompt, user_prompt)

def step2_JD_extract():
    system_prompt="""
    you are a professional HR assistant. Extract the skills from the Job description provided. Only return the skills no other information. Do not invent any skills by yourself
    """

    user_prompt=f"""
    Extract the skills from this JD
    {JD}
    """
    return ask_llm(system_prompt, user_prompt)

def step3_match(candidate,jd):
    system_prompt="""
    You are a professional HR assistant. compare the skills of candidate and the skills required in the JD and produce a final score between 1 and 100. Also produce a short verdict whether the candidate is a good fit for the role.
    """
    user_prompt=f"""
    Compare and match the skills
    JD:
    {jd}
    Candidate:
    {candidate}
    """
    return ask_llm(system_prompt, user_prompt)

candidate=step1_res_extract()
sleep(2)
jd=step2_JD_extract()
sleep(2)
score=step3_match(candidate,jd)
print(score)
