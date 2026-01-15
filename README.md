**Software Requirements Specification (SRS)  
Dinman: Hall Management System**  

---

**Document Information**  

| **Item** | **Detail** |
|----------|------------|
| Project Name | Hall Dining Management System |
| Version | 1.0 |
| Date | January 15, 2026 |
| Status | Final |
| Prepared By | Development Team |
| Organization | Hall Management Committee |

---

**Table of Contents**  

1. **Preface**  
   1.1 Purpose  
   1.2 Scope  
   1.3 Intended Audience  
   1.4 Document Conventions  
   1.5 References  

2. **Introduction**  
   2.1 System Overview  
   2.2 System Context  
   2.3 Product Functions  
   2.4 User Characteristics  
   2.5 Operating Environment  
   2.6 Design and Implementation Constraints  
   2.7 Assumptions and Dependencies  

3. **Glossary**  

4. **User Requirements Definition**  
   4.1 Functional Requirements  
   4.2 Non-Functional Requirements  

5. **System Architecture**  
   5.1 Architectural Design  
   5.2 Data Architecture  
   5.3 Technology Stack  
   5.4 Security Architecture  
   5.5 API Architecture  
   5.6 Deployment Architecture  

6. **System Requirements Specification**  
   6.1 Functional Requirements (Detailed)  
   6.2 Interface Requirements  
   6.3 System Features  

7. **System Models**  
   7.1 Use Case Diagrams  
   7.2 Sequence Diagrams  
   7.3 State Diagrams  
   7.4 Activity Diagrams  
   7.5 Data Flow Diagrams  
   7.6 Class Diagrams  

8. **System Evolution**  
   8.1 Anticipated Changes  
   8.2 Scalability Considerations  
   8.3 Maintenance Strategy  
   8.4 Technology Upgrade Path  

9. **Appendices**  
   9.1 Appendix A: Database Schema  
   9.2 Appendix B: API Documentation  
   9.3 Appendix C: Installation Guide  
   9.4 Appendix D: Configuration Guide  
   9.5 Appendix E: User Manual  
   9.6 Appendix F: Troubleshooting Guide  
   9.7 Appendix G: Security Guidelines  
   9.8 Appendix H: Glossary of Terms  

10. **Index**  

---

## 1. Preface

### 1.1 Purpose
This Software Requirements Specification (SRS) document serves as a comprehensive and detailed description of the Hall Dining Management System. It articulates the functional and non‑functional requirements, defines the system architecture and design constraints, and provides all necessary specifications to guide the development, implementation, and maintenance of the system.

### 1.2 Scope
The Hall Dining Management System is a web‑based application designed to automate and streamline the complete dining‑service operations within a residential hall. The system encompasses meal tracking, financial transactions, user‑profile management, notice dissemination, complaint handling, and feast management, serving both the residents and the dining‑hall managers.

### 1.3 Intended Audience
This document is intended for the following stakeholders:  
- Software developers and engineers who will implement the system.  
- System architects responsible for the overall design.  
- Project managers overseeing the development lifecycle.  
- Quality assurance teams conducting testing and validation.  
- Hall administrators and dining managers who will operate the system.  
- System maintenance personnel responsible for ongoing support.  
- Other stakeholders and decision‑makers involved in the project.

### 1.4 Document Conventions
To enhance readability and clarity, the following typographical conventions are used throughout this document:  
- **Bold text** indicates important terms and section headings.  
- *Italic text* denotes system‑specific terminology when first introduced.  
- `Code font` is used for technical terms, file names, database tables, and code references.  
- Identifiers such as **FR‑XXX** refer to Functional Requirements.  
- Identifiers such as **NFR‑XXX** refer to Non‑Functional Requirements.

### 1.5 References
The development of this system and document adheres to the following standards and guidelines:  
1. Django Documentation (Version 5.0+)  
2. Django REST Framework Documentation  
3. IEEE Standard 830‑1998 for Software Requirements Specifications  
4. Python PEP 8 Style Guide  
5. Web Content Accessibility Guidelines (WCAG) 2.1  

---

## 2. Introduction

### 2.1 System Overview
The Hall Dining Management System is a robust, web‑based application built upon the Django framework. Its primary purpose is to facilitate the end‑to‑end management of dining services in a residential hall. The system provides two distinct, role‑based interfaces—one for residents and another for dining managers—enabling efficient meal tracking, precise financial management, and effective communication between all parties.

### 2.2 System Context
The system is designed to operate within the specific environment of a residential hall, characterized by the following conditions:  
- Residents require reliable daily meal services.  
- All financial transactions, including recharges and meal deductions, must be recorded accurately.  
- Meal consumption must be monitored on a per‑user, per‑day basis.  
- Effective communication channels between management and residents are essential.  
- Administrative overhead should be minimized through automation.

### 2.3 Product Functions
The system delivers the following core functional areas:

#### 2.3.1 User Management
- User registration and authentication.
- Profile management including room number and contact details.
- Role‑based access control differentiating Residents from Dining Managers.
- Meal‑type selection (Full or Half meal plan).

#### 2.3.2 Meal Management
- Daily tracking of noon and dinner meals.
- Ability for users to toggle their meal service status (Active/Inactive).
- Support for special requests (e.g., noon meal for night pickup).
- Automatic deactivation of meal service when account balance reaches zero.
- Individual meal‑portion count tracking.

#### 2.3.3 Financial Management
- A secure account recharge system for managers.
- Automatic deduction of meal costs based on consumption.
- Complete transaction‑history tracking.
- Real‑time balance monitoring and low‑balance warnings.
- Financial summary reports for managerial oversight.
- Configurable meal‑rate management with historical tracking.

#### 2.3.4 Administrative Functions
- A comprehensive manager dashboard providing a user overview.
- Meal‑attendance tracking for all active users.
- User search and filtering capabilities.
- Bulk meal‑status management.
- Real‑time balance updates.

#### 2.3.5 Communication System
- A digital notice board for official announcements.
- Support for file attachments on notices.
- Management of feast announcements and events.
- Guest‑feast‑request management.
- A structured complaint‑filing and resolution system.

### 2.4 User Characteristics

#### 2.4.1 Residents
- **Technical Expertise:** Basic computer literacy; comfortable using a web browser.
- **Primary Activities:** Tracking daily meals, checking account balance, reading notices, filing complaints.
- **Frequency of Use:** Daily, typically once or twice per day.
- **Access Level:** Limited strictly to their own personal data and general notices.

#### 2.4.2 Dining Managers
- **Technical Expertise:** Moderate computer skills; capable of handling administrative interfaces.
- **Primary Activities:** Managing user accounts, recharging balances, tracking meal attendance, posting notices, resolving complaints.
- **Frequency of Use:** Multiple times throughout the day.
- **Access Level:** Full system access with administrative privileges.

### 2.5 Operating Environment
- **Platform:** Web‑based application accessible via modern desktop and mobile browsers.
- **Server:** Linux or Windows server capable of running Python 3.8+.
- **Database:** SQLite for development and testing; PostgreSQL or MySQL for production deployment.
- **Framework:** Django 5.0+ as the core backend framework.
- **Frontend:** HTML5, CSS3, Bootstrap 4 for styling, and vanilla JavaScript for interactivity.
- **API:** Django REST Framework providing a RESTful API with JWT authentication for potential mobile‑app integration.

### 2.6 Design and Implementation Constraints

#### 2.6.1 Technical Constraints
1. The system must be developed using the Django web framework (Version 5.0 or higher).
2. Python 3.8 or a more recent version is required.
3. The user interface must be fully compatible with modern web browsers, including the latest two versions of Chrome, Firefox, Safari, and Edge.
4. A mobile‑responsive design is mandatory.
5. A RESTful API must be implemented to allow for future mobile‑application integration.

#### 2.6.2 Regulatory Constraints
1. The system must comply with data‑privacy principles.
2. User passwords must be stored securely using Django’s built‑in hashing mechanisms.
3. All forms must be protected against Cross‑Site Request Forgery (CSRF) attacks.
4. Measures must be in place to prevent Cross‑Site Scripting (XSS) vulnerabilities.

#### 2.6.3 Business Constraints
1. The system must be maintainable by staff possessing basic knowledge of the Django framework.
2. Server resource requirements (CPU, RAM) should be minimal.
3. Deployment and hosting should be cost‑effective.
4. The architecture must be scalable to accommodate future expansion, such as supporting multiple halls.

### 2.7 Assumptions and Dependencies

#### 2.7.1 Assumptions
1. All users (residents and managers) will have access to an internet‑connected device (computer, tablet, or smartphone).
2. Dining managers will receive basic training on how to use the system.
3. Regular backups of the database will be performed by the system administrators.
4. Network connectivity in the hall will be generally stable.
5. Users possess a fundamental understanding of web navigation.

#### 2.7.2 Dependencies
1. Availability of the Django framework and its required third‑party packages.
2. Reliable operation of the chosen database system (SQLite/PostgreSQL/MySQL).
3. Existence of web‑server infrastructure (e.g., Nginx, Gunicorn).
4. A valid SSL certificate for enabling HTTPS in production.
5. Media storage (local filesystem or cloud) for uploaded file attachments.
6. Access to an SMTP server for email‑notification features planned for future releases.

---

## 3. Glossary

| Term | Definition |
|------|------------|
| **API** | Application Programming Interface – a set of rules that allows different software systems to communicate with each other. |
| **Authentication** | The process of verifying the identity of a user, typically through credentials like a username and password. |
| **Balance** | The remaining monetary amount in a user’s account, available for meal deductions. |
| **CORS** | Cross‑Origin Resource Sharing – a security feature that controls how web pages in one domain can request resources from another domain. |
| **CSRF** | Cross‑Site Request Forgery – a type of attack where unauthorized commands are transmitted from a user the web application trusts. |
| **Dashboard** | The main interface presented to a user after login, displaying key information and providing quick access to common actions. |
| **Dining Manager** | An authorized staff member with administrative privileges to manage the dining‑hall operations through the system. |
| **Django** | A high‑level Python web framework that encourages rapid development and clean, pragmatic design. |
| **Feast** | A special meal event organized in the hall, often on occasions or holidays. |
| **Full Meal** | A complete meal package that includes both noon and dinner at the standard rate. |
| **Guest Request** | A formal request submitted by a resident to bring an external guest to a feast event. |
| **Half Meal** | A reduced meal package offered at a discounted rate, typically for users with partial requirements. |
| **JWT** | JSON Web Token – a compact, URL‑safe means of representing claims to be transferred between two parties, used for API authentication. |
| **Meal Count** | The number of meal portions consumed by a user, which can be a decimal value (e.g., 1.0, 0.5) to represent partial meals. |
| **Meal Deduction** | The automatic reduction of a user’s account balance when the cost of consumed meals is charged. |
| **Meal Rate** | The cost per meal, which can be set separately for full‑meal and half‑meal users. |
| **Meal Record** | A database entry that tracks a user’s meal consumption for a specific meal type on a specific date. |
| **Meal Status** | An indicator (Active or Inactive) that shows whether a user’s meal service is currently enabled. |
| **Middleware** | Software that acts as a bridge between an operating system or database and applications, especially on a network. In Django, middleware is a framework of hooks into Django’s request/response processing. |
| **Mobile Number** | The contact phone number of a user, used for communication. |
| **Notice** | An official announcement posted by the hall management, viewable by all users. |
| **ORM** | Object‑Relational Mapping – a technique that lets you query and manipulate data from a database using an object‑oriented paradigm. |
| **Profile** | A collection of user‑specific information and settings beyond the basic authentication data. |
| **Recharge** | The act of adding funds to a user’s account, performed by a dining manager. |
| **REST API** | Representational State Transfer Application Programming Interface – an architectural style for designing networked applications that uses standard HTTP methods. |
| **Room Number** | A unique identifier for a resident’s accommodation within the hall. |
| **SRS** | Software Requirements Specification – the present document that describes the requirements for the system. |
| **Transaction** | A financial record documenting a recharge, a meal‑cost deduction, or another expense. |
| **User** | Any person registered in the system, either a resident or a dining manager. |
| **XSS** | Cross‑Site Scripting – a security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. |

---

## 4. User Requirements Definition

### 4.1 Functional Requirements

#### 4.1.1 User Authentication and Authorization
**FR-1.1: User Registration**  
The system shall allow new users to register by providing a username, email address, password, first name, and last name. Upon successful registration, the system shall automatically create a corresponding UserProfile containing the user’s room number and mobile number. The system shall validate the uniqueness of both the username and email address. By default, the user’s meal status shall be set to “active” at the time of registration.

**FR-1.2: User Login**  
Users shall authenticate themselves by providing their username and password. Following successful authentication, the system shall redirect the user to their respective dashboard. The system shall maintain a session for the logged‑in user. An optional “Remember Me” functionality shall be provided for convenience.

**FR-1.3: User Logout**  
Users shall be able to log out of the system securely. Upon logout, the system shall clear all session data and redirect the user to the home page or login page.

**FR-1.4: Password Management**  
Users shall have the ability to change their password. The system shall enforce password‑complexity requirements (minimum length, etc.) and confirm the password change upon successful update.

**FR-1.5: Role‑Based Access Control**  
The system shall clearly distinguish between regular users (residents) and dining managers. Dining managers shall have access to all administrative functions, while regular users shall only be able to access and modify their own personal data.

#### 4.1.2 Dashboard and User Interface
**FR-2.1: User Dashboard**  
Each resident shall be presented with a personalized dashboard upon login. This dashboard shall display: the user’s current account balance; their current meal status (Active/Inactive); today’s meal records (indicating whether noon and dinner have been taken); the total monthly meal count and corresponding cost; the current applicable meal rate; and visual indicators for today’s meal status.

**FR-2.2: Manager Dashboard**  
Dining managers shall have access to an administrative dashboard. This dashboard shall provide: a list of all users with search capability; a separate view of active users with an interface for real‑time meal tracking; key statistics such as the number of pending guest requests, unresolved complaints, and users with low balance; quick access links to all administrative functions; and an overview of today’s total meal consumption.

**FR-2.3: Navigation**  
The system shall provide an intuitive and consistent navigation menu across all pages. The current page or section shall be clearly indicated (e.g., through highlighting). Breadcrumb navigation shall be implemented where appropriate to enhance user orientation.

#### 4.1.3 Meal Management
**FR-3.1: Meal Status Toggle**  
Users shall be able to activate or deactivate their meal service with a single action (toggle). The system shall prevent any meal marking if the user’s meal status is inactive. Furthermore, the system shall automatically deactivate a user’s meal service when their account balance reaches zero.

