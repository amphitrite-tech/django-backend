    * User Authentication:
        Registration / Login (Django built-in authentication)
        Reset password
        No need for two-factor authentication

    * User Models:
        Captain
            Username
            Password
            Name
            Email
            Phone (optional)
            Metadata (to be defined)
            Assigned Ship (Foreign Key)
        Organization
            Name
            Responsible
            Contacts
            Number of Registered Ships
            IMO of ships
            Product Plan (Freemium, Paid)
        Ship
            IMO number
            Unique App Identifier
            Vessel Draft
            Vessel Power-Speed coefficient
            Type of ship
        Voyage
            Route segments (vectors)
            ETA for each segment and total ETA
            Ship speed for each segment and total ship speed
            Wind and wave conditions along each segment (vectors)
            Current impact along each segment (vectors)
            Start and end date
            Historical conditions (currents, wave, wind)

    * Database and Storage:
        Database: SQLite
        External storage (to be chosen when needed)

    * Frontend Interaction (RESTful API):
        User Authentication Endpoints (register, login, password reset)
        Voyage CRUD Endpoints (create, read, update, delete)
        Ship and Organization Endpoints (assign ships to captains, manage organization data)
        Parameter Storage Endpoints (store and retrieve user-defined parameters)
        Current Data File Upload and Retrieval Endpoints (upload and access current data files)
        Route Computation Endpoint (compute routes using parallel processing)

    * Performance and Monitoring:
        Fast response time for most requests (within seconds)
        Route computation within 1 minute using parallel processing
        Persistent logging of processes and errors
        Monitoring and analytics within the Django app

    * Miscellaneous:
        Future integration with Marine Traffic's API for AIS data (position, speed)
        Support for different file formats for current data files (choose most appropriate)