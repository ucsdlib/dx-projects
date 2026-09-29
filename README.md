# DX-Projects
## About Repo
    This repo is designed to increase transparency around and opportunity collaborate on development portions of our projects or code bases TDX-DX is responsible for maintaining and experimenting in. No single app or site is hosted/maintained by this repo. Rather, the repo helps members of the DX team experiment on ideas for our web properties, streamline the local hosting of apps/pages, document how to contribute to dx development, and host relevant resources and skills for TritonAI powered projects.
### Table of Contents
* #### [idea-garden-explorations](./idea-garden-exploration/)
    - __Description__: contains codebases for [idea garden](https://ucsdlibrary.atlassian.net/wiki/spaces/TDX/pages/3243540494/Idea+Garden) projects of concepts. 
* #### [skills-and-tools](./skills-and-tools/)
    - __Description__: contains directories tools and skills designed/developed for human-centered, principled use (and non-use) of TritonAI.
* #### [web-properties](./web-properties/)
    - __Description__: contains component mark-up, api explorations documentation, test environments for local, static testing of webpages, and documentation for developing in the respective platform.

## Working with Us (The Basics) 
### **1\. Set Up the Repository**

**Clone the Repository**  
Run the following command in your terminal to clone the repository to your local machine:  
bash  
Copy code  
`git clone <repo-url>`  
Example:  
bash  
Copy code  
`git clone https://github.com/organization/repository-name.git`

**Move Into the Repository Folder**  
bash  
Copy code  
`cd repository-name`

**Set Up Your Feature Branch**  
You need to check out the feature branch that I created for you. Run:  
bash  
Copy code  
`git checkout -b <your-feature-branch> origin/<your-feature-branch>`

1. Replace `<your-feature-branch>` with the branch name I provided (e.g., `sdt-member-feature-branch`).

---

### **2\. Before Starting Work**

Always pull the latest changes from the **remote `main` branch** directly into your **feature branch**:

**Ensure You’re on Your Feature Branch**:  
bash  
Copy code  
`git checkout <your-feature-branch>`

**Pull Remote `main` into Your Feature Branch**: Merge the latest changes from the `main` branch into your feature branch:  
bash  
Copy code  
`git pull origin main`

This ensures you are always working with the most up-to-date code.

---

### **3\. Working on Your Changes**

**Make Changes to the Code**: Edit files as needed for your task.

**Stage Changes**: Add the files you modified:  
bash  
Copy code  
`git add .`  
Or stage specific files:  
bash  
Copy code  
`git add <file-name>`

**Commit Your Changes**: Write a descriptive commit message:  
bash  
Copy code  
`git commit -m "Add description of your changes"`

**Push Changes to Your Remote Feature Branch**: Push your changes to the remote branch:  
bash  
Copy code  
`git push origin <your-feature-branch>`

---

### **4\. Email Notification**

Once you push your changes, send @Lopez-CL an email letting  know that your branch is ready for review.

Include the following:

* Branch name (e.g., `sdt-member-feature-branch`)  
* Brief description of the changes.

---