**FR-3.2: Daily Meal Tracking**  
Users shall be able to mark their noon meal as “taken.” Users shall be able to mark their dinner as “taken.” The system shall prevent duplicate marking of the same meal type on the same day. Each meal record shall track an individual meal‑count value.

**FR-3.3: Night Meal Request**  
Users shall have the option to request that their noon meal be made available for pickup at dinner time. The system shall mark the noon meal record as “requested for night.” When the user later marks dinner as taken, the system shall process both meals together and deduct the appropriate combined cost.

**FR-3.4: Manager Meal Tracking**  
Dining managers shall have the capability to mark (or unmark) meals for any active user. Managers shall be able to view the real‑time meal status for all users simultaneously. Managers shall also be able to toggle the meal‑service status for any user. The system shall handle the automatic deduction logic when a manager marks both meals for a user.

**FR-3.5: Meal Deduction Logic**  
The system shall deduct the meal cost only after both daily meals (noon and dinner) have been marked as taken. The amount deducted shall be based on the user’s designated meal rate (full or half). A transaction record shall be created for each deduction. If a manager unmarks a meal, the system shall issue a refund. Deduction shall be prevented if the user’s balance is insufficient.

#### 4.1.4 Financial Management
**FR-4.1: Account Recharge**  
Dining managers shall be able to recharge a user’s account by specifying an amount. The system shall update the user’s balance immediately and create a corresponding transaction record. A confirmation of the recharge shall be displayed to the manager.

**FR-4.2: Balance Tracking**  
The system shall maintain an accurate, real‑time balance for each user. The current balance shall be prominently displayed on the user’s dashboard. The system shall generate low‑balance warnings when a user’s balance falls below a configurable threshold (e.g., 50 currency units). Negative balances for meal deductions shall be prevented.

**FR-4.3: Transaction History**  
The system shall record every financial transaction. Each transaction record shall include: the amount, type (recharge/deduction/refund), a description, a precise timestamp, and a reference to the user who created it (if applicable). Users shall be able to view their own transaction history. Managers shall be able to view the transaction history of all users.

**FR-4.4: Meal Rate Management**  
Dining managers shall have the authority to set and update meal rates. The system shall support separate rate configurations for full meals and half meals. Each rate shall have an effective‑from date. The system shall always use the most recent effective rate for calculations.

**FR-4.5: Financial Reports**  
The system shall provide financial summaries for managerial oversight. These reports shall include: total recharges collected, total meal deductions, total other expenses, the calculated manager balance (recharges – deductions – expenses), the sum of all user balances, and a list of recent transactions.

#### 4.1.5 Profile Management
**FR-5.1: Profile Viewing**  
Users shall be able to view their complete profile information, which includes: room number, mobile number, current balance, selected meal type, and current meal status.

**FR-5.2: Profile Editing**  
Users shall be able to update certain profile information, such as their mobile number. Users shall also be able to change their meal type (between full and half). All profile updates shall be validated by the system. When changing the meal type, the system shall display the current applicable meal rates for reference.

**FR-5.3: User Details (Manager)**  
Dining managers shall be able to view detailed information for any user. This detailed view shall include the user’s monthly meal statistics and the calculated monthly meal cost based on their consumption.

#### 4.1.6 Notice Management
**FR-6.1: Notice Creation**  
Dining managers shall be able to create new notices by providing a title and description. The system shall support attaching files to notices. Each notice shall be automatically timestamped with its creation date and time. Attachments shall be stored securely in a designated directory.

**FR-6.2: Notice Listing**  
All users (both residents and managers) shall be able to view a list of all notices. Notices shall be sorted in reverse chronological order (newest first). The list view shall display a summary or excerpt of each notice.

**FR-6.3: Notice Details**  
Users shall be able to click on a notice to view its full details. If the notice has an attachment, the system shall provide a download link. The system may optionally track the date when a user viewed a particular notice.

**FR-6.4: Notice Editing**  
Dining managers shall be able to edit existing notices, including updating the title, description, and replacing the attachment. The system shall maintain a history of changes (or at least update the timestamp). The updated timestamp shall reflect the time of the edit.

**FR-6.5: Notice Deletion**  
Dining managers shall be able to delete notices. The system shall require confirmation before performing the deletion. Upon deletion, any associated attachment file shall also be removed from storage.

**FR-6.6: Attachment Management**  
The system shall support common file formats for attachments (e.g., PDF, JPEG, PNG, DOC, DOCX). A secure download mechanism shall be provided. The system shall validate file types and enforce a maximum file‑size limit (e.g., 10 MB) to prevent abuse.

#### 4.1.7 Feast Management
**FR-7.1: Feast Creation**  
Dining managers shall be able to create feast events by specifying a title, description, date, and meal time (e.g., “Dinner”). The system shall record the creator of the feast and automatically timestamp the creation.

**FR-7.2: Feast Listing**  
All users shall be able to view a list of upcoming and past feasts. Feasts shall be sorted by date. The list shall clearly display key details such as the feast title, date, and meal time.

**FR-7.3: Guest Feast Requests**  
Residents shall be able to submit requests to bring guests to a feast. The request shall include the guest’s name, the guest’s mobile number, the requester’s name, and the requester’s mobile number. The system shall track the status of each request (pending, approved, rejected) and record the timestamp of the request.

**FR-7.4: Guest Request Management**  
Dining managers shall be able to view all guest requests. Managers shall have the authority to approve or reject any pending request. Upon status change, the system shall update the request record accordingly. A notification mechanism (e.g., on‑screen update) shall inform managers of the action’s completion.

#### 4.1.8 Complaint Management
**FR-8.1: Complaint Filing**  
Users shall be able to file complaints by providing a title and a detailed description. The system shall timestamp the complaint and set its initial status to “pending.” The creator of the complaint shall be recorded.

**FR-8.2: Complaint Viewing**  
Users shall be able to view a list of their own submitted complaints. Dining managers shall be able to view a list of all complaints from all users. In both cases, complaints shall be sorted by creation date (newest first).

**FR-8.3: Complaint Resolution**  
Dining managers shall be able to update the status of a complaint (e.g., to “resolved” or “rejected”). Managers shall be able to add a response text to the complaint. The system shall support standard complaint statuses: pending, resolved, rejected. A history of status changes shall be maintained.

#### 4.1.9 Search and Filter
**FR-9.1: User Search**  
Dining managers shall be able to search for users by room number, first name, last name, or mobile number. The search shall provide real‑time results as the manager types. Matching criteria in the results shall be highlighted for easy identification.

**FR-9.2: Active User Filter**  
Dining managers shall be able to filter the user list to show only active users (those with meal service enabled). The search functionality shall also work within this filtered list. The active‑users view shall include the meal‑tracking interface for efficient daily management.

### 4.2 Non-Functional Requirements

#### 4.2.1 Performance Requirements
**NFR-1.1: Response Time**  
Under normal load conditions, the system shall respond to user actions (clicks, form submissions) within 2 seconds. The dashboard page shall load completely within 3 seconds. Search results shall appear within 1 second of initiating the search.

**NFR-1.2: Concurrent Users**  
The system shall support at least 100 concurrent users without significant degradation in performance. The architecture shall be capable of handling up to 500 registered users while maintaining acceptable response times.

**NFR-1.3: Database Performance**  
Database queries executed during normal operations shall complete within 1 second. The system shall employ database indexes to optimize frequent queries. Django’s `select_related` and `prefetch_related` methods shall be used to minimize database hits and improve efficiency.

#### 4.2.2 Security Requirements
**NFR-2.1: Authentication**  
The system shall utilize Django’s built‑in authentication system. User passwords shall be hashed using the PBKDF2 algorithm with a SHA256 hash. The system shall enforce a minimum password length of 8 characters.

**NFR-2.2: Authorization**  
The system shall verify user permissions for every protected action or page access. Django’s `@login_required` decorator shall be used for views requiring authentication. The `@user_passes_test` decorator or custom permission checks shall be used to enforce role‑based access control.

**NFR-2.3: Data Protection**  
All forms in the system shall include and validate CSRF tokens. User inputs shall be sanitized and escaped in templates to prevent XSS attacks. All database interactions shall use Django’s ORM or parameterized queries to eliminate SQL injection vulnerabilities.

**NFR-2.4: API Security**  
The REST API shall use JWT (JSON Web Token) for authentication. Access tokens shall have a finite expiration time (e.g., 24 hours). A token‑refresh mechanism shall be provided. Cross‑Origin Resource Sharing (CORS) shall be configured to restrict API access to approved origins only.

**NFR-2.5: File Upload Security**  
The system shall validate the file type (extension and MIME type) before accepting any upload. A maximum file‑size limit (e.g., 10 MB) shall be enforced. Uploaded files shall be stored outside the web server’s document root when possible. Unique filenames shall be generated to prevent overwriting and path‑traversal attacks.

#### 4.2.3 Reliability Requirements
**NFR-3.1: Availability**  
The system shall maintain an uptime of 99.5% during operational hours. Any planned maintenance requiring downtime shall be communicated to users in advance. Automated monitoring shall be in place to detect outages.

**NFR-3.2: Data Integrity**  
The database shall enforce referential integrity through foreign‑key constraints. Critical financial operations (e.g., recharge and deduction) shall be performed within database transactions to ensure atomicity. Input validation shall prevent the storage of corrupt or inconsistent data.

**NFR-3.3: Error Handling**  
The system shall display user‑friendly error messages that do not expose sensitive system information. All application errors and exceptions shall be logged with sufficient detail for administrator review. The system shall handle exceptions gracefully, preventing crashes and allowing the user to continue.

**NFR-3.4: Backup and Recovery**  
Automated daily backups of the database shall be performed. Backup files shall be stored securely, preferably in an off‑site location. In the event of a failure, the system shall be recoverable to a consistent state within 4 hours.

#### 4.2.4 Usability Requirements
**NFR-4.1: User Interface**  
The interface shall be intuitive, requiring minimal training for new users. Consistent design patterns and visual cues shall be used throughout the application. Clear feedback (success messages, error indications) shall be provided for every user action. The Bootstrap 4 framework shall be leveraged to ensure a professional and cohesive look.

**NFR-4.2: Accessibility**  
The system shall strive to comply with WCAG 2.1 Level AA guidelines. All functionality shall be accessible via keyboard navigation. Images shall have appropriate alt text. Form fields shall be properly labeled and associated with their labels.

**NFR-4.3: Mobile Responsiveness**  
The interface shall be fully functional and readable on mobile devices (smartphones and tablets). The layout shall adapt fluidly to different screen sizes using responsive CSS. Touch targets (buttons, links) shall be of sufficient size for easy interaction on touchscreens.

**NFR-4.4: Internationalization**  
The system shall display the Bangladeshi Taka currency symbol (৳) correctly. UTF‑8 encoding shall be used throughout to support Bengali and other characters. The codebase shall be structured to facilitate future localization (translation into other languages) if required.

#### 4.2.5 Maintainability Requirements
**NFR-5.1: Code Quality**  
All Python code shall adhere to the PEP 8 style guide. The codebase shall include appropriate documentation (docstrings, comments). Variable, function, and class names shall be meaningful and follow established conventions.

**NFR-5.2: Modularity**  
The system shall follow Django’s application structure, separating concerns into distinct apps (e.g., `dining`). Within apps, code shall be organized into models, views, forms, and templates. Reusable components and template inheritance shall be used to reduce duplication.

**NFR-5.3: Version Control**  
The source code shall be managed using the Git version‑control system. Commit messages shall be clear and descriptive. A branching strategy (e.g., Git Flow) shall be used to manage feature development, releases, and hotfixes.

**NFR-5.4: Documentation**  
Up‑to‑date technical documentation, including this SRS, shall be maintained. Complex logic within the code shall be explained with inline comments. API endpoints shall be documented, possibly using tools like Swagger or Django REST Framework’s built‑in documentation.

#### 4.2.6 Scalability Requirements
**NFR-6.1: Horizontal Scaling**  
The system architecture shall support deployment behind a load balancer with multiple application server instances. Session management for the API shall be stateless (using JWT) to facilitate horizontal scaling. The design shall allow for distributed deployment if needed in the future.

**NFR-6.2: Database Scaling**  
The system shall be easily migratable from SQLite to a more robust database like PostgreSQL or MySQL. The database schema shall be designed to allow for future extensions without major refactoring. Database connection pooling shall be utilized to manage concurrent connections efficiently.

**NFR-6.3: Storage Scaling**  
The system shall be designed to integrate with external file‑storage services (e.g., Amazon S3, Google Cloud Storage) for media files. This separation shall allow the application server to scale independently of file‑storage needs.

#### 4.2.7 Compatibility Requirements
**NFR-7.1: Browser Compatibility**  
The system shall function correctly on the latest two versions of the following browsers: Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Edge.

**NFR-7.2: Device Compatibility**  
The system shall provide a consistent user experience on desktop computers, tablets, and smartphones.

**NFR-7.3: API Compatibility**  
The REST API shall follow standard REST conventions (proper use of HTTP methods, status codes). Where possible, the API shall maintain backward compatibility. The API version shall be clearly indicated in the URL or headers.

#### 4.2.8 Legal and Compliance
**NFR-8.1: Data Privacy**  
The system shall handle personal user data in accordance with relevant data‑protection regulations. Users shall have the right to access and request correction of their personal data. User data shall not be shared with third parties without explicit user consent.

**NFR-8.2: Audit Trail**  
The system shall log all significant administrative actions (e.g., recharges, rate changes, complaint resolutions). Financial transaction records shall be immutable once created. All logs and records shall include accurate timestamps.

---

## 5. System Architecture

### 5.1 Architectural Design

#### 5.1.1 Overall Architecture
The Hall Dining Management System adopts a classic three‑tier architecture, implemented using Django’s Model‑View‑Template (MVT) pattern, which is a variation of the Model‑View‑Controller (MVC) pattern.

