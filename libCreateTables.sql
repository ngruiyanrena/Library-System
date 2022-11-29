CREATE TABLE Member(  
     MemberId     VARCHAR(6)    NOT NULL  UNIQUE,
     Name         VARCHAR(16)   NOT NULL,
     Faculty      VARCHAR(11)   NOT NULL,
     PhoneNumber  VARCHAR(8)    NOT NULL,
     Email        VARCHAR(21)   NOT NULL,
	 PRIMARY KEY (MemberId));
     
CREATE TABLE Book(  
     AccessionNumber      VARCHAR(3)    NOT NULL   UNIQUE,
     Title                VARCHAR(100)  NOT NULL,
     Isbn                 VARCHAR(13)   NOT NULL,
     Publisher            VARCHAR(50)   NOT NULL,
     PublicationYear      SMALLINT      NOT NULL,
     Reserved_MemberID    VARCHAR(6),
     Borrowed_MemberID    VARCHAR(6),
     Returned_MemberID    VARCHAR(6),
     BorrowDate           DATE,
     ReturnDate           DATE,
     DueDate              DATE,
     ReserveDate          DATE,
	 PRIMARY KEY (AccessionNumber));
     
CREATE TABLE Fine(  
     MemberId     VARCHAR(6)  NOT NULL  UNIQUE,
     Amount       SMALLINT    NOT NULL,
     DatePaid     DATE,
	 PRIMARY KEY (MemberId), 
     FOREIGN KEY (MemberID)    REFERENCES Member(MemberID) ON DELETE CASCADE
                                                           ON UPDATE CASCADE);
     
CREATE TABLE Authors(  
     Author             VARCHAR(50)   NOT NULL,
     AccessionNumber    VARCHAR(3)    NOT NULL,
	 PRIMARY KEY (Author, AccessionNumber),
     FOREIGN KEY (AccessionNumber)    REFERENCES Book(AccessionNumber) ON DELETE CASCADE
                                                                       ON UPDATE CASCADE);
CREATE TABLE StatusOfBook(  
     Status             VARCHAR(15)   NOT NULL,
     AccessionNumber    VARCHAR(3)   NOT NULL    UNIQUE,
	 PRIMARY KEY (Status, AccessionNumber),
     FOREIGN KEY (AccessionNumber)    REFERENCES Book(AccessionNumber) ON DELETE CASCADE
                                                                       ON UPDATE CASCADE);