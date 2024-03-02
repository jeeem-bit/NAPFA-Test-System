CREATE TABLE "Student" (
	"MatricNo"	TEXT UNIQUE,
	"Name"	TEXT,
	"Class"	TEXT,
	"IndexNo"	INTEGER,
	"Gender"	INTEGER,
	"BirthYear"	INTEGER,
	PRIMARY KEY("MatricNo")
);

CREATE TABLE "Standard" (
	"Age"	INTEGER,
	"Gender"	TEXT,
	"Item"	TEXT,
	"F,E,D,C,B"	TEXT,
	PRIMARY KEY("Age","Gender","Item")
);

CREATE TABLE "Result" (
	"MatricNo"	TEXT,
	"Year"	INTEGER,
	"SitUp,Jump,SitReach,PullUp,Shuttle,Run24"	INTEGER,
	FOREIGN KEY("MatricNo") REFERENCES "Student"("MatricNo")
);