```
┌─────────────────────────────────────────────────────────────┐
│                     Presentation Layer                       │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────────┐  │
│  │  Web UI    │  │  Mobile    │  │   REST API           │  │
│  │ (Templates)│  │  Browser   │  │   (JSON Response)    │  │
│  └────────────┘  └────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     Application Layer                        │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                    Django Views                        │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │  │
│  │  │ Function │  │  Class   │  │  API ViewSets    │   │  │
│  │  │  Views   │  │  Views   │  │                  │   │  │
│  │  └──────────┘  └──────────┘  └──────────────────┘   │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                               │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                 Business Logic Layer                   │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │  │
│  │  │ Forms    │  │ Signals  │  │  Custom Methods  │   │  │
│  │  └──────────┘  └──────────┘  └──────────────────┘   │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                       Data Layer                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                    Django ORM                          │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │  │
│  │  │  Models  │  │Migrations│  │  QuerySets       │   │  │
│  │  └──────────┘  └──────────┘  └──────────────────┘   │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                               │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Database (SQLite/PostgreSQL)              │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                               │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              File Storage (Media Files)                │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Presentation Layer:** This is the user‑facing layer, comprising the HTML templates rendered by Django, accessed via web browsers on various devices, and the REST API that serves JSON data for potential mobile clients.

**Application Layer:** This is the core of the system, implemented in Django. It contains the View functions and classes that handle HTTP requests, execute business logic, and prepare data for the presentation layer. The Business Logic Layer within this tier encapsulates forms, signals, and custom methods that enforce the rules of the dining‑hall operations.

**Data Layer:** This layer is responsible for data persistence. Django’s ORM (Object‑Relational Mapper) provides an abstraction over the underlying database (SQLite for development, PostgreSQL for production). It also manages the storage and retrieval of uploaded media files.

#### 5.1.2 Component Architecture
The system is organized as a single Django project named `Hall_dining` with one primary application named `dining`. This structure promotes modularity and separation of concerns.

```
Hall_dining/                    # Project root directory
├── Hall_dining/               # Project configuration package
│   ├── __init__.py
│   ├── settings.py           # System-wide settings and configuration
│   ├── urls.py               # Project-level URL routing
│   └── wsgi.py               # WSGI configuration for deployment
│
├── dining/                    # Main application module
│   ├── __init__.py
│   ├── models.py             # Data models (database schema)
│   ├── views.py              # View functions and class-based views
│   ├── forms.py              # Django form definitions
│   ├── urls.py               # Application-specific URL patterns
│   ├── api_urls.py           # URL patterns for the REST API
│   ├── serializers.py        # DRF serializers for API data conversion
│   ├── admin.py              # Django admin site configuration
│   ├── templates/            # HTML template files
│   │   └── dining/
│   └── static/               # Static assets (CSS, JavaScript, images)
│       └── dining/
│
├── media/                    # User-uploaded files (created at runtime)
├── db.sqlite3               # SQLite database file (development)
└── manage.py                # Django's command-line utility
```

### 5.2 Data Architecture

#### 5.2.1 Entity Relationship Diagram
The core data model revolves around the `User` (from Django's `auth` system) and its one‑to‑one extension `UserProfile`. Key entities and their relationships are depicted below:

```
            ┌─────────────────┐
            │      User       │
            │ (Django Auth)   │
            │─────────────────│
            │ id (PK)         │
            │ username        │
            │ email           │
            │ first_name      │
            │ last_name       │
            │ password        │
            │ is_active       │
            └────────┬────────┘
                     │ 1:1
                     ▼
            ┌─────────────────────┐
            │   UserProfile       │
            │─────────────────────│
            │ id (PK)             │
            │ user_id (FK)        │
            │ room_number         │
            │ mobile_number       │
            │ balance             │
            │ meal_active         │
            │ is_dining_manager   │
            │ meal_type           │
            └──────────┬──────────┘
                       │ 1:N
                       ▼
            ┌─────────────────────┐
            │   MealRecord        │
            │─────────────────────│
            │ id (PK)             │
            │ user_id (FK)        │
            │ date                │
            │ meal_type           │
            │ taken               │
            │ requested_for_night │
            │ meal_count          │
            └─────────────────────┘

            ┌─────────────────────┐
            │   Transaction       │
            │─────────────────────│
            │ id (PK)             │
            │ user_id (FK)        │
            │ amount              │
            │ transaction_type    │
            │ description         │
            │ created_by_id (FK)  │
            │ created_at          │
            └─────────────────────┘

            ┌─────────────────────┐
            │    MealRate         │
            │─────────────────────│
            │ id (PK)             │
            │ full_meal_rate      │
            │ half_meal_rate      │
            │ effective_from      │
            └─────────────────────┘

            ┌─────────────────────┐
            │     Notice          │
            │─────────────────────│
            │ id (PK)             │
            │ title               │
            │ description         │
            │ date                │
            │ attachment          │
            └─────────────────────┘

            ┌─────────────────────┐
            │      Feast          │
            │─────────────────────│
            │ id (PK)             │
            │ title               │
            │ description         │
            │ date                │
            │ meal_time           │
            │ created_by_id (FK)  │
            │ created_at          │
            └──────────┬──────────┘
                       │ 1:N
                       ▼
            ┌─────────────────────┐
            │ GuestFeastRequest   │
            │─────────────────────│
            │ id (PK)             │
            │ feast_id (FK)       │
            │ guest_name          │
            │ guest_mobile        │
            │ requested_by_name   │
            │ requested_by_mobile │
            │ requested_at        │
            │ status              │
            └─────────────────────┘

            ┌─────────────────────┐
            │    Complaint        │
            │─────────────────────│
            │ id (PK)             │
            │ user_id (FK)        │
            │ title               │
            │ description         │
            │ created_at          │
            │ status              │
            │ response            │
            └─────────────────────┘
```

*(Note: A `MealSchedule` entity was mentioned in an earlier outline but is not a core requirement for the initial version. It can be added later for menu planning.)*

### 5.3 Technology Stack

#### 5.3.1 Backend Technologies
1.  **Framework:** Django 5.0+ (Long‑Term Support version recommended).
2.  **Language:** Python 3.8 or higher.
3.  **ORM:** Django's built‑in Object‑Relational Mapper.
4.  **API Framework:** Django REST Framework (DRF) 3.16.1+.
5.  **Authentication:** Django's built‑in auth system for the web interface; Simple JWT (version 5.5.1+) for API token‑based auth.

#### 5.3.2 Frontend Technologies
1.  **Template Engine:** Django Templates (Django's native templating language).
2.  **CSS Framework:** Bootstrap 4.6+ for responsive layout and pre‑styled components.
3.  **Forms:** Django Crispy Forms configured with the Bootstrap 4 template pack for elegant form rendering.
4.  **JavaScript:** Primarily vanilla JavaScript for dynamic interactions (AJAX calls, DOM updates). May include minimal jQuery if required by Bootstrap components.

#### 5.3.3 Database
1.  **Development:** SQLite3 – lightweight and file‑based, ideal for development and testing.
2.  **Production:** PostgreSQL (strongly recommended) or MySQL – robust, scalable, and suitable for multi‑user web applications.

#### 5.3.4 Additional Libraries
1.  **Image Processing:** Pillow 11.0+ (required by Django for image‑field manipulation if image uploads are added).
2.  **CORS Handling:** `django-cors-headers` 4.9.0+ to manage Cross‑Origin Resource Sharing for the API.
3.  **JWT Support:** `PyJWT` 2.10.1+, a dependency of `djangorestframework-simplejwt`.

### 5.4 Security Architecture

#### 5.4.1 Authentication Flow
1.  **User Login Request:** User submits credentials via the login form.
2.  **Username/Password Validation:** Django's `authenticate()` function is called.
3.  **Django Authentication:** The auth backend verifies the credentials against the database.
4.  **Session Creation:** Upon success, `login()` creates a session for the user.
5.  **Dashboard Redirect:** User is redirected to their role‑specific dashboard.

#### 5.4.2 Authorization Layers
The system implements a defense‑in‑depth approach to authorization:
-   **View Level:** Using the `@login_required` decorator to ensure only logged‑in users can access certain pages.
-   **Role Level:** Using the `@user_passes_test(lambda u: u.userprofile.is_dining_manager)` decorator or custom permission checks to restrict access to manager‑only views.
-   **Object Level:** Within views, verifying that a user is only allowed to access or modify their own data (e.g., a resident viewing their own transaction history).
-   **API Level:** Using JWT token validation to authenticate API requests; permissions classes in DRF viewsets to enforce role‑based access.

#### 5.4.3 Security Measures
-   **CSRF Protection:** Django's middleware automatically adds and validates CSRF tokens for all state‑changing POST requests.
-   **XSS Protection:** Django templates auto‑escape variables by default, preventing most XSS attacks. User‑provided content in notices and complaints is also sanitized.
-   **SQL Injection Prevention:** Using Django's ORM exclusively for database queries, which uses parameterized queries internally.
-   **Password Hashing:** Django uses the PBKDF2 algorithm with a SHA256 hash, a salt, and multiple iterations by default.
-   **Secure File Upload:** Validating file extensions and MIME types, storing files with sanitized names.
-   **HTTPS Enforcement:** In production, the application should be served over HTTPS, with HTTP requests redirected. This is typically configured at the web‑server (Nginx/Apache) level.

### 5.5 API Architecture

#### 5.5.1 RESTful API Endpoints (Sample)
The API is designed following REST principles and uses Django REST Framework.

| Endpoint | HTTP Method | Description | Access |
| :--- | :--- | :--- | :--- |
| `/api/token/` | POST | Obtain JWT access and refresh tokens. | Public |
| `/api/token/refresh/` | POST | Refresh an expired access token. | Public (with valid refresh token) |
| `/api/users/` | GET | List all users (paginated). | Dining Managers only |
| `/api/users/<id>/` | GET | Retrieve details of a specific user. | Dining Managers or the user themselves |
| `/api/meal-records/` | GET | List meal records (filterable by user/date). | Authenticated Users |
| `/api/meal-records/` | POST | Create a new meal record (mark a meal). | Residents & Managers |
| `/api/transactions/` | GET | List financial transactions. | Users see their own; Managers see all |
| `/api/notices/` | GET | List all notices. | Public / Authenticated |
| `/api/complaints/` | GET | List complaints. | Users see their own; Managers see all |
| `/api/complaints/` | POST | File a new complaint. | Residents |

#### 5.5.2 API Response Format
The API will return consistent JSON responses. A typical successful response structure is:

```json
{
  "success": true,
  "data": {
    "id": 1,
    "field": "value"
  },
  "message": "Operation successful"
}
```

For errors, the structure will be:

```json
{
  "success": false,
  "errors": {
    "field_name": ["Error description 1", "Error description 2"]
  },
  "message": "A summary error message"
}
```

### 5.6 Deployment Architecture
For a production environment, a typical deployment setup is recommended:

```
                       ┌────────────────────────────────────────┐
                       │         Load Balancer (Optional)       │
                       └────────────────┬───────────────────────┘
                                        │
                ┌───────────┴────────────┐
                │                        │
        ┌───────▼─────┐          ┌───────▼────┐
        │  Web        │          │    Web     │
        │ Server 1    │          │  Server 2  │
        │ (Gunicorn   │          │ (Gunicorn) │
        │  + Nginx)   │          │  + Nginx)  │
        └───────┬─────┘          └───────┬────┘
                │                        │
                └───────────┬────────────┘
                            │
                ┌───────────▼────────────┐
                │   Database Server      │
                │   (PostgreSQL)         │
                └───────────┬────────────┘
                            │
                ┌───────────▼────────────┐
                │   File Storage         │
                │   (Media Files - S3)   │
                └────────────────────────┘
