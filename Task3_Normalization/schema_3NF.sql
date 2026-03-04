CREATE TABLE Student (
  StudentID INT PRIMARY KEY,
  StudentName VARCHAR(50),
  Email VARCHAR(100)
);

CREATE TABLE Club (
  ClubID INT PRIMARY KEY,
  ClubName VARCHAR(50),
  ClubRoom VARCHAR(20),
  ClubMentor VARCHAR(50)
);

CREATE TABLE Membership (
  StudentID INT,
  ClubID INT,
  JoinDate DATE,
  PRIMARY KEY (StudentID, ClubID),
  FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
  FOREIGN KEY (ClubID) REFERENCES Club(ClubID)
);
