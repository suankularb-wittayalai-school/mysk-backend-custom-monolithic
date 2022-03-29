
BEGIN TRANSACTION;

CREATE TABLE PrefixType
(
    id INTEGER PRIMARY KEY,
    value TEXT NOT NULL
);

INSERT INTO PrefixType
    (id, value)
VALUES
    (1, 'Mr.'),
    (2, 'Mrs.'),
    (3, 'Ms.'),
    (4, 'Master.'),
    (5, 'เด็กชาย'),
    (6, 'นาย'),
    (7, 'นาง'),
    (8, 'นางสาว');


CREATE TABLE ContactType
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO ContactType
    (id, name)
VALUES
    (1, 'Phone'),
    (2, 'Email'),
    (3, 'Facebook'),
    (4, 'Line'),
    (5, 'Instagram'),
    (6, 'Twitter'),
    (7, 'Website'),
    (8, 'Discord'),
    (9, 'Other');


CREATE TABLE Contact
(
    id INTEGER PRIMARY KEY,
    type INTEGER NOT NULL REFERENCES ContactType (id),
    name TEXT NOT NULL,
    value TEXT NOT NULL,
);

CREATE TABLE Person
(
    id INTEGER PRIMARY KEY,
    prefix_th int CHECK(prefix_th >= 5 AND prefix_th < 9) NOT NULL REFERENCES PrefixType(id),
    prefix_en int CHECK(prefix_en >= 1 AND prefix_en < 4) NOT NULL REFERENCES PrefixType(id),
    first_name_th TEXT NOT NULL,
    last_name_th TEXT NOT NULL,
    middle_name_th TEXT,
    first_name_en TEXT NOT NULL,
    last_name_en TEXT NOT NULL,
    middle_name_en TEXT,
    birthdate DATE NOT NULL,
    citizen_id TEXT NOT NULL,
    contact int REFERENCES Contact(id),
);

CREATE TABLE Teacher
(
    id INTEGER PRIMARY KEY,
    people_id INTEGER NOT NULL REFERENCES Person(id),
    teacher_id TEXT NOT NULL
);

CREATE TABLE Teacher_SubjectGroup
(
    id INTEGER PRIMARY KEY,
    teacher_id INTEGER NOT NULL REFERENCES Teacher(id),
    subject_group_id INTEGER NOT NULL,
);

CREATE TABLE Student
(
    id INTEGER PRIMARY KEY,
    people_id INTEGER NOT NULL REFERENCES Person(id),
    student_id TEXT NOT NULL
);

COMMIT;