```

- **Load Balancer:** Distributes incoming HTTP/HTTPS traffic across multiple application servers for high availability and scalability.
- **Application Servers:** Run the Django application via Gunicorn (WSGI HTTP server). Nginx acts as a reverse proxy, serving static/media files and passing dynamic requests to Gunicorn.
- **Database Server:** A dedicated PostgreSQL server for data persistence.
- **File Storage:** For production, media files (notice attachments) should be stored on a dedicated service like Amazon S3 or a separate volume, decoupling them from the application servers.

---

## 6. System Requirements Specification

### 6.1 Functional Requirements (Detailed)

#### 6.1.1 User Management Module

**FR-UM-001: User Registration**  
**Priority:** High  
**Description:** The system shall provide a mechanism for new users to self‑register.  
**Inputs:** Username, email, password, first name, last name, room number, mobile number.  
**Processing:**  
1. Validate that the username and email are unique in the system.  
2. Create a new `User` object in Django's `auth_user` table.  
3. Hash the provided password using Django's default hasher.  
4. Create an associated `UserProfile` object, linking it to the new `User`, and populate the room number and mobile number.  
5. Set the `meal_active` flag in the profile to `True` by default.  
**Outputs:** A success confirmation message displayed to the user, followed by a redirect to the login page.  
**Error Handling:** If the username or email already exists, or if any field validation fails, clear error messages shall be displayed next to the respective form fields.

**FR-UM-002: User Authentication**  
**Priority:** High  
**Description:** The system shall authenticate registered users attempting to log in.  
**Inputs:** Username and password.  
**Processing:**  
1. Invoke Django's `authenticate()` function with the provided credentials.  
2. If authentication succeeds, call Django's `login()` function to establish a session.  
3. Load the user's `UserProfile` and store relevant information in the session if needed.  
**Outputs:** Redirect the authenticated user to their role‑appropriate dashboard.  
**Error Handling:** If authentication fails, a generic "Invalid username or password" message shall be displayed, without specifying which was incorrect.

**FR-UM-003: Profile Management**  
**Priority:** Medium  
**Description:** Users shall be able to view and update certain aspects of their profile.  
**Inputs:** Updated room number, mobile number, meal type (full/half).  
**Processing:**  
1. Retrieve the current user's `UserProfile` object.  
2. Validate the new input data (e.g., phone number format).  
3. Update the profile fields.  
4. If the meal type is changed, the user's future deductions will use the new rate, but past transactions remain unaffected.  
**Outputs:** A success message confirming the profile has been updated.  
**Error Handling:** Display validation errors if the mobile number is in an invalid format or if required fields are missing.

**FR-UM-004: Role Verification**  
**Priority:** High  
**Description:** Before granting access to any page or functionality, the system shall verify the user's role and permissions.  
**Inputs:** The current `User` object and the requested resource/URL.  
**Processing:**  
1. Check if the user is authenticated (`request.user.is_authenticated`).  
2. Check the `is_dining_manager` flag on the user's associated `UserProfile`.  
3. Verify that the requested action or data is permitted for the user's role (e.g., a resident cannot access another user's transaction page).  
**Outputs:** Access is granted, and the requested view is rendered.  
**Error Handling:** If the user is not logged in, redirect to the login page. If the user lacks permission, return an HTTP 403 Forbidden response or redirect to a "Permission Denied" page.

#### 6.1.2 Meal Management Module

**FR-MM-001: Meal Status Toggle**  
**Priority:** High  
**Description:** Users shall be able to manually activate or deactivate their meal service.  
**Inputs:** A toggle action from the user (e.g., clicking an "Activate/Deactivate" button).  
**Processing:**  
1. Retrieve the user's `UserProfile`.  
2. Invert the boolean value of the `meal_active` field.  
3. Save the updated profile.  
4. If deactivating, ensure no future meals can be marked. If activating, check that the balance is positive.  
**Outputs:** The dashboard is updated to reflect the new status (Active/Inactive). A confirmation message is shown.  
**Error Handling:** If a user tries to activate with a zero or negative balance, the system may display a warning and keep the status inactive, prompting for a recharge.

**FR-MM-002: Mark Noon Meal**  
**Priority:** High  
**Description:** A resident shall be able to record that they have taken their noon meal.  
**Inputs:** Meal type ("noon") and the current date.  
**Processing:**  
1. Check that the user's `UserProfile.meal_active` is `True`.  
2. Check if a `MealRecord` for "noon" on the current date already exists for this user.  
3. If it exists and is not taken, update it to `taken=True`. If it doesn't exist, create a new `MealRecord` with `taken=True` and `meal_count=1.0`.  
**Outputs:** A confirmation message (e.g., "Noon meal marked as taken").  
**Error Handling:** Prevent the action if the meal is already marked as taken, or if the user's meal service is inactive. Display an appropriate error message.

**FR-MM-003: Mark Dinner**  
**Priority:** High  
**Description:** A resident shall be able to record that they have taken their dinner.  
**Inputs:** Meal type ("dinner") and the current date.  
**Processing:**  
1. Check that the user's `UserProfile.meal_active` is `True`.  
2. Check for an existing "noon" meal record for today that is `requested_for_night=True`.  
3. If such a noon request exists, this triggers the combined meal processing (see FR-MM-005).  
4. Otherwise, create or update the "dinner" `MealRecord` to `taken=True`.  
5. After marking dinner, check if both "noon" and "dinner" are now `taken=True`. If yes, trigger the automatic deduction process (FR-MM-007).  
**Outputs:** A confirmation message. If a deduction occurs, the message should include the deducted amount and new balance.  
**Error Handling:** Prevent marking if already taken, or if the meal service is inactive. Check balance before any deduction.

**FR-MM-004: Request Noon Meal for Night**  
**Priority:** Medium  
**Description:** Users shall be able to indicate they will pick up their noon meal at dinner time.  
**Inputs:** User action to request a noon meal for night pickup.  
**Processing:**  
1. Check that no regular "noon" meal record with `taken=True` exists for today.  
2. Create or update the "noon" `MealRecord` for today, setting `taken=False` and `requested_for_night=True`.  
**Outputs:** A confirmation message (e.g., "Noon meal requested for night pickup").  
**Error Handling:** Prevent the request if the noon meal has already been marked as taken normally.

**FR-MM-005: Combined Meal Processing**  
**Priority:** High  
**Description:** When a user who requested a noon meal for night later marks dinner, the system shall process both meals together.  
**Inputs:** The action of marking "dinner" when a "noon" record with `requested_for_night=True` exists.  
**Processing:**  
1. Locate the "noon" `MealRecord` for today with `requested_for_night=True`.  
2. Set both the "noon" and the new "dinner" records to `taken=True`.  
3. For accounting, set `meal_count=2.0` on one of the records (or handle logically) to represent two meal portions.  
4. Deduct `2 * user_meal_rate` from the user's balance.  
5. Create a single transaction record for the combined deduction.  
**Outputs:** Both meals are marked as taken, the balance is updated, and a transaction is logged.  
**Error Handling:** Ensure the user has sufficient balance for two meal portions before processing.

**FR-MM-006: Manager Meal Tracking**  
**Priority:** High  
**Description:** Dining managers shall have an interface to mark or unmark meals for any active user.  
**Inputs:** User ID, meal type (noon/dinner), action (mark as taken, mark as not taken), date (defaults to today).  
**Processing:**  
1. Verify the current user is a dining manager.  
2. Fetch or create the `MealRecord` for the specified user, date, and meal type.  
3. Update the `taken` field based on the manager's action.  
4. If marking a meal as taken, check if the other meal for the day is also taken. If both are now taken, trigger the deduction process.  
5. If unmarking a meal that was part of a deducted pair, trigger a refund process (FR-MM-008).  
**Outputs:** The user's meal status is updated in real‑time on the manager's interface. If a deduction or refund occurs, the user's balance is updated and a transaction is created.  
**Error Handling:** Validate that the target user exists and that the action is logical (e.g., cannot unmark a meal that wasn't marked).

**FR-MM-007: Automatic Deduction**  
**Priority:** Critical  
**Description:** The system shall automatically deduct the cost of meals when both noon and dinner are recorded as taken for a user on the same day.  
**Inputs:** The user's ID and the current date, after confirming both meal records have `taken=True`.  
**Processing:**  
1. Verify that both `MealRecord` objects (noon and dinner) for the user and date have `taken=True`.  
2. Retrieve the user's current meal rate based on their `meal_type` and the active `MealRate`.  
3. Check that the user's `balance` is greater than or equal to the meal rate.  
4. Deduct the meal rate amount from the user's `balance`.  
5. Create a `Transaction` record with `type='deduction'`, the amount, and a description like "Meal cost for [date]".  
**Outputs:** The user's balance is reduced. A transaction is saved.  
**Error Handling:** If the balance is insufficient, do not perform the deduction. Log an error and optionally notify the manager. The meal records remain marked, but the financial transaction is pending.

**FR-MM-008: Meal Refund**  
**Priority:** High  
**Description:** When a dining manager unmarks a meal that was part of a deducted pair, the system shall refund the cost to the user's account.  
**Inputs:** Manager's unmark action, the user, and the date.  
**Processing:**  
1. Identify the deduction `Transaction` for that user on that specific date with `type='deduction'`.  
2. Add the deducted amount back to the user's `balance`.  
3. Create a new `Transaction` record with `type='refund'`, a positive amount, and a description explaining the reason (e.g., "Refund for meal unmarked on [date]").  
**Outputs:** User's balance is increased. A refund transaction is logged.  
**Error Handling:** Only proceed if a corresponding deduction transaction exists. If not, alert the manager that no deduction was found to refund.

**FR-MM-009: Meal Count Tracking**  
**Priority:** Medium  
**Description:** The system shall track meal consumption in portions, which can be fractional (e.g., 0.5 for a half portion).  
**Inputs:** A `meal_count` value (typically 0.5, 1.0, 1.5, 2.0, etc.).  
**Processing:**  
1. Store the `meal_count` decimal value in the `MealRecord` model.  
2. Use this value in calculations for monthly consumption summaries and, if extended, for proportional cost calculations.  
**Outputs:** Accurate tracking of meal portions consumed.  
**Error Handling:** Validate that the `meal_count` is a positive decimal number.

#### 6.1.3 Financial Management Module

**FR-FM-001: Account Recharge**  
**Priority:** High  
**Description:** Dining managers shall be able to add funds to a user's account.  
**Inputs:** Target user's ID, recharge amount (positive number), optional description.  
**Processing:**  
1. Verify the current user has dining‑manager privileges.  
2. Validate that the recharge amount is greater than zero.  
3. Create a new `Transaction` record with `type='recharge'`, the amount, description, `created_by` set to the manager, and timestamp.  
4. Increase the target user's `UserProfile.balance` by the recharge amount.  
**Outputs:** The user's balance is updated instantly. A success message is displayed to the manager, and the transaction is recorded.  
**Error Handling:** If the amount is zero or negative, display a validation error. If the user does not exist, show an error.

**FR-FM-002: Balance Calculation**  
**Priority:** Critical  
**Description:** The system must maintain a consistent and accurate balance for each user at all times.  
**Inputs:** The complete history of `Transaction` records for a user.  
**Processing:**  
1. The balance is a derived state: `current_balance = sum(recharges) - sum(deductions) + sum(refunds)`.  
2. To ensure integrity, the balance field is updated atomically with each financial transaction (recharge, deduction, refund).  
3. The system shall prevent a meal deduction transaction from being created if it would result in a negative balance.  
**Outputs:** The correct balance is displayed on the user's dashboard and in all relevant views.  
**Error Handling:** Use database transactions to ensure balance updates and transaction creation succeed or fail together, preventing inconsistent states.

**FR-FM-003: Transaction Recording**  
**Priority:** High  
**Description:** Every financial movement must be recorded in an immutable audit log.  
**Inputs:** User ID, amount, transaction type (recharge/deduction/refund/expense), description, creator ID (if applicable).  
**Processing:**  
1. Create a new `Transaction` object, populating all fields.  
2. Set `created_at` to the current date and time.  
**Outputs:** A permanent record saved in the `dining_transaction` database table.  
**Error Handling:** Ensure database constraints prevent saving a transaction without a linked user or a valid amount.

**FR-FM-004: Monthly Meal Cost Calculation**  
**Priority:** Medium  
**Description:** The system shall calculate the total meal cost for a user for the current calendar month.  
**Inputs:** The user object and the start date of the current month.  
**Processing:**  
1. Query all `MealRecord` objects for the user where the `date` falls within the current month and `taken=True`.  
2. Sum the `meal_count` values from these records to get the total portions consumed.  
3. Retrieve the user's applicable meal rate (full or half).  
4. Calculate: `monthly_cost = total_portions * user_meal_rate`.  
**Outputs:** Display the calculated monthly cost on the user's dashboard and in manager reports.  
**Error Handling:** Handle cases where no meals have been taken in the month (cost = 0).

**FR-FM-005: Meal Rate Configuration**  
**Priority:** High  
**Description:** Dining managers shall be able to define the cost of full and half meals.  
**Inputs:** New `full_meal_rate`, new `half_meal_rate`, and an `effective_from` date.  
**Processing:**  
1. Create a new `MealRate` object with the provided rates and effective date.  
2. Save the object. Previous rates remain in the database for historical reference.  
**Outputs:** The new rates are saved. Confirmation is shown to the manager.  
**Error Handling:** Validate that rates are positive numbers and that the `effective_from` date is not in the past (or handle past‑dated rates appropriately for record‑keeping).

**FR-FM-006: Rate History Management**  
**Priority:** Low  
**Description:** The system shall maintain a history of all meal rate changes.  
**Inputs:** All saved `MealRate` objects.  
**Processing:**  
1. Query `MealRate` objects ordered by `effective_from` in descending order (newest first).  
2. Display them in a list or table, showing the rate values and the date they became effective.  
**Outputs:** A viewable history of meal‑rate changes for administrative reference.  
**Error Handling:** None specific.

**FR-FM-007: Current Rate Selection**  
**Priority:** High  
**Description:** For any financial calculation, the system must determine the correct meal rate to apply based on the date of consumption.  
**Inputs:** The date for which the rate is needed (typically the current date or the date of a meal record).  
**Processing:**  
1. Query the `MealRate` table for records where `effective_from` is less than or equal to the target date.  
2. Order the results by `effective_from` in descending order.  
3. The first record in this list is the rate that was effective on that date.  
**Outputs:** The applicable `full_meal_rate` and `half_meal_rate` for the given date.  
**Error Handling:** If no rate is found for a date, the system should use a sensible default (e.g., the most recent rate) and log a warning.

**FR-FM-008: Financial Summary**  
**Priority:** Medium  
**Description:** The manager dashboard shall present a high‑level financial overview.  
**Inputs:** All `Transaction` records and the sum of all user balances.  
**Processing:**  
1. **Total Recharges:** Sum of all transactions with `type='recharge'`.  
2. **Total Deductions:** Sum of all transactions with `type='deduction'`.  
3. **Total Expenses:** Sum of all transactions with `type='expense'` (if implemented).  
4. **Manager Balance:** Calculated as `Total Recharges - Total Deductions - Total Expenses`. This represents the net cash the manager should have.  
5. **Total User Balances:** Sum of `balance` from all `UserProfile` objects.  
**Outputs:** These figures displayed prominently on the manager dashboard.  
**Error Handling:** Handle cases with no transactions gracefully, displaying zeros.

**FR-FM-009: Transaction History**  
**Priority:** Medium  
**Description:** Users and managers shall be able to browse historical financial transactions.  
**Inputs:** For a resident: their own user ID. For a manager: optionally a filter for a specific user.  
**Processing:**  
1. Query the `Transaction` model, filtering by the relevant user(s).  
2. Order the results by `created_at` in descending order (newest first).  
3. Implement pagination for large result sets.  
**Outputs:** A paginated list of transactions, showing date, type, amount, description, and creator.  
**Error Handling:** Show an "No transactions found" message if the list is empty.

**FR-FM-010: Low Balance Alerts**  
**Priority:** Medium  
**Description:** The system shall identify and highlight users whose balance has fallen below a warning threshold.  
**Inputs:** Configurable threshold value (e.g., 50).  
**Processing:**  
1. Periodically (e.g., each time the manager dashboard loads) query `UserProfile` where `balance < THRESHOLD` and `meal_active = True`.  
2. Compile a list of these users.  
**Outputs:** Display the list of low‑balance users in a dedicated section of the manager dashboard.  
**Error Handling:** None specific.

**FR-FM-011: Auto Deactivation**  
**Priority:** High  
**Description:** To prevent debt, the system shall automatically disable meal service for any user whose balance reaches or falls below zero.  
**Inputs:** User's balance (checked during balance update operations or periodically).  
**Processing:**  
1. After any operation that updates a user's balance (deduction, recharge), check if the new `balance <= 0`.  
2. If true, and if the user's `meal_active` status is currently `True`, set `meal_active = False`.  
3. Save the `UserProfile` and optionally log this action.  
**Outputs:** The user's meal status becomes "Inactive". A warning can be displayed on their next login.  
**Error Handling:** Ensure this logic does not create infinite loops (e.g., deactivation should not trigger another balance check that causes further action).

#### 6.1.4 Notice Management Module

**FR-NM-001: Create Notice**  
**Priority:** High  
**Description:** Dining managers shall publish notices to all users.  
**Inputs:** Notice title, detailed description, optional file attachment.  
**Processing:**  
1. Verify the user is a dining manager.  
2. Validate the attached file's type and size (if present).  
3. Create a `Notice` object, saving the title, description, current timestamp, and the attachment file path.  
4. Save the uploaded file to a secure location (e.g., `media/notices/attachments/`).  
**Outputs:** The notice is saved and immediately appears in the notice list. A confirmation message is shown.  
**Error Handling:** Display errors for invalid file types or oversized files. Handle file‑upload failures gracefully.

**FR-NM-002: List Notices**  
**Priority:** High  
**Description:** All users shall see a chronological list of published notices.  
**Inputs:** None – this is a public or authenticated view.  
**Processing:**  
1. Query all `Notice` objects from the database.  
2. Order them by the `date` field in descending order (newest first).  
3. Apply pagination to limit the number of notices per page.  
**Outputs:** A paginated list showing notice titles, creation dates, and perhaps a short excerpt.  
**Error Handling:** Display a friendly message like "No notices have been posted yet" if the list is empty.

**FR-NM-003: View Notice Details**  
**Priority:** Medium  
**Description:** Clicking on a notice in the list shall display its full content.  
**Inputs:** The unique ID of the selected notice.  
**Processing:**  
1. Retrieve the `Notice` object with the given ID from the database.  
2. Render a template that displays the title, full description, date, and, if an attachment exists, a download link.  
**Outputs:** A dedicated page showing the complete notice.  
**Error Handling:** If the notice ID is invalid (does not exist), return an HTTP 404 "Not Found" error.

**FR-NM-004: Edit Notice**  
**Priority:** Medium  
**Description:** Managers shall be able to modify existing notices.  
**Inputs:** Notice ID and updated fields (title, description, possibly a new attachment).  
**Processing:**  
1. Verify manager privileges.  
2. Fetch the existing `Notice` object.  
3. Update its fields with the new data. If a new attachment is provided, replace the old file (and delete the old file from storage). Update the timestamp.  
4. Save the notice.  
**Outputs:** The notice is updated. Users viewing it will see the new content. A confirmation is shown to the manager.  
**Error Handling:** Similar to creation: validate new attachments, handle file‑system errors.

**FR-NM-005: Delete Notice**  
**Priority:** Medium  
**Description:** Managers shall be able to permanently remove notices.  
**Inputs:** Notice ID and a confirmation of the delete action (to prevent accidents).  
**Processing:**  
1. Verify manager privileges.  
2. Fetch the `Notice` object.  
3. If an attachment exists, delete the associated file from the filesystem.  
4. Delete the `Notice` object from the database.  
**Outputs:** The notice is removed from the list and is no longer accessible. A confirmation message is shown.  
**Error Handling:** Use a confirmation dialog or a two‑step process to prevent accidental deletion.

**FR-NM-006: Download Attachment**  
**Priority:** Medium  
**Description:** Users shall be able to download files attached to notices.  
**Inputs:** The filename or path of the attachment.  
**Processing:**  
1. Verify the file exists on the server's filesystem (or in cloud storage).  
2. Serve the file using Django's `FileResponse` with `as_attachment=True`, which prompts the user to save the file.  
3. Set appropriate HTTP headers (Content‑Type, Content‑Disposition).  
**Outputs:** The user's browser downloads the file.  
**Error Handling:** If the file is missing, return an HTTP 404 error.

#### 6.1.5 Feast Management Module

**FR-FT-001: Create Feast**  
**Priority:** Medium  
**Description:** Managers shall announce special feast events.  
**Inputs:** Feast title, description, date, meal time (e.g., "Dinner").  
**Processing:**  
1. Verify manager privileges.  
2. Create a `Feast` object, populating the fields and setting `created_by` to the current manager and `created_at` to the current time.  
**Outputs:** The feast is saved and appears in the feast list. A confirmation is shown.  
**Error Handling:** Validate the date format and ensure the date is in the future (or allow past feasts for record‑keeping).

**FR-FT-002: List Feasts**  
**Priority:** Medium  
**Description:** All users shall see a list of upcoming and past feasts.  
**Inputs:** None.  
**Processing:**  
1. Query all `Feast` objects.  
2. Order them by `date` (typically descending to show upcoming ones first, or ascending for a timeline).  
**Outputs:** A list displaying feast title, date, meal time, and a short description excerpt.  
**Error Handling:** Show "No feasts scheduled" if the list is empty.

**FR-FT-003: Request Guest for Feast**  
**Priority:** Medium  
**Description:** Residents shall be able to request permission to bring a guest to a feast.  
**Inputs:** Feast ID, guest's name, guest's mobile number, requester's name, requester's mobile number.  
**Processing:**  
1. Create a `GuestFeastRequest` object linked to the specified feast.  
2. Populate the guest and requester details.  
3. Set `status='pending'` and `requested_at` to the current time.  
**Outputs:** The request is submitted. A confirmation message informs the user that their request is pending approval.  
**Error Handling:** Validate phone number formats. Ensure the feast exists.

**FR-FT-004: View Guest Requests**  
**Priority:** Medium  
**Description:** Managers shall see all pending and processed guest requests.  
**Inputs:** None (manager view).  
**Processing:**  
1. Verify manager privileges.  
2. Query all `GuestFeastRequest` objects, optionally prefetching related `Feast` details.  
3. Order by `requested_at` descending (newest requests first).  
**Outputs:** A table listing requests, showing guest name, feast details, requester, date of request, and current status.  
**Error Handling:** None specific.

**FR-FT-005: Update Request Status**  
**Priority:** Medium  
**Description:** Managers shall approve or reject guest feast requests.  
**Inputs:** The ID of the `GuestFeastRequest` and the new status ("approved" or "rejected").  
**Processing:**  
1. Verify manager privileges.  
2. Fetch the `GuestFeastRequest` object.  
3. Update its `status` field to the new value.  
4. Save the object.  
**Outputs:** The request's status is updated in the database and reflected in the manager's view. A confirmation message is shown.  
**Error Handling:** Validate that the new status is one of the allowed choices.

#### 6.1.6 Complaint Management Module

**FR-CM-001: File Complaint**  
**Priority:** High  
**Description:** Residents shall be able to submit formal complaints regarding dining services.  
**Inputs:** Complaint title and a detailed description.  
**Processing:**  
1. Create a `Complaint` object.  
2. Set `user` to the currently logged‑in resident.  
3. Set `status='pending'` and `created_at` to the current time.  
4. Save the complaint.  
**Outputs:** The complaint is recorded. A confirmation message thanks the user and informs them that management will review it.  
**Error Handling:** Validate that title and description are not empty.

**FR-CM-002: View Own Complaints**  
**Priority:** Medium  
**Description:** Residents shall see a history of complaints they have filed.  
**Inputs:** The current user's ID.  
**Processing:**  
1. Query the `Complaint` model, filtering by `user_id` equal to the current user's ID.  
2. Order results by `created_at` descending.  
**Outputs:** A list showing the complaint title, submission date, and current status.  
**Error Handling:** Show "You haven't filed any complaints" if the list is empty.

**FR-CM-003: View All Complaints**  
**Priority:** High  
**Description:** Dining managers shall see all complaints submitted by all residents.  
**Inputs:** None (manager view).  
**Processing:**  
1. Verify manager privileges.  
2. Query all `Complaint` objects, optionally selecting related `User` information to show who filed it.  
3. Order by `created_at` descending.  
**Outputs:** A comprehensive list of all complaints for managerial review.  
**Error Handling:** None specific.

**FR-CM-004: Update Complaint Status**  
**Priority:** High  
**Description:** Managers shall resolve complaints and provide feedback.  
**Inputs:** Complaint ID, new status ("resolved", "rejected"), and an optional response text.  
**Processing:**  
1. Verify manager privileges.  
2. Fetch the `Complaint` object.  
3. Update the `status` field.  
4. If response text is provided, update the `response` field.  
5. Save the complaint.  
**Outputs:** The complaint's status and response are updated. The resident will see the update when they view their complaint.  
**Error Handling:** Ensure the new status is valid. Validate that a response is provided when marking as "resolved" or "rejected".

**FR-CM-005: Complaint Statistics**  
**Priority:** Low  
**Description:** The manager dashboard shall display a count of pending complaints.  
**Inputs:** None.  
**Processing:**  
1. Count the number of `Complaint` objects where `status='pending'`.  
**Outputs:** A badge or number displayed on the manager dashboard.  
**Error Handling:** None.

#### 6.1.7 Search and Filter Module

**FR-SF-001: User Search**  
**Priority:** High  
**Description:** Managers shall quickly locate users by various criteria.  
**Inputs:** A search query string (could be part of a name, room number, or mobile).  
**Processing:**  
1. Perform a case‑insensitive search across `UserProfile` fields (`room_number`, `user__first_name`, `user__last_name`, `mobile_number`) using Django's `Q` objects for OR conditions.  
2. Return matching users.  
**Outputs:** A dynamically updated list of users matching the search term.  
**Error Handling:** If the search query is empty, return all users or a default subset.

**FR-SF-002: Active User Filter**  
**Priority:** Medium  
**Description:** Managers shall isolate users who currently have active meal service for daily tracking.  
**Inputs:** Optional search query within active users.  
**Processing:**  
1. Base query: `UserProfile.objects.filter(meal_active=True)`.  
2. If a search query is provided, apply the same search logic (FR-SF-001) to this filtered queryset.  
**Outputs:** A list of only active users, potentially filtered further by search.  
**Error Handling:** None.

**FR-SF-003: Low Balance Filter**  
**Priority:** Low  
**Description:** System shall provide a list of users with balance below a threshold.  
**Inputs:** Threshold value (default 50).  
**Processing:**  
1. Query: `UserProfile.objects.filter(balance__lt=threshold, meal_active=True)`.  
**Outputs:** A list of users needing a balance recharge.  
**Error Handling:** None.

**FR-SF-004: Inactive User Filter**  
**Priority:** Low  
**Description:** System shall list users whose meal service is currently inactive.  
**Inputs:** None.  
**Processing:**  
1. Query: `UserProfile.objects.filter(meal_active=False)`.  
**Outputs:** A list of inactive users.  
**Error Handling:** None.

#### 6.1.8 Dashboard Module

**FR-DB-001: User Dashboard**  
**Priority:** High  
**Description:** The resident's landing page after login shall present all key information at a glance.  
**Inputs:** The current authenticated user.  
**Processing:**  
1. Load the user's `UserProfile`.  
2. Fetch today's `MealRecord` objects for noon and dinner.  
3. Calculate monthly meal count and cost (see FR-FM-004).  
4. Retrieve the current applicable `MealRate`.  
5. Determine meal status (Active/Inactive) and current balance.  
**Outputs:** A visually organized dashboard displaying all this information in clearly labeled sections or cards.  
**Error Handling:** Gracefully handle missing data (e.g., no meal records for today, no rate set) by showing default/placeholder values.

**FR-DB-002: Manager Dashboard**  
**Priority:** High  
**Description:** The manager's central hub shall provide an overview of system state and quick access to tasks.  
**Inputs:** The current manager user.  
**Processing:**  
1. Load lists of all users and active users.  
2. Count pending `GuestFeastRequest` and pending `Complaint` objects.  
3. Calculate today's total meals taken (sum of `meal_count` for today's taken records).  
4. Identify low‑balance users (FR-FM-010).  
5. List inactive users.  
**Outputs:** A dashboard with statistics cards, search bar, active‑user tracking table, and quick‑action buttons/links.  
**Error Handling:** Handle empty datasets, showing zero counts and empty lists where appropriate.

**FR-DB-003: Today's Meal Status**  
**Priority:** High  
**Description:** Both dashboards shall visually indicate whether today's noon and dinner meals have been taken.  
**Inputs:** Current user and today's date.  
**Processing:**  
1. Query for a `MealRecord` with `meal_type='noon'` and `date=today`. Check its `taken` and `requested_for_night` flags.  
2. Query for a `MealRecord` with `meal_type='dinner'` and `date=today`. Check its `taken` flag.  
**Outputs:** Visual indicators (e.g., green checkmark for taken, red cross for not taken, clock icon for requested for night) next to "Noon" and "Dinner" labels.  
**Error Handling:** If no record exists for a meal type, treat it as "not taken".

**FR-DB-004: User Details Modal**  
**Priority:** Medium  
**Description:** Managers shall be able to view expanded details for a user without leaving the dashboard.  
**Inputs:** User ID (triggered by clicking a user's name).  
**Processing:**  
1. Fetch the `User` and `UserProfile` data for the given ID.  
2. Calculate their monthly meal statistics and cost.  
3. Return this data in a structured format (JSON).  
**Outputs:** A modal (pop‑up) window displaying the detailed user information.  
**Error Handling:** If the user ID is invalid, return a JSON error response.

### 6.2 Interface Requirements

#### 6.2.1 User Interfaces

**UI-001: Login Page**  
A clean, centered form with fields for Username and Password. It will include a "Login" button and a link for new users to "Register". The page will be fully responsive.

**UI-002: Registration Page**  
A form collecting all required registration data: Username, Email, Password, Confirm Password, First Name, Last Name, Room Number, Mobile Number. It will have a "Register" button and a link to go back to the Login page. Real‑time validation (e.g., password strength, username availability) may be implemented.

**UI-003: User Dashboard**  
The resident's primary interface, organized into sections:
-   **Profile Summary Card:** Showing balance, room number, meal status (with toggle button), and meal type.
-   **Today's Meal Status Card:** With clear buttons to "Mark Noon Meal", "Request Noon for Night", and "Mark Dinner". Visual indicators show the current state.
-   **Monthly Statistics Card:** Displaying meals taken this month and the estimated cost.
-   **Quick Links:** To notices, complaints, and feast list.

**UI-004: Manager Dashboard**  
The administrator's control panel:
-   **Top Bar:** Search input for finding users quickly.
-   **Statistics Cards:** Displaying counts for total users, active users, pending requests, pending complaints, low‑balance users.
-   **Active Users Tracking Table:** A table listing all active users with checkboxes to mark noon/dinner meals in real‑time. Includes user name, room, balance, and meal status toggle.
-   **Management Panels:** Tabs or sections for managing notices, feasts, complaints, and financial reports.

**UI-005: Notice Board**  
A public/list view showing notices in reverse chronological order. Each notice in the list shows its title, date, and a short preview. Clicking a notice leads to a detail view showing the full text and an attachment download link. Managers will see "Create", "Edit", and "Delete" buttons.

**UI-006: Complaint System**  
For residents: A form to file a complaint and a list of their own complaints with status badges (Pending, Resolved, Rejected).  
For managers: A list of all complaints with action buttons to update status and add responses. A detail view shows the full complaint and the manager's response.

#### 6.2.2 Hardware Interfaces
-   **Client Devices:** The system is accessed via standard desktop computers, laptops, tablets, and smartphones with modern web browsers.
-   **Server Hardware:** A typical web server with minimum specifications of 2GB RAM, 2 CPU cores, and 20GB of storage is sufficient for initial deployment.
-   **Storage:** Adequate disk space for the application code, database, and uploaded media files. A minimum of 10GB is recommended.
-   **Network:** Requires a stable broadband internet connection for the server and client devices.

#### 6.2.3 Software Interfaces

**Database Interface**
-   **System:** SQLite3 (development), PostgreSQL or MySQL (production).
-   **Communication:** Django ORM provides the interface, translating Python code into SQL.
-   **Data Format:** Standard relational database tables as defined in the models.

**File System Interface**
-   **Media Storage:** Local filesystem for development; configurable to use cloud storage (Amazon S3, Google Cloud Storage) for production.
-   **Path:** Uploaded files are stored under a configurable `MEDIA_ROOT` (e.g., `/app/media/`).
-   **Operations:** The system performs create (upload), read (download), and delete operations on files.

**Email Interface (Future)**
-   **Service:** An external SMTP server (e.g., Gmail, SendGrid, institutional mail server).
-   **Purpose:** Sending notifications (low‑balance alerts, complaint updates).
-   **Protocol:** SMTP with TLS encryption.

#### 6.2.4 Communications Interfaces

**HTTP/HTTPS**
-   **Protocol:** HTTP/1.1 for development; HTTPS (HTTP over TLS) is mandatory for production.
-   **Methods:** Primary use of GET (retrieve data) and POST (submit data) methods.
-   **Format:** Responses are primarily HTML for web pages and JSON for API endpoints.

**REST API**
-   **Data Format:** JSON (JavaScript Object Notation).
-   **Authentication:** JWT (JSON Web Tokens) passed in the `Authorization` header as `Bearer <token>`.
-   **Content‑Type:** `application/json` for request and response bodies.
-   **CORS:** Enabled for specific front‑end origins to allow safe cross‑domain requests from future mobile apps.

### 6.3 System Features

#### 6.3.1 Dual Meal Payment System
A core innovation of this system is the "full‑day meal" concept. Users mark each meal (noon and dinner) independently, but the financial transaction occurs only once per day, triggered when *both* meals are marked. This model:
-   Simplifies accounting by creating one daily transaction instead of two.
-   Encourages residents to take both meals from the hall.
-   Handles the special case of "noon meal for night pickup" seamlessly by processing a double deduction when dinner is marked.

#### 6.3.2 Flexible Meal Types
The system accommodates different user needs:
-   **Full Meal:** Standard plan for users taking both meals regularly.
-   **Half Meal:** Discounted plan, likely for users who only take one meal per day or have smaller portions.
-   Managers can set and change these rates independently, with the system automatically applying the correct rate based on the user's profile.

#### 6.3.3 Manager Control System
Managers have a powerful, real‑time interface for daily operations:
-   View all active users on a single screen.
-   Mark meals for users with a single click, which instantly updates balances.
-   Comprehensive search and filtering to quickly find any user.
-   Oversight of all financial inflows (recharges) and outflows (deductions, expenses).

#### 6.3.4 Automatic Balance Management
The system enforces financial discipline automatically:
-   Meal service is automatically suspended when a user's balance hits zero, preventing debt.
-   Low‑balance warnings help managers proactively engage with users.
-   All balance updates are immediate and recorded in an immutable transaction log.

#### 6.3.5 Communication Platform
The system integrates several communication channels:
-   A **digital notice board** replaces physical posters, ensuring all residents see announcements.
-   A structured **complaint system** ensures user feedback is logged, tracked, and resolved.
-   **Feast management** allows for planning special events and managing guest invitations formally.

---

## 7. System Models

### 7.1 Use Case Diagrams

#### 7.1.1 User Management Use Cases
```
                             ┌─────────────────────┐
                             │   User Management   │
                             │       System        │
                             └─────────────────────┘
                                        │
        ┌──────────────────────────────────────────────────┐
        │                                                  │
        │                                                  │
