CREATE TABLE MembershipRaw (
  StudentID INT,
  StudentName VARCHAR(50),
  Email VARCHAR(100),
  ClubName VARCHAR(50),
  ClubRoom VARCHAR(20),
  ClubMentor VARCHAR(50),
  JoinDate DATE,
  PRIMARY KEY (StudentID, ClubName)
);