┌───────▼───────┐                                ┌─────────▼─────────┐
│   Register    │                                │       Login       │
└───────────────┘                                └───────────────────┘
        │                                                  │
        │                                                  │
        │                                                  │
┌───────▼───────┐                                ┌─────────▼─────────┐
│ Update Profile│                                │   Change Password │
└───────────────┘                                └───────────────────┘
        │                                                  │
        └──────────────────────────────────────────────────┘
                                        │
                              ┌─────────▼─────────┐
                              │       User        │
                              └───────────────────┘
```

#### 7.1.2 Meal Management Use Cases
```
                           ┌─────────────────────┐
                           │   Meal Management   │
                           │       System        │
                           └─────────────────────┘
                                      │
        ┌─────────────────────────────────────────────────────┐
        │                                                     │
┌───────▼───────┐                                   ┌────────▼────────┐
│Toggle Meal    │                                   │ Mark Noon Meal  │
│Status         │                                   │                 │
└───────────────┘                                   └─────────────────┘
        │                                                     │
        │                                                     │
┌───────▼───────┐                                   ┌────────▼────────┐
│Request Meal   │                                   │   Mark Dinner   │
│for Night      │                                   │                 │
└───────────────┘                                   └─────────────────┘
        │                                                     │
        │                   For Residents                     │
        └─────────────────────────────────────────────────────┘
                                      │
                                      │
        ┌─────────────────────────────────────────────────────┐
        │                                                     │
┌───────▼───────┐                                   ┌────────▼────────┐
│Track User     │                                   │ Toggle User Meal│
│Meals          │                                   │ Status          │
└───────────────┘                                   └─────────────────┘
        │                                                     │
        │                  For Managers                       │
        └─────────────────────────────────────────────────────┘
                                      │
                              ┌───────▼───────┐
                              │ Auto Deduct   │
                              │ Meal Cost     │
                              └───────────────┘
```

#### 7.1.3 Financial Management Use Cases
```
                          ┌─────────────────────┐
                          │    Financial        │
                          │   Management        │
                          │     System          │
                          └─────────────────────┘
                                     │
        ┌─────────────────────────────────────────────────────┐
        │                                                     │
┌───────▼───────┐                                   ┌────────▼────────┐
│  View Balance │                                   │View Transaction │
│               │                                   │History          │
└───────────────┘                                   └─────────────────┘
        │                                                     │
        │                 For Residents                       │
        └─────────────────────────────────────────────────────┘
                                     │
                                     │
        ┌─────────────────────────────────────────────────────┐
        │                                                     │
┌───────▼───────┐                                   ┌────────▼────────┐
│ Recharge      │                                   │  Set Meal Rates │
│ Account       │                                   │                 │
└───────────────┘                                   └─────────────────┘
        │                                                     │
        │                 For Managers                       │
        └─────────────────────────────────────────────────────┘
                                     │
                             ┌───────▼───────┐
                             │ Process Meal  │
                             │ Deduction     │
                             └───────┬───────┘
                                     │
                             ┌───────▼───────┐
                             │ Auto Deactivate│
                             │ Low Balance   │
                             └───────────────┘
```

### 7.2 Sequence Diagrams

#### 7.2.1 User Login Sequence
```
Resident         Web Browser      Django View      Auth System      Database
   │                  │                │               │               │
   │  1. Visit login  │                │               │               │
   │─────────────────►│                │               │               │
   │                  │ 2. Display form│               │               │
   │◄─────────────────│                │               │               │
   │                  │                │               │               │
   │  3. Submit creds │                │               │               │
   │─────────────────►│ 4. Login POST  │               │               │
   │                  │───────────────►│ 5. Authenticate│              │
   │                  │                │──────────────►│               │
   │                  │                │               │ 6. Query user │
   │                  │                │               │──────────────►│
   │                  │                │               │ 7. User data  │
   │                  │                │               │◄──────────────│
   │                  │                │ 8. Verify pwd │               │
   │                  │                │◄──────────────│               │
   │                  │                │               │               │
   │                  │                │ 9. Create session             │
   │                  │                │──────────────────────────────►│
   │                  │                │               │               │
   │                  │ 10. Redirect   │               │               │
   │                  │◄───────────────│               │               │
   │  11. Dashboard   │                │               │               │
   │◄─────────────────│                │               │               │
```

#### 7.2.2 Mark Meal Sequence (Both Meals)
```
Resident    Browser    Django View    Models Layer    Database
   │           │            │              │             │
   │ 1. Mark   │            │              │             │
   │   noon    │            │              │             │
   │──────────►│ 2. POST    │              │             │
   │           │───────────►│ 3. Check     │             │
   │           │            │   active     │             │
   │           │            │─────────────►│ 4. Query    │
   │           │            │              │────────────►│
   │           │            │              │ 5. Profile  │
   │           │            │              │◄────────────│
   │           │            │ 6. Create    │             │
   │           │            │   noon record│             │
   │           │            │─────────────►│ 7. Save     │
   │           │            │              │────────────►│
   │           │ 8. Success │              │             │
   │           │◄───────────│              │             │
   │ 9. Confirm│            │              │             │
   │◄──────────│            │              │             │
   │           │            │              │             │
   │ 10. Mark  │            │              │             │
   │    dinner │            │              │             │
   │──────────►│ 11. POST   │              │             │
   │           │───────────►│ 12. Check    │             │
   │           │            │    both meals│             │
   │           │            │─────────────►│ 13. Query   │
   │           │            │              │────────────►│
   │           │            │              │ 14. Records │
   │           │            │              │◄────────────│
   │           │            │ 15. Both     │             │
   │           │            │    taken!    │             │
   │           │            │              │             │
   │           │            │ 16. Deduct   │             │
   │           │            │    balance   │             │
   │           │            │─────────────►│ 17. Update  │
   │           │            │              │────────────►│
   │           │            │              │             │
   │           │            │ 18. Create   │             │
   │           │            │    transaction│            │
   │           │            │─────────────►│ 19. Save    │
   │           │            │              │────────────►│
   │           │ 20. Success│              │             │
   │           │    + balance│             │             │
   │           │◄───────────│              │             │
   │ 21. Confirm│           │              │             │
   │    + new   │           │              │             │
   │    balance │           │              │             │
   │◄───────────│           │              │             │
```

#### 7.2.3 Manager Recharge Sequence
```
Manager     Browser    Django View    Models Layer    Database
   │           │            │              │             │
   │ 1. Select │            │              │             │
   │   user    │            │              │             │
   │──────────►│ 2. Show    │              │             │
   │           │   recharge │              │             │
   │           │   form     │              │             │
   │◄──────────│            │              │             │
   │           │            │              │             │
   │ 3. Enter  │            │              │             │
   │   amount  │            │              │             │
   │──────────►│ 4. POST    │              │             │
   │           │───────────►│ 5. Validate  │             │
   │           │            │   manager    │             │
   │           │            │─────────────►│             │
   │           │            │              │             │
   │           │            │ 6. Create    │             │
   │           │            │   transaction│             │
   │           │            │─────────────►│ 7. Save     │
   │           │            │              │────────────►│
   │           │            │              │             │
   │           │            │ 8. Update    │             │
   │           │            │   balance    │             │
   │           │            │─────────────►│ 9. Update   │
   │           │            │              │────────────►│
   │           │ 10. Success│              │             │
   │           │◄───────────│              │             │
   │ 11. Confirm│           │              │             │
   │◄───────────│           │              │             │
```

### 7.3 State Diagrams

#### 7.3.1 Meal Status State Diagram
```
                ┌─────────────┐
                │  Inactive   │◄──┐
                └──────┬──────┘   │
                       │          │
             Toggle    │    Auto-deactivate
             (User)    │    (Balance ≤ 0)
                       │          │
                       ▼          │
                ┌─────────────┐   │
                │   Active    │───┘
                └──────┬──────┘
                       │
               Mark    │
               meal    │
                       │
                       ▼
                ┌─────────────┐
                │ Processing  │
                │  Deduction  │
                └──────┬──────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
Sufficient      Insufficient    Both meals
balance         balance         not taken
        │              │              │
        ▼              ▼              ▼
 ┌──────────┐   ┌──────────┐  ┌──────────┐
 │ Deducted │   │ Warning  │  │  Waiting │
 └──────────┘   └──────────┘  └──────────┘
```

#### 7.3.2 Complaint Status State Diagram
```
                ┌─────────────┐
                │   Pending   │
                │  (Filed)    │
                └──────┬──────┘
                       │
     ┌─────────────────┼─────────────────┐
     │                 │                 │
Manager            Manager          Manager
reviews            responds         rejects
     │                 │                 │
     ▼                 ▼                 ▼
┌──────────┐      ┌──────────┐     ┌──────────┐
│Under     │      │Resolved  │     │Rejected  │
│Review    │      └──────────┘     └──────────┘
└────┬─────┘
     │
     │ Manager
     │ resolves
     ▼
┌──────────┐
│Resolved  │
└──────────┘
```

### 7.4 Activity Diagrams

#### 7.4.1 Daily Meal Process Activity Diagram
```
        START
          │
          ▼
    ┌──────────────┐
    │User navigates│
    │to dashboard  │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │Check meal    │
    │status        │
    └──────┬───────┘
           │
    ┌──────┴──────┐
    │  Active?    │
    └──────┬──────┘
    No     │     Yes
           │        │
           │        ▼
           │  ┌──────────────┐
           │  │Mark noon meal│
           │  └──────┬───────┘
           │         │
           │         ▼
           │  ┌──────────────┐
           │  │Record saved  │
           │  └──────┬───────┘
           │         │
           │         ▼
           │  ┌──────────────┐
           │  │Evening: Mark │
           │  │dinner        │
           │  └──────┬───────┘
           │         │
           │         ▼
           │  ┌──────────────┐
           │  │Check: Both   │
           │  │meals taken?  │
           │  └──────┬───────┘
           │    Yes  │   No
           │    │    │
           │    │    ▼
           │    │  ┌──────────────┐
           │    │  │Wait for      │
           │    │  │other meal    │
           │    │  └──────────────┘
           │    │
           │    ▼
           │  ┌──────────────┐
           │  │Check balance │
           │  └──────┬───────┘
           │         │
           │    ┌────┴────┐
           │    │Sufficient│
           │    └────┬────┘
           │    Yes  │   No
           │    │    │
           │    │    ▼
           │    │  ┌──────────────┐
           │    │  │Show error    │
           │    │  │No deduction  │
           │    │  └──────────────┘
           │    │
           │    ▼
           │  ┌──────────────┐
           │  │Deduct meal   │
           │  │cost          │
           │  └──────┬───────┘
           │         │
           │         ▼
           │  ┌──────────────┐
           │  │Create        │
           │  │transaction   │
           │  └──────┬───────┘
           │         │
           │         ▼
           │  ┌──────────────┐
           │  │Update balance│
           │  └──────┬───────┘
           │         │
           └─────────┼─────────┐
                     │         │
                     ▼         ▼
               ┌────────────────┐
               │Show result to  │
               │user            │
               └────────┬───────┘
                        │
                        ▼
                       END
```

### 7.5 Data Flow Diagrams

#### 7.5.1 Level 0 DFD (Context Diagram)
```
                ┌──────────────────┐
                │                  │
┌───────────────┤  Hall Dining     ├───────────────┐
│               │  Management      │               │
│               │  System          │               │
│               └──────────────────┘               │
│                                                   │
│                                                   │
┌───▼────┐                                         ┌───▼────┐
│        │  Login, Meal marking, Balance check    │        │
│Resident│────────────────────────────────────────►│ System │
│        │◄────────────────────────────────────────│        │
└────────┘  Dashboard, Transactions, Notices      └────────┘
                     ▲
                     │
┌─────────┐          │
│         │  User management, Recharge, Reports   │
│ Manager │───────────────────────────────────────┘
│         │◄───────────────────────────────────────
└─────────┘  User data, Financial data, Statistics
```

#### 7.5.2 Level 1 DFD
```
┌─────────┐           meal_marking          ┌───────────────┐
│Resident │──────────────────────────────────►│               │
│         │           balance_check           │  Process Meal │
│         │◄──────────────────────────────────│  Management   │
└─────────┘                                   │               │
                                              └───────┬───────┘
                                                      │
                                               meal_records
                                                      │
                                                      ▼
┌─────────┐           recharge_request       ┌───────────────┐
│Manager  │──────────────────────────────────►│               │
│         │           user_data               │   Process     │
│         │◄──────────────────────────────────│   Financial   │
└─────────┘                                   │   Management  │
                                              │               │
                                              └───────┬───────┘
                                                      │
                                               transactions
                                                      │
                                                      ▼
┌─────────┐           notice_create          ┌───────────────┐
│Manager  │──────────────────────────────────►│               │
│         │           notices                 │   Manage      │
│Resident │◄──────────────────────────────────│   Communication│
└─────────┘                                   │               │
                                              └───────┬───────┘
                                                      │
                                            notices/complaints
                                                      │
                                                      ▼
                                              ┌───────────────┐
                                              │   Database    │
                                              └───────────────┘
```

### 7.6 Class Diagrams
*(Represented textually due to diagram constraints)*

**User (Django Built‑in)**
- `username: String`
- `email: String`
- `first_name: String`
- `last_name: String`
- `password: String`
- `is_active: Boolean`
- `date_joined: DateTime`
- `last_login: DateTime`
*Methods:*
- `get_full_name()`
- `check_password(raw_password)`

**UserProfile**
- `user: OneToOneField(User)`
- `room_number: CharField`
- `mobile_number: CharField`
- `balance: DecimalField`
- `meal_active: BooleanField`
- `is_dining_manager: BooleanField`
- `meal_type: CharField` (choices: 'full', 'half')
*Methods:*
- `get_meal_rate(): Decimal` (returns the current rate based on meal_type)
- `__str__()` (returns a readable representation)

**MealRecord**
- `user: ForeignKey(User)`
- `date: DateField`
- `meal_type: CharField` (choices: 'noon', 'dinner')
- `taken: BooleanField`
- `requested_for_night: BooleanField`
- `meal_count: DecimalField`
*Methods:*
- `__str__()`

**Transaction**
- `user: ForeignKey(User)`
- `amount: DecimalField`
- `transaction_type: CharField` (choices: 'recharge', 'deduction', 'refund', 'expense')
- `description: TextField`
- `created_by: ForeignKey(User)` (null=True, for system‑generated deductions)
- `created_at: DateTimeField`
*Methods:*
- `__str__()`

**MealRate**
- `full_meal_rate: DecimalField`
- `half_meal_rate: DecimalField`
- `effective_from: DateField`
*Methods:*
- `__str__()`

**Notice**
- `title: CharField`
- `description: TextField`
- `date: DateTimeField`
- `attachment: FileField` (optional)
*Methods:*
- `get_file_name(): String`
- `__str__()`

**Feast**
- `title: CharField`
- `description: TextField`
- `date: DateField`
- `meal_time: CharField`
- `created_by: ForeignKey(User)`
- `created_at: DateTimeField`
*Methods:*
- `__str__()`

**GuestFeastRequest**
- `feast: ForeignKey(Feast)`
- `guest_name: CharField`
- `guest_mobile: CharField`
- `requested_by_name: CharField`
- `requested_by_mobile: CharField`
- `requested_at: DateTimeField`
- `status: CharField` (choices: 'pending', 'approved', 'rejected')
*Methods:*
- `__str__()`

**Complaint**
- `user: ForeignKey(User)`
- `title: CharField`
- `description: TextField`
- `created_at: DateTimeField`
- `status: CharField` (choices: 'pending', 'resolved', 'rejected')
- `response: TextField` (blank=True)
*Methods:*
- `__str__()`

---

## 8. System Evolution

### 8.1 Anticipated Changes

#### 8.1.1 Short-term Evolution (0-6 months)
1.  **Email Notifications:** Implement automated email alerts for low balances, new notices, and updates to complaint status. Weekly meal‑summary emails could also be introduced.
2.  **Enhanced Reporting:** Add functionality to generate and download PDF reports for monthly financial statements, user meal consumption, and manager balance sheets.
3.  **Mobile Application:** Develop native Android and iOS applications that consume the existing REST API, providing push notifications and potentially QR‑code‑based meal scanning for faster check‑ins.
4.  **Payment Integration:** Integrate with a local online payment gateway (e.g., bKash, Nagad, bank portals) to allow residents to recharge their own accounts online, reducing the managerial workload.

#### 8.1.2 Medium-term Evolution (6-12 months)
1.  **Advanced Analytics:** Introduce dashboards with charts and graphs showing meal wastage trends, consumption patterns by day/week, and predictive analytics for meal planning.
2.  **Menu Management:** A module for dining managers to plan and publish weekly menus. Could include dietary tags (vegetarian, vegan) and allergen information.
3.  **Enhanced Guest Management:** A formal guest registration system with temporary access codes, differential pricing for guest meals, and a history of guests per resident.
4.  **Inventory Management:** Basic tracking of kitchen stock, linking ingredient usage to meals served, and generating purchase orders for suppliers.

#### 8.1.3 Long-term Evolution (12+ months)
1.  **AI/ML Integration:** Experiment with machine learning to predict daily meal attendance, optimize food preparation quantities to reduce waste, and even suggest menu items based on historical popularity.
2.  **Multi-hall Support:** Redesign the architecture to support multiple residential halls from a single centralized installation, with hall‑specific administrators and consolidated reporting for higher management.
3.  **Integration Ecosystem:** Develop APIs for integration with university‑wide student information systems (for automatic user synchronization), accounting software, and other campus management systems.
4.  **Advanced Social & Sustainability Features:** Introduce a meal‑feedback and rating system, "meal buddy" matching, and dashboards tracking the hall's carbon footprint or food‑waste reduction achievements.

### 8.2 Scalability Considerations

#### 8.2.1 Database Scalability
- The initial use of Django ORM with PostgreSQL provides a solid foundation. For multi‑hall deployment, database sharding strategies (sharding by hall_id) can be explored.
- Implementing read replicas can offload reporting and analytical queries from the primary transactional database.
- Connection pooling (e.g., via PgBouncer) will be essential for handling high concurrent connections efficiently.

#### 8.2.2 Application Scalability
- The stateless nature of the web application (with session data stored in the database or cache) allows for easy horizontal scaling. Multiple instances of the Django app can run behind a load balancer (Nginx, HAProxy).
- Introducing a caching layer (Redis or Memcached) for frequently accessed but rarely changed data (e.g., current meal rates, active user lists for the day) can dramatically improve response times.
- Static and media files should be served from a Content Delivery Network (CDN) or object storage (S3) to reduce load on application servers.

#### 8.2.3 Storage Scalability
- From the outset, the system should be configured to use external object storage (AWS S3, Google Cloud Storage, or a compatible MinIO instance) for media files. This separates storage scaling from application scaling.
- An automated data‑archiving policy should be defined to move old transaction and meal records to cheaper, long‑term storage or archive tables, keeping the operational database lean.

### 8.3 Maintenance Strategy

#### 8.3.1 Regular Maintenance Tasks
- **Daily:** Automated backups of the database. Verification of backup integrity.
- **Weekly:** Review of application and server logs for errors or suspicious activity. Cleanup of temporary files.
- **Monthly:** Application of security patches and updates to the operating system, Python, Django, and other dependencies.
- **Quarterly:** Performance review, including database query optimization and analysis of slow‑running pages.

#### 8.3.2 Update and Deployment Process
A structured CI/CD (Continuous Integration/Continuous Deployment) pipeline is recommended:
1.  **Development:** Features are developed on separate Git branches.
2.  **Testing:** Automated tests run on a staging server that mirrors production.
3.  **Staging:** Manual User Acceptance Testing (UAT) is performed by a select group of managers/residents.
4.  **Production Deployment:** Scheduled during low‑traffic periods. Use blue‑green deployment or rolling updates to minimize downtime.
5.  **Post‑deployment:** Monitor error rates and performance metrics closely for a defined period after release.
6.  **Rollback Plan:** A clear and tested procedure to revert to the previous version in case of critical issues.

#### 8.3.3 Monitoring
- **Infrastructure Monitoring:** CPU, memory, disk I/O, and network usage of servers.
- **Application Monitoring:** Response times, error rates (e.g., using Django's logging or tools like Sentry), and uptime.
- **Business Monitoring:** Key metrics like daily active users, meals served, recharge volume.
- **Database Monitoring:** Query performance, connection counts, and slow‑query logs.

### 8.4 Technology Upgrade Path

#### 8.4.1 Framework and Language Updates
- Adhere to Django's Long‑Term Support (LTS) release cycle for stability. Plan upgrades from one LTS version to the next during maintenance windows.
- Similarly, plan Python version upgrades in alignment with Django's support matrix and the end‑of‑life dates of Python releases.
- Use a dependency management tool (like `pip-tools` or `Poetry`) to keep third‑party packages updated and secure.

#### 8.4.2 Infrastructure Modernization
- **Containerization:** Package the application and its dependencies into Docker containers. This ensures consistency across development, testing, and production environments.
- **Orchestration:** For complex deployments, use an orchestration platform like Kubernetes to manage containerized application instances, scaling, and service discovery.
- **Infrastructure as Code (IaC):** Use tools like Terraform or Ansible to define and provision the server infrastructure, making deployments repeatable and version‑controlled.
- **Cloud Migration:** Have a documented strategy for migrating from on‑premise servers to a cloud provider (AWS, Google Cloud, Azure) to leverage managed services and global scalability.

---

## 9. Appendices

### 9.1 Appendix A: Database Schema
*(Complete SQL `CREATE TABLE` statements for the core models. Note: This is a representation; Django migrations generate the actual SQL.)*

#### 9.1.1 `auth_user` (Django Default)
```sql
CREATE TABLE auth_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME NULL,
    is_superuser BOOLEAN NOT NULL,
    username VARCHAR(150) NOT NULL UNIQUE,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined DATETIME NOT NULL
);
```

#### 9.1.2 `dining_userprofile`
```sql
CREATE TABLE dining_userprofile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    room_number VARCHAR(10) NOT NULL,
    mobile_number VARCHAR(15) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    meal_active BOOLEAN NOT NULL DEFAULT 1,
    is_dining_manager BOOLEAN NOT NULL DEFAULT 0,
    meal_type VARCHAR(10) NOT NULL DEFAULT 'full',
    FOREIGN KEY (user_id) REFERENCES auth_user (id) ON DELETE CASCADE
);
```

#### 9.1.3 `dining_mealrecord`
```sql
CREATE TABLE dining_mealrecord (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    meal_type VARCHAR(10) NOT NULL,
    taken BOOLEAN NOT NULL DEFAULT 0,
    requested_for_night BOOLEAN NOT NULL DEFAULT 0,
    meal_count DECIMAL(4, 2) NOT NULL DEFAULT 1.00,
    FOREIGN KEY (user_id) REFERENCES auth_user (id) ON DELETE CASCADE,
    UNIQUE(user_id, date, meal_type)
);
CREATE INDEX dining_mealrecord_user_id_date ON dining_mealrecord (user_id, date);
```

#### 9.1.4 `dining_transaction`
```sql
CREATE TABLE dining_transaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_type VARCHAR(20) NOT NULL,
    description TEXT,
    created_by_id INTEGER,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user (id) ON DELETE CASCADE,
    FOREIGN KEY (created_by_id) REFERENCES auth_user (id) ON DELETE SET NULL
);
CREATE INDEX dining_transaction_user_id ON dining_transaction (user_id);
CREATE INDEX dining_transaction_created_at ON dining_transaction (created_at);
```

#### 9.1.5 `dining_mealrate`
```sql
CREATE TABLE dining_mealrate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_meal_rate DECIMAL(10, 2) NOT NULL,
    half_meal_rate DECIMAL(10, 2) NOT NULL,
    effective_from DATE NOT NULL UNIQUE
);
```

#### 9.1.6 `dining_notice`
```sql
CREATE TABLE dining_notice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    date DATETIME NOT NULL,
    attachment VARCHAR(100)
);
CREATE INDEX dining_notice_date ON dining_notice (date);
```

#### 9.1.7 `dining_feast`
```sql
CREATE TABLE dining_feast (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    date DATE NOT NULL,
    meal_time VARCHAR(10) NOT NULL,
    created_by_id INTEGER NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (created_by_id) REFERENCES auth_user (id) ON DELETE CASCADE
);
CREATE INDEX dining_feast_date ON dining_feast (date);
```

#### 9.1.8 `dining_guestfeastrequest`
```sql
CREATE TABLE dining_guestfeastrequest (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feast_id INTEGER NOT NULL,
    guest_name VARCHAR(100) NOT NULL,
    guest_mobile VARCHAR(15) NOT NULL,
    requested_by_name VARCHAR(100) NOT NULL,
    requested_by_mobile VARCHAR(15) NOT NULL,
    requested_at DATETIME NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    FOREIGN KEY (feast_id) REFERENCES dining_feast (id) ON DELETE CASCADE
);
CREATE INDEX dining_guestfeastrequest_feast_id ON dining_guestfeastrequest (feast_id);
CREATE INDEX dining_guestfeastrequest_status ON dining_guestfeastrequest (status);
```

#### 9.1.9 `dining_complaint`
```sql
CREATE TABLE dining_complaint (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    response TEXT,
    FOREIGN KEY (user_id) REFERENCES auth_user (id) ON DELETE CASCADE
);
CREATE INDEX dining_complaint_user_id ON dining_complaint (user_id);
CREATE INDEX dining_complaint_status ON dining_complaint (status);
```

### 9.2 Appendix B: API Documentation

#### 9.2.1 Authentication Endpoints

**Endpoint:** `POST /api/token/`  
**Description:** Authenticates a user and returns a pair of JWT tokens (access and refresh).  
**Request Body (JSON):**
```json
{
    "username": "john_doe",
    "password": "securepassword123"
}
```
**Success Response (HTTP 200):**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```
**Error Response (HTTP 401):**
```json
{
    "detail": "No active account found with the given credentials"
}
```

**Endpoint:** `POST /api/token/refresh/`  
**Description:** Uses a valid refresh token to obtain a new access token.  
**Request Body (JSON):**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```
**Success Response (HTTP 200):**
```json
{
    "access": "new_access_token_here..."
}
```

#### 9.2.2 User Endpoints

**Endpoint:** `GET /api/users/`  
**Description:** Retrieves a paginated list of all users. **Manager access only.**  
**Headers:** `Authorization: Bearer <access_token>`  
**Query Parameters (optional):** `?search=101` (searches room, name, mobile)  
**Success Response (HTTP 200):**
```json
{
    "count": 150,
    "next": "http://api.example.com/api/users/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "john_doe",
            "email": "john@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "profile": {
                "room_number": "101",
                "mobile_number": "01712345678",
                "balance": "250.00",
                "meal_active": true,
                "meal_type": "full"
            }
        }
    ]
}
```

**Endpoint:** `GET /api/users/{id}/`  
**Description:** Retrieves details for a specific user. Users can only access their own data; managers can access any.  
**Headers:** `Authorization: Bearer <access_token>`  
**Success Response (HTTP 200):**
```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "profile": {
        "room_number": "101",
        "mobile_number": "01712345678",
        "balance": "250.00",
        "meal_active": true,
        "meal_type": "full"
    },
    "monthly_stats": {
        "meals_taken": 45,
        "total_cost": "2250.00"
    }
}
```

#### 9.2.3 Meal Record Endpoints

**Endpoint:** `GET /api/meal-records/`  
**Description:** Lists meal records. Filterable by user and date.  
**Headers:** `Authorization: Bearer <access_token>`  
**Query Parameters:** `?date=2026-01-15&user_id=1&meal_type=noon`  
**Success Response (HTTP 200):**
```json
{
    "count": 1,
    "results": [
        {
            "id": 1,
            "user": 1,
            "date": "2026-01-15",
            "meal_type": "noon",
            "taken": true,
            "requested_for_night": false,
            "meal_count": "1.00"
        }
    ]
}
```

**Endpoint:** `POST /api/meal-records/`  
**Description:** Creates a new meal record (i.e., marks a meal). Residents can only mark for themselves. Managers can mark for any user.  
**Headers:** `Authorization: Bearer <access_token>`  
**Request Body (JSON):**
```json
{
    "meal_type": "dinner",
    "requested_for_night": false
}
```
**Success Response (HTTP 201):**
```json
{
    "id": 2,
    "user": 1,
    "date": "2026-01-15",
    "meal_type": "dinner",
    "taken": true,
    "requested_for_night": false,
    "meal_count": "1.00"
}
```

#### 9.2.4 Notice Endpoints

**Endpoint:** `GET /api/notices/`  
**Description:** Lists all notices, newest first. Does not require authentication for reading.  
**Success Response (HTTP 200):**
```json
{
    "count": 5,
    "results": [
        {
            "id": 1,
            "title": "Holiday Feast Announcement",
            "description": "A special dinner will be served on...",
            "date": "2026-01-15T10:00:00Z",
            "attachment": "http://example.com/media/notices/feast_menu.pdf"
        }
    ]
}
```

### 9.3 Appendix C: Installation Guide

#### 9.3.1 Prerequisites
Ensure the following are installed on your development or server machine:
- **Python 3.8** or higher.
- **pip**, the Python package installer.
- **Git**, for cloning the repository.
- A **virtual environment** tool (`venv` is included with Python 3.3+).

#### 9.3.2 Step-by-Step Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourorganization/hall-dining-system.git
    cd hall-dining-system
    ```

2.  **Create and Activate a Virtual Environment**
    *On Linux/Mac:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *On Windows (Command Prompt):*
    ```bash
    python -m venv venv
    venv\Scripts\activate.bat
    ```
    *On Windows (PowerShell):*
    ```bash
    python -m venv venv
    venv\Scripts\Activate.ps1
    ```

3.  **Install Python Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Settings**
    Copy the example settings file and edit it with your specific configuration (database, secret key, etc.).
    ```bash
    cp Hall_dining/settings.example.py Hall_dining/settings.py
    # Use a text editor to modify settings.py
    ```

5.  **Apply Database Migrations**
    This creates the necessary database tables.
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser (Administrator)**
    Follow the prompts to create the first dining manager account.
    ```bash
    python manage.py createsuperuser
    ```

7.  **Collect Static Files**
    Gathers CSS, JavaScript, and images into a single directory for production serving.
    ```bash
    python manage.py collectstatic
    ```

8.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```
    The application will now be accessible at `http://127.0.0.1:8000/`. The admin panel is at `http://127.0.0.1:8000/admin/`.

### 9.4 Appendix D: Configuration Guide

#### 9.4.1 Database Configuration (Production)
In `Hall_dining/settings.py`, replace the SQLite configuration with PostgreSQL settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hall_dining_db',           # Database name
        'USER': 'hall_dining_user',         # Database user
        'PASSWORD': 'YourStrongPassword123', # Database password
        'HOST': 'localhost',                # Set to your DB server address
        'PORT': '5432',                     # Default PostgreSQL port
    }
}
```

#### 9.4.2 Media and Static Files
```python
# URL to use when referring to media files (attachments)
MEDIA_URL = '/media/'
# Filesystem path where media files will be stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL to use when referring to static files (CSS, JS)
STATIC_URL = '/static/'
# The absolute path to the directory where `collectstatic` will gather static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

#### 9.4.3 Email Configuration (For Future Notifications)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Or your institutional SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-app-specific-password'  # Use environment variables for security!
DEFAULT_FROM_EMAIL = 'Hall Dining <noreply@yourhall.edu>'
```

### 9.5 Appendix E: User Manual

#### 9.5.1 For Residents

**Getting Started**
1.  Navigate to the system's web address (provided by your hall).
2.  If you are a new user, click "Register" and fill out the form with your details (Username, Room Number, Mobile, etc.).
3.  After registration, use your username and password to log in.

**Using Your Dashboard**
After login, you will see your personal dashboard. Here you can:
-   See your **Current Balance** at the top.
-   Check your **Meal Status**: "Active" (green) means you can take meals. Click the button to toggle it on/off.
-   **Mark Meals**: For lunch, click "Mark Noon Meal". If you will pick up lunch at dinner, click "Request Noon Meal for Night". In the evening, click "Mark Dinner". **Remember:** Money is deducted only after *both* meals are marked.
-   View **Monthly Summary**: See how many meals you've taken this month and the estimated cost.
-   Read **Notices**: Click "Notices" in the menu to see all announcements from the hall office.
-   **File a Complaint**: If you have an issue, go to "Complaints", click "File New Complaint", describe the problem, and submit.

**Managing Your Account**
-   To update your phone number or switch between Full/Half meal plans, go to "My Profile".
-   To see all your financial transactions (recharges, meal deductions), go to "Transaction History".
-   If your balance is low, contact a dining manager in person for a recharge.

#### 9.5.2 For Dining Managers

**Access and Overview**
1.  Log in with your manager credentials.
2.  You will be taken to the **Manager Dashboard**, which is your command center.

**Key Tasks**
1.  **Daily Meal Tracking:**
    -   The main table shows all users with active meal service.
    -   Simply check the boxes under "Noon" and "Dinner" as users collect their meals.
    -   The system automatically deducts the cost and updates balances when both boxes for a user are checked.
    -   To unmark a meal (if there was a mistake), uncheck the box. The system will refund the amount.

2.  **Managing Users:**
    -   Use the **search bar** at the top to find any user by name, room, or mobile number.
    -   Click on a user's name to see their detailed profile, monthly stats, and transaction history.
    -   To **recharge** a user's account, find them, click "Recharge", enter the amount and a note, and confirm.
    -   You can also **toggle a user's meal status** (Active/Inactive) from their row in the table.

3.  **Financial Oversight:**
    -   The dashboard shows key financial totals: Total Recharges, Total Deductions, Manager Balance, etc.
    -   Go to "Financial Reports" for more detailed breakdowns and to set new meal rates.

4.  **Communication:**
    -   **Post a Notice:** Go to "Notices", click "Create Notice", add a title, description, and attach a file if needed.
    -   **Handle Complaints:** Go to "Complaints". View all submitted complaints. Update their status and add a response to resolve them.
    -   **Manage Feasts:** Announce special feasts under the "Feasts" section. Review and approve/reject guest requests from residents.

### 9.6 Appendix F: Troubleshooting Guide

#### 9.6.1 Common Issues and Solutions

| Issue | Possible Cause | Solution |
| :--- | :--- | :--- |
| **Cannot log in.** | Incorrect username/password. | Double‑check your credentials. Use the "Forgot Password?" link if enabled. Contact an administrator if locked out. |
| **"Meal already taken" error.** | Attempting to mark the same meal twice. | Refresh your dashboard. The meal should already be marked as taken. |
| **"Insufficient balance" error.** | Account balance is less than the meal cost. | Your meal service may be auto‑deactivated. Contact a manager to recharge your account. |
| **Checkbox in manager view doesn't update balance.** | Network delay or browser cache. | Refresh the page. Ensure you have a stable internet connection. Check the browser's developer console for JavaScript errors. |
| **File upload fails.** | File is too large (>10MB) or of an unsupported type. | Reduce the file size or convert it to a supported format (PDF, JPG, PNG, DOC). |
| **Page loads very slowly.** | High server load or network issue. | Try again later. Inform the system administrator if the problem persists. |

#### 9.6.2 Administrator Troubleshooting
-   **Database errors:** Check Django logs (`logs/` directory or server logs). Run `python manage.py check` to detect common issues.
-   **Email not sending:** Verify SMTP settings in `settings.py`. Check that the email service credentials are correct and that the server allows outgoing connections on port 587.
-   **Static files not loading (404):** Ensure the `STATIC_ROOT` is set correctly and the web server (Nginx/Apache) is configured to serve files from that location.
-   **User reports missing transaction:** Check the `dining_transaction` table directly via the Django admin panel or database client. Verify the user's meal records for the date in question.

### 9.7 Appendix G: Security Guidelines

#### 9.7.1 For All Users
-   **Password Security:** Choose a strong, unique password that you don't use elsewhere. A combination of letters, numbers, and symbols is recommended.
-   **Session Management:** Always log out when using a shared or public computer. Do not use the "Remember Me" feature on such devices.
-   **Phishing Awareness:** The hall management will never ask for your password via email or phone. Any official communication will come through the system's notice board.
-   **Data Privacy:** Do not share your login details with anyone. Your transaction history and meal records are confidential.

#### 9.7.2 For Dining Managers
-   **Account Privilege:** Manager accounts have full control over finances and user data. Protect your login credentials rigorously.
-   **Audit Trail:** Use the system's built‑in features for all actions (recharges, marking meals). Do not make manual adjustments outside the system, as this breaks the audit trail.
-   **Regular Reviews:** Periodically review the transaction logs and user activity for any anomalies.
-   **Software Updates:** Cooperate with the technical administrator to apply security updates to the system promptly.

### 9.8 Appendix H: Glossary of Terms
*(Consolidated from Section 3 for quick reference.)*

| Term | Definition |
| :--- | :--- |
| **Balance** | The amount of money remaining in a user's account, used to pay for meals. |
| **Deduction** | The automatic process of subtracting the cost of a meal from a user's balance. |
| **Dining Manager** | A staff member with administrative rights to manage all aspects of the dining system. |
| **Feast** | A special meal event announced by management. |
| **Full Meal** | The standard meal plan, costing the full meal rate. |
| **Guest Request** | A resident's formal request to bring an external guest to a feast. |
| **Half Meal** | A discounted meal plan for users with reduced requirements. |
| **Meal Active** | A status indicating a user is currently eligible to take and pay for meals. |
| **Meal Count** | The number of meal portions consumed, can be a decimal (e.g., 0.5, 2.0). |
| **Meal Rate** | The price of one meal, different for full and half plans. |
| **Notice** | An official announcement posted by hall management. |
| **Recharge** | The act of adding money to a user's account, performed by a manager. |
| **Transaction** | A permanent record of any financial activity (recharge, deduction, refund). |

---

## 10. Index

- **A**
    - API Documentation, 9.2
    - Architecture, 5.1
    - Authentication, 6.1.1
    - Auto Deactivation, FR-FM-011
- **B**
    - Balance Management, 6.1.4
    - Business Constraints, 2.6.3
- **C**
    - Class Diagrams, 7.6
    - Complaint Management, 6.1.6
    - Configuration Guide, 9.4
    - CORS, 5.3.4
- **D**
    - Dashboard, 6.1.8
    - Data Architecture, 5.2
    - Database Schema, 9.1
    - Design Constraints, 2.6
- **E**
    - Entity Relationship Diagram, 5.2.1
    - Error Handling, NFR-3.3
    - Evolution, 8.0
- **F**
    - Feast Management, 6.1.5
    - Financial Management, 6.1.4
    - Functional Requirements, 4.1
- **G**
    - Glossary, 3.0, 9.8
    - Guest Requests, FR-FT-003
- **H**
    - Hardware Interfaces, 6.2.2
- **I**
    - Installation Guide, 9.3
    - Interface Requirements, 6.2
- **J**
    - JWT Authentication, 5.3.4, 5.5.1
- **M**
    - Maintainability, NFR-5.0
    - Meal Management, 6.1.3
    - Meal Rate, FR-FM-005
    - Models (System), 7.0
- **N**
    - Non-Functional Requirements, 4.2
    - Notice Management, 6.1.4
- **P**
    - Performance Requirements, NFR-1.0
    - Profile Management, 6.1.2
- **R**
    - Recharge, FR-FM-001
    - Reliability, NFR-3.0
- **S**
    - Scalability, NFR-6.0, 8.2
    - Search and Filter, 6.1.7
    - Security, NFR-2.0, 5.4
    - Sequence Diagrams, 7.2
    - State Diagrams, 7.3
    - System Overview, 2.1
- **T**
    - Technology Stack, 5.3
    - Transaction, FR-FM-003
    - Troubleshooting, 9.6
- **U**
    - Usability, NFR-4.0
    - Use Case Diagrams, 7.1
    - User Management, 6.1.1
    - User Manual, 9.5

---

## Document Approval

| **Role** | **Name** | **Signature** | **Date** |
| :--- | :--- | :--- | :--- |
| Project Manager | | | |
| Lead Developer | | | |
| System Architect | | | |
| Quality Assurance Lead | | | |
| Client Representative (Hall Management) | | | |

---

## Revision History

| **Version** | **Date** | **Author** | **Description** |
| :--- | :--- | :--- | :--- |
| 1.0 | January 15, 2026 | Development Team | Initial release of the Software Requirements Specification. |

---

**End of Document**
